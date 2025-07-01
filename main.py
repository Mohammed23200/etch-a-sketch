from turtle import Turtle,Screen

soso = Turtle()
screen = Screen()
def forward_w():
    soso.forward(30)
def backward_s():
    soso.backward(30)
def clock_wise():
    new_heading =soso.heading()+10
    soso.setheading(new_heading)
def de_clock_wise():
    new_heading =soso.heading()-10
    soso.setheading(new_heading)
def clear_screen():
    soso.clear()
    soso.penup()
    soso.home()
    soso.pendown()
screen.listen()
screen.onkey(key='w',fun=forward_w)
screen.onkey(key='s',fun=backward_s)
screen.onkey(key='d',fun=clock_wise)
screen.onkey(key='a',fun=de_clock_wise)
screen.onkey(key='c',fun=clear_screen)
screen.exitonclick()
