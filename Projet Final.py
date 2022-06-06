import pygame
import random
from pyswip import Prolog

pygame.init()
pygame.mixer.init()



prolog = Prolog()

win = pygame.display.set_mode((720,720))
pygame.display.set_caption("Run, Cow Run")

                        
clock = pygame.time.Clock()

#picture
bg = [pygame.image.load('Pic/Board2.png'),
      pygame.image.load('Pic/StartPage.png'),
      pygame.image.load('Pic/Winpage.png'),
      pygame.image.load('Pic/LosePage.png')]

enemy = [pygame.image.load('Pic/Enemy/Enemy1.png'),
         pygame.image.load('Pic/Enemy/Enemy2.png'),
         pygame.image.load('Pic/Enemy/Enemy3.png'),
         pygame.image.load('Pic/Enemy/Enemy4.png'),
         pygame.image.load('Pic/Enemy/Enemy5.png'),
         pygame.image.load('Pic/Enemy/Enemy6.png'),
         pygame.image.load('Pic/Enemy/Enemy7.png'),
         pygame.image.load('Pic/Enemy/Enemy8.png')]
player = pygame.image.load('Pic/Player/Player.png')

startText = [pygame.image.load('Pic/Text/Start.png'),
             pygame.image.load('Pic/Text/Start2.png'),
             pygame.image.load('Pic/Text/Start3.png')]

tryAgainText = [pygame.image.load('Pic/Text/TryAgain.png'),
                pygame.image.load('Pic/Text/TryAgain2.png'),
                pygame.image.load('Pic/Text/TryAgain3.png')]

#necessary function

def calculateposition(x,y):
    position = ''
    if(x == 87):
        position = position + 'a'
    elif(x == 140.5):
        position = position + 'b'
    elif(x == 195):
        position = position + 'c'
    elif(x == 252):
        position = position + 'd'
    elif(x == 308):
        position = position + 'e'
    elif(x == 363):
        position = position + 'f'
    elif(x == 418):
        position = position + 'g'
    elif(x == 474):
        position = position + 'h'
    elif(x == 529):
        position = position + 'i'
    elif(x == 584):
        position = position + 'j'

    if(y == 70):
        position = position + '1'
    elif(y == 130):
        position = position + '2'
    elif(y == 190):
        position = position + '3'
    elif(y == 250):
        position = position + '4'
    elif(y == 310):
        position = position + '5'
    elif(y == 370):
        position = position + '6'
    elif(y == 430):
        position = position + '7'
    elif(y == 490):
        position = position + '8'
    elif(y == 550):
        position = position + '9'
    elif(y == 610):
        position = position + '10'

    return position


def calculateXpos(x):
    position = ''
    if(x == 87):
        position = position + '1'
    elif(x == 140.5):
        position = position + '2'
    elif(x == 195):
        position = position + '3'
    elif(x == 252):
        position = position + '4'
    elif(x == 308):
        position = position + '5'
    elif(x == 363):
        position = position + '6'
    elif(x == 418):
        position = position + '7'
    elif(x == 474):
        position = position + '8'
    elif(x == 529):
        position = position + '9'
    elif(x == 584):
        position = position + '10'
    return position


    
def calculateYpos(y):
    position = ''
    if(y == 70):
        position = position + '1'
    elif(y == 130):
        position = position + '2'
    elif(y == 190):
        position = position + '3'
    elif(y == 250):
        position = position + '4'
    elif(y == 310):
        position = position + '5'
    elif(y == 370):
        position = position + '6'
    elif(y == 430):
        position = position + '7'
    elif(y == 490):
        position = position + '8'
    elif(y == 550):
        position = position + '9'
    elif(y == 610):
        position = position + '10'
        
    return position

def calculateEnemyMove(enemyMove):
    position = []
    if(len(enemyMove) < 3):
        enemyX = enemyMove[0]
        enemyY = enemyMove[1]
    else:
        enemyX = enemyMove[0]
        enemyY = enemyMove[1]+enemyMove[2]

    if(enemyX == 'a'):
        enemyX = 0
    elif(enemyX == 'b'):
        enemyX = 1
    elif(enemyX == 'c'):
        enemyX = 2
    elif(enemyX == 'd'):
        enemyX = 3
    elif(enemyX == 'e'):
        enemyX = 4
    elif(enemyX == 'f'):
        enemyX = 5
    elif(enemyX == 'g'):
        enemyX = 6
    elif(enemyX == 'h'):
        enemyX = 7
    elif(enemyX == 'i'):
        enemyX = 8
    elif(enemyX == 'j'):
        enemyX = 9
    position.append(int(enemyX))
    position.append(int(enemyY)-1)
    
    return position



