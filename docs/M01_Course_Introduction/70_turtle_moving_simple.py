#Jonathan Hudson
#Student Number 12347890
#Date: 2021-08-24
#Lecture Practice

#Importing
import turtle 

#Creating Alex the turtle <- (better name could be pointer)
alex = turtle.Turtle()

### #Make Alex look like turtle
alex.shape("turtle")

#Alex is red
alex.color("red")

#Make Alex's trail bigger
alex.pensize(7)

#Moving and turning alex
alex.forward(100)
alex.left(45)
alex.forward(50)
alex.penup()
alex.left(45)
alex.forward(50)
alex.left(45)
alex.pendown()
alex.forward(50)
alex.left(45)
alex.forward(100)

#Where the turtle lives
window = turtle.Screen()
#Exit on click so the result can be seen
window.exitonclick()