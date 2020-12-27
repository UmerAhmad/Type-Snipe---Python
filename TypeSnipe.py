#   Umer Ahmad
#   January 8, 2018
#   This program is a game where you can shoot ships by typing out the words on them.

import pygame
import sys
import random

#Pre - Requisites for python, initalizing music usage and pygame, setting screen size and caption
pygame.mixer.pre_init(44100, -16,1,512)
pygame.init()
pygame.mixer.init()
width = 1400
height = 900
screenSize = (width,height)
screen = pygame.display.set_mode((screenSize),0)
pygame.display.set_caption("Type Snipe")


#Setting up different colours to use throughout the code
WHITE = (255,255,255)
GREEN = (0,255,0)
PURPLE = (128,0,128)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK =(0,0,0)
GRAY =(128,128,128)


textColour = WHITE



#Various positions on the screen that will be used often, usually text
xCenter = screen.get_width()/2
yCenter = screen.get_height()/2

xCenterTitle = screen.get_width()/2
yCenterTitle = screen.get_height()/2 - 200

xCenterSubtitle = screen.get_width()/2
yCenterSubtitle = screen.get_height()/2 + 100



#Setting up the file variable to manipulate to change files
wordBankTxt = "wordBankNormal.txt"


wordBank = []

firstFile = open(wordBankTxt, "r")

#Appending all read words into the array
for line in firstFile:
    for word in line.split():
        wordBank.append(word)


#Getting a random word within the array
wordBankLength = len(wordBank)
randomWord = random.randint(0, wordBankLength - 1)
word = wordBank[randomWord]



#Loading in my various sounds and images that will be used
titleTextImage = pygame.image.load("titleTextImage.png")


background = pygame.image.load("spaceWallpaper.png")
background_rect = background.get_rect()


playerShipImage = pygame.image.load("PlayerShip.png")

playerBulletImage = pygame.image.load("playerBullet.png")
playerBulletImage = pygame.transform.scale(playerBulletImage, (25,25))



bulletSound = pygame.mixer.Sound("bulletSound.wav")

enemyHit = pygame.mixer.Sound("enemyHit.wav")

pygame.mixer.music.load("soundtrack.wav")
pygame.mixer.music.set_volume(0.5)


enemyNormalShipImage = pygame.image.load("enemyNormalShip.jpg")

enemyMediumShipImage = pygame.image.load("enemyMediumShip.png")


enemyLargeShipImage = pygame.image.load("enemyLargeShip.png")


enemyBossShipImage = pygame.image.load("enemyBossShip.png")

playerHealthPoints = pygame.image.load("playerHealth.png")
playerHealthPoints = pygame.transform.scale(playerHealthPoints, (50,50))



#Different fonts that will be used in the code
fontTitle = pygame.font.SysFont("arial",70)
fontTitle2 = pygame.font.SysFont("arial", 48)
fontSubTitle = pygame.font.SysFont("arial",16)
fontExplainText = pygame.font.SysFont("arial",32)



#Game variables
score = 0

enemyShipSpeed = 2
playerHP = 3



#Classifying the sprites to manipulate easier

#The player ship
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.transform.scale(playerShipImage, (150,150))
        self.rect = self.image.get_rect()
        self.rect.centerx = xCenterSubtitle
        self.rect.bottom = height - 10
    def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bulletSound.play()
            all_sprites.add(bullet)
            bullets.add(bullet)

    
            


