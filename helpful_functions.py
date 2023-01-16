from Level import *


def calculate_current_level(variables_dic: dict):
    current_level = variables_dic["level"]
    if not current_level:
        levels = variables_dic["users"][variables_dic["current_user"][0]][1]
        print(levels)
        for level in level_list:
            for i in levels:
                if level.str == i[0]:
                    break
            else:
                current_level = level
                break
    else:
        # Could have also looped over all the levels in the level list and checked their str but this was faster and shorter
        current_level = eval(current_level)

    return current_level


def blit_text(surface, text, pos, font: pygame.font.Font, max_width, color=(0, 0, 0)):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    centerx, centery = pos
    for line in words:
        text_line = ""
        for word in line:
            text_line += word + " "
            word_surface = font.render(text_line, True, color)
            word_width, word_height = word_surface.get_size()
            if centerx + word_width/2 > max_width:
                word = font.render(text_line, True, color)
                surface.blit(word, word.get_rect(center=(centerx, centery)))
                text_line = ""
                centery += word_height  # Start on new row.
        word = font.render(text_line, True, color)
        surface.blit(word, word.get_rect(center=(centerx, centery)))
        centery += word_height  # Start on new row.
