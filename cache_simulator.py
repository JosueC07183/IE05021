import sys
import argparse
import os
import gzip
import pandas as pd

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('-s', 
  type=int, required=True, help='Capacidad del caché.')
arg_parser.add_argument('-a', type=int, required=True, help='Asociatividad del caché.')
arg_parser.add_argument('-b', type=int, required=True, help='Tamaño del bloque.')
arg_parser.add_argument('-file', type=str, required=True, help='Nombre del benchmark.')
args = arg_parser.parse_args()

#traces = os.listdir('traces')
#Miss_rate_total = []
#col1 = str(b)


# Aquí se cuentan la cantidad de "r" en cada benchmark. 
trace = str(args.file)
l=str("r")
Lecturas = 0
with open(trace, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    Lecturas += 1


def main():
  lines = readlines(args.file)
  memory_accesses = parseTraceInfo(lines)
   
  cache = [[{'tag': None, 'LRU': 0} for x in range(args.a)] for y in range(args.s)]
  misses = { 'Total Misses': 0, 'Miss rate total':0, 'Misses Lectura': 0, 'Misses Escritura': 0, 'Miss rate lectura': 0, 'Miss rate escritura':0 }
  
  for entry in memory_accesses:
    slot = cache[entry['slot']]
    match = None
    for set in slot:
      if set['tag'] != entry['tag']:
        set['LRU'] += 1
      else:
        set['LRU'] = 0
        match = set
    if not match:
      misses[entry['type']] += 1
      evict_me = max(slot, key = lambda _set: _set['LRU'])
      evict_me['tag'] = entry['tag']
      evict_me['LRU'] = 0
  
  number_of_accesses = len(memory_accesses)
  Escrituras = number_of_accesses- Lecturas
  misses['Total Misses'] = misses['Misses Lectura'] + misses['Misses Escritura']
  misses['Miss rate total'] = (misses['Total Misses']*100)/number_of_accesses
  misses['Misses Lectura'] = misses['Misses Lectura']
  misses['Misses Escritura'] = misses['Misses Escritura']
  misses['Miss rate lectura'] =round((misses['Misses Lectura']*100)/Lecturas, 3)
  misses['Miss rate escritura'] =round((misses['Misses Escritura']*100)/Escrituras, 4)
  
  for key, value in misses.items():
    print("{0} : {1}".format(key, value))

def parseTraceInfo(lines):
  a = vars(args).items() 
  bit_lengths = { k: len(bin(v-1)[2:]) for k, v in a if k != 'file' }
  offset_start = -bit_lengths['b']
  slot_start = -(bit_lengths['s'] + bit_lengths['b'])
  
  def mappingFunc(line):
    parts = line.split()
    result = {}
    num_of_bits = 32
    a = bin(int(parts[1], 16))[2:].zfill(num_of_bits)
    result['address'] = a
    result['offset'] = int(a[offset_start:], 2)
    result['slot'] = int(a[slot_start:offset_start], 2)
    result['tag'] = int(a[:slot_start])
    result['type'] = 'Misses Lectura' if parts[0] == 'r' else 'Misses Escritura'
    return result
    
  return list(map(mappingFunc, lines))
  

def readlines(filename):
  try:
    return [ line.strip() for line in open(filename) ]
  except:
    sys.exit('Error: The provided filename "{0}" does not exist in this directory.'.format(filename))
  


main()
