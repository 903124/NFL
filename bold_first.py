#!/usr/bin/env python3

# python script for evaluating 2pt vs pat
# u/conceptuality and u/903124 on reddit

# team traditional:
# Go for two points for every opponent's successful two points attempt
# Kick extra point for every opponent's misses
# Go for two points when trailing by two after touchdown

# team bold:
#Always go for two point

# each team scores one touchdown (close game assumption), and then does the above xp 
# routine. The difference from the one on reddit is that the touchdowns are ordered, so
# if team traditional scores first, they go for the pat, which means the score
# differential (#bold - #trad) can now also be +1 (trad goes first, both succesful).


import sys
import random
import numpy as np

def main():
 
    
    
  # parameters:
  trad_pat_rate = 0.95
  trad_two_pt_rate = 0.5  # this is the main hyper parameter
  bold_two_pt_rate = 0.52
  number_of_runs = 10000
  

  
  # 
  # SIMULATION!
  #
  
  # counters
  
  games = 0 
  team_bold_wins = 0
  team_trad_wins = 0
  tied_games = 0
  margin = 0
  
  while games < number_of_runs:
    pair_td = np.random.poisson(2.5,1)
    
    for td in range(pair_td):
      
      if random.random() < bold_two_pt_rate:       # team bold converts 2pt
        if random.random() < trad_two_pt_rate:       # team trad  also converts 2pt
          margin += 0
        else:                                   # team trad misses 2pt
          margin += 2
      else:                                   # team bold misses 2pt
        if random.random() < trad_pat_rate:          # team trad scores pat
            margin += -1
        else:                                   # team trad misses pat
         margin += 0
    
    if margin == 1:                           # team trad go for two when trailing by two
      if random.random() < trad_two_pt_rate:
        margin += -1
      else:
        margin += 1
       
    if margin == 0:
        tied_games += 1
        
    elif margin < 0:
        team_trad_wins += 1
    else:
        team_bold_wins += 1
    games += 1  # increase counter
    margin = 0
  
  # win rate:
  
  bold_wr = team_bold_wins / games
  trad_wr = team_trad_wins / games
  bayes_wr = bold_wr / ( bold_wr + trad_wr)
  tie_r = tied_games / games
  
  print("Team bold wins: ", team_bold_wins)
  print("Team Traditional wins: ", team_trad_wins)
  print("Tie: ", tied_games)
  print('Team bold win rate: ', bold_wr)
  print('Team traditional win rate: ', trad_wr)
  print('Tie rate: ', tie_r)
  print('Baye Wins', bayes_wr)          

    
if __name__ == '__main__':
  main()