def enemyMoveCheck(enemyX,enemyY,playerX,playerY):
    list1 = []
    list2 = []
    
    prolog.consult("D:/Study/AIProject/Project3.pl")
    enemyPos = calculateposition(enemyX,enemyY)
    playerPos = calculateposition(playerX,playerY)
    
    position = "astar("+enemyPos+","+playerPos+",P)."
    result = list(prolog.query(position))

    for x in (result[0]['P']):
        list1.append(str(x))
        if(len(list1) > 3):
            break

    if(len(list1) < 3):
        list1.append('finish')

    
    list2.append(list1[1])
    list2.append(list1[2])

    return list2

def loseCheck(enemyX,enemyY,playerX,playerY):
    if(enemyX == playerX and enemyY == playerY):
        x = 0
        return x
    else:
        x = 1
        return x

def winCheck(playerX,playerY):
    if(playerX == 9 and playerY == 0):
        x = 0
        return x
    else:
        x = 1
        return x

def wallchecking(x,y,x1,y1):
    prolog.consult("D:/Study/AIProject/Project3wall.pl")
    
    posx = str(calculateXpos(x))
    posy = str(calculateXpos(y))
    posx1 = str(calculateXpos(x1))
    posy1 = str(calculateXpos(y1))

    position = "moveable("+posy+","+posx+","+posy1+","+posx1+")."

    result = list(prolog.query(position))

    if len(result)>0:
        if(x == x1):
            return int(posy1)-1
        else:
            return int(posx1)-1
    else:
        if(x == x1):
            return int(posy)-1
        else:
            return int(posx)-1
    

#Set up the variable

moveX = [87,140.5,195,252,308,363,418,474,529,584]
moveY = [70,130,190,250,310,370,430,490,550,610]

playerPosX = [3,3,5,5,3,2,3,7,7,9,4,7,9]
playerPosY = [1,7,9,1,6,7,8,0,6,8,1,3,6]

enemyPosX = [6,6,6,6,6,4,4,4,0,0,0,0,4,4]
enemyPosY = [0,0,0,0,0,0,0,0,8,8,8,8,8,8]

random.seed(10)
run = 1
Play = True
countX = 0
countY = 0
enemyframe = 0
Win = False
Lose = False
FirstPage = True
countEnemyX = 6
countEnemyY = 0
enemyframe = 0
turn = 0

End = False

#Cover page

while FirstPage:
    win.blit(bg[1], (0,0))
    win.blit(startText[1], (275,150))
    win.blit(startText[0], (275,150))

    pygame.display.flip()
    pygame.display.update

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        FirstPage = False
        win.blit(startText[2], (275,150))
        win.blit(startText[0], (275,150))
        pygame.display.flip()
        pygame.display.update
        pygame.time.delay(250)


#Game page

