import pygame

from player import *
from Level import level1
import screen_size as ss
import json

pygame.init()


def platformer_game(screen):
    pressed = False
    with open('variables.json', 'r') as f:
        var = json.load(f)
    current_level = eval(var["level"])
    clock = pygame.time.Clock()
    player = Player(4*ss.tile_size, 4*ss.tile_size, var["skins"])
    while True:
        current_level.draw(screen)
        current_level.obstruct_group.draw(screen)
        current_level.platform_group.draw(screen)
        current_level.letter_group.draw(screen)
        for i in current_level.letter_group:
            i.bounce_brighten()
        screen.blit(player.image, player.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        if not player.kill_player:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.move_right(current_level, "right")
            elif keys[pygame.K_LEFT]:
                player.move_right(current_level, "left")
            else:
                player.move_right(current_level, "")

            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                if player.on_ground or pressed:
                    player.jumping = True
                    pressed = True
                else:
                    player.double_jump_bool = True
            else:
                pressed = False

        player.kill_self()
        player.gravity(current_level)
        player.jump(current_level)
        player.collect_letter(current_level)
        for i in player.letter_lis:
            i.collect_self(player, current_level)
            screen.blit(i.image, i.rect)
        pygame.display.update()
        clock.tick(75)


if __name__ == "__main__":
    root = pygame.display.set_mode((ss.SCREEN_WIDTH, ss.SCREEN_HEIGHT))
    level1 = Level.Level1()
    level = level1
    platformer_game(root)
