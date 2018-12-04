import pyglet
from pyglet.gl import *
from random import randint
import datetime
import random
from pyglet.window import key
from pyglet.gl import*

def game_proper(): #This is what happens when the game is launched. It also loads the sounds
    sound = pyglet.media.load('music/song.wav')
    looper = pyglet.media.SourceGroup(sound.audio_format, None)
    looper.loop = True
    looper.queue(sound)
    p = pyglet.media.Player()
    p.queue(looper)
    p.play()

window = pyglet.window.Window(640, 480, "Singko Gaming") #Size of the Window and the title
icon1 = pyglet.image.load('icons/cinco.png') #This is for the icon
window.set_icon(icon1)
megaman = pyglet.resource.image('icons/megaman.png') #This is the character sprite
megaman.anchor_x = megaman.width // 2
megaman.anchor_y = 0

game_bg = pyglet.resource.image('bg/game_opening_bg.jpg') #This is the background of the opening
game_bg.anchor_x = 0
game_bg.anchor_y = 0
#Below are the icons used for the corresponding grades
uno = pyglet.resource.image('icons/uno.png')
uno.anchor_x = uno.width // 2
uno.anchor_y = uno.height

dos = pyglet.resource.image('icons/dos.png')
dos.anchor_x = dos.width // 2
dos.anchor_y = dos.height

tres = pyglet.resource.image('icons/tres.png')
tres.anchor_x = tres.width // 2
tres.anchor_y = tres.height

cuatro = pyglet.resource.image('icons/cuatro.png')
cuatro.anchor_x = cuatro.width // 2
cuatro.anchor_y = cuatro.height

dropped = pyglet.resource.image('icons/dropped.png')
dropped.anchor_x = dropped.width // 2
dropped.anchor_y = dropped.height

cinco = pyglet.resource.image('icons/cinco.png')
cinco.anchor_x = cinco.width // 2
cinco.anchor_y = cinco.height

#This is page when the player decided to continue
def introduction():

    introbg = pyglet.resource.image('bg/intro_bg.jpg')
    introbg.anchor_x = 0
    introbg.anchor_y = 0

    
    @window.event
    def on_draw():
        window.clear()
        introbg.blit(0, 0)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.RIGHT:
            shortstory()
            
    pyglet.app.run()
#This is the page when the player decided to continue after the introduction, to know the Short Story of the Game
def shortstory():

    storybg = pyglet.resource.image('bg/story_bg.jpg')
    storybg.anchor_x = 0
    storybg.anchor_y = 0

    
    @window.event
    def on_draw():
        window.clear()
        storybg.blit(0, 0)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.RIGHT:
            guidelines()
#This refers to the guidelines of the game
def guidelines():

    guidelinesbg = pyglet.resource.image('bg/guidelines_bg.jpg')
    guidelinesbg.anchor_x = 0
    guidelinesbg.anchor_y = 0

    
    @window.event
    def on_draw():
        window.clear()
        guidelinesbg.blit(0, 0)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.RIGHT:
            alert()
#This is for alert purposes, if the player wants to go back to guidelines            
def alert():

    alertbg = pyglet.resource.image('bg/alert_bg.jpg')
    alertbg.anchor_x = 0
    alertbg.anchor_y = 0

    
    @window.event
    def on_draw():
        window.clear()
        alertbg.blit(0, 0)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.LEFT:
            guidelines()
        if symbol == key.RIGHT:
            maingame()
            
