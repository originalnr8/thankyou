
from graphics import *
from datetime import datetime
from random import randint

def main():
    win = GraphWin ("My Window", 800, 600)
    win.setBackground(color_rgb(0,0,0))
    
    global intReference

    while intReference < 16:
        sayWho(win)
        sayThanks(win)
        sayWhy(win)
        dtObject = datetime.now()
        if dtObject.hour > 17:
            intReference = 16
        if intReference > 0:
             intReference = 0
        else:
            intReference = randint(0,14)
        time.sleep(1)
        clearWindow(win)

    win.close()

def sayThanks(Window):
    pt = Point(250,50)
    txt = Text(pt,"Thank You")
    txt.setTextColor('white')
    txt.setSize(70)
    txt.setFace('arial')
    txt.draw(Window)

def sayWho(Window):
    global intReference
    pt2 = Point(400,300)
    img = Image(pt2, getCompany(intReference))
    img.draw(Window)

def sayWhy(Window):
    global intReference
    pt3 = Point(300,550)
    txt2 = Text(pt3, getReason(intReference))
    txt2.setTextColor('white')
    txt2.setSize(40)
    txt2.setFace('times roman')
    txt2.draw(Window)

def clearWindow(Window):
    pt4 = Point(0,0)
    pt5 = Point(800,600)
    rect = Rectangle(pt4,pt5)
    rect.setFill('black')
    rect.draw(Window)

def getCompany(number):
    switcher = {
        0: "NHS.gif",
        1: "Tesco.gif",
        2: "Asda.gif",
        3: "Aldi.gif",
        4: "Lidl.gif",
        5: "Sainsburys.gif",
        6: "Amazon.gif",
        7: "Netflix.gif",
        8: "Sky.gif",
        9: "BT.gif",
        10: "npower.gif",
        11: "SSE.gif",
        12: "Trash.gif",
        13: "VirginMedia.gif",
        14: "Wessex.gif",
        15: "RoyalMail.gif"
        }
    return switcher.get(number,"Invalid number")

def getReason(number):
    switcher = {
        0: 'For keeping us alive',
        1: 'For feeding us',
        2: 'For feeding us',
        3: 'For feeding us',
        4: 'For feeding us',
        5: 'For feeding us',
        6: 'For entertaining us',
        7: 'For entertaining us',
        8: 'For entertaining us',
        9: 'For helping us talk',
        10: 'For powering everyone',
        11: 'For powering everyone',
        12: 'For keeping us civilised',
        13: 'For connecting everyone',
        14: 'For keeping us clean',
        15: 'For keeping us connected'
        }
    return switcher.get(number,"Invalid number")

intReference = 0
main()