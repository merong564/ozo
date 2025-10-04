# 다른 파일에 정의된 함수를 가져와 특정 좌표에 무지개, 별을 그리는 문제

from ex_18_25 import drawRainbow
from ex_18_star import drawStar
import turtle

turtle.title('🌈무지개 별 그리기⭐️')
turtle.setup(500,400)
turtle.bgcolor("#BEF6FF")

drawStar(30, -100, 100)
drawStar(50, 30, 160)
drawRainbow(50, 0, -100)

turtle.exitonclick()
