import pygame
import random
import time

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
numbers_list = []
randomized_list = []
list_size = 1792
color = (255, 255, 255)
w_constant = WINDOW_WIDTH / list_size

pygame.init()
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("visualize sort")


def make_rgb_list():
    rgb_list = []
    for i in range(256):
        rgb_list.append((255, 255, 255 - i))  # white to yellow
    for i in range(256):
        rgb_list.append((255, 255 - i, 0))  # yellow to red
    for i in range(256):
        rgb_list.append((255 - i, i, 0))  # red to green
    for i in range(256):
        rgb_list.append((0, 255, i))  # green to light blue
    for i in range(256):
        rgb_list.append((0, 255 - i, 255))  # light blue to blue
    for i in range(256):
        rgb_list.append((i, 0, 255))  # from blue to pink
    for i in range(256):
        rgb_list.append((255, i, 255))  # from pink to white
    return rgb_list


for i in range(list_size):
    numbers_list.append(i)

for i in range(list_size):
    my_index = random.randint(0, len(numbers_list) - 1)
    randomized_list.append(numbers_list[my_index])
    numbers_list.pop(my_index)

print(randomized_list)
stop = False
new_rgb_list = make_rgb_list()
print(len(new_rgb_list))
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_0:
                stop = True
            if event.key == pygame.K_SPACE:
                screen.fill((0, 0, 0))
                for z in range(len(randomized_list)):
                    w = w_constant
                    h = randomized_list[z] * (WINDOW_HEIGHT / list_size)
                    x = z * (WINDOW_WIDTH / list_size)
                    y = WINDOW_HEIGHT - h
                    color = new_rgb_list[randomized_list[z]]
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
                    pygame.display.flip()
                for i in range(len(randomized_list)):
                    min_idx = i
                    for j in range(i + 1, len(randomized_list)):
                        if randomized_list[min_idx] > randomized_list[j]:
                            min_idx = j
                    randomized_list[i], randomized_list[min_idx] = randomized_list[min_idx], randomized_list[i]
                    w = w_constant
                    h = randomized_list[min_idx] * (WINDOW_HEIGHT / list_size)
                    x = i * (WINDOW_WIDTH / list_size)
                    y = WINDOW_HEIGHT - h

                    h1 = randomized_list[i] * (WINDOW_HEIGHT / list_size)
                    x1 = min_idx * (WINDOW_WIDTH / list_size)
                    y1 = WINDOW_HEIGHT - h
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, w, h))
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, w, h))
                    pygame.display.flip()
                    time.sleep(0.05)
                    h = randomized_list[i] * (WINDOW_HEIGHT / list_size)
                    x = i * (WINDOW_WIDTH / list_size)
                    y = WINDOW_HEIGHT - h
                    color = new_rgb_list[randomized_list[i]]
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

                    h1 = randomized_list[min_idx] * (WINDOW_HEIGHT / list_size)
                    x1 = min_idx * (WINDOW_WIDTH / list_size)
                    y1 = WINDOW_HEIGHT - h
                    color = new_rgb_list[min_idx]
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, w, h1))
                    pygame.display.flip()

pygame.quit()