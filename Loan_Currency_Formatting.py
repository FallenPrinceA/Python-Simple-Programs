#This program demonstrates how a floating point
#number can be formatted using a loan

amount_due = float(input('Enter the amount of the loan: '))

monthly_payment = amount_due / 12

print('The monthly payment is',
      format(monthly_payment, '.2f'))

