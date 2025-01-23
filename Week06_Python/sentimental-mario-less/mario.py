from cs50 import get_int


def main():

    height = get_height()
    draw(height, height)


def get_height():
    while True:
        try:
            height = get_int("Height: ")
            if (0 < height < 9):
                break
        except ValueError:
            None

    return height


def draw(height, bricks):
    if height == 0:
        return
    draw(height - 1, bricks)
    print(" " * (bricks - height), end='')
    print("#" * height)


main()
