import pygame
import platform_and_obstacles as po
import screen_size as ss
import letter
import cv2
import numpy as np
import power_ups as pu


class Level:
    def __init__(self, bg, no_tiles: int):
        self.bg_start = cv2.imread(bg)
        self.platform_group = pygame.sprite.Group()
        self.obstruct_group = pygame.sprite.Group()
        self.letter_group = pygame.sprite.Group()
        self.power_up_group = pygame.sprite.Group()
        self.start = 0
        self.width = no_tiles * ss.tile_size
        bg_lis = []
        for i in range(int(self.width / self.bg_start.shape[0]) + 1):
            bg_lis.append(self.bg_start)
        self.bg = np.concatenate(bg_lis, axis=1)
        self.bg = pygame.image.frombuffer(self.bg.tostring(), self.bg.shape[1::-1],
                                          "RGB").convert()
        self.bg = pygame.transform.scale(self.bg, (ss.SCREEN_HEIGHT / self.bg.get_height() * self.bg.get_width(),
                                                   ss.SCREEN_HEIGHT))
        self.bg_display = pygame.image.frombuffer(self.bg_start.tostring(), self.bg_start.shape[1::-1],
                                                  "RGB").convert()
        self.bg_display = pygame.transform.scale(self.bg_display, (ss.SCREEN_WIDTH, ss.SCREEN_HEIGHT))
        # self.bg_display = pygame.transform.scale(
        #     self.bg_display,
        #     (ss.SCREEN_WIDTH / 2.86,
        #      ss.SCREEN_HEIGHT / 1.56 / self.bg_display.get_width() * self.bg_display.get_height()))

    def draw_for_display(self):
        for i in self.obstruct_group:
            if i.rect.x <= ss.SCREEN_WIDTH:
                # i_pos = ((i.rect.x / ss.SCREEN_WIDTH) * self.bg_display.get_width(),
                #          (i.rect.y / ss.SCREEN_HEIGHT) * self.bg_display.get_height())
                # i_image = pygame.transform.scale(i.image, (i.rect.w * self.bg_display.get_width() / ss.SCREEN_WIDTH,
                #                                            i.rect.h * self.bg_display.get_height() / ss.SCREEN_HEIGHT))
                # i_image.set_colorkey((0, 0, 0))
                self.bg_display.blit(i.image, i.rect)

        for i in self.platform_group:
            if i.rect.x <= ss.SCREEN_WIDTH:
                # i_pos = ((i.rect.x / ss.SCREEN_HEIGHT) * self.bg_display.get_height(),
                #          (i.rect.y / ss.SCREEN_HEIGHT) * self.bg_display.get_height())
                # i_image = pygame.transform.scale(i.image, (i.rect.w * self.bg_display.get_width() / ss.SCREEN_WIDTH,
                #                                            i.rect.h * self.bg_display.get_height() / ss.SCREEN_HEIGHT))
                # i_image.set_colorkey((0, 0, 0))
                self.bg_display.blit(i.image, i.rect)
        for i in self.letter_group:
            if i.rect.x <= ss.SCREEN_WIDTH:
                self.bg_display.blit(i.image, (i.rect.x, i.rect.y + ss.tile_size))
        for i in self.power_up_group:
            if i.rect.x <= ss.SCREEN_WIDTH:
                self.bg_display.blit(i.image, i.rect)

    def draw(self, screen):
        screen.blit(self.bg, (self.start, 0))


