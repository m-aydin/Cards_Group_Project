#Imports
import core.data_gen                                           #This lets the main program access functions from data_gen.py
import core.data_proc                                          #This lets the main program access functions from data_proc.py
import core.ui                                                 #This lets the main program access functions from ui.py          

#Global Variables
card_num_in_hand=int(0)                                        #How many cards are in the user's hand
hand_suits=[]                                                  #Holds all suits for the hand
hand_vals=[]                                                   #Holds all face values for the hand

#Main program
card_num_in_hand=int(input("Input Card Amount In Your Hand: "))#Gets user input for card amount in hand
hand_suits=core.data_gen.gen_suit_hands(card_num_in_hand)      #Generates suits in hand from user selected card amount
hand_vals=core.data_gen.gen_hand_vals(card_num_in_hand)        #Generates values of hand from user selected card amount

print("\nSuits In The Hand:\n"+core.ui.list_cleaner(hand_suits)+"\n")                             #Outputs all suits in user's hand
print("Values Of The Hand:\n"+core.ui.list_cleaner(hand_vals)+"\n")                               #Outputs values of user's hand
print("Total Hand Value:\n"+core.data_proc.add_card_vals(hand_vals)+"\n")                         #Outputs total value of user's hand
print("Face Value Counts:\n"+core.ui.list_cleaner(core.data_proc.count_face_vals(hand_vals))+"\n")#Outputs how much of each face value is present

core.ui.display_hand(hand_vals,hand_suits)                     #Calls function to display hand in human-readable way
core.ui.count_suits(hand_suits)                                #Calls function to display how much of each suit is present
                                                            
