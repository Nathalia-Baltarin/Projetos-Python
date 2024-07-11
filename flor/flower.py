import turtle as T
import colorsys as C

T.setup(800,800)
T.speed(0)
T.tracer(10)
T.width(2)
T.bgcolor("#03071e")

for j in range (25):
    for i in range (15):
        T.color(C.hsv_to_rgb(i/15,j/25,1))
        T.right(90)
        T.circle(200-j*4,90)
        T.left(90)
        T.circle(200-j*4,90)
        T.right(180)
        T.circle(50,24)
T.hideturtle()
T.done()        