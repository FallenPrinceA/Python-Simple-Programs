#Purpose: To allow user to insert celsius temperature and convert it to
            #fahrenheit by rounding to second whole number

#Insert the celsius temperature
celsius_tempt = float(input('Insert the Temperature in Celsius: '))

#Formula to convert celsius to fahrenheit
fahrenheit_tempt = 9/5 * celsius_tempt + 32

#print the fahrenheit temperature
print('The fahrenheit temperature is %',
          format(fahrenheit_tempt))
