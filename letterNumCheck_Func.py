#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:17:25 2016

@author: yifan
"""
import numpy as np


def checkLetter(letter_string):
            
    np.chararray = list(letter_string)
    
    def checkNote(letter_string):
        if letter_string == 'c' or letter_string == 'C':
            return True
        elif letter_string == 'd' or letter_string == 'D':
            return True
        elif letter_string == 'e' or letter_string == 'E':
            return True
        elif letter_string == 'f' or letter_string == 'F':
            return True
        elif letter_string == 'g' or letter_string == 'G':
            return True
        elif letter_string == 'a' or letter_string == 'A':
            return True
        elif letter_string == 'b' or letter_string == 'B':
            return True
        else:
            return False
            
    while np.size(list(letter_string)) !=1 or np.chararray[0].isalpha() == False or checkNote(letter_string) == False:
        
        letter_string = input("Input is invalid, please enter a valid letter for pitch class/note: ")
        np.chararray = list(letter_string)
        
    return letter_string # WE NEED to return the updated local variable value back to the 
                         # global variable appeared in the main() or another script(module)
    


def checkNum(num_string):
    
#    def isInteger(num_string):
#        
#        try: 
#            int(num_string)
#            return True
#        except:
#            return False
            
    def checkOctave(num_string):
        if num_string == '0':
            return True
        elif num_string == '1':
            return True
        elif num_string == '2':
            return True
        elif num_string == '3':
            return True
        elif num_string == '4':
            return True
        elif num_string == '5':
            return True
        elif num_string == '6':
            return True
        elif num_string == '7':
            return True
        elif num_string == '8':
            return True
        else:
            return False
            
    while np.size(list(num_string)) != 1 or isInteger(num_string)== False or checkOctave(num_string) ==False:
        
        num_string = input("Input is invalid, please enter an integer between 0 and 8 for octave/registra number: ")

    
    return num_string # WE NEED to return the updated local variable value back to the 
                      # global variable appeared in the main() or another script(module)
    
    

def isInteger(num_string):
        
        try: 
            int(num_string)
            return True
        except:
            return False
            
            
            
def isFloat(num_string):
        
        try: 
            float(num_string)            
            return True
        except:
            return False
            
            

def isOneChar(letter_string):
    
    if np.size(list(letter_string)) == 1:
        return True
    else:
        return False
            
        
            
            
def isAlpha(letter_string):
    
    np.chararray = list(letter_string)
    
    if isOneChar(letter_string) == True and np.chararray[0].isalpha() == True:
        return True
    else: 
        return False
      
    
        
    
def main():
    
    CONST_C4=1
    CONST_D4=2
    CONST_E4=3
    CONST_F4=4
    CONST_G4=5
    CONST_A4=6
    CONST_B4=7
    
    letter_string = input("Please enter the pitch class/note: ")
    letter_string=checkLetter(letter_string)
              
    
    num_string = input("Please enter the octave number/registra: ")    
    num_string = checkNum(num_string)
    #print(num_string,"is the octave str in the global main function")
           
    if letter_string == 'c' or letter_string == 'C':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_C4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'd' or letter_string == 'D':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_D4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'e' or letter_string == 'E':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_E4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'f' or letter_string == 'F':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_F4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'g' or letter_string == 'G':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_G4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'a' or letter_string == 'A':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_A4*2**(int(num_string)-4)," Hz.")
    elif letter_string == 'b' or letter_string == 'B':
       print("The note ",letter_string,int(num_string),"has a freq of :",CONST_B4*2**(int(num_string)-4)," Hz.")
      
#Try out whether the above defined functions work or not  
    var="3.00"
    
    print(var,"has only one char: ",isOneChar(var))   
    print(var,"is a letter in alphabet: ",isAlpha(var))
    print(var,"is an Integer: ",isInteger(var))
    print(var,"is a float: ",isFloat(var))  
    
# when this script is directly run, then the __name__ is set to '__main__'
# and thus we can tryout the above defined main() function
# otherwise when this script(module) is imported by another script(module)
# then __name__ is set to the name of this script, 'letterNumCheck_Func'
# thus the main() function would't be triggered  
if __name__ == '__main__':
    
    main()
 
    
