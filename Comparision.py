# Compare the two cases for traditional team get a touchddown first
# and bold team get a touchdown first

import random
import numpy as np


 
    
    
  # parameters:
trad_pat_rate = 0.95
bold_pat_rate = 0.95
trad_two_pt_rate = 0.5  # this is the main hyper parameter
bold_two_pt_rate = 0.5
number_of_runs = 10000
  

def bold_first(trad_pat_rate,bold_pat_rate,trad_two_pt_rate,bold_two_pt_rate,number_of_runs):
  
  import sys
  import random
  import numpy as np


 
    
    
  
  

  
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
    
    if margin == 1:
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
  
  return bayes_wr
  
  
def trad_first(trad_pat_rate,bold_pat_rate,trad_two_pt_rate,bold_two_pt_rate,number_of_runs):
    
       

  
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
    
    for td in range(pair_td):                         #initialization
      
      if random.random() < trad_pat_rate:       # team trad scores pat
        if random.random() < bold_two_pt_rate:       # team bold converts 2pt
          margin += 1
        else:                                   # team bold misses 2pt
          margin += -1
      else:                                   # team trad misses pat
        if random.random() < bold_pat_rate:          # team bold scores pat
            margin += 1
        else:                                   # team bold misses pat
         margin += 0
      
    if pair_td >= 2:
      for td in range(pair_td -1):
        if margin >= 2 :                           # margin >= 2
          if random.random() < trad_two_pt_rate:    #team trad converts 2pt
            if random.random() < bold_two_pt_rate:  # team bold converts 2pt
              margin += 0
            else:                                # team bold misses 2pt
              margin += -2 
          else:                               # team trad misses 2pt
            if random.random() < bold_pat_rate:  # team bold converts pat
              margin += 1
            else:                             # team bold misses pat
              margin += 0
        if margin == 1 :                         # margin = 1
           if random.random() < trad_two_pt_rate:    #team trad converts 2pt
            if random.random() < bold_two_pt_rate:  # team bold converts 2pt
              margin += 0
            else:                                # team bold misses 2pt
              margin += -2 
           else:                               # team trad misses 2pt
              if random.random() < bold_pat_rate:  # team bold converts pat
                margin += 1
              else:                             # team bold misses pat
                margin += 0
         
        if margin ==  0:                     # margin = 0 
          if random.random() < trad_pat_rate:       # team trad scores pat
            if random.random() < bold_two_pt_rate:       # team bold converts 2pt
              margin += 1
            else:                                   # team bold misses 2pt
              margin += -1
          else:                                   # team trad misses pat
            if random.random() < bold_pat_rate:          # team bold scores pat
                margin += 1
            else:                                   # team bold misses pat
              margin += 0
        if margin <=  -1:                     # margin <= -1
          if random.random() < trad_pat_rate:       # team trad scores pat
            if random.random() < bold_two_pt_rate:       # team bold converts 2pt
              margin += 1
            else:                                   # team bold misses 2pt
              margin += -1
          else:                                   # team trad misses pat
            if random.random() <  bold_two_pt_rate:          # team bold converts 2pt
              margin += 1
            else:                                   # team bold misses pat
              margin += 0
        
            
    if margin == 0:
        tied_games += 1
        
    elif margin < 0:
        team_trad_wins += 1
    else:
        team_bold_wins += 1
    games += 1  # increase counter
    margin = 0  #reset game
  
  # win rate:
  
  bold_wr = team_bold_wins / games
  trad_wr = team_trad_wins / games
  bayes_wr = bold_wr / ( bold_wr + trad_wr)
  tie_r = tied_games / games
  
  return bayes_wr
  
bold_first_wr = bold_first(trad_pat_rate,bold_pat_rate,trad_two_pt_rate,bold_two_pt_rate,number_of_runs)

trad_first_wr = trad_first(trad_pat_rate,bold_pat_rate,trad_two_pt_rate,bold_two_pt_rate,number_of_runs)

diff = ((trad_first_wr-0.5) - (0.5 - bold_first_wr)) * 100
print("Wins by going for 2pt after first touchdown per 100 games: %f" % diff)
