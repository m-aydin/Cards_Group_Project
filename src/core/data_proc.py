#Functions
def add_card_vals(p_vals):               #This function calculates and returns hand's total value
  hand_total_val=int(0)                  #Keeps count of card total value
  
  for loop_count in range(0,len(p_vals)):#Counts total value of hand
    hand_total_val=hand_total_val+p_vals[loop_count]
    
  return(str(hand_total_val))            #Returns total value of hand


def count_face_vals(p_vals):             #This function counts and returns a list with how much of each face value is present
  face_val_count=[]                      #Stores how many of each face value there are
  
  for loop_count in range(1,14):         #Gets how many instances of face value there is, 
                                         #and puts it in appropriate position
    face_val_count.append(p_vals.count(loop_count))
    
  return(face_val_count)                 #Returns data 