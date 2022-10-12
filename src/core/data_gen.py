#Imports
import random                                 #This lets this part of the program access the random.randint function built into python

#Functions
def gen_suit():                               #This functions generates and returns a random suit
  rand_pick=int(0)                            #Stores number for random pick
  suits=["Hearts","Clubs","Spades","Diamonds"]#Stores all possible suits 
  rand_pick=random.randint(0,3)               #Generates random number, which corresponds
                                              #to one of the suits
  
  return(suits[rand_pick])                    #Returns random suit pick


def gen_suit_hands(p_num_cards):              #This function assembles and returns a hand's suits
  suitHands = []                              #Stores the suits in the hand
  
  for loopCount in range(0,p_num_cards):      #Assigns random suit to all cards in hand
    suitHands.append(gen_suit())
    
  return(suitHands)                           #Returns suits for the hand

  
def gen_face_vals():                          #This functions generates and returns a random face value
  face_val=int(0)                             #Stores generated face value
  face_val=random.randint(1,13)               #Generates random face value from 1-13
  
  return(face_val)                            #Returns generated face value


def gen_hand_vals(p_num_cards):               #This function assembles and returns a hand's face values
  face_value = int(0)                         #Holds face value of an individual card in for loop
  hand = []                                   #Holds face values of cards in hand
  
  for loop_counter in range(0,p_num_cards):   #Assigns random face value to each card
    face_value = gen_face_vals()
    hand.append(face_value)
    
  return(hand)                                #Returns face values for hand