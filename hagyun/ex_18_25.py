import turtle

t=turtle.Turtle()
turtle.bgcolor('skyblue')
turtle.setup(750,750)
t.shape('turtle')
t.color('indigo','slategray')
colors=['red','orange','yellow','green','blue','navy','purple']
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

# rainbow(t,50,50,50,50)


# 밑은 수업 내용
tr=turtle.Turtle()
tr.speed(0)
tr.pensize(5)

def draw_rainbow(radius,x,y):
    for color in reversed_colors:
        tr.color(color)
        tr.penup()
        tr.goto(x,y)
        tr.pendown()
        tr.setheading(90)
        #현재상태에 상관없이 오른쪽을 기준으로 양의 방향으로 90도, 바라보는 방향 정렬
        tr.circle(radius,180)
        x+=7
        radius+=7

if __name__=='__main__':
    rainbow(t,10,50,50,0)
    turtle.exitonclick()