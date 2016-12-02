#coding=utf-8
# 1 - import library导入pygame库

import time
import random
import math
import pygame
from pygame.locals import *
'''
2 - initialize the game
初始化pygame并设置显示窗口
'''
pygame.init()
width,height = 1000, 600
#使用一个数组保存键盘键的按下状态； 定义玩家初始位置
keys = [False,False,False,False,False,False,False,False]
playerpos=[100,100]   
screen=pygame.display.set_mode((width,height))

PI=3.1415926

#主角添加更多的动作：发射苦无
acc = [0,0]  #变量：记录苦无射击精度 命中/发射

arrows = []  
wuqi="arrow"





#敌人
bosstimer=1000                  #计时器，每秒每帧地减少它到0,就出敌兵
bosstimer1=0

badtimer=100
badtimer1=0

maotimer=1000
maotimer1=0


showtimer=0                          #计时器
showtime=15                           #攻击特效持续时间
showtime2=1
showtime3=18
daoqitimer=0
daoqitime=18

tudunexistimer=0                   #像天照这种，显示完全跟开关状态一致的，就不用timer
#tianzhaotimer=0                 #像土遁这种，显示有延迟的，开关关闭后一定时间内都会持续的，就要timer计时

oddeven=1                             #记录一下形态，P1：鼬，P2:佐助，即奇数鼬，偶数佐助


tianzhaoUP=False                           #这些就像开关一样
huoqiushuUP=False
hqsexist=False
tudunUP=False
tudunexist=False


o=0   
justnow=(-888,-888)


bosses=[[1000,100]]    #第1个出现的位置给出了
rzs=[[1000,300]]
maos=[[500,400]]

xuzuos =[]


hqs1=[0,0]
hqs2=[0,0]
hqs3=[0,0]


healthvalue=194
#初始化混音器
pygame.mixer.init()


# 3- 加载图片

player2 = pygame.image.load("resources/images/hy/z.png")
player = pygame.image.load("resources/images/hy/y.png")
player3 = pygame.image.load("resources/images/hy/gj.png")
bg1 = pygame.image.load("resources/images/hy/bg.png")
bg2 = pygame.image.load("resources/images/hy/bg2.png")
bg = bg1
start = pygame.image.load("resources/images/hy/begin.png")

tianzhao = pygame.image.load("resources/images/hy/tianzhao.png")
huoqiushu = pygame.image.load("resources/images/hy/huoqiushu.png")
tudun = pygame.image.load("resources/images/hy/tudun.png")

xuzuogongjian = pygame.image.load("resources/images/hy/xuzuo.png")

attack = pygame.image.load("resources/images/hy/attack.png")
attack2 = pygame.image.load("resources/images/hy/attacklight.png")
attack3 = pygame.image.load("resources/images/hy/xly.png")
attack4 = pygame.image.load("resources/images/hy/shui.png")

tishenshu = pygame.image.load("resources/images/hy/tishenshu.png")
dq0 = pygame.image.load("resources/images/hy/0.png")
dq1 = pygame.image.load("resources/images/hy/1.png")
dq2 = pygame.image.load("resources/images/hy/2.png")
dq3 = pygame.image.load("resources/images/hy/3.png")
dq4 = pygame.image.load("resources/images/hy/4.png")
dq5 = pygame.image.load("resources/images/hy/5.png")

castle1 = pygame.image.load("resources/images/hy/yan.png")
castle2 = pygame.image.load("resources/images/hy/mu.png")
castle3 = pygame.image.load("resources/images/hy/sha.png")
castle4 = pygame.image.load("resources/images/hy/wu.png")

arrow2 = pygame.image.load("resources/images/hy/lighting.png")
arrow = pygame.image.load("resources/images/hy/bullet.png")
arrow3 = pygame.image.load("resources/images/hy/shayu.png")

dsw1 = pygame.image.load("resources/images/hy/she.png")
dsw=dsw1  #设置一个图片副本，以便动起来

dswmao1 = pygame.image.load("resources/images/hy/mc.png")
dswmao=dswmao1


rz1 = pygame.image.load("resources/images/hy/rz1.png")
rztu = rz1



healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")#血条

gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

#3.1加载声音及音量大小
# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")#简单的音频文件
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hq = pygame.mixer.Sound("resources/audio/hqs.wav")
xly = pygame.mixer.Sound("resources/audio/xielunyan.wav")
sy = pygame.mixer.Sound("resources/audio/shayu.wav")
tu = pygame.mixer.Sound("resources/audio/tu.ogg")
tz = pygame.mixer.Sound("resources/audio/tianzhao.wav")
bgmy = pygame.mixer.Sound("resources/audio/qianye.wav")

