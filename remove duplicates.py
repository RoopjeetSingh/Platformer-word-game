import cv2
import numpy as np


def remove_duplicates():
    number = 1
    import os

    # Get the list of all files and directories
    path_dir = "/Users/roopjeetsingh/Downloads/2D Platformer Snow Pack (Tio Aimar)/PNG"
    dir_list = os.listdir(path_dir)
    for i, path in enumerate(dir_list):
        dupli = False
        if "png" not in path:
            continue
        a = cv2.imread(rf"/Users/roopjeetsingh/Downloads/2D Platformer Snow Pack (Tio Aimar)/PNG/{path}")
        for j, path2 in enumerate(dir_list[i + 1:]):
            if "png" not in path2:
                continue
            b = cv2.imread(rf"/Users/roopjeetsingh/Downloads/2D Platformer Snow Pack (Tio Aimar)/PNG/{path2}")
            if a.shape == b.shape:
                difference = cv2.subtract(a, b)
                result = not np.any(difference)
                if result:
                    dupli = True
        if not dupli:
            cv2.imwrite(f"./images/platform/platform_sprites_({number}).png", a)
            number += 1


def sprite_sheet_cutter(sprite_sheet: np.ndarray, total_sprites: int = 0):
    def empty(a):
        pass

    cv2.namedWindow("TrackBars", cv2.WINDOW_AUTOSIZE)
    # cv2.resizeWindow("TrackBars", 1000, 640)
    cv2.createTrackbar("blur", "TrackBars", 0, 4, empty)
    cv2.createTrackbar("canny1", "TrackBars", 20, 300, empty)
    cv2.createTrackbar("canny2", "TrackBars", 20, 300, empty)
    sprite_sheet2 = cv2.cvtColor(sprite_sheet, cv2.COLOR_RGB2GRAY)
    while True:
        sprite_sheet2 = sprite_sheet.copy()
        blur = cv2.getTrackbarPos("blur", "TrackBars")
        canny1 = cv2.getTrackbarPos("canny1", "TrackBars")
        canny2 = cv2.getTrackbarPos("canny2", "TrackBars")
        sprite_sheet_blur = cv2.GaussianBlur(sprite_sheet2, (blur * 2 + 1, blur * 2 + 1), 0)
        sprite_sheet_canny = cv2.Canny(sprite_sheet_blur, canny1, canny2)
        # sprite_sheet_canny = cv2.adaptiveThreshold(sprite_sheet_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        contours, heirarchy = cv2.findContours(sprite_sheet_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv2.drawContours(sprite_sheet, contours, -1, (0, 0, 255), 5)
        if not total_sprites or len(contours) < total_sprites:
            for i, cnt in enumerate(contours):
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(sprite_sheet2, (x, y), (x + w, y + h), (0, 0, 255), 5)
                # cv2.imshow(f"images/platform_{i}.png", sprite_sheet[y: y + h, x: x + w])
                # cv2.imwrite(f"images/platform_{i}.png", sprite_sheet[y: y+h, x: x+w])
        else:
            cnts_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            for i, cnt in enumerate(cnts_sorted[0: total_sprites]):
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(sprite_sheet2, (x, y), (x + w, y + h), (0, 0, 255), 5)
                # cv2.imshow(f"images/platform_{i}.png", sprite_sheet[y: y + h, x: x + w])
                # cv2.imwrite(f"images/platform_{i}.png", sprite_sheet[y: y + h, x: x + w])
        cv2.imshow("Sprites", sprite_sheet2)
        if cv2.waitKey(30) == ord('q'):
            break
    return sprite_sheet_canny, sprite_sheet


def crop(img):
    img_read = cv2.imread(img)
    grayscale = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)

    ret, thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY)

    bbox = cv2.boundingRect(thresholded)

    x, y, w, h = bbox

    foreground = img_read[y:y + h, x:x + w]

    # cv2.imshow(img, foreground)
    cv2.imwrite(img, foreground)


for i in range(2, 6):
    crop(f"images/platform/platform_sprites_(17) ({i}).png")

