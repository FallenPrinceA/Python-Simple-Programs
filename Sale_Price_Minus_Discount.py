#This program gets an item's original price and
#calculates its sale price, with a discount and taxes

#Get the item's original price.
original_price = float(input("Enter the item's original price: "))

#Enter Discount's percentage
discount_percentage = float(input("Enter the discount's percentage: "))

#Enter Sales Tax
sales_tax= float(input("Enter the sale's tax, as a decimal: "))

#Calculate the amount of the discount.
discount = original_price * discount_percentage

#Calculate the sale price
sale_price = original_price - discount

#Calculate the sales price after taxes
Price_After_Tax = sale_price + (sale_price * sales_tax)

#Display the sale price
print('The sale price is $', sale_price)

#Display sales price after taxes
print ('The Final price is $', Price_After_Tax)