#This is the very core of the game where all the important algorithms are contained
def maingame():
    #This is the page when the game has finally been over
    def game_over():
            game.finalscore.append(game.score)
            score=open("text/score.txt", "w+") #This is for the program to record the previous score
            score.write(str(game.finalscore[0]))
            score.close
            highestscore=open("text/highestscore.txt", "r+") #This is for the program to record the highest ever score
            highestscorel = highestscore.readlines()
            highestscorevalue = highestscorel[0]
            highestscore.close
            if int(highestscorevalue) < game.score: #Just to check if the present user has beat the highest ever score record
                highestscore=open("text/highestscore.txt", "w+")
                highestscore.write(str(game.score))
                highestscore.close
            gameoverbg = pyglet.resource.image('bg/game_over_bg.jpg')
            gameoverbg.anchor_x = 0
            gameoverbg.anchor_y = 0
            game_over_score_label.text = 'Game Over! Your final score is: %d' % game.finalscore[0]
            @window.event
            def on_draw():
                window.clear()
                gameoverbg.blit(0, 0)
                game_over_score_label.draw()
            @window.event
            def on_key_press(symbol, modifiers):
                if symbol == key.RIGHT:
                    introduction()
    #This is for initializing the game and all the values of score as well as the position of the character and the falling grade icons
    class Game(object):
        def __init__(self):
            self.megaman_x = window.width // 2
            self.megaman_y = window.height // 2
            self.uno_x = random.randint(0, window.width) #This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.uno_y = window.height
            self.dos_x = random.randint(0, window.width)#This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.dos_y = window.height
            self.tres_x = random.randint(0, window.width)#This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.tres_y = window.height
            self.cuatro_x = random.randint(0, window.width)#This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.cuatro_y = window.height
            self.dropped_x = random.randint(0, window.width)#This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.dropped_y = window.height
            self.cinco_x = random.randint(0, window.width)#This is to make sure that even in the beginning, all the falling grade icons will have random x position
            self.cinco_y = window.height
            self.score = 0
            self.unoscore = 0
            self.dosscore = 0
            self.tresscore = 0
            self.cuatroscore = 0
            self.droppedscore = 0
            self.cincoscore = 0
            self.finalscore = []
            valuescore=open("text/score.txt", "r+") #This is to know the score of the last user
            valuescorel = valuescore.readlines()
            valuescorevalue = valuescorel[0]
            valuescore.close
            valuehighestscore=open("text/highestscore.txt", "r+") #This is to print the highest ever score
            valuehighestscorel = valuehighestscore.readlines()
            valuehighestscorevalue = valuehighestscorel[0]
            valuehighestscore.close
            self.lastscore = int(valuescorevalue)
            self.highestscore = int(valuehighestscorevalue)
            self.gameover = False
            
    game = Game()
#This is for printing the scores for the game
    score_label = pyglet.text.Label(str(game.score),
                                    x=0,
                                    y=window.height,
                                    anchor_x='left',
                                    anchor_y='top')
    unoscore_label = pyglet.text.Label(str(game.unoscore),
                                    x=66,
                                    y=366,
                                    anchor_x='left',
                                    anchor_y='top')
    dosscore_label = pyglet.text.Label(str(game.dosscore),
                                    x=66,
                                    y=318,
                                    anchor_x='left',
                                    anchor_y='top')
    tresscore_label = pyglet.text.Label(str(game.tresscore),
                                    x=66,
                                    y=270,
                                    anchor_x='left',
                                    anchor_y='top')
    cuatroscore_label = pyglet.text.Label(str(game.cuatroscore),
                                    x=66,
                                    y=222,
                                    anchor_x='left',
                                    anchor_y='top')
    droppedscore_label = pyglet.text.Label(str(game.droppedscore),
                                    x=66,
                                    y=174,
                                    anchor_x='left',
                                    anchor_y='top')
    cincoscore_label = pyglet.text.Label(str(game.cincoscore),
                                    x=66,
                                    y=126,
                                    anchor_x='left',
                                    anchor_y='top')

    lastscore_label = pyglet.text.Label(str(game.lastscore),
                                    x=window.width,
                                    y=window.height,
                                    anchor_x='right',
                                    anchor_y='top')

    highestscore_label = pyglet.text.Label(str(game.highestscore),
                                    x=window.width,
                                    y=0,
                                    anchor_x='right',
                                    anchor_y='bottom')
    game_over_score_label = pyglet.text.Label(str(game.score),
                                    x=window.width // 2,
                                    y=window.height // 2,
                                    anchor_x='center',
                                    anchor_y='center')
