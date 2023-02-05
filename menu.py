import pygame.transform

import ui_tools as pgb
from instructions import instructions
from score_board import scoreboard
from leaderboard import leaderboard
from skins import skins
import json
from Level import *
from level_screen import level_screen
from platformer_game import platformer_game
from helpful_functions import calculate_current_level, blit_text
from users import users
from letter import Letter
import random

pygame.init()


def menu(screen):

    def change_screen(func):
        with open('variables.json', 'w') as wvar:
            json.dump(var, wvar, indent=4)
        func["func"]()

    def end_screen():
        with open('variables.json', 'w') as wvar:
            json.dump(var, wvar, indent=4)
        pygame.quit()
        exit()

    def show_multiplayer():
        show_no_multiplayer_page = True
        return show_no_multiplayer_page

    with open('variables.json', 'r') as f:
        var = json.load(f)
    clock = pygame.time.Clock()
    background = pygame.image.load("images/Menu_page/new_winter_bg.jpg").convert()
    background = pygame.transform.scale(background, (ss.SCREEN_WIDTH, ss.SCREEN_HEIGHT))
    help_text = pygame.transform.scale(pygame.image.load("images/Menu_page/help.png").convert_alpha(),
                                       (ss.SCREEN_WIDTH / 5.7, ss.SCREEN_HEIGHT / 8.4))  # 250, 50
    score_board_img = pygame.transform.scale(
        pygame.image.load("images/Menu_page/scoreboard.png").convert_alpha(),
        (ss.SCREEN_WIDTH / 9.53, ss.SCREEN_HEIGHT / 8.4))  # 150, 100
    leader_board_img = pygame.transform.scale(
        pygame.image.load("images/Menu_page/leaderboard.png").convert_alpha(),
        (ss.SCREEN_WIDTH / 11.1, ss.SCREEN_HEIGHT / 6.7))  # 125, 125
    skins_img = pygame.transform.scale(
        pygame.image.load("images/Menu_page/skins.png").convert(),
        (ss.SCREEN_WIDTH / 7.15, ss.SCREEN_HEIGHT / 8.4))  # 200, 100
    lock = pygame.transform.scale(
        pygame.image.load("images/Menu_page/lock_bg.png").convert_alpha(),
        (3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16))

    leader_board_img.set_colorkey((255, 255, 255))

    level_img = calculate_current_level(var)
    level_img.clear()
    level_img.letter_list = level_generator(level_img.no_of_letter)
    level_img.start = 0
    level_img.make_platforms_objects()
    level_img.make_letters()
    level_img.draw_for_display()
    level_img.make_power_ups()
    # level_img = level_img()
    level_img = level_img.bg_display
    level_img = pygame.transform.scale(
        level_img,
        (ss.SCREEN_WIDTH / 2.86,
         ss.SCREEN_HEIGHT / 1.56 / level_img.get_width() * level_img.get_height()))

    quit_button = pgb.Button((ss.SCREEN_WIDTH / 2 - 3 * ss.SCREEN_WIDTH / 16 / 2, 3 * ss.SCREEN_HEIGHT / 4,
                              3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16), (255, 255, 255),
                             end_screen, hover_color=(150, 150, 150), clicked_color=(80, 80, 80), text="Quit",
                             font=pygame.font.Font(None, int(ss.SCREEN_WIDTH // 17.875)), font_color=(0, 0, 0),
                             border_radius=int(ss.SCREEN_WIDTH // 95.33))
    users_button = pgb.Button(
        (ss.SCREEN_WIDTH - 3 * ss.SCREEN_WIDTH / 16, ss.SCREEN_HEIGHT / 2 - 3 * ss.SCREEN_HEIGHT / 32,
         3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16), (255, 255, 255),
        change_screen, hover_color=(150, 150, 150), clicked_color=(80, 80, 80), text="Users",
        font=pygame.font.Font(None, int(ss.SCREEN_WIDTH / 17.875)), font_color=(0, 0, 0),
        func=lambda: users(screen, menu))
    instructions_btn = pgb.Button((13 * ss.SCREEN_WIDTH / 16, 0, 3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16),
                                  (255, 255, 255), change_screen, func=lambda: instructions(screen, menu),
                                  hover_color=(150, 150, 150), clicked_color=(80, 80, 80), image=help_text)
    scoreboard_btn = pgb.Button((0, 13 * ss.SCREEN_HEIGHT / 16, 3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16),
                                (255, 255, 255), change_screen, func=lambda: scoreboard(screen, menu),
                                hover_color=(150, 150, 150), clicked_color=(80, 80, 80), image=score_board_img,
                                text="Scoreboard", image_align="bottom", font_color=(0, 0, 0))
    leaderboard_btn = pgb.Button(
        (13 * ss.SCREEN_WIDTH / 16, 13 * ss.SCREEN_HEIGHT / 16, 3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16),
        (255, 255, 255), change_screen,
        hover_color=(150, 150, 150), clicked_color=(80, 80, 80), image=leader_board_img,
        text="Leaderboard", image_align="bottom", font_color=(0, 0, 0), func=lambda: leaderboard(screen, menu))

    single_player = pgb.Button(
        (ss.SCREEN_WIDTH / 4, ss.SCREEN_HEIGHT / 2, 3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16),
        (255, 185, 2), change_screen, hover_color=(254, 158, 2),
        clicked_color=(187, 99, 5), func=lambda: platformer_game(screen, menu),
        text="Single player", border_radius=int(ss.SCREEN_WIDTH // 143), border_color=(254, 158, 2),
        font=pygame.font.Font(None, int(ss.SCREEN_WIDTH / 29.79)))
    multiplayer = pgb.Button(
        (3 * ss.SCREEN_WIDTH / 4 - 3 * ss.SCREEN_WIDTH / 16, ss.SCREEN_HEIGHT / 2, 3 * ss.SCREEN_WIDTH / 16,
         3 * ss.SCREEN_HEIGHT / 16),
        (5, 176, 254), show_multiplayer, hover_color=(8, 143, 254), clicked_color=(2, 92, 177),
        text="Multiplayer", border_radius=10, border_color=(8, 143, 254),
        font=pygame.font.Font(None, int(ss.SCREEN_WIDTH // 29.79)), image=lock,
        image_position=(0, 0))
    multiplayer.text_position = (multiplayer.rect.w / 2 - multiplayer.text.get_width() / 2,
                                 multiplayer.rect.h / 2 - multiplayer.text.get_height() / 2)
    skins_btn = pgb.Button(
        (0, 0, 3 * ss.SCREEN_WIDTH / 16, 3 * ss.SCREEN_HEIGHT / 16),
        (255, 255, 255), change_screen, hover_color=(150, 150, 150),
        clicked_color=(80, 80, 80), font_color=(0, 0, 0),
        text="Avatar", image_align="bottom", image=skins_img, func=lambda: skins(screen, menu))
    level_btn = pgb.Button(
        (ss.SCREEN_WIDTH / 2 - level_img.get_width() / 2, ss.SCREEN_HEIGHT / 4 - level_img.get_height() / 2,
         level_img.get_width(), level_img.get_height()), (0, 0, 0),
        change_screen,
        image=level_img, func=lambda: level_screen(screen, menu))

    button_lis = [quit_button, instructions_btn, scoreboard_btn, leaderboard_btn, single_player, multiplayer,
                  skins_btn, level_btn, users_button]
    font = pygame.font.Font(None, int(ss.SCREEN_WIDTH // 39.72))
    alpha = 0
    games_played = sorted(var["users"][var["current_user"][0]][1], key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)

    current_stars = 0
    for level in level_list:
        for game in games_played:
            if level.str == game[0]:
                current_stars += game[1]
                break

    letter_lis = []
    font_stars = pygame.font.Font("images/Menu_page/SnowtopCaps.ttf", 50)
    number_stars = font_stars.render(str(current_stars), True, (0, 0, 0))
    stars_img = pygame.image.load('images/Menu_page/numberOfStars.png').convert()
    stars_img = pygame.transform.scale(stars_img, (40 / stars_img.get_height() * stars_img.get_width(), 40))
    stars_img.set_colorkey((255, 255, 255))
    # stars_img.set_colorkey((0, 0, 0))
    # surface_stars = pygame.Surface(
    #     (15 + number_stars.get_width() + 41/2, number_stars.get_height() - 22))
    # surface_stars.set_alpha(120)
    while True:
        screen.blit(background, (0, 0))
        # screen.blit(surface_stars, (916 + 41/2, 15))
        screen.blit(stars_img, (916, 18))
        screen.blit(number_stars, (916 + 41 + 5, 3))
        print(stars_img.get_width())
        show_no_multiplayer_page = multiplayer.value_from_function or False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                end_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                rand_letter = random.choice(tuple(Letter.letter_dic.keys()))
                image = pygame.image.load(Letter.letter_dic.get(rand_letter))
                image = pygame.transform.scale(image, (50, 50))
                letter_lis.append([image, [event.pos[0], event.pos[1]]])
            for i in button_lis:
                i.check_event(event)
        if show_no_multiplayer_page:
            blit_text(screen, "Multiplayer would be added in the next update",
                      (multiplayer.rect.centerx, multiplayer.rect.bottom + int(ss.SCREEN_WIDTH / 39.72) / 2),
                      font, multiplayer.rect.right, color=(255, 255, 255, 0), alpha=min(alpha, 255))
            if alpha <= 300:  # Don't change this to ss.SCREEN_WIDTH / number
                alpha += 0.75

        for i in button_lis:
            i.update(screen)

        for i in letter_lis:
            if i[1][1] + 0.5 < ss.SCREEN_HEIGHT - i[0].get_height():
                i[1][1] += 0.5
            screen.blit(i[0], i[1])
        pygame.display.update()
        clock.tick()
        # print(clock.get_fps())


if __name__ == "__main__":
    root = pygame.display.set_mode((ss.SCREEN_WIDTH, ss.SCREEN_HEIGHT))
    menu(root)
