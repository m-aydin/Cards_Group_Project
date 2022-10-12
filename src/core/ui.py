#Functions
def display_hand (p_vals,p_suits):               #This function displays hand in human-readable form
  hand_list=[]                                   #Has human-readable form of current hand
  print("~"*6+" Current Hand "+"~"*6)            #Creates border
  
  for loop_count in range(0,len(p_vals)):        #Assembles what in hand in human-readable way, then displays it
    hand_list.append(str(p_vals[loop_count])+" of "+str(p_suits[loop_count]))
    print(hand_list[loop_count])
    
  print("~"*6+" Current Hand "+"~"*6+"\n")       #Creates border again
  
  
def count_suits(p_suits):                        #This function tallies up how much of each suit are present and displays it in human-readable form
  count_hearts = str(p_suits.count("Hearts"))    #All of these count variables keep count of corresponding
  count_clubs = str(p_suits.count("Clubs"))      #mentions of each suit, and used when displaying counts 
  count_diamonds = str(p_suits.count("Diamonds"))#of hearts,spades, etc
  count_spades = str(p_suits.count("Spades"))
                                                 #Print below displays above data in human-friendly way
  print("The Amount Of Hearts Is {0}. \nThe Amount Of Clubs Is {1}.\nThe Amount Of Diamonds Is {2}.\nThe Amount Of Spades Is {3}.".format(count_hearts,count_clubs,count_diamonds,count_spades))


def list_cleaner(list):                          #This function cleans and returns a list as a string that is more human-readable
  chars_to_cull="[]'"                            #Stores characters to remove from the "dirty" list
  list=str(list)                                 #Converts the list to a string

  for current_pos in chars_to_cull:              #Culls all designated characters
    list=list.replace(current_pos,"")

  return(list)                                   #Returns cleaned list

  