import turtle as tr
njan = tr.Turtle()

njan.penup()
njan.rt(90)
njan.fd(10)
njan.speed(0)
njan.pendown()
njan.width(5)
njan.color("#821131")
njan.begin_fill()
njan.circle(200)
njan.end_fill()
njan.color("#ffeb55")
njan.begin_fill()
njan.circle(200, 360, 10)
njan.end_fill()



njan.color("#821131", "#347928")
njan.begin_fill()
for i in range(10):
    
    njan.circle(200, 36, 10)
    njan.begin_fill()
    njan.width(1)
    njan.circle(10, 360)
    njan.end_fill()
njan.end_fill()

njan.width(1)
njan.penup()
njan.lt(90)
njan.fd(200)
njan.pendown()
njan.width(2.5)

njan.color("#ff6500", "#f0f0f0")
njan.begin_fill()
njan.width(2)
for i in range(36):
    njan.rt(10)
    for j in range(1):
        njan.circle(60)
njan.end_fill()
njan.penup()
njan.fd(140)
njan.lt(90)
njan.pendown()

def cirincir(size, side, num, n):
    njan.width(2)
    for i in range(n):
        rel_numm = 360/num
        num += 3
        for i in range(num):
            njan.circle(size, rel_numm)
            njan.color("#e85c0d", "#c40c0c")
            njan.begin_fill()
            njan.circle(5, 360, side)
            njan.end_fill()
        njan.penup()
        njan.rt(90)
        njan.fd(10)
        njan.lt(90)
        njan.pendown()
        size += 10

njan.color("#e85c0d")
njan.circle(140, 360, 6)
njan.color("#e85c0d")
njan.circle(140)
njan.penup()
njan.rt(90)
njan.fd(10)
#-njan.fd(90)
njan.pendown()
njan.lt(90)

cirincir(150, 4, 30, 4)
tr.done()



