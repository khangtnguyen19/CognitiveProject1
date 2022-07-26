import random
import pygame
import tkinter as tk
from math_class import Foot
from math_class import CloudNumber
import cv2
import mediapipe as mp
import time


FPS = 60
game_start = 0
mode = 0
correct_answers = 0
wrong_answers = 0
flag = 0


# def game_start_moderator():

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def main( pressed_keys=None):
    # 1- Initialize the game
    global game_start
    global mode
    global correct_answers
    global wrong_answers
    global ans

     # level
    global easy
    global medium
    global hard

    pygame.init()
    easy = 0
    medium = 0
    hard = 0

    width, height = 1530, 780
    bg = [255, 255, 255]
    screen = pygame.display.set_mode((width, height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Math Game')
    pygame.mixer.init()
    print("Rerun")
    welcome = pygame.image.load("resources/welcome_fig.png").convert_alpha()
    welcome = pygame.transform.scale(welcome, (width, height))

    game_background = pygame.image.load("resources/pexels-francesco-ungaro-281260.jpg").convert_alpha()
    game_background = pygame.transform.scale(game_background, (width, height))

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    ans_cloud = random.randint(0, 3)
    print("Check index: ", ans_cloud)

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
    cloud2_num.set_pos(1300, 50)
    cloud3_num = CloudNumber()
    cloud3_num.set_pos(250, 570)
    cloud4_num = CloudNumber()
    cloud4_num.set_pos(1350, 570)



    screen.blit(welcome, (0, 0))
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    big_text = pygame.font.Font("freesansbold.ttf", 50)

    # Easy button
    easy_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 200, 100, 50)
    pygame.draw.rect(screen, [255, 0, 0], easy_button)  # draw button
    text_surf, text_rect = text_objects("Easy", small_text)
    text_rect.center = ((round(width / 2)), round(height / 2) - 175)
    screen.blit(text_surf, text_rect)

    # Medium button
    medium_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 130, 100, 50)
    pygame.draw.rect(screen, [255, 0, 0], medium_button)  # draw button
    text_surf_medium, text_rect_medium = text_objects("Medium", small_text)
    text_rect_medium.center = (round(width / 2), round(height / 2) - 105)
    screen.blit(text_surf_medium, text_rect_medium)

    # Hard button
    hard_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 60, 100, 50)
    pygame.draw.rect(screen, [255, 0, 0], hard_button)  # draw button
    text_surf_hard, text_rect_hard = text_objects("Hard", small_text)
    text_rect_hard.center = (round(width / 2), round(height / 2) - 35)
    screen.blit(text_surf_hard, text_rect_hard)

    print("Check")

    clock = pygame.time.Clock()

    # Varaiable initialization
    # Set up for motion tracking
    fpsClock = pygame.time.Clock()

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)
    pTime = 0


    setCountDown = time.time()
    frameTimeFlag = False
    time_gap = 5.0
    x = 0
    y = 0

    # Calculate the average point
    list = []
    list2 = []
    count = 0
    avgx = 0.0
    avgy = 0.0

    # ---------------------------
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                numbers = random.sample(range(1, 20), 3)
                if event.type == pygame.QUIT:
                    return False

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_BACKSPACE and mode == 1:
                #         mode = 2
                #     if event.key == pygame.K_SPACE and mode == 1:
                #         mode = 0
                #         main()
                if event.type == pygame.MOUSEBUTTONDOWN and game_start == 0:
                    mouse_pos = event.pos  # gets mouse position

                    # checks if mouse position is over the button

                    if easy_button.collidepoint(mouse_pos):
                        # prints current location of mouse
                        game_start = 1
                        easy = 1
                        mode = 0
                        ans = num1 + num2
                        # numbers = random.sample(range(1, 20), 3)
                        while ans in numbers:
                            numbers = random.sample(range(1, 20), 3)

                        numbers.insert(ans_cloud, ans)
                        cloud1_num.set_num(numbers[0])
                        cloud2_num.set_num(numbers[1])
                        cloud3_num.set_num(numbers[2])
                        cloud4_num.set_num(numbers[3])
                    elif medium_button.collidepoint(mouse_pos):
                        # prints current location of mouse
                        game_start = 1
                        medium = 1
                        mode = 0
                        while (num1 < num2):
                            num1 = random.randint(1, 10)
                            num2 = random.randint(1, 10)
                        ans = num1 - num2
                        # numbers = random.sample(range(1, 20), 3)
                        while ans in numbers:
                            numbers = random.sample(range(1, 20), 3)

                        numbers.insert(ans_cloud, ans)
                        cloud1_num.set_num(numbers[0])
                        cloud2_num.set_num(numbers[1])
                        cloud3_num.set_num(numbers[2])
                        cloud4_num.set_num(numbers[3])

                    elif hard_button.collidepoint(mouse_pos):
                        # prints current location of mouse
                        game_start = 1
                        hard = 1
                        mode = 0
                        ans = num1 * num2
                        # numbers = random.sample(range(1, 20), 3)
                        while ans in numbers:
                            numbers = random.sample(range(1, 20), 3)

                        numbers.insert(ans_cloud, ans)
                        cloud1_num.set_num(numbers[0])
                        cloud2_num.set_num(numbers[1])
                        cloud3_num.set_num(numbers[2])
                        cloud4_num.set_num(numbers[3])

                # if event.type == pygame.MOUSEBUTTONDOWN and game_start == 1:
                #     print("Target: ")
                #     mouse_pos = event.pos  # gets mouse position
                #
                #     # checks if mouse position is over the button
                #
                #     # numbers = random.sample(range(1, 20), 3)
                #
                #     if easy_button.collidepoint(mouse_pos):
                #         # prints current location of mouse
                #         game_start = 1
                #         easy = 1
                #         medium = 0
                #         hard = 0
                #         mode = 0
                #         ans = num1 + num2
                #         while ans in numbers:
                #             numbers = random.sample(range(1, 20), 3)
                #
                #         numbers.insert(ans_cloud, ans)
                #         cloud1_num.set_num(numbers[0])
                #         cloud2_num.set_num(numbers[1])
                #         cloud3_num.set_num(numbers[2])
                #         cloud4_num.set_num(numbers[3])
                #
                #         text_surf, text_rect = text_objects(str(num1) + "+" + str(num2) + "= ?", big_text)
                #         screen.blit(text_surf, (round(width / 2) - 50, 10))
                #     if medium_button.collidepoint(mouse_pos):
                #         # prints current location of mouse
                #         print("Medium pushed")
                #         print("Medium num1", num1)
                #         print("medium num2", num2)
                #         game_start = 1
                #         medium = 1
                #         easy = 0
                #         hard = 0
                #         mode = 0
                #         while (num1 < num2):
                #             num1 = random.randint(1, 10)
                #             num2 = random.randint(1, 10)
                #         ans = num1 - num2
                #         # numbers = random.sample(range(1, 20), 3)
                #         while ans in numbers:
                #             numbers = random.sample(range(1, 20), 3)
                #
                #         numbers.insert(ans_cloud, ans)
                #         cloud1_num.set_num(numbers[0])
                #         cloud2_num.set_num(numbers[1])
                #         cloud3_num.set_num(numbers[2])
                #         cloud4_num.set_num(numbers[3])
                #
                #         # text_surf, text_rect = text_objects(str(num1) + "-" + str(num2) + "= ?", big_text)
                #         # screen.blit(text_surf, (round(width / 2) - 50, 10))
                #
                #     if hard_button.collidepoint(mouse_pos):
                #         # prints current location of mouse
                #         game_start = 1
                #         hard = 1
                #         easy = 0
                #         medium = 0
                #         mode = 0
                #         ans = num1 * num2
                #         # numbers = random.sample(range(1, 20), 3)
                #         while ans in numbers:
                #             numbers = random.sample(range(1, 20), 3)
                #
                #         numbers.insert(ans_cloud, ans)
                #         cloud1_num.set_num(numbers[0])
                #         cloud2_num.set_num(numbers[1])
                #         cloud3_num.set_num(numbers[2])
                #         cloud4_num.set_num(numbers[3])

                    foot.rect.left = round(width / 2)
                    foot.rect.top = round(height / 2 - 50)
                    time.sleep(5)




            if game_start == 1:
                if mode == 0:
                    screen.blit(game_background, (0, 0))
                    if easy == 1:
                        text_surf, text_rect = text_objects(str(num1) + "+" + str(num2) + "= ?", big_text)
                        screen.blit(text_surf, (round(width / 2) - 50, 10))


                    elif medium == 1:
                        text_surf, text_rect = text_objects(str(num1) + "-" + str(num2) + "= ?", big_text)
                        screen.blit(text_surf, (round(width / 2) - 50, 10))
                        print("Check")
                        # pygame.display.flip()
                        # time.sleep(5)

                    elif hard == 1:
                        text_surf, text_rect = text_objects(str(num1) + "x" + str(num2) + "= ?", big_text)
                        screen.blit(text_surf, (round(width / 2) - 50, 10))

                    screen.blit(cloud1, (30, 30))
                    screen.blit(cloud2, (1240, 30))
                    screen.blit(cloud3, (30, 540))
                    screen.blit(cloud4, (1210, 540))

                    screen.blit(cloud1_num.image, cloud1_num.rect)
                    screen.blit(cloud2_num.image, cloud2_num.rect)
                    screen.blit(cloud3_num.image, cloud3_num.rect)
                    screen.blit(cloud4_num.image, cloud4_num.rect)

                    # tracking the motion
                    movement_change = 0
                    movement_change_vertical = 0
                    success, frame = cap.read()

                    # Recolor image
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False

                    # Make detection
                    results = pose.process(image)

                    # Find the coordinates
                    if results.pose_landmarks:
                        landmarks = results.pose_landmarks.landmark
                        x = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
                        y = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y

                    cTime = time.time()
                    if frameTimeFlag is False:
                        time.sleep(3)
                        orgx = x
                        orgy = y
                        frameTimeFlag = True
                        print("CALIBRATE DONE!")

                    if frameTimeFlag:
                        list2.insert(0, x)
                        list.insert(0, y)
                        count += 1
                        if count == 3:
                            avgy = sum(list) / 3.0
                            avgx = sum(list2) / 3.0
                            list.pop()
                            list2.pop()
                            count -= 1

                        movement_change = avgx - orgx
                        movement_change_vertical = avgy - orgy
                        time.sleep(0.1)
                        orgx = avgx
                        orgy = avgy


                    # time_gap = time.time()
                    # pTime = cTime

                    # Reset the color back
                    image.flags.writeable = True
                    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    # Render the detection
                    # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    #                           mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                    #                                                  circle_radius=2),
                    #                           mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2,
                    #                                                  circle_radius=2))
                    # # print(mp_pose.POSE_CONNECTIONS)
                    # cv2.imshow('Mediapipe Feed', image)
                    # cv2.putText(img, str(FPS), (50, 50),
                    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    # cv2.imshow("Image", img)
                    fpsClock.tick(FPS)
                    cv2.waitKey(1)
                    # ------------------------------------------------------------------------------#
                    if abs(movement_change) < 0.1 and abs(movement_change_vertical) <0.1:
                        foot.pos_update(movement_change, movement_change_vertical)
                        time.sleep(0.05)

                    foot.rect.clamp_ip(screen_rect)
                    # pressed_mice = pygame.mouse.get_pressed()
                    # foot.pos_update(pressed_mice)
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
                        pygame.time.delay(2000)


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
                        pygame.time.delay(2000)

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
                        pygame.time.delay(2000)

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
                        pygame.time.delay(2000)

                elif mode == 1:
                    num1 = random.randint(1, 10)
                    num2 = random.randint(1, 10)
                    ans_cloud = random.randint(0, 3)
                    medium = 0
                    easy = 0
                    game_start = 0
                    hard = 0
                    print("Check gamestart: ", game_start)
                    screen.fill(0)
                    screen.blit(welcome, (0, 0))

                    # easy button
                    easy_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 200, 100, 50)
                    pygame.draw.rect(screen, [255, 0, 0], easy_button)  # draw button
                    text_surf, text_rect = text_objects("Easy", small_text)
                    text_rect.center = ((round(width / 2)), round(height / 2) - 175)
                    screen.blit(text_surf, text_rect)

                    # Medium button
                    medium_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 130, 100, 50)
                    pygame.draw.rect(screen, [255, 0, 0], medium_button)  # draw button
                    text_surf_medium, text_rect_medium = text_objects("Medium", small_text)
                    text_rect_medium.center = (round(width / 2), round(height / 2) - 105)
                    screen.blit(text_surf_medium, text_rect_medium)

                    # Hard button
                    hard_button = pygame.Rect(round(width / 2) - 50, round(height / 2) - 60, 100, 50)
                    pygame.draw.rect(screen, [255, 0, 0], hard_button)  # draw button
                    text_surf_hard, text_rect_hard = text_objects("Hard", small_text)
                    text_rect_hard.center = (round(width / 2), round(height / 2) - 35)
                    screen.blit(text_surf_hard, text_rect_hard)

            pygame.display.update()


if __name__ == '__main__':
    main()

