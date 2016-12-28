#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:09:38 2016

@author: yifan
"""

import letterNumCheck_Func
    
def main():
    
    CONST_C4=261.63
    CONST_D4=293.66
    CONST_E4=329.63
    CONST_F4=349.23
    CONST_G4=392.00
    CONST_A4=440.00
    CONST_B4=493.88
    
    letter_string = input("Please enter the pitch class/note: ")
    # Then check and update the value of letter_string using a separate
    # function in the module letterNumCheck_Func.py to make sure
    # it is a valid input letter.
    letter_string = letterNumCheck_Func.checkLetter(letter_string)
              
    
    num_string = input("Please enter the octave number/registra: ")
    # Then check and update the value of num_string using a separate
    # function in the module letterNumCheck_Func.py to make sure
    # it is a valid input integer.
    num_string = letterNumCheck_Func.checkNum(num_string)

    
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
    
       
# when this script is directly run, then the __name__ is set to '__main__'
# and thus we can run the above defined main() function

if __name__ == '__main__':
    
    main()
 
    
