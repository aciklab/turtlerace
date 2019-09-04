from  turtle import *
from random import randint
import sys

colors = ["red","blue","green","orange"]

def generateTurtles(number):
    turtles = []
    for x in range(0, number):
        turtle = Turtle()
        turtle.color(colors[x])
        turtle.shape('turtle')

        turtle.penup()
        turtle.goto(-160, 100-(x*30))
        turtle.pendown()
        turtles.append(turtle)
    return turtles

def main(number):

    turtlePage = Turtle()
    turtlePage.speed()
    turtlePage.penup()
    turtlePage.goto(-140,140)

    for step in range(15):
        turtlePage.write(step,align='center')
        turtlePage.right(90)
        turtlePage.forward(10)
        turtlePage.pendown()
        turtlePage.forward(150)
        turtlePage.penup()
        turtlePage.backward(160)
        turtlePage.left(90)
        turtlePage.forward(20)

    turtles = generateTurtles(int(number))
    for turn in range(100):
        for turtle in turtles:
            turtle.forward(randint(1, 5))
    exit()


if __name__ == '__main__':
    main(sys.argv[:1])