#Enemyship : Image, Speed and Size will be changed depending on score
class enemyShip(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            if score < 500:
                self.image = pygame.transform.scale(enemyNormalShipImage, (75, 75))
                enemyShipSpeed = 2
                startingY = - 40
            if score >= 500 and score < 1000:
                self.image = pygame.transform.scale(enemyMediumShipImage, (150, 150))
                enemyShipSpeed = 3
                startingY = - 80
            if score >= 1000:
                self.image = pygame.transform.scale(enemyLargeShipImage, (190, 190))
                enemyShipSpeed = 4
                if FPS > 200:
                    enemyShipSpeed = 5
                if FPS > 400:
                    enemyShipSpeed = 6
                if FPS > 500:
                    enemyShipSpeed = 7
                if FPS > 600:
                    enemyShipSpeed = 8
                startingY = - 100
            if score == 450 or score == 950:
                self.image = pygame.transform.scale(enemyBossShipImage, (360, 360))
                enemyShipSpeed = 1
                startingY = - 200
 
                
            self.rect = self.image.get_rect()
            startingX = random.randint(50,750)
            
            
            self.rect.x = startingX
            self.rect.y = startingY
            self.speedy = enemyShipSpeed 
        def update(self):
            global playerHP
            self.rect.y += self.speedy
            if self.rect.top > height + 3:
                    startingX = random.randint(50,750)
                    self.rect.x = startingX
                    self.rect.y = startingY
                    playerHP -= 1
                    if score == 500 or score == 1000:
                        playerHP -= 1




                    

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.transform.scale(playerBulletImage,(30,30))
        self.rect = self.image.get_rect()
        self.rect.bottom = height - 15
        self.rect.centerx = xCenterSubtitle
    def update(self):
        bulletSpeed = 25
        if score == 500 or score == 1000:
            bulletSpeed = 50
        if e.rect.centery == self.rect.centery:
            self.speedy = 0
        if e.rect.centery > self.rect.centery:
            self.speedy = bulletSpeed
        if e.rect.centery < self.rect.centery:
          self.speedy = - bulletSpeed
        if e.rect.centerx < self.rect.centerx:
          self.speedx = - bulletSpeed
        if e.rect.centerx > self.rect.centerx:
          self.speedx = bulletSpeed
        if self.rect.y == e.rect.centery:
                self.speedy = 0
        if self.rect.x == e.rect.centerx:
                self.speedx = 0
        self.rect.y += self.speedy
        self.rect.x += self.speedx


             




#Setting up the various sprite groups to allow usage of previous setup sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(1):
        e = enemyShip()
        all_sprites.add(e)
        enemies.add(e)





screen.fill(WHITE)
pygame.display.update()


FPS = 60

#More game variables
bossHP = 8

letterMiss = 0
totalLetters = 0
wordCount = 0

beginTimer = True


clickTextColour = WHITE
clickTextColour2 = WHITE
clickTextColour3 = WHITE



#Setting loops to false so I can use them later
main = True
menu = False
game = False
instructions = False
gameOver = False

#Starting music and telling it to loop when its about to end
pygame.mixer.music.play(loops = -1)
while main:
        menu = True
        #Position of Enemy ships
        startingX = random.randint(50,750)
        startingY = 10
        while menu:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                menu = False
                                main = False



                #Setting backdrop
                screen.fill(BLACK)
                screen.blit(background, background_rect)

                #resetting variables if user goes back to menu
                score = 0
                letterMiss = 0
                totalLetters = 0
                beginTimer = True
                wordCount = 0

        
                screen.blit(titleTextImage, (xCenterTitle - 225, yCenterTitle))
                
                textStart = fontTitle2.render("PLAY", True, clickTextColour)
                textStart_rect = textStart.get_rect(center=(xCenterSubtitle, yCenterSubtitle))
                screen.blit(textStart, textStart_rect)
                #Mouse over text detection
                mousePos = pygame.mouse.get_pos()
                if textStart_rect.collidepoint(mousePos):
                    clickTextColour = RED
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu = False
                        game = True
                else:
                    clickTextColour = WHITE

                
                textInstructions = fontTitle2.render("HOW TO PLAY", True, clickTextColour2)
                textInstructions_rect = textInstructions.get_rect(center=(xCenterSubtitle, yCenterSubtitle + 75))
                screen.blit(textInstructions, textInstructions_rect)

                if textInstructions_rect.collidepoint(mousePos):
                    clickTextColour2 = RED
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu = False
                        instructions = True
                else:
                    clickTextColour2 = WHITE
                

                textQuit = fontTitle2.render("QUIT", True, clickTextColour3)
                textQuit_rect = textQuit.get_rect(center=(xCenterSubtitle, yCenterSubtitle + 150))
                screen.blit(textQuit, textQuit_rect)

                if textQuit_rect.collidepoint(mousePos):
                    clickTextColour3 = RED
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu = False
                        main = False
                else:
                    clickTextColour3 = WHITE


                pygame.display.update()
                
        while game:
                if beginTimer:
                    startTime = pygame.time.get_ticks()
                    beginTimer = False
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                main = False
                                game = False
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        game = False
                                        score = 0
                                        playerHP = 3
                                        letterMiss = 0
                                        totalLetters = 0
                                        wordCount = 0
                                        beginTimer = True
                                        e.kill()
                                        e = enemyShip()
                                        all_sprites.add(e)
                                        enemies.add(e)
                                        menu = True
                                if event.key == firstLetter:
                                    if word != "":
                                        player.shoot()
                                        word = word[1:]
                                        textColour = RED
                                        totalLetters += 1
                                if event.key != firstLetter:
                                    letterMiss += 1
                                    totalLetters += 1


                                        





                firstFile = open(wordBankTxt, "r")
                clock = pygame.time.Clock()
                if score == 500 or score == 1000:
                    FPS = 45
                clock.tick(FPS)
                
                bulletCount = (len(bullets.sprites()))

                all_sprites.update()
                wordLength = len(word) +1
                
                collisionDetection = pygame.sprite.groupcollide(enemies, bullets, False, True)
                for collision in collisionDetection:
                    enemyHit.play()
                
                if word != "":
                    firstLetter = ord(word[0])
                if score == 500 or score == 1000:
                    if word == "":
                        if bulletCount == 0:
                            bossHP -= 1
                            wordCount += 1
                            if bossHP != 0:
                                del wordBank[:]
                                wordBankTxt = "wordBankHard.txt"
                                for line in firstFile:
                                    for word in line.split():
                                        wordBank.append(word)
                                wordBankLength = len(wordBank)
                                randomWord = random.randint(0, wordBankLength -1)
                                word = wordBank[randomWord]
                                wordLength = len(word)

                                    
                                firstLetter = ord(word[0])


                            if bossHP == 0:
                                e.kill()
                                textColour = WHITE
                                e = enemyShip()
                                all_sprites.add(e)
                                enemies.add(e)
                                for line in firstFile:
                                    for word in line.split():
                                        wordBank.append(word)
                                wordBankLength = len(wordBank)
                                randomWord = random.randint(0, wordBankLength -1)
                                word = wordBank[randomWord]
                                firstLetter = ord(word[0])
                                score += 50
                                wordCount+= 1
                                bossHP = 8
                                FPS = 60


                            
                if score != 500 or score != 1000:
                    if word == "":
                        if bulletCount == 0:
                            e.kill()
                            textColour = WHITE
                            e = enemyShip()
                            all_sprites.add(e)
                            enemies.add(e)

                            if score > 500:
                                del wordBank[:]
                                wordBankTxt = "wordBankMedium.txt"
                            if score > 1000:
                                del wordBank[:]
                                wordBankTxt = "wordBankHard.txt"
                            for line in firstFile:
                                for word in line.split():
                                    wordBank.append(word)
                            wordBankLength = len(wordBank)
                            randomWord = random.randint(0, wordBankLength -1)
                            word = wordBank[randomWord]
                            firstLetter = ord(word[0])
                            score += 50
                            wordCount += 1
                            if score > 1000:
                                FPS = FPS + 15
                        
                                



                displayScore = str(score)
                
                screen.fill(GRAY)
                screen.blit(background, background_rect)
                all_sprites.draw(screen)

                playerHpLocationX = 20
                for i in range(0, playerHP, 1):
                    screen.blit(playerHealthPoints, (playerHpLocationX, height - 50))
                    playerHpLocationX += playerHealthPoints.get_width()


                if playerHP == 0:
                    game = False
                    gameOver = True
                    endTime = pygame.time.get_ticks()
                    score = 0

                
                for enemy in enemies:
                    enemyText = fontSubTitle.render(word, True, textColour)
                    enemyText_rect = enemyText.get_rect(center =(e.rect.x, e.rect.bottom + 5))
                    pygame.draw.rect(screen, BLACK, [e.rect.x - enemyText.get_width() / 2, e.rect.bottom + 5 - enemyText.get_height() / 2, enemyText.get_width()+3, enemyText.get_height()],)
                    screen.blit(enemyText, enemyText_rect)
                    hpLocationX = e.rect.x - 25
                    if score == 500 or score == 1000:
                        textBossBattle = fontTitle.render("BOSS", True, RED)
                        textBossBattle_rect = textBossBattle.get_rect(center=(width - textBossBattle.get_width() + 75, textBossBattle.get_height() - 30))
                        screen.blit(textBossBattle, textBossBattle_rect)
                        for i in range (0, bossHP, 1):
                            pygame.draw.rect(screen, RED, [hpLocationX, e.rect.bottom + enemyText.get_height() + 5, 5, 3])
                            hpLocationX += 6
                            
                
                waveCountText = fontSubTitle.render("SCORE :" + displayScore, True, WHITE)
                waveCountText_rect = waveCountText.get_rect(center=(width - waveCountText.get_width() - 1, height - waveCountText.get_height() - 1))
                screen.blit(waveCountText, waveCountText_rect)
     
                        


                
                pygame.display.update()
        
      
        while instructions:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                instructions = False
                                main = False
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        instructions = False
                                        main = False
                                if event.key == pygame.K_ESCAPE:
                                        instructions = False
                                        menu = True


                screen.fill(BLACK)
                screen.blit(background, background_rect)
                
                textInstructionsTitle = fontTitle.render("HOW TO PLAY", True, WHITE)
                textInstructionsTitle_rect = textInstructionsTitle.get_rect(center=(xCenterTitle, yCenterTitle))
                screen.blit(textInstructionsTitle, textInstructionsTitle_rect)

                textHowToPlay = fontExplainText.render("You are a ship that will appear at the bottom of the screen, tasked with defending your station. ", True, WHITE)
                textHowToPlay_rect = textHowToPlay.get_rect(center=(xCenter, yCenter))
                screen.blit(textHowToPlay, textHowToPlay_rect)

                textHowToPlay2 = fontExplainText.render("You will accomplish this by typing out the words on the enemies that are trying to pass you.", True, WHITE)
                textHowToPlay2_rect = textHowToPlay2.get_rect(center=(xCenter, yCenter + 50))
                screen.blit(textHowToPlay2, textHowToPlay2_rect)

                textHowToPlay3 = fontExplainText.render("You don't need to use WASD or the arrow keys, simply type the words you see.", True, WHITE)
                textHowToPlay3_rect = textHowToPlay3.get_rect(center=(xCenter, yCenter + 100))
                screen.blit(textHowToPlay3, textHowToPlay3_rect)

                textHowToPlay4 = fontExplainText.render("Gets harder the more enemies you defeat(bigger words, faster enemies) and bosses will appear", True, WHITE)
                textHowToPlay4_rect = textHowToPlay4.get_rect(center=(xCenter, yCenter + 150))
                screen.blit(textHowToPlay4, textHowToPlay4_rect)

                textHowToPlay5 = fontExplainText.render("Try to last as long as possible and achieve a high score", True, WHITE)
                textHowToPlay5_rect = textHowToPlay5.get_rect(center=(xCenter, yCenter + 200))
                screen.blit(textHowToPlay5, textHowToPlay5_rect)

                textEscape = fontTitle2.render("Press ESCAPE to go back.", True, WHITE)
                textEscape_rect = textEscape.get_rect(center=(width / 2, height - textEscape.get_height()))
                screen.blit(textEscape, textEscape_rect)


                
                pygame.display.update()



                
        while gameOver:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameOver = False
                                main = False
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        gameOver = False
                                        main = False
                                if event.key == pygame.K_ESCAPE:
                                        gameOver = False
                                        menu = True
                                        letterMiss = 0
                                        totalLetters = 0
                                        wordCount = 0
                                        playerHP = 3
                                        beginTimer = True
                                        e.kill()
                                        e = enemyShip()
                                        all_sprites.add(e)
                                        enemies.add(e)


                screen.fill(BLACK)
                screen.blit(background, background_rect)
                
                textInstructionsTitle = fontTitle.render("GAME OVER!", True, RED)
                textInstructionsTitle_rect = textInstructionsTitle.get_rect(center=(xCenterTitle, yCenterTitle))
                screen.blit(textInstructionsTitle, textInstructionsTitle_rect)


                textDisplayScore = fontTitle2.render("Your Score : " + displayScore, True, WHITE)
                textDisplayScore_rect = textDisplayScore.get_rect(center=(xCenter, yCenter))
                screen.blit(textDisplayScore, textDisplayScore_rect)

                
                displayLetterMiss = str(letterMiss)
                if totalLetters == 0:
                    displayAccuracy = "0"
                else:
                    displayAccuracy = str(round(((totalLetters - letterMiss) / totalLetters) * 100, 2))
                    
                correctWords = (totalLetters - letterMiss) / 5
                gameLength = ((endTime - startTime) / 1000) - (wordCount * 0.7)
                wordsPerMinute = str(round((correctWords/ gameLength) * 60,2))


                textLetterMiss = fontTitle2.render("Your letters missed : " + displayLetterMiss ,True, WHITE)
                textLetterMiss_rect = textLetterMiss.get_rect(center=(xCenter, yCenter + textDisplayScore.get_height() + 5))
                screen.blit(textLetterMiss, textLetterMiss_rect)

                textAccuracy = fontTitle2.render("Accuracy : " + displayAccuracy + "%" ,True, WHITE)
                textAccuracy_rect = textAccuracy.get_rect(center=(xCenter, yCenter + textLetterMiss.get_height() * 2  + 5))
                screen.blit(textAccuracy, textAccuracy_rect)

                textWPM = fontTitle2.render("WPM : " + wordsPerMinute,True, WHITE)
                textWPM_rect = textWPM.get_rect(center=(xCenter, yCenter + textLetterMiss.get_height() * 3  + 5))
                screen.blit(textWPM, textWPM_rect)
    
                textEscape = fontTitle2.render("Press ESCAPE to go back.", True, WHITE)
                textEscape_rect = textEscape.get_rect(center=(width / 2, height - textEscape.get_height()))
                screen.blit(textEscape, textEscape_rect)




                
                pygame.display.update()
                

pygame.quit()
sys.exit()



