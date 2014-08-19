#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, pygame
from pygame.locals import *
import datetime
from subprocess import *

def main():
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)

    icon = pygame.Surface((1,1))
    icon.set_alpha(0)
    pygame.display.set_icon(icon)

    pygame.display.set_caption("Horloge numérique")

    pygame.init()

    black = 0,0,0
    white = 255,255,255
    font = pygame.font.Font("font.ttf", 128)

    #commandeDate = ["date", "+%Y-%m-%d %H:%M:%S.%N"]
    commandeDate = ["date", "+%S.%N"]

    delta = datetime.timedelta(seconds = 0)


    alarm1 = "2014-08-19 22:13:00"

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit(0)

        screen.fill(black)

        now = datetime.datetime.today()
        secPython = float(str(now)[17:26])


        dt = str(now - delta)
        time = dt[11:19]

        fontimg = font.render(time, 1, white)
        screen.blit(fontimg, (50,80))

        pygame.display.update() 
        pygame.time.delay(1000)
        
        # Compute delta
        out=Popen(commandeDate,stdout=PIPE)
        (secUnix,serr)=out.communicate()
        delta = datetime.timedelta(seconds = int(float(secUnix) - float(secPython)))
        if alarm1 == str(now)[0:19]:
            print "Alarm"



if __name__ == '__main__': 
    main()    
