import turtle

t=turtle.Turtle()
turtle.bgcolor('skyblue')
turtle.setup(500,500)
# t.shape('turtle')
# t.color('indigo','slategray')
colors=['red','yellow','blue','green','purple']

# 별 모양을 오목 정다각형이라고 보고, 변 수와 건너뛰는 꼭짓점 보폭을 각각 n q로 설정
# 일반적인 별 모양은 n=5, q=2임
def star(t,n,q,length):
    t.speed(0)
    t.pensize(2)
    angle=360*q/n
    for i in range(n):
        t.pencolor(colors[i%len(colors)])
        t.fd(length)
        t.left(angle)
    t.hideturtle()


if __name__=='__main__':
    star(t,5,2,20)
    turtle.exitonclick()