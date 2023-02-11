#-------------------------------------------------------------------------------
#Danyal Rana

#12/22/2016

#Christmas Animation

#The purpose of this program is to serve as a Christmas themed animation

#-------------------------------------------------------------------------------

#Importing modules
import pygame, random
import sys
from pygame.locals import *
pygame.init()

#Setting screen size and window title
WINDOW=pygame.display.set_mode((1200,700))
pygame.display.set_caption(((str)("Merry Christmas!             "))*8)

#Fps code
fpsClock=pygame.time.Clock()

#Colour codes, for future reference
white=(255,255,255)
orange=(235, 137, 33)
black=(0,0,0)
yellow=(255,255,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
peach=(234,192,134)
mouth=(234,200,100)
brown=(102, 51, 0)
darkBlue=(0,24,72)
moonBlue=(192, 192, 240)
grey=(128,128,128)
lightGrey=(180,180,180)

#Christmas colours that will swap between eachother
colour1=red
colour2=green

#Declaring variables to change between elf and snowman positions, and move him across the screen
z=0
c=1
w=1
b=0
y=0
count=0
count1=0

#Prtinting interaction keys
print("Press 'Spacebar' key to alternate between Christmas colours!")
print("Hold'Left' key to make him look back!")

#Closes window when user clicks the 'x' on the top right of the window
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

#If user presses spacebar, colours change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                colour1=green
                colour2=red

#Using a count to switch colours again if spacebar is pressed again, rather than spacebar only changing colours once
                count1+=1
                if count1==2:
                    colour1=red
                    colour2=green
                    count1=0

#Sky
    WINDOW.fill(darkBlue)

#Moon
    pygame.draw.circle(WINDOW,moonBlue,(200,150),200,0)

#Farthest hills and black highlight around them
    pygame.draw.ellipse(WINDOW,grey,(500,330,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(500,330,900,400),1)
    pygame.draw.ellipse(WINDOW,grey,(100,330,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(100,330,900,400),1)
    pygame.draw.ellipse(WINDOW,grey,(-300,330,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(-300,330,900,400),1)

#Closest hills, and black highlight around them
    pygame.draw.ellipse(WINDOW,lightGrey,(-500,430,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(-500,430,900,400),1)
    pygame.draw.ellipse(WINDOW,lightGrey,(0,430,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(0,430,900,400),1)
    pygame.draw.ellipse(WINDOW,lightGrey,(500,430,900,400),0)
    pygame.draw.ellipse(WINDOW,black,(500,430,900,400),1)


#North Pole sign
    pygame.draw.line(WINDOW,colour1,(900,50),(900,700),25)
    pygame.draw.line(WINDOW,white,(910,100),(1150,100),50)
    pygame.draw.line(WINDOW,white,(887,100),(660,100),50)
    pygame.draw.polygon(WINDOW,white,((660,76),(660,125),(610,100)),0)
    pygame.draw.polygon(WINDOW,white,((1150,76),(1150,125),(1200,100)),0)

#Merry Christmas Sign
    pygame.draw.rect(WINDOW,white,(25,75,574,124),0)
    pygame.draw.rect(WINDOW,colour2,(25,75,574,20),0)
    pygame.draw.rect(WINDOW,colour2,(25,179,574,20),0)
    pygame.draw.line(WINDOW,colour2,(100,190),(100,530),25)
    pygame.draw.line(WINDOW,colour2,(525,190),(525,530),25)
    pygame.draw.rect(WINDOW,colour1,(37,87,550,100),25)


#Different text for every other letter in 'Merry Christmas' to alternate between colours
    font=pygame.font.SysFont("adobedevanagariitalic",60,False,False)
    text=font.render("M  r  y C  r  s  m  s ",True,colour2)
    font=pygame.font.SysFont("adobedevanagariitalic",60,False,False)
    text1=font.render("   e  r      h  i  t    a  !",True,colour1)

#'Try spacebar' text
    font=pygame.font.SysFont("Mistral",30,False,False)
    text2=font.render("Try'Spacebar'!",True,colour2)

#Different text for "By:","Danyal", and "Rana" to alternate between colours
    font=pygame.font.SysFont("PLAYBILL",30,False,False)
    text3=font.render("By:",True,colour2)

    font=pygame.font.SysFont("PLAYBILL",30,False,False)
    text6=font.render("Danyal",True,colour1)

    font=pygame.font.SysFont("PLAYBILL",30,False,False)
    text7=font.render("Rana",True,colour2)

#'Santas workshop' text
    font=pygame.font.SysFont("adobedevanagariitalic",30,False,False)
    text4=font.render("Santa's  Workshop --> ",True,colour2)

#'Try holding left key' text
    font=pygame.font.SysFont("Mistral",30,False,False)
    text5=font.render("Try Holding 'left' key!",True,colour1)

#'Dangerous snowmen!' text
    font=pygame.font.SysFont("adobedevanagariitalic",28,False,False)
    text8=font.render("<--Dangerous snowmen! ",True,colour2)

#Setting location for each text line
    WINDOW.blit(text,(100,105))
    WINDOW.blit(text1,(112,105))
    WINDOW.blit(text2,(750,10))
    WINDOW.blit(text3,(20,10))
    WINDOW.blit(text4,(920,80))
    WINDOW.blit(text5,(900,10))
    WINDOW.blit(text6,(50,10))
    WINDOW.blit(text7,(110,10))
    WINDOW.blit(text8,(620,80))

#Position #1 of elf and snowman
    if c==1:

#Elf arms and hands
        pygame.draw.line(WINDOW,colour2,(z,250),(z+100,150),35)
        pygame.draw.line(WINDOW,colour2,(z,250),(z-100,150),35)
        pygame.draw.line(WINDOW,peach,(z+90,160),(z+120,135),35)
        pygame.draw.line(WINDOW,peach,(z-90,160),(z-120,135),35)

#Top of elf legs
        pygame.draw.line(WINDOW,colour1,(z,400),(z-10,450),35)
        pygame.draw.line(WINDOW,colour1,(z,400),(z+30,450),35)

#Bottom of elf legs
        pygame.draw.line(WINDOW,colour2,(z-50,500),(z-10,450),35)
        pygame.draw.line(WINDOW,colour2,(z+50,500),(z+30,450),35)

#Snowman arms
        pygame.draw.line(WINDOW,brown,(w-350,240),(w-150,240),10)
        pygame.draw.line(WINDOW,brown,(w-300,240),(w-460,240),10)

#Snowman fingers
        pygame.draw.line(WINDOW,brown,(w-180,240),(w-175,215),10)
        pygame.draw.line(WINDOW,brown,(w-180,240),(w-175,270),10)
        pygame.draw.line(WINDOW,brown,(w-430,240),(w-440,215),10)
        pygame.draw.line(WINDOW,brown,(w-430,240),(w-440,270),10)

#Using count to alternate between positions at a set speed (Change positions when count is a specific number, so it doesnt transition too fast)
        count+=1

#Resetting Animations
        if z>2000:
            z=0
            w=0
        if count==3:
            c=0
            count=0
        if b>900:
            b=0
        if y>650:
            y=0

#Position #2 of elf and snowman
    else:

#Elf arms
        pygame.draw.line(WINDOW,colour2,(z,250),(z+100,200),35)
        pygame.draw.line(WINDOW,colour2,(z,250),(z-100,200),35)

#Elf hands
        pygame.draw.line(WINDOW,peach,(z-100,200),(z-130,182),35)
        pygame.draw.line(WINDOW,peach,(z+100,200),(z+130,182),35)


#Top of elf legs
        pygame.draw.line(WINDOW,colour1,(z,400),(z-50,450),35)
        pygame.draw.line(WINDOW,colour1,(z,400),(z+70,430),35)

#Bottom of elf legs
        pygame.draw.line(WINDOW,colour2,(z-100,470),(z-50,450),35)
        pygame.draw.line(WINDOW,colour2,(z+70,430),(z+100,480),35)

#Elf knees (To fill in blank spots and make it look more like knees)
        pygame.draw.circle(WINDOW,colour2,(z-50,450),16,0)
        pygame.draw.circle(WINDOW,colour2,(z+70,430),16,0)

#Snowman arms
        pygame.draw.line(WINDOW,brown,(w-330,230),(w-180,190),10)
        pygame.draw.line(WINDOW,brown,(w-300,240),(w-450,190),10)

#Snowman fingers
        pygame.draw.line(WINDOW,brown,(w-440,230),(w-420,200),10)
        pygame.draw.line(WINDOW,brown,(w-420,170),(w-420,200),10)
        pygame.draw.line(WINDOW,brown,(w-190,225),(w-200,200),10)
        pygame.draw.line(WINDOW,brown,(w-200,170),(w-200,200),10)

#Setting count to 0 to switch back to position 1, but at a fixed rate
        count+=1
        if count==3:
            c=1
            count=0

#Snowman parts that dont change position

#Snowman body
    pygame.draw.circle(WINDOW,white,(w-300,170),50,0)
    pygame.draw.circle(WINDOW,white,(w-300,280),75,0)
    pygame.draw.circle(WINDOW,white,(w-300,410),100,0)

#Snowman buttons
    pygame.draw.circle(WINDOW,black,(w-260,400),10,0)
    pygame.draw.circle(WINDOW,black,(w-260,325),10,0)
    pygame.draw.circle(WINDOW,black,(w-260,250),10,0)

#Snowman mouth
    pygame.draw.circle(WINDOW,black,(w-295,190),3,0)
    pygame.draw.circle(WINDOW,black,(w-290,187),3,0)
    pygame.draw.circle(WINDOW,black,(w-285,185),3,0)
    pygame.draw.circle(WINDOW,black,(w-280,185),3,0)
    pygame.draw.circle(WINDOW,black,(w-275,185),3,0)
    pygame.draw.circle(WINDOW,black,(w-270,187),3,0)

#Snowman eyes
    pygame.draw.circle(WINDOW,black,(w-300,150),8,0)
    pygame.draw.circle(WINDOW,black,(w-270,150),8,0)

#Snowman eyebrows
    pygame.draw.line(WINDOW,black,(w-310,140),(w-290,145),3)
    pygame.draw.line(WINDOW,black,(w-280,145),(w-260,135),3)

#Snowman nose
    pygame.draw.polygon(WINDOW,orange,((w-275,170),(w-280,180),(w-230,175)))

#Snowman hat
    pygame.draw.rect(WINDOW,black,(w-340,60,80,80),0)
    pygame.draw.line(WINDOW,black,(w-240,135),(w-360,135),10)
    pygame.draw.line(WINDOW,colour2,(w-260,110),(w-340,110),20)

#Parts of the elf that dont move positions

#Elf neck
    pygame.draw.line(WINDOW,peach,(z,185),(z,220),30)

#Elf body/shirt
    pygame.draw.line(WINDOW,colour2,(z,220),(z,400),45)
    pygame.draw.line(WINDOW,colour1,(z,220),(z,250),45)
    pygame.draw.line(WINDOW,colour1,(z,280),(z,310),45)
    pygame.draw.line(WINDOW,colour1,(z,340),(z,370),45)

#Elf head
    pygame.draw.circle(WINDOW,peach,(z,130),70,0)

#Elf eyes
    pygame.draw.circle(WINDOW,white,(z+25,120),20,0)
    pygame.draw.circle(WINDOW,white,(z-25,120),20,0)
    pygame.draw.circle(WINDOW,black,(z+37,120),5,0)
    pygame.draw.circle(WINDOW,black,(z-15,120),5,0)

#Cloth that connects the hat and the pompom
    pygame.draw.line(WINDOW,colour2,(z-105,130),(z-70,90),20)

#The hats core(Part on the elfs head)
    pygame.draw.polygon(WINDOW, colour2,((z-80,100),(z-70,70),(z-40,40),(z,30),(z+30,40),(z+60,70),(z+70,90),(z+30,80)),0)

#Hat pompom
    pygame.draw.circle(WINDOW,colour1,(z-115,130),15)

#Elf ears
    pygame.draw.polygon(WINDOW,peach,((z-70,140),(z-80,120),(z-90,90),(z-75,100),(z-60,100)),0)
    pygame.draw.polygon(WINDOW,peach,((z+70,140),(z+80,120),(z+90,90),(z+75,100),(z+60,100)),0)

#Hat lining around the edges
    pygame.draw.arc(WINDOW,colour1,(z-70,80,145,40),0.05235987756,3.1415926536 ,10)

#Elf mouth
    pygame.draw.ellipse(WINDOW,black,(z-15,170,30,10),0)

#Elf eyebrow
    pygame.draw.line(WINDOW,black,(z-50,100),(z-15,85),3)
    pygame.draw.line(WINDOW,black,(z+15,85),(z+50,100),3)

#Elf top of nose
    pygame.draw.line(WINDOW,black,(z,135),(z+10,145),3)

#Elf bottom of nose
    pygame.draw.arc(WINDOW,black,(z-18,130,30,30),5.235987756,6.2831853072,2)

#Snowy ground
    pygame.draw.line(WINDOW,white,(0,700),(1900,700),400)

#Snowflakes
    pygame.draw.circle(WINDOW,white,(15,y-55),5,0)
    pygame.draw.circle(WINDOW,white,(300,y+2),5,0)
    pygame.draw.circle(WINDOW,white,(150,b-122),5,0)
    pygame.draw.circle(WINDOW,white,(11,y+200),5,0)
    pygame.draw.circle(WINDOW,white,(400,b+44),5,0)
    pygame.draw.circle(WINDOW,white,(223,y+12),5,0)
    pygame.draw.circle(WINDOW,white,(700,y-40),5,0)
    pygame.draw.circle(WINDOW,white,(153,b+30),5,0)
    pygame.draw.circle(WINDOW,white,(235,y),5,0)
    pygame.draw.circle(WINDOW,white,(786,y-55),5,0)
    pygame.draw.circle(WINDOW,white,(334,y+2),5,0)
    pygame.draw.circle(WINDOW,white,(855,b-122),5,0)
    pygame.draw.circle(WINDOW,white,(563,y+200),5,0)
    pygame.draw.circle(WINDOW,white,(460,b+44),5,0)
    pygame.draw.circle(WINDOW,white,(223,y+12),5,0)
    pygame.draw.circle(WINDOW,white,(900,y-40),5,0)
    pygame.draw.circle(WINDOW,white,(600,b+30),5,0)
    pygame.draw.circle(WINDOW,white,(675,y),5,0)
    pygame.draw.circle(WINDOW,white,(786,y+300),5,0)
    pygame.draw.circle(WINDOW,white,(334,y+500),5,0)
    pygame.draw.circle(WINDOW,white,(855,b+235),5,0)
    pygame.draw.circle(WINDOW,white,(563,y+799),5,0)
    pygame.draw.circle(WINDOW,white,(460,b+123),5,0)
    pygame.draw.circle(WINDOW,white,(223,y+800),5,0)
    pygame.draw.circle(WINDOW,white,(900,y+665),5,0)
    pygame.draw.circle(WINDOW,white,(600,b+312),5,0)
    pygame.draw.circle(WINDOW,white,(123,b-700),5,0)
    pygame.draw.circle(WINDOW,white,(100,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(692,b-670),5,0)
    pygame.draw.circle(WINDOW,white,(324,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(122,b-520),5,0)
    pygame.draw.circle(WINDOW,white,(354,y-450),5,0)
    pygame.draw.circle(WINDOW,white,(234,b-331),5,0)
    pygame.draw.circle(WINDOW,white,(214,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(120,b-450),5,0)
    pygame.draw.circle(WINDOW,white,(354,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(450,y-465),5,0)
    pygame.draw.circle(WINDOW,white,(234,b-331),5,0)
    pygame.draw.circle(WINDOW,white,(214,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(990,b-450),5,0)
    pygame.draw.circle(WINDOW,white,(1100,y-500),5,0)
    pygame.draw.circle(WINDOW,white,(1000,b-340),5,0)
    pygame.draw.circle(WINDOW,white,(900,y-465),5,0)
    pygame.draw.circle(WINDOW,white,(15,y-80),5,0)
    pygame.draw.circle(WINDOW,white,(300,y+24),5,0)
    pygame.draw.circle(WINDOW,white,(150,b-0),5,0)
    pygame.draw.circle(WINDOW,white,(11,y+231),5,0)
    pygame.draw.circle(WINDOW,white,(400,b+45),5,0)
    pygame.draw.circle(WINDOW,white,(223,y+111),5,0)
    pygame.draw.circle(WINDOW,white,(700,y-400),5,0)
    pygame.draw.circle(WINDOW,white,(153,b+900),5,0)
    pygame.draw.circle(WINDOW,white,(235,y),5,0)
    pygame.draw.circle(WINDOW,white,(786,y-600),5,0)
    pygame.draw.circle(WINDOW,white,(334,y+234),5,0)
    pygame.draw.circle(WINDOW,white,(855,b-180),5,0)
    pygame.draw.circle(WINDOW,white,(100,y+223),5,0)
    pygame.draw.circle(WINDOW,white,(900,b+523),5,0)
    pygame.draw.circle(WINDOW,white,(850,y+123),5,0)
    pygame.draw.circle(WINDOW,white,(900,y-434),5,0)
    pygame.draw.circle(WINDOW,white,(600,b+377),5,0)
    pygame.draw.circle(WINDOW,white,(1100,y),5,0)
    pygame.draw.circle(WINDOW,white,(786,y+302),5,0)
    pygame.draw.circle(WINDOW,white,(334,y+242),5,0)
    pygame.draw.circle(WINDOW,white,(855,b+278),5,0)
    pygame.draw.circle(WINDOW,white,(563,y+457),5,0)
    pygame.draw.circle(WINDOW,white,(460,b+167),5,0)
    pygame.draw.circle(WINDOW,white,(223,y+3),5,0)
    pygame.draw.circle(WINDOW,white,(900,y+355),5,0)
    pygame.draw.circle(WINDOW,white,(600,b+56),5,0)
    pygame.draw.circle(WINDOW,white,(1150,b-23),5,0)
    pygame.draw.circle(WINDOW,white,(1200,y-512),5,0)
    pygame.draw.circle(WINDOW,white,(1070,b-11),5,0)
    pygame.draw.circle(WINDOW,white,(324,y-125),5,0)
    pygame.draw.circle(WINDOW,white,(122,b-457),5,0)
    pygame.draw.circle(WINDOW,white,(354,y-347),5,0)
    pygame.draw.circle(WINDOW,white,(234,b-100),5,0)
    pygame.draw.circle(WINDOW,white,(214,y-77),5,0)
    pygame.draw.circle(WINDOW,white,(120,b-11),5,0)
    pygame.draw.circle(WINDOW,white,(354,y-22),5,0)
    pygame.draw.circle(WINDOW,white,(450,y-808),5,0)
    pygame.draw.circle(WINDOW,white,(234,b-444),5,0)
    pygame.draw.circle(WINDOW,white,(214,y-333),5,0)
    pygame.draw.circle(WINDOW,white,(990,b-222),5,0)
    pygame.draw.circle(WINDOW,white,(1100,y-122),5,0)
    pygame.draw.circle(WINDOW,white,(1000,b-352),5,0)
    pygame.draw.circle(WINDOW,white,(900,y-465),5,0)

#Elf looks back as long as the user holds left
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

#Adding white part again to overlap previous eyes
                pygame.draw.circle(WINDOW,white,(z+25,120),20,0)
                pygame.draw.circle(WINDOW,white,(z-25,120),20,0)
                pygame.draw.circle(WINDOW,black,(z+15,120),5,0)
                pygame.draw.circle(WINDOW,black,(z-35,120),5,0)

#Adding value to variables to make animation move
    b+=7
    z+=10
    y+=5
    w+=8

#Esential screen update code
    pygame.display.update()

#Fps set
    fpsClock.tick(20)
