# A simple graphical Timer Application in Python
import time
from graphics import *


def main():
    workArea = GraphWin('A Simple Python timer', 300, 300)  # give title and dimensions
    workArea.setBackground('yellow')
    message = Text(Point(workArea.getWidth() / 2 - len('Click to start Timer') / 2, 50), 'Click to start Timer')
    message.setFace('helvetica')  # change text style
    message.setStyle('italic')
    message.setTextColor("blue")  # change text color
    message.draw(workArea)
    workArea.getMouse()  # get mouse click on screen to start timer

    start = True

    # initilize variables
    vSec = 0
    vMin = 0

    timerCont = start
    while timerCont:
        message.undraw()
        vSec += 1
        label = Text(Point(workArea.getWidth() / 2 - len("Minutes:Seconds") / 2, 100), "Minutes:Seconds")
        label.setTextColor("green")  # change color
        label.setSize(24)
        label.draw(workArea)
        message = Text(Point(workArea.getWidth() / 2, 150), str(vMin) + " : " + str(vSec))
        message.setTextColor("purple")  # change color
        message.setSize(36)
        message.setStyle('bold')
        message.draw(workArea)
        time.sleep(1)
        if vSec > 59:
            vSec = 0
            vMin += 1
        if workArea.checkMouse():
            workArea.close()
            break


main()

