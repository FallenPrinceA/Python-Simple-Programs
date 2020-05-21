# This program demonstrates how a floating-point
# number can be displayed as currency

monthly_pay = float(input('Enter your monthly pay: '))

annual_pay = monthly_pay * 12

print('Your annual pay is $',
          format(annual_pay, ',.2f'),
              sep='')