#This is for windows event such as clicking the directional keyboards as well as moving the cursor. This is to move the character.
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.RIGHT:
            game.megaman_x += 10
        elif symbol == key.LEFT:
            game.megaman_x -= 10
        if symbol == key.UP:
            game.megaman_y += 10
        elif symbol == key.DOWN:
            game.megaman_y -= 10
        elif symbol == pyglet.window.key.ESCAPE:
            window.close()
    @window.event
    def on_mouse_motion(x,y,dx,dy):
        game.megaman_x = x
        game.megaman_y = y
    @window.event
    def on_draw():
        if not game.gameover:
            window.clear()
            glEnable(GL_BLEND)
            game_bg.blit(0, 0)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            megaman.blit(game.megaman_x, game.megaman_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            uno.blit(game.uno_x, game.uno_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            dos.blit(game.dos_x, game.dos_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            tres.blit(game.tres_x, game.tres_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            cuatro.blit(game.cuatro_x, game.cuatro_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            dropped.blit(game.dropped_x, game.dropped_y)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#This is basically to make the PNG works its transparency on the game
            cinco.blit(game.cinco_x, game.cinco_y)
            score_label.text = 'Your score is: %d' % game.score
            score_label.draw()
            unoscore_label.text = ' %d' % game.unoscore
            unoscore_label.draw()
            dosscore_label.text = ' %d' % game.dosscore
            dosscore_label.draw()
            tresscore_label.text = ' %d' % game.tresscore
            tresscore_label.draw()
            cuatroscore_label.text = ' %d' % game.cuatroscore
            cuatroscore_label.draw()
            droppedscore_label.text = ' %d' % game.droppedscore
            droppedscore_label.draw()
            cincoscore_label.text = ' %d' % game.cincoscore
            cincoscore_label.draw()
            lastscore_label.text = 'Last Game Score: %d' % game.lastscore
            lastscore_label.draw()
            highestscore_label.text = 'Highest Game Score Ever: %d' % game.highestscore
            highestscore_label.draw()
            
        else:
            game_over()

    def grades_drop(dt):
        #This is for collission.
        if game.cincoscore == 3: #If the condition that the cinco has been crossed thrice, then the game is over.
            game.gameover = True
            return
        if (abs(game.cinco_x - game.megaman_x) < 30 and abs(game.cinco_y -
                game.megaman_y) < 30):
            game.cincoscore += 1
            game.cinco_x = random.randint(0, window.width)
            game.cinco_y = window.height
        if (abs(game.uno_x - game.megaman_x) < 30  and abs(game.uno_y -
                game.megaman_y) < 30):
            game.score += 1
            game.unoscore += 1
            game.uno_x = random.randint(0, window.width)
            game.uno_y = window.height
        if (abs(game.dos_x - game.megaman_x) < 30 and abs(game.dos_y -
                game.megaman_y) < 30):
            game.score += 2
            game.dosscore += 1
            game.dos_x = random.randint(0, window.width)
            game.dos_y = window.height
        if (abs(game.tres_x - game.megaman_x) < 30 and abs(game.tres_y -
                game.megaman_y) < 30):
            game.score += 3
            game.tresscore += 1
            game.tres_x = random.randint(0, window.width)
            game.tres_y = window.height
        if (abs(game.cuatro_x - game.megaman_x) < 30 and abs(game.cuatro_y -
                game.megaman_y) < 30):
            game.score += 4
            game.cuatroscore += 1
            game.cuatro_x = random.randint(0, window.width)
            game.cuatro_y = window.height
        if (abs(game.dropped_x - game.megaman_x) < 30 and abs(game.dropped_y -
                game.megaman_y) < 30):
            game.droppedscore += 1
            game.dropped_x = random.randint(0, window.width)
            game.dropped_y = window.height

        #This code is for resetting the ball.
        if game.uno_y < 0:
            game.uno_x = random.randint(0, window.width)
            game.uno_y = window.height
        else:
            game.uno_y -= 2
        if game.dos_y <0:
            game.dos_x = random.randint(0, window.width)
            game.dos_y = window.height
        else:
            game.dos_y -=2
        if game.tres_y <0:
            game.tres_x = random.randint(0, window.width)
            game.tres_y = window.height
        else:
            game.tres_y -=2
        if game.cuatro_y <0:
            game.cuatro_x = random.randint(0, window.width)
            game.cuatro_y = window.height
        else:
            game.cuatro_y -=2
        if game.dropped_y <0:
            game.dropped_x = random.randint(0, window.width)
            game.dropped_y = window.height
        else:
            game.dropped_y -=2
        if game.cinco_y <0:
            game.cinco_x = random.randint(0, window.width)
            game.cinco_y = window.height
        else:
            game.cinco_y -=2

            
    pyglet.clock.schedule(grades_drop)#This is to know when the grades will dropp
