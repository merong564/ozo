import turtle

def draw_rainbow_circles(r0=50, step=5):
    screen = turtle.Screen()
    screen.setup(500, 450)
    screen.bgcolor('black')

    t = turtle.Turtle()
    t.speed(0)          
    t.pensize(2)
    colors = ['red','orange','yellow','green','blue','navy','purple']

    for i, c in enumerate(colors):
        r = r0 + i*step
        t.penup()
        t.goto(0, -r)  
        t.pendown()
        t.pencolor(c)
        t.circle(r)

    t.hideturtle()
    turtle.exitonclick()  

if __name__ == "__main__":
    draw_rainbow_circles(50)

