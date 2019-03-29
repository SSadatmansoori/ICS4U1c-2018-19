class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

def get__area(rec):
    """

    :param rec:
    :return:
    """
    return rec.width * rec.height


def main():
    user_width = float(input("Enter a width"))
    user_height = float(input("Enter a height"))

    rect1 = Rectangle()
    rect1.width = user_width
    rect1.height = user_height

    area = get__area(rect1)
    print("THe area of the rectangle is" + str(area))

main()