class Level1(Level):
    def __init__(self):
        super(Level1, self).__init__(r"images/Background_platformer/BG_03.png", 62)
        self.letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.make_platforms_objects()
        self.make_letters()
        self.draw_for_display()
        self.str = "level1"
        self.stars = [5, 15, 25]
        self.time = 90

    def make_platforms_objects(self):
        # two rows at the bottom of the screen
        for j in range(1, 3):
            self.platform_group.add(po.Platform(0 * ss.tile_size, ss.SCREEN_HEIGHT - j * ss.tile_size, 63, False,
                                                "images/platform/platform_sprites_(1).png"))
        # # ground row
        self.platform_group.add(po.Platform(0, ss.SCREEN_HEIGHT - 3 * ss.tile_size, 63, False))

        # obstacles and platforms
        self.platform_group.add(po.Platform(7 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))  # first platform
        self.platform_group.add(po.Platform(10 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size, 7,
                                            False))  # down row after first platform
        self.platform_group.add(
            po.Platform(12 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size, 2))  # second tower platform

        self.obstruct_group.add(po.Obstacle(19 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))  # cutter
        self.platform_group.add(po.Platform(29 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(32 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size, 7, False))
        self.platform_group.add(po.Platform(34 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size, 1))

        self.obstruct_group.add(po.Obstacle(43 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))  # cutter
        self.platform_group.add(po.Platform(53 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(56 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size, 6, False))
        self.platform_group.add(po.Platform(58 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size, 1))

        # Letters

    def make_letters(self):
        self.letter_group.add(letter.Letter(self.letter_list[0], 8 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 8 * ss.tile_size))  # on the first block
        # on the second block
        self.letter_group.add(
            letter.Letter(self.letter_list[1], 12.5 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[2], 14.5 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(23 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[3], 30 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[4], 35 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(35 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[5], 38 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[6], 48 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[7], 54 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[8], 60 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size))
        self.letter_group.add(
            letter.Letter(self.letter_list[9], 59 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size))


class Level2(Level):
    def __init__(self):
        super(Level2, self).__init__(r"images/Background_platformer/BG_04.png", 112)
        self.letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        self.make_platforms_objects()
        self.make_letters()
        self.draw_for_display()
        self.make_power_ups()
        self.str = "level2"
        self.stars = [5, 15, 25]
        self.time = 90

    def make_letters(self):
        self.letter_group.add(letter.Letter(self.letter_list[0], 4 * ss.tile_size,  # tile_size = 200
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))  # 1 is the original +3 ground platform+1 bouncing=5 normally, 5
        self.letter_group.add(letter.Letter(self.letter_list[1], 8 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 8 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[2], 14 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 12 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[3], 23 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(31 * ss.tile_size,
                                                   ss.SCREEN_HEIGHT - 12 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[4], 37 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 9 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[5], 40 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[6], 54 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 11 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[7], 59 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[8], 67 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[9], 73 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 13 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[10], 80 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 13 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[11], 85 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 10 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[12], 92 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 13 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[13], 98 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 14 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(102 * ss.tile_size,
                                                   ss.SCREEN_HEIGHT - 14 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[14], 106 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 6 * ss.tile_size))

    def make_platforms_objects(self):
        for j in range(1, 3):
            self.platform_group.add(po.Platform(0 * ss.tile_size, ss.SCREEN_HEIGHT - j * ss.tile_size, 113, False,
                                                "images/platform/platform_sprites_(1).png"))
        # # ground row
        self.platform_group.add(po.Platform(0, ss.SCREEN_HEIGHT - 3 * ss.tile_size, 113, False))  # 0+3
        # the upper stuff should be copied

        self.platform_group.add(po.Platform(8 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))  # x, y, no_of_tiles, rectangle or curve
        self.platform_group.add(po.Platform(13 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(25 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(30 * ss.tile_size, ss.SCREEN_HEIGHT - 13 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(35 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(53 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 4, False))
        self.platform_group.add(po.Platform(69 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(76 * ss.tile_size, ss.SCREEN_HEIGHT - 11 * ss.tile_size, 7, False))
        self.platform_group.add(po.Platform(84 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 7, False))
        self.platform_group.add(po.Platform(92 * ss.tile_size, ss.SCREEN_HEIGHT - 11 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(97 * ss.tile_size, ss.SCREEN_HEIGHT - 15 * ss.tile_size, 1))
        self.platform_group.add(po.Platform(102 * ss.tile_size, ss.SCREEN_HEIGHT - 11 * ss.tile_size, 2, False))
        self.platform_group.add(po.Platform(105 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(106 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size, 6, False))

        self.obstruct_group.add(po.Obstacle(17 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(42 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(50 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size,
                                            "snowman", w=ss.tile_size * 2, h=ss.tile_size * 2))
        self.obstruct_group.add(po.Obstacle(63 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size,
                                            "tree", w=ss.tile_size * 2 / 1.7, h=ss.tile_size * 2))
        self.obstruct_group.add(po.Obstacle(78 * ss.tile_size, ss.SCREEN_HEIGHT - 12 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(87 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size,
                                            "snowman", w=ss.tile_size * 2, h=ss.tile_size * 2))
        self.obstruct_group.add(po.Obstacle(109 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size,
                                            "tree", w=ss.tile_size * 2 / 1.7, h=ss.tile_size * 2))

    def make_power_ups(self):
        self.power_up_group.add(pu.PowerUp(46 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size))
        self.power_up_group.add(pu.PowerUp(71 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size))


class Level3(Level):
    def __init__(self):
        super(Level3, self).__init__(r"images/Background_platformer/BG_04.png", 91)
        self.letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        self.make_platforms_objects()
        self.make_letters()
        self.draw_for_display()
        self.make_power_ups()
        self.str = "level3"
        self.stars = [5, 15, 25]
        self.time = 90

    def make_letters(self):
        self.letter_group.add(letter.Letter(self.letter_list[0], 3 * ss.tile_size,  # tile_size = 200
                                            ss.SCREEN_HEIGHT - 6 * ss.tile_size))  # 1 is the original +3 ground platform+1 bouncing=5 normally, 5
        self.letter_group.add(letter.Letter(self.letter_list[1], 14 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 8 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[2], 20 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[3], 23 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 9 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(53 * ss.tile_size,
                                                   ss.SCREEN_HEIGHT - 10 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[4], 28 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 11 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[5], 34 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[6], 59 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 11 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[7], 64 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 11 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[8], 72 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[9], 75 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 7 * ss.tile_size))
        self.letter_group.add(letter.MysteryLetter(79 * ss.tile_size,
                                                   ss.SCREEN_HEIGHT - 13 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[10], 82 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 9 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[11], 87 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 7 * ss.tile_size))
        self.letter_group.add(letter.Letter(self.letter_list[12], 89 * ss.tile_size,
                                            ss.SCREEN_HEIGHT - 5 * ss.tile_size))

    def make_platforms_objects(self):
        for j in range(1, 3):
            self.platform_group.add(po.Platform(0 * ss.tile_size, ss.SCREEN_HEIGHT - j * ss.tile_size, 92, False,
                                                "images/platform/platform_sprites_(1).png"))
        # # ground row
        self.platform_group.add(po.Platform(0, ss.SCREEN_HEIGHT - 3 * ss.tile_size, 92, False))  # 0+3
        # the upper stuff should be copied

        self.platform_group.add(po.Platform(0 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size, 8, False))  # x, y, no_of_tiles, rectangle or curve
        self.platform_group.add(po.Platform(7 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(9 * ss.tile_size, ss.SCREEN_HEIGHT - 8 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(11 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 3))
        self.platform_group.add(po.Platform(23 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 2))
        self.platform_group.add(po.Platform(27 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 3))
        self.platform_group.add(po.Platform(32 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(44 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(46 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(48 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(49 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(50 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(52 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 3))
        self.platform_group.add(po.Platform(56 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 3))
        self.platform_group.add(po.Platform(62 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(64 * ss.tile_size, ss.SCREEN_HEIGHT - 9 * ss.tile_size, 0))
        self.platform_group.add(po.Platform(67 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 1, False))
        self.platform_group.add(po.Platform(69 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size, 0))
        self.platform_group.add(po.Platform(75 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size, 0))
        self.platform_group.add(po.Platform(79 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size, 0))
        self.platform_group.add(po.Platform(82 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size, 0))
        self.platform_group.add(po.Platform(85 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size, 4, False))

        self.obstruct_group.add(po.Obstacle(26 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(12 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(46 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(37 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size,
                                            "snowman", w=ss.tile_size * 2, h=ss.tile_size * 2))
        self.obstruct_group.add(po.Obstacle(43 * ss.tile_size, ss.SCREEN_HEIGHT - 5 * ss.tile_size,
                                            "tree", w=ss.tile_size * 2 / 1.7, h=ss.tile_size * 2))
        self.obstruct_group.add(po.Obstacle(56 * ss.tile_size, ss.SCREEN_HEIGHT - 10 * ss.tile_size,
                                            "spikes", w=ss.tile_size * 2, h=ss.tile_size))
        self.obstruct_group.add(po.Obstacle(85 * ss.tile_size, ss.SCREEN_HEIGHT - 7 * ss.tile_size,
                                            "snowman", w=ss.tile_size * 2, h=ss.tile_size * 2))

    def make_power_ups(self):
        self.power_up_group.add(pu.PowerUp(17 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size))
        self.power_up_group.add(pu.PowerUp(39 * ss.tile_size, ss.SCREEN_HEIGHT - 4 * ss.tile_size))
        self.power_up_group.add(pu.PowerUp(69 * ss.tile_size, ss.SCREEN_HEIGHT - 6 * ss.tile_size))


class Level4(Level):
    def __init__(self):
        super(Level4, self).__init__(r"images/Background_platformer/BG_04.png", 112)
        self.letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        self.make_platforms_objects()
        self.make_letters()
        self.draw_for_display()
        self.make_power_ups()
        self.str = "level4"
        self.stars = [5, 15, 25]
        self.time = 90

    def make_platforms_objects(self):
        pass

    def make_power_ups(self):
        pass

    def make_letters(self):
        pass


class Level5(Level):
    def __init__(self):
        super(Level5, self).__init__(r"images/Background_platformer/BG_04.png", 112)
        self.letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        self.make_platforms_objects()
        self.make_letters()
        self.draw_for_display()
        self.make_power_ups()
        self.str = "level5"
        self.stars = [5, 15, 25]
        self.time = 90

    def make_platforms_objects(self):
        pass

    def make_power_ups(self):
        pass

    def make_letters(self):
        pass


level1 = Level1()
level2 = Level2()
level3 = Level3()
level4 = Level4()
level5 = Level5()
level_list = [level1, level2, level3, level4, level5]
