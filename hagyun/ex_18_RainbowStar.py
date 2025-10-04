import turtle
# import turtle_rainbow
# import turtle_star
import random

turtle.bgcolor('skyblue')
turtle.setup(750,750)

t=turtle.Turtle()
t.color('indigo','slategray')
colors=['red','orange','yellow','green','blue','navy','purple']
# reversed는 한 번만 순회 가능한 iterator를 생성하므로 list로 바꿔줘야 반복 사용 가능
reversed_colors=list(reversed(colors))

def rainbow(t,n,radius,x,y):
    t.speed(0)
    t.pensize(5)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.left(90)
    for i in range(n):
        t.pencolor(reversed_colors[i%len(colors)])
        t.circle((-1)**i*(radius+i*5),180)
        # 마지막 무지개 그리면 다음 좌표로 전진하는 걸 막기 위한 조건문
        if i==n-1:
            break
        t.right((-1)**i*90)
        t.fd(5)
        t.right((-1)**i*90)
    t.hideturtle()

def star(t,n,q,length):
    t.speed(0)
    t.pensize(2)
    angle=360*q/n
    for i in range(n):
        t.pencolor(colors[i%len(colors)])
        t.fd(length)
        t.left(angle)
    t.hideturtle()

rainbow(t,50,50,0,-200)

n=15
for i in range(n):
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    t.penup()
    t.goto(x,y)
    t.pendown()
    star(t,5,2,50)

t.hideturtle()
turtle.exitonclick()