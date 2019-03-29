class Rectangle():

    def __init__(self, rwidth, rlength):
        self.width = rwidth
        self.length = rlength

    def get_area(self):

        return self.width * self.length

def main():
     my_rectangle = Rectangle(2, 5)

     print("The area is " + str(my_rectangle.get_area()))

main()

