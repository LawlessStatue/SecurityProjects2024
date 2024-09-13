""" 
This python script is to check the strength of a given password
It will judge such password based on complexity requirements, 
length, special characters, numbers, and upper/lowercase letters.

"""
import re

def main():
  pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$'
  pattern2 = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{12,}$'
  pattern3 = r'^(?=.*\d)[\d]{12,}$'
  pattern4 = r'^(?=.*[A-Za-z])[A-Za-z]{12,}$'

  while input != 0:
    password = input("Enter a password: ")

    if (password == 0 or password == "0"):
      print("No password used, ending script")
      break

    elif (re.match(pattern, password)):
      print("Password is strong")
      break

    elif (re.match(pattern2, password)):
      print("Password is moderate")
      break
    
    elif (re.match(pattern3, password) or re.match(pattern4, password)):
      print("Password is weak")
      break
      

main()
