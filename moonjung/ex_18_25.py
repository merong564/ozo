import turtle

def drawRainbow(radius, x, y):
    t.speed(0)
    t.pensize = 5

    for color in colors:
        # 좌표로 이동
        t.penup()
        t.goto(x,y)
        t.pendown()

        # 무지개 그리기
        t.pencolor(color)       # 색깔 설정
        t.setheading(90)        # 거북이가 북쪽을 보도록 고정
        t.circle(radius, 180)   # 반원 그리기
        radius += 5             # 반원 반지름이 5씩 커지도록 설정
        x += 5                  # 그리기 시작하는 위치가 5씩 커지도록 설정
        
        t.hideturtle()          # 그린 뒤 거북이 숨기기


turtle.title('🐢거북이 무지개 그리기🌈')

turtle.setup(500,500)

t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

if __name__ == '__main__':

    drawRainbow(50, 0, 20)
    turtle.exitonclick()
        



