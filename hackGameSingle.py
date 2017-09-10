import pickle
import pygame
import random
import socket
import pygame_textinput
import math
import threading
import hacks
#import OtherShip


pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Hackable(object):
    def __init__(self, steps, data=[]):
        self.r=[0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.data=data
        self.dataHash={}
        self.keyList=[]
        for i in range(1,len(data)):
            self.keyList.append(data[i][0])
        for i in range(1,len(data)):
            self.dataHash[data[i][0]]=data[i][1]        #self.code
        self.current=0
        self.tries=0
        self.steps=[]
        self.attempt=''
        for i in range(0,len(steps)):
            if steps[i][0]=='ad':
                #print("line "+str(i)+" is AD")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.ad(steps[i][1],steps[i][2],steps[i][3],cod))
            elif steps[i][0]=='cop':
                #print("line "+str(i)+" is COP")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.cop(steps[i][1],steps[i][2],cod))
            elif steps[i][0]=='comp':
                #print("line "+str(i)+" is COMP")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.comp(steps[i][1],steps[i][2],cod))
            elif steps[i][0]=='goto':
                #print("line "+str(i)+" is GOTO")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.goto(steps[i][1],cod))
            elif steps[i]=='get':
                #print("line "+str(i)+" is GET")
                self.steps.append(lambda i=i, inpt='0', cod=False: str(i)+": "+self.get(inpt, cod))
            elif steps[i][0]=='win':
                #print("line "+str(i)+" is WIN")
                self.steps.append(lambda i=i, key=steps[i][1], cod=False: str(i)+": "+self.win(key, cod))
            elif steps[i]=='lose':
                #print("line "+str(i)+" is LOSE")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.lose(cod))
            elif steps[i][0]=='output':
                #print("line "+str(i)+" is OUT")
                self.steps.append(lambda i=i, cod=False: str(i)+": "+self.output(steps[i][1],cod))
    def cop(self,x,y,cod):
        if cod:
            return 'False'   
        xx=0
        yy=0
        if type(x)==int:
            xx=int(self.r[x])
        elif x[0]=='n':
            xx=int(x[1:])
        else:
            xx=int(self.r[int(x)])
        self.r[int(y)]=xx
        return(str(x)+" copied to memory location "+str(y))
    def ad(self,x,y,z,cod):
        if cod:
            return 'False'
        xx=0
        yy=0
        zz=0
        if type(x)==int:
            xx=int(self.r[x])
        elif x[0]=='n':
            xx=int(x[1:])
        else:
            xx=int(self.r[int(x)])
        if type(z)==int:
            zz=int(self.r[z])
        elif z[0]=='n':
            zz=int(z[1:])  
        else:
            zz=int(self.r[int(z)])  
        yy=int(self.r[int(y)])
        self.r[int(y)]=(xx+yy)*zz
        return(str(x)+" added to "+str(y)+" result multiplied by "+str(z)+" and put into memory slot " +str(y))
    def comp(self,x,y,cod):
        if cod:
            return 'False'
        xx=0
        yy=0
        if type(x)==int:
            xx=int(self.r[x])
        elif x[0]=='n':
            xx=int(x[1:])
        else:
            xx=int(self.r[int(x)])
        if type(y)==int:
            yy=int(self.r[y])
        elif y[0]=='n':
            yy=int(y[1:])
        else:
            yy=int(self.r[int(y)])
        if xx-yy==0:
            self.r[-1]=0
        else:
            self.r[-1] = int((xx-yy)/abs(xx-yy))
        return(str(x)+" compared to "+str(y)+" result:"+str(self.r[-1]))
    def goto(self, x,cod):
        memLoc = ''
        if cod:
            return 'False'
        if type(x)==int:
            memLoc=", taken from memory location "+str(x)
            xx=self.r[x]
        elif x[0]=='n':
            xx=int(x[1:])
        else:
            memLoc=True
            xx=self.r[int(x)]
            memLoc=", taken from memory location "+str(x)
        self.current=xx
        return("Next instruction is "+str(xx)+memLoc)
    def get(self,inpt='0',cod=False):
        #print("Getting inptut with message: "+message)
        #print("Get called, cod is "+str(cod))
        if cod:
            return 'True'
        try:
            x=int(inpt)
        except:
            self.lose(False)
            return 'Lose'
        self.r[-1]=x
        return("Input "+str(x)+" Received")
    def output(self,message, cod):
        if cod:
            return 'False'
        return(message)
    def displayMemory(self):
        print(str(self.r))
    def step(self, inp=''):
        self.current+=1
        if self.current<=len(self.steps):    
            if 'True' in self.steps[self.current-1](cod=True):
                return(str(self.steps[self.current-1](inpt=inp)))
            else:
                return(str(self.steps[self.current-1]()))
        else:
            return "Out of program error, "+self.lose(cod=False)
    def run(self):
        self.current=0
        while True:
            if self.current >= len(self.steps):
                break
            self.step()            
    def win(self, key, cod):
        if cod:
            return 'False'
        self.current=0
        index = min(len(self.keyList)-1,int(key))
        if self.data==[]:
            return "Hack Successful"
        else:
            return "Hack Successful. Use code "+data[0]+" to access data"
        return
    def lose(self, cod):
        if cod:
            return 'False'
        self.r=[0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.i=0
        self.current=0
        self.tries+=1
        return "Program Restarting"
    def getData(self, cod):
        if cod in self.dataHash.keys():
            return(self.dataHash[cod])
        else:
            return("Wrong code.")

puzzle1 = ['puzzle1clue',
('get'),
('cop',-1,1),
('get'),
('cop',-1,2),
('get'),
('cop',-1,3),
('ad','n1',4,'n12'),
('ad',1,2,'n2'),
('comp',2,3),
('ad','n0',-1,-1),
('ad',-1,4,'n1'),
('goto',4),
('win',0),
('lose')
]            

currentHack = Hackable(puzzle1)
hacking=False
                        
def hackerView():
    global currentHack
    global hacking
    hacking = False
    size = (500,650)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("HACKER")
    timeLapse = 0
    ips = {'125.387.2.1':1, '125.311.0.1':2,'114.957.2.0':3,'125.278.2.1':4, '122.156.0.0':5 };
    compData = [('Professor Plum','125.387.2.1'),('Colonol Mustard','125.311.0.1'),('Ms. Scarlet','114.957.2.0'),('Waldo','125.278.2.1'), ('Sylica PD','122.156.0.0')];
    font = pygame.font.SysFont('Calibri', 25, False, False)
    smallFont = pygame.font.SysFont('Calibri', 15, False, False)
    compInput = pygame_textinput.TextInput(200,12,text_color=GREEN, cursor_color=GREEN)   
    instruct1 = font.render("Command/Input:", True, GREEN)    
    instruct2 = smallFont.render("Memory      - displays values in memory slots", False, GREEN)
    instruct3 = smallFont.render("Step          - run one line in the target program", False, GREEN)
    instruct4 = smallFont.render("Quit          - stop hacking", False, GREEN)
    instruct5 = smallFont.render("Data 'code' - downloads hacked data if the correct code is input", False, GREEN)
    instruct6 = smallFont.render("Restart     - resets the program", False, GREEN)
    instruct7 = smallFont.render("Run         - Run program until next input request.", False, GREEN)
    instruct8 = smallFont.render("If the command box is red, input a number for the program to use.", False, RED)
    codeLines=['','','','','','','','','','','','','','','','','','','','']
    error = smallFont.render("Bad Command or File Name", False, RED)
    names = []
    addresses = []
    for i in range(0,len(compData)):
        names.append(smallFont.render('Name: '+compData[i][0], False, GREEN));
        addresses.append(smallFont.render('IP: '+compData[i][1], False, GREEN));     
    homeInstruct2 = smallFont.render("Type IP address to hack computer", False, GREEN)
    compIcon = pygame.image.load("computerIcon.jpg").convert()
    compIcon = pygame.transform.scale(compIcon, (30,30))
    inputColor = GREEN
    memText = ''
    dataLines=[]
    gettingInput=False
    receivedInput=''
    while True:
        events = pygame.event.get()
        compEnter = compInput.update(events)
        screen.fill((0,0,0))
        screen.blit(compInput.get_surface(), [200,12])
        pygame.draw.rect(screen, inputColor, (199,7,150,25),1)
        screen.blit(instruct1, [20,10])
        screen.blit(homeInstruct2, [20,38])
        screen.blit(instruct4, [20,58])
        screen.blit(instruct5, [20,78])
        for i in range(0,len(compData)):
            screen.blit(compIcon, [30,i*85+120])
            screen.blit(names[i], [70,i*85+120])
            screen.blit(addresses[i],[70,i*85+137])
        pygame.display.flip()
        if compEnter:
            currentInput = compInput.get_text()
            if currentInput in ips.keys():
                currentHack = Hackable(hacks.puzzles[ips[currentInput]])
                hacking=True
                break
        for event in events:
            powerUse = 0
            if event.type == pygame.QUIT:
                done = True
                print ("quit pressed")
                pygame.quit()
                return False
            
    while True:
        events = pygame.event.get()
        compEnter = compInput.update(events)
        for event in events:
            powerUse = 0
            if event.type == pygame.QUIT:
                done = True
                print ("quit pressed")
                pygame.quit()
                return True
        if hacking:
            if currentHack.current==0 and 'True' in currentHack.steps[0](i=0, cod=True):
                inputColor = RED
            if compEnter:
                #print("enter pressed")
                currentInput = compInput.get_text()
                for i in range(0,len(codeLines)-1):
                    codeLines[i]=codeLines[i+1]
                if inputColor==RED:
                    try:
                        testInput=int(currentInput)
                    except:
                        continue     
                    codeLines[-1]=currentHack.step(inp=currentInput)
                    f = open('attempt.txt','a')
                    f.write(codeLines[-1]+'\n')
                    f.close()                    
                else:
                    if currentInput.lower() == 'step':
                        codeLines[-1]=currentHack.step()
                        f=open('attempt.txt','a')
                        f.write(codeLines[-1]+'\n')
                        f.close()
                    elif currentInput.lower() == 'run':
                        f=open('attempt.txt','a')
                        while True:
                            if 'True' in currentHack.steps[currentHack.current](cod=True):
                                inputColor=RED
                                break
                            else:
                                codeLines[-1]=currentHack.step()
                                for i in range(0,len(codeLines)-1):
                                    codeLines[i]=codeLines[i+1]
                                f.write(codeLines[-1]+'\n')
                                if 'Hack Successful' in codeLines[-1] or 'Program Restarting' in codeLines[-1]:
                                    break
                        f.close()                     
                    elif currentInput.lower() == 'memory':
                        memText=''
                        for ii in range(0,len(currentHack.r)):
                            memText = memText + " " + str(ii) + "(" + str(currentHack.r[ii]) + ") "
                    elif 'data' in currentInput.lower():
                        code = currentInput.lower()[5:]
                        memText = currentHack.getData(code)
                    elif 'quit' == currentInput.lower():
                        hacking=False
                        codeLines=['','','','','','','','','','','','','','','','','','','','']
                        memText=''
                        return True
                    elif 'restart'==currentInput.lower():
                        currentHack.lose(False)
                        codeLines=['','','','','','','','','','','','','','','','','','','','']
                        memText=''
                    else:
                        pass
                try:
                    if 'True' in currentHack.steps[currentHack.current](cod=True):
                        inputColor=RED
                    else:
                        #print("changing to black")
                        inputColor=GREEN
                except:
                    pass
        screen.fill((0,0,0)) 
        screen.blit(compInput.get_surface(), [200,12])
        pygame.draw.rect(screen, inputColor, (199,7,150,25),1)
        screen.blit(instruct2, [20,38])
        screen.blit(instruct3, [20,56])
        screen.blit(instruct4, [20,74])
        #screen.blit(instruct5, [20,92])
        screen.blit(instruct1, [20,10])
        screen.blit(instruct6, [20,92])
        screen.blit(instruct7, [20,110])
        screen.blit(instruct8, [20,128])
        screen.blit(smallFont.render(codeLines[0], False, GREEN),[20,205+20*19])
        screen.blit(smallFont.render(codeLines[1], False, GREEN),[20,205+20*18])
        screen.blit(smallFont.render(codeLines[2], False, GREEN),[20,205+20*17])
        screen.blit(smallFont.render(codeLines[3], False, GREEN),[20,205+20*16])
        screen.blit(smallFont.render(codeLines[4], False, GREEN),[20,205+20*15])
        screen.blit(smallFont.render(codeLines[5], False, GREEN),[20,205+20*14])
        screen.blit(smallFont.render(codeLines[6], False, GREEN),[20,205+20*13])
        screen.blit(smallFont.render(codeLines[7], False, GREEN),[20,205+20*12])
        screen.blit(smallFont.render(codeLines[8], False, GREEN),[20,205+20*11])
        screen.blit(smallFont.render(codeLines[9], False, GREEN),[20,205+20*10])
        screen.blit(smallFont.render(codeLines[10], False, GREEN),[20,205+20*9])
        screen.blit(smallFont.render(codeLines[11], False, GREEN),[20,205+20*8])
        screen.blit(smallFont.render(codeLines[12], False, GREEN),[20,205+20*7])
        screen.blit(smallFont.render(codeLines[13], False, GREEN),[20,205+20*6])
        screen.blit(smallFont.render(codeLines[14], False, GREEN),[20,205+20*5])
        screen.blit(smallFont.render(codeLines[15], False, GREEN),[20,205+20*4])
        screen.blit(smallFont.render(codeLines[16], False, GREEN),[20,205+20*3])
        screen.blit(smallFont.render(codeLines[17], False, GREEN),[20,205+20*2])
        screen.blit(smallFont.render(codeLines[18], False, GREEN),[20,205+20*1])
        screen.blit(smallFont.render(codeLines[19], False, GREEN),[20,205+20*0])
        screen.blit(smallFont.render(memText[0:78], False, GREEN),[20,160])
        screen.blit(smallFont.render(memText[78:], False, GREEN),[20,180])
        pygame.display.flip()
    return True

while hackerView():
    pass

