# 18차시 강의안 p.21 별 그리기 문제

import turtle

def drawStar(length, x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    for color in colors:
        t.pencolor(color)
        t.fd(length)
        t.right(144)

turtle.title('🌠⭐️거북이 별 그리기⭐️🌟')
turtle.setup(400, 300)
turtle.bgcolor('black')

t = turtle.Turtle()
t.shape('turtle')

t.speed(10)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'purple']

t.hideturtle()

if __name__ == '__main__':

    drawStar(100, 0, 50)

    turtle.exitonclick()


