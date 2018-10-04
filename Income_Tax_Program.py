'''
Name Kang Jaehoon
email jkang36@binghamton.edu
Assignment6 -2
Lab# C60
CA Vlad Malcevic
Phone 9177246430
'''

'''
RESTATEMENT:
  Create a program to calculate a tax for either single or married

OUTPUT to monitor:
  marital_status[status] (str)
  total_income[status][income] (float)
  tax (float)

GIVEN:
  marital_status (str) - ['single', 'married']
  
  total_income[status][income] (float):
    [[0,9075, 9076, 36900, 36901, 89350, 89351,
      186350, 186351, 405100, 405101, 406750, 406751],
     [0, 18150, 18151, 73800, 73801, 148850, 148851,
      226850, 226851,  405100, 405101, 457600, 457601]]
  
  tax rate (float):
    [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

FORMULA:
  tax = base tax amount for bracket
          + (tax rate for bracket * (total_income[status][income]
          - base total_income[status][income] level for bracket))
'''

# No MAGIC numbers!
# CONSTANTS

# base total_income[status][income] levels
# for single and married tax brackets
SINGLE_BRACKET0 = 0
SINGLE_BRACKET1 = 9075
SINGLE_BRACKET2 = 36900
SINGLE_BRACKET3 = 89350
SINGLE_BRACKET4 = 186350
SINGLE_BRACKET5 = 405100
SINGLE_BRACKET6 = 406750

MARRIED_BRACKET0 = 0
MARRIED_BRACKET1 = 18150
MARRIED_BRACKET2 = 73800
MARRIED_BRACKET3 = 148850 
MARRIED_BRACKET4 = 226850
MARRIED_BRACKET5 = 405100
MARRIED_BRACKET6 = 457600

# Define base tax amounts for single and married tax brackets
BASE_SINGLE0 = 0
BASE_SINGLE1 = 907.50
BASE_SINGLE2 = 5081.25
BASE_SINGLE3 = 18193.75
BASE_SINGLE4 = 45353.75
BASE_SINGLE5 = 117541.25
BASE_SINGLE6 = 118118.75

BASE_MARRIED0 = 0
BASE_MARRIED1 = 1815
BASE_MARRIED2 = 10162.5
BASE_MARRIED3 = 28925
BASE_MARRIED4 = 50765
BASE_MARRIED5 = 109587.5
BASE_MARRIED6 = 127962.5

# Define tax rate applied to total_income[status][income] over
# base total_income[status][income] of given tax bracket
TAX_RATE1 = 0.1
TAX_RATE2 = 0.15
TAX_RATE3 = 0.25
TAX_RATE4 = 0.28
TAX_RATE5 = 0.33
TAX_RATE6 = 0.35
TAX_RATE7 = 0.396
 

# This progam displays the simple tax for single and married
# filers given a set of incomes


# Define a Function to decide if the year is an integer or > 0
def is_positive(year):
  return year.isdigit() and int(year) > 0

# Define a Function to decide if the string is only 's' or 'm'
def is_valid_status(status):
  return status == 's' or status == 'm'

# Define a Function to calculate tax
def compute_tax_for_bracket(income, base, braket, rate):
  return base + (income - braket) * rate

# Define a Function to take in status and income using compute_tax_for_bracket()
def compute_tax(status, income):
  tax = 0
  if status == 's':    
    
      if (income < SINGLE_BRACKET1):
        tax = compute_tax_for_bracket(income, BASE_SINGLE0, SINGLE_BRACKET0, TAX_RATE1)
        
      elif (income < SINGLE_BRACKET2):
        tax = compute_tax_for_bracket(income, BASE_SINGLE1, SINGLE_BRACKET1, TAX_RATE2)
          
      elif (income < SINGLE_BRACKET3):
        tax = compute_tax_for_bracket(income, BASE_SINGLE2, SINGLE_BRACKET2, TAX_RATE3)
          
      elif (income < SINGLE_BRACKET4):
        tax = compute_tax_for_bracket(income, BASE_SINGLE3, SINGLE_BRACKET3, TAX_RATE4)
          
      elif (income < SINGLE_BRACKET5):
        tax = compute_tax_for_bracket(income, BASE_SINGLE4, SINGLE_BRACKET4, TAX_RATE5)

      elif (income < SINGLE_BRACKET6):
        tax = compute_tax_for_bracket(income, BASE_SINGLE5, SINGLE_BRACKET5, TAX_RATE6)

      else:
        tax = compute_tax_for_bracket(income, BASE_SINGLE6, SINGLE_BRACKET6, TAX_RATE7)
          
  # else the user chose the status as married      
  else:
      
      if (income < MARRIED_BRACKET1):
        tax = compute_tax_for_bracket(income, BASE_MARRIED0, MARRIED_BRACKET0, TAX_RATE1)
        
      elif (income < MARRIED_BRACKET2):
        tax = compute_tax_for_bracket(income, BASE_MARRIED1, MARRIED_BRACKET1, TAX_RATE2)
          
      elif (income < MARRIED_BRACKET3):
        tax = compute_tax_for_bracket(income, BASE_MARRIED2, MARRIED_BRACKET2, TAX_RATE3)
          
      elif (income < MARRIED_BRACKET4):
        tax = compute_tax_for_bracket(income, BASE_MARRIED3, MARRIED_BRACKET3, TAX_RATE4)
          
      elif (income < MARRIED_BRACKET5):
        tax = compute_tax_for_bracket(income, BASE_MARRIED4, MARRIED_BRACKET4, TAX_RATE5)

      elif (income < MARRIED_BRACKET6):
        tax = compute_tax_for_bracket(income, BASE_MARRIED5, MARRIED_BRACKET5, TAX_RATE6)

      else:
        tax = compute_tax_for_bracket(income, BASE_MARRIED6, MARRIED_BRACKET6, TAX_RATE7)
        
  return tax

# Design
def main():
  # Explain what this program does
  print("This program computes a tax table for single and married filers")

  # Priming Read:
  #  get an input from a user to decide if the user is single or married
  print("Are you filing single or married?")
  status = input("(Type 's' for single or 'm' for married or <ENTER> to quit):  ")

  # Continuation Loop:
  #   Keeping a program going until a user wants to quit(hit <Enter>)
  while status:

    # Validation Loop for status: to force the user to give a valid input
    #   Whether the input is not single and married
    while not (status == 's' or status == 'm'):
      print("INVALID INPUT:  input only 's' or 'm'.")

      # Once the Validation is done, convert the value into an integer
      status = input("Type 's' for single or 'm' for married ONLY:  ")

    
    income_str = input("Please your annual income:  ")
    
    # Validation Loop for income: to force the user to give a valid input
    #   Whether the input is an integer and is greater than 0
    while not (income_str.isdigit() and int(income_str) > 0):
      print("INVALID INPUT:  input only whole number greater than 0.")
      income_str = input("Enter your income rounded to the whole number: ")
      
    # Convert the value into an integer
    income = int(income_str)


    # Use a funtion and save a returned value in tax
    tax = compute_tax(status, income)
    
    # Change 's' or 'm' to 'single' or 'married'
    if status == 's':
      status = 'single'
    else:
      status = 'married'
      
    # print out the sentence with the calculated outcome with % specifiers
    print("Tax for %s filer, with income $%9.2d = $%9.2f" %(status, income, tax))

    print("")
    print("Are you filing single or married?")
    
    # Continuation Read:
    #   Keeps the program going as long as user enters input
    status = input("(Type 's' for single or 'm' for married or <ENTER> to quit):  ")
            
main()
