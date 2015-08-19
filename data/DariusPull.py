#This python file is downloading match data given a file of match ids.
# e.g. python DariusPull.py BILGEWATER/NA.json
# NOTES: key need to updated after session expires
# NOTES: RiotWatcher(key)

import time
import sys
import os
import json
from riotwatcher import RiotWatcher, NORTH_AMERICA, BRAZIL, EUROPE_NORDIC_EAST, EUROPE_WEST,\
  KOREA, LATIN_AMERICA_NORTH, LATIN_AMERICA_SOUTH, NORTH_AMERICA, OCEANIA, RUSSIA, TURKEY
from riotwatcher import LoLException

##############################################################################
#You need to define these two variables before running the script            #
#key   : Riot developer API key, get it from https://developer.riotgames.com/#
#region: Region the match comes from										 #
##############################################################################
key = "d6d2296a-434a-4084-b4ee-c2d8347f41a6"
region = NORTH_AMERICA

w = RiotWatcher(key, region)
match_array = []

def wait():
    while not w.can_make_request():
        time.sleep(1)
        
def get_match(matchId):
    wait()
    m = w.get_match(matchId)
    return m
    
def main(match_array, out_path):
  with open(out_path, 'a+') as outfile:
    for matchId in match_array:
      print('start getting match' + matchId)
      retry = 0
      while (retry < 3):
        try:
          m = get_match(matchId)
          break
        except LoLException, e:
          time.sleep(60)
          continue
      print m["matchId"]
      json.dump(m, outfile)
      outfile.write('\r\n')
  print('match passed')
    
if __name__ == '__main__':
  input_path = sys.argv[1]
  output_path = input_path + ".data"
  with open(input_path) as infile:
    for line in infile:
      global match_array
      if (line.startswith('[') == False and line.startswith(']') == False):
        match_array.append(line.replace('\r\n', '').replace(', ', ''))
    print match_array
    main(match_array, output_path)