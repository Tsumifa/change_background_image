# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:    
    import random as _random
    import ctypes as _ctypes
    import json
    '''with open(r"assets/data/images.json", 'r') as data_file:
        paths = json.load(data_file)'''

except Exception as e:
    raise e

# == LOGIC PART == #


class Main:

    def __init__(self):
        self.path_list = [
            r"assets\img\Beatles1.webp",
            r"assets\img\Beatles2.jpg",
            r"assets\img\Beatles3.jpg",
            r"assets\img\Beatles4.jpg",
            r"assets\img\Beatles5.jpg",
            r"assets\img\Beatles6.jpg",
            r"assets\img\Beatles7.jpg",
            r"assets\img\Beatles8.jpg",
            r"assets\img\Beatles9.jpg",
            r"assets\img\Beatles10.jpg",
            r"assets\img\Bird1.jpg",
            r"assets\img\Bird2.jpg",
            r"assets\img\Bird3.jpg",
            r"assets\img\Bird4.jpg",
            r"assets\img\Bird5.jpg",
            r"assets\img\Bird6.jpg",
            r"assets\img\Bird7.jpg",
            r"assets\img\Bird8.jpg",
            r"assets\img\Bird9.jpg",
            r"assets\img\Bird10.jpg",
            r"assets\img\Butterfly1.jpg",
            r"assets\img\Butterfly2.jpg",
            r"assets\img\Butterfly3.jpg",
            r"assets\img\Butterfly4.jpg",
            r"assets\img\Butterfly5.jpg",
            r"assets\img\Butterfly6.jpg",
            r"assets\img\Butterfly7.jpg",
            r"assets\img\Butterfly8.jpg",
            r"assets\img\Butterfly9.jpg",
            r"assets\img\Butterfly10.jpg",
            r"assets\img\Mushroom1.jpg",
            r"assets\img\Mushroom2.jpg",
            r"assets\img\Mushroom3.jpg",
            r"assets\img\Mushroom4.jpg",
            r"assets\img\Mushroom5.jpg",
            r"assets\img\Mushroom6.jpg",
            r"assets\img\Mushroom7.jpg",
            r"assets\img\Mushroom8.jpg",
            r"assets\img\Mushroom9.jpg",
            r"assets\img\Mushroom10.jpg"
        ]
        self.image = r"D:\THOMAS\github\change_background_image" + self.path_list[_random.randint(0, len(self.path_list) - 1)]
        self.change_desktop()

    def change_desktop(self):
        print('img :' + self.image)
        _ctypes.windll.user32.SystemParametersInfoW(20, 0, self.image, 0)


# == START PROGRAM == #

if __name__ == "__main__":
    main = Main()