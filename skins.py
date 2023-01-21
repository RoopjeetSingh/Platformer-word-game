import pygame
import ui_tools as pgb
import screen_size as ss
import json

pygame.init()


def skins(screen, back_button_func):
    def change_skin(skin: dict):
        var["users"][var["current_user"][0]][2] = skin["skin"]

    def change_screen(func):
        with open('variables.json', 'w') as wvar:
            json.dump(var, wvar, indent=4)
        func()

    with open('variables.json', 'r') as f:
        var = json.load(f)
    clock = pygame.time.Clock()
    background = pygame.image.load("images/Menu_page/menu_bg.png").convert()
    santa = pygame.image.load("images/Santa/Idle (1).png").convert_alpha()
    boy = pygame.image.load("images/Boy/Idle (1).png").convert_alpha()
    female_zombie = pygame.image.load("images/Female_zombie/Idle (1).png").convert_alpha()
    male_zombie = pygame.image.load("images/Male_zombie/Idle (1).png").convert_alpha()

    santa = pygame.transform.scale(santa,
                                   (ss.SCREEN_WIDTH / 5, ss.SCREEN_WIDTH / 5 / santa.get_width() * santa.get_height()))
    santa.set_colorkey((0, 0, 0))

    boy = pygame.transform.scale(boy,
                                 (ss.SCREEN_WIDTH / 5, ss.SCREEN_WIDTH / 5 / boy.get_width() * boy.get_height()))
    boy.set_colorkey((0, 0, 0))

    male_zombie = pygame.transform.scale(male_zombie,
                                         (ss.SCREEN_WIDTH / 5,
                                          ss.SCREEN_WIDTH / 5 / male_zombie.get_width() * male_zombie.get_height()))
    male_zombie.set_colorkey((0, 0, 0))

    female_zombie = pygame.transform.scale(female_zombie,
                                           (ss.SCREEN_WIDTH / 5,
                                            ss.SCREEN_WIDTH / 5 / female_zombie.get_width() * female_zombie.get_height()))
    female_zombie.set_colorkey((0, 0, 0))

    back_image = pygame.transform.scale(pygame.image.load("images/back_button.png").convert_alpha(),
                                        (ss.SCREEN_WIDTH / 14.3, ss.SCREEN_HEIGHT / 8.4))  # 75, 75

    font = pygame.font.Font(None, 156)
    skins_txt = font.render("Choose your Avatar", True, (255, 255, 255))

    back_button = pgb.Button((20, 20, ss.SCREEN_WIDTH / 19.1, ss.SCREEN_HEIGHT / 10.4), (0, 0, 0),
                             lambda: change_screen(lambda: back_button_func(screen)), image=back_image, fill_bg=False,
                             border_color=(255, 255, 255))

    santa_btn = pgb.Button((ss.SCREEN_WIDTH / 8 - santa.get_width() / 2, ss.SCREEN_HEIGHT / 2 - santa.get_height() / 2,
                            santa.get_width(), santa.get_height()), (0, 0, 0), change_skin,
                           image=santa, border_color=(255, 255, 255), border_radius=1, skin="santa")
    boy_btn = pgb.Button((3 * ss.SCREEN_WIDTH / 8 - boy.get_width() / 2, ss.SCREEN_HEIGHT / 2 - boy.get_height() / 2,
                          boy.get_width(), boy.get_height()), (0, 0, 0), change_skin, image=boy,
                         border_color=(255, 255, 255), border_radius=1, skin="boy")
    female_zombie_btn = pgb.Button(
        (5 * ss.SCREEN_WIDTH / 8 - female_zombie.get_width() / 2, ss.SCREEN_HEIGHT / 2 - female_zombie.get_height() / 2,
         female_zombie.get_width(), female_zombie.get_height()), (0, 0, 0), change_skin,
        image=female_zombie, border_color=(255, 255, 255), border_radius=1, skin="female_zombie")
    male_zombie_btn = pgb.Button(
        (7 * ss.SCREEN_WIDTH / 8 - santa.get_width() / 2, ss.SCREEN_HEIGHT / 2 - santa.get_height() / 2,
         santa.get_width(), santa.get_height()), (0, 0, 0), change_skin, image=male_zombie,
        border_color=(255, 255, 255), border_radius=1, skin="male_zombie")
    button_lis = [back_button, santa_btn, boy_btn, female_zombie_btn, male_zombie_btn]
    while True:
        santa_border = boy_border = female_zombie_border = male_zombie_border = 0
        match var["users"][var["current_user"][0]][2]:
            case "santa":
                santa_border = 25
            case "boy":
                boy_border = 25
            case "male_zombie":
                male_zombie_border = 25
            case "female_zombie":
                female_zombie_border = 25
        santa_btn.border_thickness = santa_border
        boy_btn.border_thickness = boy_border
        female_zombie_btn.border_thickness = female_zombie_border
        male_zombie_btn.border_thickness = male_zombie_border
        screen.blit(background, (0, 0))
        screen.blit(skins_txt, (
            ss.SCREEN_WIDTH / 2 - skins_txt.get_width() / 2, ss.SCREEN_HEIGHT / 12 - skins_txt.get_height() / 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                with open('variables.json', 'w') as wvar:
                    json.dump(var, wvar, indent=4)
                pygame.quit()
                exit()
            for i in button_lis:
                i.check_event(event)

        for i in button_lis:
            i.update(screen)
        pygame.display.update()
        clock.tick(75)


if __name__ == "__main__":
    from menu import menu

    root = pygame.display.set_mode((ss.SCREEN_WIDTH, ss.SCREEN_HEIGHT))
    skins(root, menu)
