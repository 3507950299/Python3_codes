# coding=cp936
import math
import turtle
from datetime import *  


t=0
def Tick(t):
    #global t
    # ���Ʊ���Ķ�̬��ʾ
    t=t+0.01
    turtle.bgcolor(1,1,1)
    turtle.tracer(False)
    turtle.clear()

    x=400*math.cos(t)
    y=300*math.sin(t)
    turtle.goto(0,0)
    turtle.goto(x,y)
    turtle.dot(50)

    # 100ms���������tick
    turtle.ontimer(Tick(t), 100)

Tick(t)

