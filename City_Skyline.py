# Program: We use the turtle to draw a skyscraper with stars and lighted windows

#import the turtle to start
import turtle
import random

#The Main Function of the program
def main():
    turtle.setup(600, 600)
    turtle.bgcolor('black')
    turtle.hideturtle()
    turtle.speed(0)
    stars()
    skyline(-300, -400, 300, 'gray')
    skyline(0, -400, 300, 'gray')
    skyscrapers(-300, -100, 'gray')
    #Middle Skyscraper Window
    window(10, 50, 20, 'white')    
    window(-100, 150, 20, 'white') 
    window(-100, 120, 20, 'white') 
    window(-20, -120, 20, 'white') 
    #Left Skyscraper Window
    window(-200, -40, 20, 'white') 
    #Right Skyscraper Window
    window(125, 85, 20, 'white')   

#The star function that we call in main
def stars():
    for stars in range(75):
        x = random.randrange(-300, 300)
        y = random.randrange(-100, 300)
        turtle.pencolor('white')
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot()
        
#Skyline Function
def skyline(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor('gray')
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def skyscrapers(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()    
    turtle.begin_fill()
    turtle.forward(70)  
    turtle.left(90)
    #Left Skyscraper Wall
    turtle.forward(100)
    #Left Skyscraper
    turtle.right(90)
    #Left Skyscraper Roof
    turtle.forward(100) 
    turtle.left(90)
    #Middle Skyscraper Wall
    turtle.forward(200)
    # Middle Skyscraper
    turtle.right(90)
    # Middle Skyscraper Roof
    turtle.forward(150)
    # Middle Skyscraper
    turtle.right(90)
    # Middle Skyscraper Wall
    turtle.forward(225)  
    turtle.left(90)
    turtle.forward(75)  
    turtle.left(90)
    # 1st Right Skyscraper Wall
    turtle.forward(150)
    # 1st Right Skyscraper
    turtle.right(90)
    # 1st Right Skyscraper Roof
    turtle.forward(100)
    # 1st Right Skyscraper 
    turtle.right(90)
    # 1st Right Skyscraper Wall
    turtle.forward(100)  
    turtle.left(90)
    # 2nd Right Skyscraper Roof
    turtle.forward(50)
     # 2nd Right Skyscraper
    turtle.right(90)
    # 2nd Right Skyscraper Wall
    turtle.forward(175) 
    turtle.left(90)
     # (300, -100)
    turtle.forward(105)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    #Complete Skyscraper Box
    turtle.forward(600) 
    turtle.right(90)
    turtle.forward(1)    
    turtle.end_fill()

def window(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()



    
# Call the main function.
main()
