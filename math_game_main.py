import random
import pygame
import config
from pygame.locals import *
from math_class import Foot
from math_class import CloudNumber

FPS = 60
game_start = 0
mode = 0
correct_answers = 0
wrong_answers = 0
flag = 0


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def main(pressed_keys=None):
    # 1- Initialize the game
    global game_start
    global mode
    global correct_answers
    global wrong_answers
    global flag
    pygame.init()
    width, height = 960, 480
    bg = [255, 255, 255]
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Math Game')
    pygame.mixer.init()

    welcome = pygame.image.load("resources/welcome_fig.png").convert_alpha()
    welcome = pygame.transform.scale(welcome, (width, height))

    game_background = pygame.image.load("resources/pexels-francesco-ungaro-281260.jpg").convert_alpha()
    game_background = pygame.transform.scale(game_background, (width, height))
    # welcome.set_colorkey((255, 255, 255), RLEACCEL)

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = num1 + num2
    ans_cloud = random.randint(0, 3)

    cloud1 = pygame.image.load("resources/cloud1.png").convert_alpha()
    cloud1 = pygame.transform.scale(cloud1, (71 * 5, 40 * 5))
    cloud2 = pygame.image.load("resources/cloud2.png").convert_alpha()
    cloud2 = pygame.transform.scale(cloud2, (52 * 5, 39 * 5))
    cloud3 = pygame.image.load("resources/cloud3.png").convert_alpha()
    cloud3 = pygame.transform.scale(cloud3, (69 * 5, 28 * 5))
    cloud4 = pygame.image.load("resources/cloud4.png").convert_alpha()
    cloud4 = pygame.transform.scale(cloud4, (58 * 5, 35 * 5))

    correct_answer_cloud = pygame.image.load("resources/correct_answer_cloud.png").convert_alpha()
    correct_answer_cloud = pygame.transform.scale(correct_answer_cloud, (58 * 5, 34 * 5))
    wrong_answer_cloud = pygame.image.load("resources/wrong_answer_cloud.png").convert_alpha()
    wrong_answer_cloud = pygame.transform.scale(wrong_answer_cloud, (58 * 5, 34 * 5))

    foot = Foot()
    foot.rect.left = round(width / 2)
    foot.rect.top = round(height / 2 - 50)

    cloud1_num = CloudNumber()
    cloud1_num.set_pos(250, 60)
    cloud2_num = CloudNumber()
    cloud2_num.set_pos(750, 50)
    cloud3_num = CloudNumber()
    cloud3_num.set_pos(250, 350)
    cloud4_num = CloudNumber()
    cloud4_num.set_pos(710, 410)

    numbers = random.sample(range(1, 20), 3)
    while ans in numbers:
        numbers = random.sample(range(1, 20), 3)

    numbers.insert(ans_cloud, ans)
    cloud1_num.set_num(numbers[0])
    cloud2_num.set_num(numbers[1])
    cloud3_num.set_num(numbers[2])
    cloud4_num.set_num(numbers[3])

    screen.blit(welcome, (0, 0))
    button = pygame.Rect(round(width / 2) - 50, height - 300, 100, 50)
    pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    big_text = pygame.font.Font("freesansbold.ttf", 50)
    text_surf, text_rect = text_objects("GO!", small_text)
    text_rect.center = ((round(width / 2)), round(height - 300 + (50 / 2)))
    screen.blit(text_surf, text_rect)
    clock = pygame.time.Clock()
    random_cloud = random.randint(1, 4)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and mode == 1:
                    mode = 2
                if event.key == pygame.K_SPACE and mode == 1:
                    mode = 0
                    main()

            if event.type == pygame.MOUSEBUTTONDOWN and game_start == 0:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    game_start = 1

        if game_start == 1:
            # screen.fill(bg)
            if mode == 0:
                screen.blit(game_background, (0, 0))
                text_surf, text_rect = text_objects(str(num1) + "+" + str(num2) + "= ?", big_text)
                screen.blit(text_surf, (round(width / 2) - 50, 10))

                screen.blit(cloud1, (30, 30))
                screen.blit(cloud2, (680, 30))
                screen.blit(cloud3, (30, 310))
                screen.blit(cloud4, (660, 300))

                screen.blit(cloud1_num.image, cloud1_num.rect)
                screen.blit(cloud2_num.image, cloud2_num.rect)
                screen.blit(cloud3_num.image, cloud3_num.rect)
                screen.blit(cloud4_num.image, cloud4_num.rect)

                pressed_mice = pygame.mouse.get_pressed()
                foot.pos_update(pressed_mice)
                screen.blit(foot.image, foot.rect)
                cloud_size = (round(width / 2 - (58 * 5 / 2)), round(height / 2 - (34 * 5 / 2)))
                if foot.rect.colliderect(cloud1_num.rect):
                    if ans_cloud == 0:
                        screen.blit(correct_answer_cloud, cloud_size)
                        correct_answers += 1
                    else:
                        screen.blit(wrong_answer_cloud, cloud_size)
                        wrong_answers += 1
                    print("collision1")
                    mode = 1
                    pygame.display.update()
                    pygame.time.delay(5000)


                if foot.rect.colliderect(cloud2_num.rect):
                    if ans_cloud == 1:
                        screen.blit(correct_answer_cloud, cloud_size)
                        correct_answers += 1
                    else:
                        screen.blit(wrong_answer_cloud, cloud_size)
                        wrong_answers += 1
                    print("collision2")
                    mode = 1
                    pygame.display.update()
                    pygame.time.delay(5000)

                if foot.rect.colliderect(cloud3_num.rect):
                    if ans_cloud == 2:
                        screen.blit(correct_answer_cloud, cloud_size)
                        correct_answers += 1
                    else:
                        screen.blit(wrong_answer_cloud, cloud_size)
                        wrong_answers += 1
                    print("collision3")
                    mode = 1
                    pygame.display.update()
                    pygame.time.delay(5000)

                if foot.rect.colliderect(cloud4_num.rect):
                    if ans_cloud == 3:
                        screen.blit(correct_answer_cloud, cloud_size)
                        correct_answers += 1
                    else:
                        screen.blit(wrong_answer_cloud, cloud_size)
                        wrong_answers += 1
                    print("collision4")
                    mode = 1
                    pygame.display.update()
                    pygame.time.delay(5000)

            elif mode == 1:
                screen.blit(game_background, (0, 0))
                text_surf, text_rect = text_objects("Press Space to Continue or Backspace to finish", small_text)
                text_rect.center = ((round(width / 2)), round(height - 300 + (50 / 2)))
                screen.blit(text_surf, text_rect)

            elif mode == 2:
                screen.blit(game_background, (0, 0))
                text_surf, text_rect = text_objects("Scores:", big_text)
                text_rect.center = ((round(width / 2)), 50)
                text_surf2, text_rect2 = text_objects("Correct Answers: " + str(correct_answers), small_text)
                text_rect2.center = ((round(width / 2)), round(height - 300 + (50 / 2)))
                text_surf3, text_rect3 = text_objects("Wrong Answers: " + str(wrong_answers), small_text)
                text_rect3.center = ((round(width / 2)), round(height - 300 + (50 / 2) + 50))
                screen.blit(text_surf, text_rect)
                screen.blit(text_surf2, text_rect2)
                screen.blit(text_surf3, text_rect3)

        pygame.display.update()


if __name__ == '__main__':
    main()
