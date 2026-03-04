import math
def scale_image(size, scale):
    # I use math.floor to eliminate the .0 in last two cases. The others acctions are too redundants to explain.
    return str(math.floor(int(size[:size.find('x')])*scale)) + 'x' + str(math.floor(int(size[size.find('x')+1:])*scale))

if __name__ == '__main__':
    print(scale_image("800x600", 2))
    print('=======')
    print(scale_image("100x100", 10))
    print('=======')
    print(scale_image("1024x768", 0.5))
    print('=======')
    print(scale_image("300x200", 1.5))