#coding=gbk
#-*- codeing = utf-8 -*-
#@Time : 2022/11/2 21:17
#@Author :DHD
#@File : Gluttonous snake.py
#@Software : PyCharm

import pygame
import sys
import random
from pygame.locals import *

class Snake:
    def __init__(self):
        self.black = pygame.Color(0,0, 0)
        self.red = pygame.Color(255, 0, 0)
        self.white = pygame.Color(255, 255, 255)

    def initialize(self):
        pygame.init()
        snakespeed = pygame.time.Clock()
        playSurface = pygame.display.set_mode((1400, 600))
        pygame.display.set_caption('Gluttonous snake')
        snakePosition = [700, 300]
        snakebody = [[700, 300], [720, 300], [740, 300]]
        spotPosition = [200, 400]
        spotflag = 1
        direction = 'left'
        changeDirection = direction
        self.main(snakebody, spotPosition, spotflag, direction, changeDirection, snakePosition, playSurface, snakespeed)

    def main(self,snakebody,spotPosition,spotflag,direction,changeDirection,snakePosition,playSurface,snakespeed):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        changeDirection = 'right'
                    if event.key == K_LEFT:
                        changeDirection = 'left'
                    if event.key == K_DOWN:
                        changeDirection = 'down'
                    if event.key == K_UP:
                        changeDirection = 'up'
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

            if (changeDirection == 'left' and not direction == 'right'):
                direction = changeDirection
            if (changeDirection == 'right' and not direction == 'left'):
                direction = changeDirection
            if (changeDirection == 'down' and not direction == 'up'):
                direction = changeDirection
            if (changeDirection == 'up' and not direction == 'down'):
                direction = changeDirection
            if direction == 'right':
                snakePosition[0] += 20
            if direction == 'left':
                snakePosition[0] -= 20
            if direction == 'up':
                snakePosition[1] -= 20
            if direction == 'down':
                snakePosition[1] += 20

            snakebody.insert(0, list(snakePosition))
            if (snakePosition[0] == spotPosition[0] and snakePosition[1] == spotPosition[1]):
                spotflag = 0
            else:
                snakebody.pop()

            if spotflag == 0:
                x = random.randrange(1, 40)
                y = random.randrange(1, 30)
                spotPosition = [int(x * 20), int(y * 20)]
                spotflag = 1

            playSurface.fill(self.black)
            for position in snakebody:
                pygame.draw.rect(playSurface, self.white, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(playSurface, self.red, Rect(spotPosition[0], spotPosition[1], 20, 20))

            pygame.display.flip()
            if (snakePosition[0] > 900 or snakePosition[0] < 0):
                snake.gameover()
            elif (snakePosition[1] > 800 or snakePosition[1] < 0):
                snake.gameover()
            for i in snakebody[1:]:
                if(snakePosition[0] == i[0] and snakePosition[1] == i[1]):
                    snake.gameover()

            snakespeed.tick(5)

    def gameover(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    snake = Snake()
    snake.initialize()