bgmy.set_volume(0.36)
tz.set_volume(0.66)
tu.set_volume(0.5)
sy.set_volume(0.36)
xly.set_volume(0.28)
hit.set_volume(0.05)
enemy.set_volume(0.08)
shoot.set_volume(0.05)

hq.set_volume(0.3)
pygame.mixer.music.load('resources/audio/hy.mp3')#游戏背景音乐
#pygame.mixer.music.play(-1, 0.0)                        #    一直重复
pygame.mixer.music.play(-1, 0.0)    
pygame.mixer.music.set_volume(0.25)


'''
4 - keep looping through
循环执行以下缩进的代码
'''

# 4 - keep looping through
running = 0
exitcode = 0    #running变量跟踪游戏是否结束，exitcode变量跟踪玩家是赢了还是输了。
begin = 1
begintime=666
begintimer=begintime
n=9
#pausetimer =666


while begin:
    begintimer-=1
    screen.fill((255,255,255))
    for n in (1,2,3,4,5,6,7,8,9):
        if begintimer<=(begintime*n/9): 
            screen.blit(start,(333*(n%3),200*(3-((n+2)//3))),(333*(n%3),200*(3-((n+2)//3)),333,200),0)
        #if begintimer<=(begintime*8/9): 
           # screen.blit(start,(0,0),(0,0,333,200),0)
            n-=1
        
        
    #blit(source, dest, area=None, special_flags = 0) -> Rect
    pygame.display.flip()
    if begintimer<=-88:
        begin=0
        running=1

               
while running:
  
    badtimer-=1
    bosstimer-=1
    showtimer-=1
    maotimer-=1
    tudunexistimer-=1
    daoqitimer-=1
    #tianzhaotimer-=1
 
    
    
    '''
    while 1:
        badtimer-=1  #decrement the value of badtimer for each frame: 每帧都在倒计时
    '''   
    #5 绘图前，将屏幕填充为黑色
    screen.fill(0)
    #6 将之前加载的图片在第四象限（x,y）的位置显示在屏幕上
    
    screen.blit(bg,(0,0))
    if tianzhaoUP==True:
        screen.blit(tianzhao,(0,0))
    
    
    
    screen.blit(castle1,(0,30))
    screen.blit(castle2,(0,180))
    screen.blit(castle3,(0,330))
    screen.blit(castle4,(0,480))
    
    # 6.1 - Set player position and rotation 替换之前的 screen.blit(player,playerpos) 
    # 贴上玩家，并且利用鼠标位置、玩家位置，构造三角函数，计算角度弧度。
    # 6.2   atan  player和mouse x坐标差除以y坐标差
    #数学方面的知识再慢慢消化
    
    
    
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
 
    playerrot = pygame.transform.rotate(player,-angle*57.29)        #python里逆时针正数，顺时针负数
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)#rect是矩形实例
    if player!=player3:
        screen.blit(playerrot, playerpos1)
    elif player==player3:
        screen.blit(player, playerpos1)    #鬼鲛因为图片原因还是不能转的好
    
    #screen.blit(playerrot, playerpos1)
    #screen.blit(playerrot, playerpos)
    #playerrot还是属于对象（亦及加载的图片），只是已经旋转过，成为另一个对象了。
    
    
    
    
    # 6.3 - 贴弓箭
    #index=0
    for bullet in arrows:  #数组里的元素，就是子弹bullet
        index=0          
                           #这样弓箭占存的数目永远会维持在较低水平。
                           
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10   #速度分量
        bullet[1]+=velx      
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>920 or bullet[2]<-64 or bullet[2]>580:
            arrows.pop(index)   
        index+=1     #这句话好像是没什么用，无利无弊。
     
        
        for bullet in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-bullet[0]*57.29)
            screen.blit(arrow1, (bullet[1], bullet[2]))
        
    
    #6.3-贴敌方boss大蛇丸
    
    
    
    if bosstimer==0:
        bosses.append([1000,random.randint(50,500)])
        bosstimer=1000-(bosstimer1*2)#badtimer1变大ing:出敌人频率上升     
        if bosstimer1>=100:
            bosstimer1=100
        else:
            bosstimer1+=5
    index=0
    for boss in bosses:
        if boss[0]<-64:
            bosses.pop(index)
        boss[0]-=6         #大蛇丸的速度
        #6.3.1 攻击城堡
        bossrect=pygame.Rect(dsw.get_rect())
        bossrect.top=boss[1]
        bossrect.left=boss[0]
        if bossrect.left<64:
            # section 6.3.1 after if badrect.left<64:
            hit.play()
            healthvalue -= random.randint(8,20)#还有暴击2333
            bosses.pop(index)
        if tudunexist==True:
            bossrect=pygame.Rect(dsw.get_rect())
            bossrect.top=rz[1]
            bossrect.left=rz[0]                                #土遁持续时
            if bossrect.left<940 and bossrect.left>648:             #土遁范围680-780  宽度168
                bosses.pop(index)
        
            
        #6.3.2attack
        index1=0
        
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if bossrect.colliderect(bullrect):
            #矩形是否相交
                # section 6.3.2 after if badrect.colliderect(bullrect):
                enemy.play()
                acc[0]+=1
                if len(bosses)!=0 and index<=(len(rzs)-1):
                    justnow = bosses[index]
                    bosses.pop(index)   
                arrows.pop(index1)
                
                screen.blit(tishenshu,boss) 
                showtimer = showtime
            index1+=1
        if showtime>0:
            screen.blit(tishenshu,justnow)
        
        
        if daoqitimer>0 and math.sqrt((boss[0]-(playerpos1[0]+76))**2+(boss[1]-(playerpos1[1]+96))**2)<=126:
                
            enemy.play()               
            if len(bosses)!=0 and index<=(len(bosses)-1):           #问题1：   index比len()-1还大
                justnow = bosses[index]
                bosses.pop(index)                     
                showtimer = showtime
                screen.blit(tishenshu,boss)
        
        #6.3.3-下一个大蛇丸
        index+=1
    for boss in bosses:
        screen.blit(dsw,boss)
        
        
        
        
        
        
        
             #冒出大蛇丸
    if maotimer==0:
        maos.append([random.randint(300,1000),random.randint(50,500)])
        maotimer=500-(maotimer1*2)#badtimer1变大ing:出敌人频率上升     
        if maotimer1>=100:
            maotimer1=100
        else:
            maotimer1+=5
    index=0
    for mao in maos:
        if mao[0]<-64:
            maos.pop(index)
        mao[0]-=3.6        #大蛇丸的速度
        #6.3.1 攻击城堡
        maorect=pygame.Rect(dswmao1.get_rect())
        maorect.top=mao[1]
        maorect.left=mao[0]
        if maorect.left<64:
            # section 6.3.1 after if badrect.left<64:
            hit.play()
            healthvalue -= random.randint(8,20)#还有暴击2333
            maos.pop(index)
        
        if tudunexist==True:
            maorect=pygame.Rect(dswmao1.get_rect())
            maorect.top=rz[1]
            maorect.left=rz[0]                                #土遁持续时
            if maorect.left<940 and maorect.left>648:             #土遁范围680-780  宽度168
                maos.pop(index)
            
        #6.3.2attack
        index1=0
        
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if maorect.colliderect(bullrect):
            #矩形是否相交
            # section 6.3.2 after if badrect.colliderect(bullrect):
                enemy.play()
                acc[0]+=1
                if len(maos)!=0 and index<=(len(rzs)-1):
                    justnow = maos[index]
                    maos.pop(index)
                arrows.pop(index1)
                
                screen.blit(tishenshu,mao) 
                showtimer = showtime
            index1+=1
        if showtimer>0:  
            screen.blit(tishenshu,justnow)
        
        if daoqitimer>0 and math.sqrt(((mao[0]+60)-(playerpos1[0]+76))**2+((mao[1]+60)-(playerpos1[1]+96))**2)<=126:
                
            enemy.play()               
            if len(maos)!=0 and index<=(len(maos)-1):           #问题1：   index比len()-1还大
                justnow = maos[index]
                maos.pop(index)                    
                showtimer = showtime
                screen.blit(tishenshu,mao)
        
        
        
        #6.3.3-下一个大蛇丸
        index+=1
    for mao in maos:
        screen.blit(dswmao,mao)
        
       
        
        
        
        
        
        
        
  
   
   #贴敌方忍者小兵
    
    
    
    if badtimer==0:
        rzs.append([1000,random.randint(8,500)])
        badtimer=100-(badtimer1*2)#badtimer1变大ing:出獾的频率越来越快？
        if badtimer1>=30:
            badtimer1=30
        else:
            badtimer1+=5
    index=0                                                                                    
    for rz in rzs:
        if rz[0]<-64:
            rzs.pop(index)
        rz[0]-=2  #速度      
        #6.3.1 
        rzrect=pygame.Rect(rztu.get_rect())
        rzrect.top=rz[1]
        rzrect.left=rz[0]
        if rzrect.left<64:                                
            # section 6.3.1 after if badrect.left<64:
            hit.play()
            healthvalue -= random.randint(2,6)#还有暴击2333
            rzs.pop(index)    
        
        
        if tudunexist==True:
            rzrect=pygame.Rect(rztu.get_rect())
            rzrect.top=rz[1]
            rzrect.left=rz[0]                                #土遁持续时
            if rzrect.left<940 and rzrect.left>648:             #土遁范围680-780  宽度168
                rzs.pop(index)
            
        #6.3.2attack
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if rzrect.colliderect(bullrect):
            #矩形是否相交
                # section 6.3.2 after if badrect.colliderect(bullrect):
                
                enemy.play()
                acc[0]+=1
                if len(rzs)!=0 and index<=(len(rzs)-1):           #问题1：   index比len()-1还大
                    justnow = rzs[index]
                    rzs.pop(index)        #pop index out of range  
                arrows.pop(index1)        #问题2：   len()=0    已解决ok
                                          #终于知道为什么有时候，会pop一个空的list了！！！！
                
                #if showtimer!=0:                           #因为多支箭打中同一个敌人！！！
                screen.blit(attack,rz) 
                
                showtimer = showtime
        
            index1+=1
        if daoqitimer>0 and math.sqrt((rz[0]-(playerpos1[0]+76))**2+(rz[1]-(playerpos1[1]+96))**2)<=100:
                
            enemy.play()               
            if len(rzs)!=0 and index<=(len(rzs)-1):           #问题1：   index比len()-1还大
                justnow = rzs[index]
                rzs.pop(index)        
                screen.blit(attack,rz) 
                showtimer = showtime
        #if showtimer>0:
        if showtimer>0:  
            screen.blit(attack,justnow)
        
        #创新：下一个小兵
        index+=1
    for rz in rzs:
        rztu = rz1
        screen.blit(rztu,rz)
        
        
    
   
    #6.4 贴时钟
    font = pygame.font.Font(None,24) #使用默认字体，24的大小
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))  #这一行非要顶头写，才表示接上行吗
    
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext,textRect)
    #再定位绘制到屏幕上
    
    #6.5贴血条
    screen.blit(healthbar,(5,5))  #bar分辨率200x20
    for health1 in range(healthvalue):   #health分辨率1x14
        screen.blit(health,(health1+8,8)) #??
        
    
    
   # if tianzhaoUP==True:
      #  bg = tianzhao
    #elif tianzhaoUP==False:
        #if attack ==pygame.image.load("resources/images/hy/attack.png"):
           # bg = bg1
       # elif attack ==pygame.image.load("resources/images/hy/attacklight.png"): 
         #   bg = bg2
                
    
    if huoqiushuUP==True:
        #hqs1=[random.randint(180,800),random.randint(20,100)]
        #hqs2=[random.randint(180,800),random.randint(200,380)]
        #hqs3=[random.randint(180,800),random.randint(480,500)]
        #screen.blit(huoqiushu,(random.randint(180,800),random.randint(20,100) ) )
        #screen.blit(huoqiushu,(random.randint(180,800),random.randint(200,380) ) )
        #screen.blit(huoqiushu,(random.randint(180,800),random.randint(480,500) ) )
        if hqsexist==False:
            hqs1=[random.randint(180,800),random.randint(1,68)]
            hqs2=[random.randint(180,800),random.randint(108,268)]
            hqs3=[random.randint(180,800),random.randint(360,380)]
        screen.blit(huoqiushu,hqs1)
        screen.blit(huoqiushu,hqs2)
        screen.blit(huoqiushu,hqs3)
        hqsexist=True
    
    if tudunUP==True:
        tudunexistimer=88
    if tudunUP==True or tudunexistimer>0:
        screen.blit(tudun,(random.randint(680,780),0))
        #screen.blit(tudun,(800,0))
        tudunexist=True
    else :
        tudunexist=False
        
    
    if wuqi=="daoqi" and daoqitimer>0:
        if 15<daoqitimer<=18:
            screen.blit(dq0,(playerpos1[0]+12,playerpos1[1]+20))
        if 12<daoqitimer<=15:
            screen.blit(dq1,(playerpos1[0]+12,playerpos1[1]+20))
        if 9<daoqitimer<=12:
            screen.blit(dq2,(playerpos1[0]+12,playerpos1[1]+20))
        if 6<daoqitimer<=9:
            screen.blit(dq3,(playerpos1[0]+12,playerpos1[1]+20))
        if 3<daoqitimer<=6:
            screen.blit(dq4,(playerpos1[0]+12,playerpos1[1]+20))
        if 0<daoqitimer<=3:
            screen.blit(dq5,(playerpos1[0]+12,playerpos1[1]+20))

        
   
        
        
        
                       
            
    #7 更新屏幕
    pygame.display.flip()
    #8 loop through the events检查任何新事件如果有的话，否则转到退出命令，退出程序.
    
    
        
    
       
    for event in pygame.event.get():
        
        #check if the event is the X button
        
        if event.type==pygame.QUIT:
            
                        #if itis quit the game
            pygame.quit()
            exit(0)
            
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
            elif event.key==K_e:               #大招
                keys[4]=True
            elif event.key==K_r:
                keys[5]=True
            elif event.key==K_q:
                keys[6]=True
            elif event.key==K_SPACE:
                keys[7]=True
            
            
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
            elif event.key==pygame.K_e:
                keys[4]=False
                oddeven=2
            elif event.key==pygame.K_r:
                keys[5]=False
                oddeven=1
            elif event.key==pygame.K_q:
                keys[6]=False
                tianzhaoUP=False 
                huoqiushuUP=False        
                hqsexist=False
                tz.stop()
                
                
                
            elif event.key==pygame.K_SPACE:
                keys[7]=False
                tudunUP=False
                #tudunexist=False
                
        #新的事件句柄（event handler）
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button==1 and player==player3:
                daoqitimer=daoqitime
                if daoqitimer>0:
                    wuqi="daoqi"
                
            
            elif (event.button==1 or (event.button==4 or event.button==5) and oddeven==1) and player!=player3:  
                          
                acc[1]+=1                      
                arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
            
           
       
    #9 移动玩家     
            
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5             
    elif keys[4]:      #大招！
                       #设置一个判断奇偶数       
        
        if oddeven==2:                                                           
            xly.play()
            attack = attack3     
            showtime = showtime3                                                                       
            
        else:              #在鼬状态时按E

            #shoot.play() 
            pygame.mixer.music.unpause()
            bgmy.stop()
            acc[1]+=10
            circle = 0
            for circle in range(0,6,1):
                arrows.append([circle,playerpos1[0]+32,playerpos1[1]+32])
                player = player2
                bg = bg2
                arrow = arrow2
                attack =attack2
                showtime =showtime2

    
    
    
    elif keys[5]:      #大招2！
        
        if player==player3 and len(arrows)<=1:
            sy.play()
            arrows.append([math.atan2(position[1]-(playerpos1[1]+60),position[0]-(playerpos1[0]+80)),playerpos1[0],playerpos1[1]])
        
        
        elif oddeven==1:    #鼬状态按R
            pygame.mixer.music.unpause()
            bgmy.stop()
            player = player3
            bg = bg1
            arrow = arrow3
            attack = attack4
            showtime =15                    
                
                        
               
        elif oddeven==2:
            #shoot.play()
            pygame.mixer.music.pause()            
            bgmy.play()
            acc[1]+=10           
            player = pygame.image.load("resources/images/hy/y.png")
            bg = bg1
            arrow = pygame.image.load("resources/images/hy/bullet.png")
            attack =pygame.image.load("resources/images/hy/attack.png")
            showtime =15
        
        
            
            
            
        
        
        
    
    
    elif keys[6]:       #q
        
        index5=0
        index6=0
        
        if len(rzs)!=0 and index5<(len(rzs)-1) and bg!=bg2:          #问题1：   index比len()-1还大
            tz.play()
            rzs.pop(index5)   
            index5+=1
            tianzhaoUP =True
        
        if bg==bg2:
            
            huoqiushuUP =True           
            hq.play()
            if len(rzs)!=0 and index6<(len(rzs)-1): #and rzs[index6][1]>250:          #问题1：   index比len()-1还大
                rzs.pop(index6)   
                index6+=1
        
            

        
        
    elif keys[7]:
        tu.play()
        tudunUP=True
        
    
   # if not pygame.mixer.music.get_busy():
      #  print("没有歌")

    
    
''' 
  #10 - Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

        

# 11 - Win/lose display       
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
'''







'''
  rannum = random.randint(1,800)
    if rannum<=200:
        rztu = rz1
    elif rannum<=400 and rannum>200:
        rztu = rz2
    elif rannum<=600 and rannum>400:
        rztu = rz3
    elif rannum<800 and rannum>600:
        rztu = rz4
'''