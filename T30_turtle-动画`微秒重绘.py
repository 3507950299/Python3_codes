# coding=cp936
import math
import turtle
from datetime import *  

#t=0
def Tick():
    #global t
    # ���Ʊ���Ķ�̬��ʾ
    dt = datetime.today()

    #t = dt.second + dt.microsecond * 0.000001
    t = dt.microsecond * 0.001
    turtle.tracer(False)
    x=400*math.cos(t)
    y=300*math.sin(t)
    turtle.goto(0,0)
    turtle.goto(x,y)
    turtle.dot()

    # 100ms���������tick
    turtle.ontimer(Tick, 5)

Tick()

