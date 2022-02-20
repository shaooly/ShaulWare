import pygame
import math
import time
pi = math.pi
n = int(input("please enter z^?"))

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
size = (WINDOW_HEIGHT, WINDOW_WIDTH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("KODKOD")
stop = False
screen.fill(WHITE)
pygame.draw.line(screen, BLACK, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))
pygame.draw.line(screen, BLACK, (0, WINDOW_HEIGHT / 2), (WINDOW_WIDTH, WINDOW_HEIGHT / 2))
for k in range(n): # z^n = 1 --> z,n = cis(2pi*k/n), k = 1,2,3...n
    start_point = (250 * math.cos(2*pi*k / n) + 500, 250 * math.sin(2*pi*k / n) + 500)
    end_point = (250 * math.cos(2*pi*(k + 1) / n) + 500, 250 * math.sin(2*pi*(k + 1) / n) + 500)
    pygame.draw.line(screen, BLACK, start_point, end_point)
pygame.display.flip()
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

pygame.quit()
