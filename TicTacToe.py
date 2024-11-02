
import pygame as p
import random
import sys

p.init()
p.font.init()

w = p.display.set_mode((300,330))
w.fill((150,200,255))
p.display.set_caption("TicTacToe")

r = 0

con = p.font.Font(None,26)
cron = p.font.Font(None,170)

p.draw.line(w,"black",(100,0),(100,300),3)
p.draw.line(w,"black",(200,0),(200,300),3)
p.draw.line(w,"black",(0,100),(300,100),3)
p.draw.line(w,"black",(0,200),(300,200),3)

p.draw.rect(w,"darkgrey",p.Rect(0,300,300,30))
cro = con.render(f"X's Turn",True,"black")
w.blit(cro,(110,305))
p.display.update()
clock = p.time.Clock()

bb = [[None,None,None],
      [None,None,None],
      [None,None,None]]


def Game():
    global cc,bb,con,cron,w,r
    
    while r<10:

        def res():
            p.draw.rect(w,"darkgrey",p.Rect(0,300,300,30))
            cro = con.render(f"{a} has Won",True,"black")
            w.blit(cro,(110,305))
            p.display.update()

        if r>=5:
            for x in range(0,3):
                if (bb[x][0]==bb[x][1]==bb[x][2] and bb[x][0]!=None):
                    p.draw.line(w,"red",(25,x*100+50),(275,x*100+50),4) 
                    res()
                    r=10
            for x in range(0,3):
                if (bb[0][x]==bb[1][x]==bb[2][x] and bb[0][x]!=None):
                    p.draw.line(w,"red",(x*100+42,25),(x*100+42,275),4)
                    res()
                    r=10
            if (bb[0][0]==bb[1][1]==bb[2][2] and bb[0][0]!=None):
                p.draw.line(w,"red",(25,25),(275,275),4)
                res()
                r=10
            elif (bb[0][2]==bb[1][1]==bb[2][0] and bb[0][2]!=None):
                p.draw.line(w,"red",(275,25),(25,275),6)
                res()
                r=10
            if r == 9:
                for x in range(0,3):
                    for y in range(0,3):
                        if bb[x][y]!=None:
                            a=None
                            res()
                            r=10
            
        a = None
        m = p.mouse.get_pos()
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONUP:
                if r%2==0:
                    a = 'X'
                    p.draw.rect(w,"darkgrey",p.Rect(0,300,300,30))
                    cro = con.render(f"O's Turn",True,"black")
                    w.blit(cro,(110,305))
                    p.display.update()
                else:
                    a= 'O'
                    p.draw.rect(w,"darkgrey",p.Rect(0,300,300,30))
                    cro = con.render(f"X's Turn",True,"black")
                    w.blit(cro,(110,305))
                    p.display.update()
                    
                if (bb[0][0]==None) and (0<=m[0]<=100 and 0<=m[1]<=100):
                    r += 1
                    bb[0][0] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(5,1))
                    p.display.update()
                elif (bb[0][1]==None) and (100<=m[0]<=200 and 0<=m[1]<=100):
                    r += 1
                    bb[0][1] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(105,0))
                    p.display.update()
                elif (bb[0][2]==None) and (200<=m[0]<=300 and 0<=m[1]<=100):
                    r += 1
                    bb[0][2] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(205,0))
                    p.display.update()
                elif (bb[1][0]==None) and (0<=m[0]<=100 and 100<=m[1]<=200):
                    r += 1
                    bb[1][0] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(5,100))
                    p.display.update()
                elif (bb[1][1]==None) and (100<=m[0]<=200 and 100<=m[1]<=200):
                    r += 1
                    bb[1][1] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(105,100))
                    p.display.update()
                elif (bb[1][2]==None) and (200<=m[0]<=300 and 100<=m[1]<=200):
                    r += 1
                    bb[1][2] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(205,100))
                    p.display.update()
                elif (bb[2][0]==None) and (0<=m[0]<=100 and 200<=m[1]<=300):
                    r += 1
                    bb[2][0] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(5,200))
                    p.display.update()
                elif (bb[2][1]==None) and (100<=m[0]<=200 and 200<=m[1]<=300):
                    r += 1
                    bb[2][1] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(105,200))
                    p.display.update()
                elif (bb[2][2]==None) and (200<=m[0]<=300 and 200<=m[1]<=300):
                    r += 1
                    bb[2][2] = a
                    cro = cron.render(a,True,"black")
                    w.blit(cro,(205,200))
                    p.display.update()
            elif event.type == p.QUIT:
                p.quit()
                sys.exit()

while True:
    Game()
    for event in p.event.get():
        if event.type == p.KEYDOWN and event.key == p.K_RETURN:
            w = p.display.set_mode((300,330))
            w.fill((150,200,255))
            p.display.set_caption("TicTacToe")
            r = 0
            con = p.font.Font(None,26)
            cron = p.font.Font(None,170)

            p.draw.line(w,"black",(100,0),(100,300),3)
            p.draw.line(w,"black",(200,0),(200,300),3)
            p.draw.line(w,"black",(0,100),(300,100),3)
            p.draw.line(w,"black",(0,200),(300,200),3)

            p.draw.rect(w,"darkgrey",p.Rect(0,300,300,30))
            cro = con.render(f"X's Turn",True,"black")
            w.blit(cro,(110,305))
            p.display.update()
            clock = p.time.Clock()

            bb = [[None,None,None],
                  [None,None,None],
                  [None,None,None]]

            Game()
        elif event.type == p.QUIT:
            p.quit()
            sys.exit()
