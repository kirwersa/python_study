from battery import Battery
from robot import Robot


def main():
    b = Battery(100)
    b.move()
    g = Battery(85)
    g.move()

    r = Robot(105)
    r.move()
    h = Robot(45)
    h.move()


if __name__ == '__main__':
    main()
