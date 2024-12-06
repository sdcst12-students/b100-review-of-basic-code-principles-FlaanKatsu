"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

print('welcome to lord beelzebub\'s simple intrest calculator !!!!!!!!');
try:
  P = float(input('what is the amount of money you are putting in ?: '));
  R = float(input('what is the rate ? (needs to be a percentage !!: ')) * 0.01;
  toki = int(input('What is the amount of time ? (Enter 1 for years, 2 for months, 3 for days: '));
  input_complete = 0;
  while input_complete == 0:
    if toki == 1:
      T = int(input("please enter the time in years: "));
      input_complete = 1;
    elif toki == 2:
      T = float(input("please enter the time in months: ")) / 12;
      input_complete = 1;
    elif toki == 3:
      T = float(input("please enter the time in days: ")) / 365;
      input_complete = 1;
    else:
      print("Input error, please try again");
  A = P * R * T;
  print(f"The total value of the investment is {round(A + P,2)}, the intrest earned is {round(A,2)}");

except Exception as e:
  print(f"Error: {e}");