while Play:

    
    randPos = random.randint(0,13)
    countPlayerX = playerPosX[randPos]    #2
    countPlayerY = playerPosY[randPos]    #7

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        win.blit(bg[0], (0,0))
        win.blit(enemy[enemyframe], (moveX[countEnemyX],moveY[countEnemyY]))
        win.blit(player, (moveX[countPlayerX],moveY[countPlayerY]))
        pygame.display.flip()
        pygame.display.update
        
        clock.tick(30)

        #Player's turn

        if(turn%2 == 1):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and countPlayerY > 0:
                countPlayerY = wallchecking(moveX[countPlayerX],moveX[countPlayerY],moveX[countPlayerX],moveX[countPlayerY-1])
                position = calculateposition(moveX[countPlayerX],moveY[countPlayerY])
                turn+=1
            elif keys[pygame.K_LEFT] and countPlayerX > 0:
                countPlayerX = wallchecking(moveX[countPlayerX],moveX[countPlayerY],moveX[countPlayerX-1],moveX[countPlayerY])
                position = calculateposition(moveX[countX],moveY[countY])
                turn+=1
            elif keys[pygame.K_DOWN] and countPlayerY < 9:
                countPlayerY = wallchecking(moveX[countPlayerX],moveX[countPlayerY],moveX[countPlayerX],moveX[countPlayerY+1])
                position = calculateposition(moveX[countPlayerX],moveY[countPlayerY])
                turn+=1
            elif keys[pygame.K_RIGHT] and countPlayerX < 9:
                countPlayerX = wallchecking(moveX[countPlayerX],moveX[countPlayerY],moveX[countPlayerX+1],moveX[countPlayerY])
                position = calculateposition(moveX[countPlayerX],moveY[countPlayerY])
                turn+=1

            win.blit(bg[0], (0,0))
            win.blit(enemy[enemyframe], (moveX[countEnemyX],moveY[countEnemyY]))
            win.blit(player, (moveX[countPlayerX],moveY[countPlayerY]))
            pygame.display.flip()
            pygame.display.update
            
            playable = loseCheck(countEnemyX,countEnemyY,countPlayerX,countPlayerY)
            if(playable == 0):
                Lose = True
                break
            playable = winCheck(countPlayerX,countPlayerY)
            if(playable == 0):
                Win = True
                break

        else:

            #Enemy's turn

            enemyMove = enemyMoveCheck(moveX[countEnemyX],moveY[countEnemyY],moveX[countPlayerX],moveY[countPlayerY])
            move1 = calculateEnemyMove(enemyMove[0])
            countEnemyX = move1[0]
            countEnemyY = move1[1]
            win.blit(bg[0], (0,0))
            
            win.blit(player, (moveX[countPlayerX],moveY[countPlayerY]))
            win.blit(enemy[enemyframe], (moveX[countEnemyX],moveY[countEnemyY]))
            pygame.display.flip()
            pygame.display.update
            
            playable = loseCheck(countEnemyX,countEnemyY,countPlayerX,countPlayerY)
            if(playable == 0):
                Lose = True
                break
            playable = winCheck(countPlayerX,countPlayerY)
            if(playable == 0):
                Win = True
                break
            pygame.time.delay(250)
            move2 = calculateEnemyMove(enemyMove[1])
            countEnemyX = move2[0]
            countEnemyY = move2[1]
            win.blit(bg[0], (0,0))
            
            win.blit(player, (moveX[countPlayerX],moveY[countPlayerY]))
            win.blit(enemy[enemyframe], (moveX[countEnemyX],moveY[countEnemyY]))
            pygame.display.flip()
            pygame.display.update
            
            playable = loseCheck(countEnemyX,countEnemyY,countPlayerX,countPlayerY)
            if(playable == 0):
                Lose = True
                break
            playable = winCheck(countPlayerX,countPlayerY)
            if(playable == 0):
                Win = True
                break
            
            turn+=1


        win.blit(bg[0], (0,0))
        enemyframe+=1
        if(enemyframe == 8):
            enemyframe = 0
        win.blit(bg[0], (0,0))
        
        win.blit(player, (moveX[countPlayerX],moveY[countPlayerY]))
        win.blit(enemy[enemyframe], (moveX[countEnemyX],moveY[countEnemyY]))
                    
        pygame.display.flip()
        pygame.display.update

    End = True

    #Win/Lose screen

    while End:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()

        if(Win == True):
            win.blit(bg[2], (0,0))
            win.blit(tryAgainText[1], (25,450))
            win.blit(tryAgainText[0], (25,450))
            pygame.display.flip()
            pygame.display.update

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                win.blit(tryAgainText[2], (25,450))
                win.blit(tryAgainText[0], (25,450))
                pygame.display.flip()
                pygame.display.update
                End = False
                Win = False
                countPlayerX = 2    #2
                countPlayerY = 7    #7
                countEnemyX = 6
                countEnemyY = 0
                enemyframe = 0
                turn = 0
                pygame.time.delay(250)

            

        elif(Lose == True):
            win.blit(bg[3], (0,0))
            win.blit(tryAgainText[1], (375,225))
            win.blit(tryAgainText[0], (375,225))
            
            pygame.display.flip()
            pygame.display.update

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
     
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                win.blit(tryAgainText[2], (375,225))
                win.blit(tryAgainText[0], (375,225))
                pygame.display.flip()
                pygame.display.update
                End = False
                Lose = False
                countPlayerX = 2    #2
                countPlayerY = 7    #7
                countEnemyX = 6
                countEnemyY = 0
                enemyframe = 0
                turn = 0
                pygame.time.delay(250)
        


            


