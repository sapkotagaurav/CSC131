class Point:
    COUNT = 0

    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y
        Point.COUNT += 1

    def __str__(self):
        return f"({self.getX()}, {self.getY()})"

    def setX(self, value):
        self.X = value

    def setY(self, value):
        self.Y = value

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distanceFromPoint(self, aPoint):#returns distance from a point
        return ((self.X - aPoint.X) ** 2 + (self.Y - aPoint.Y) ** 2) ** 0.5

    def distanceFromOrigin(self):#returns distance from origin
        return (self.X**2 + self.Y**2) ** 0.5

    def __eq__(self, o):
        return (
            self.distanceFromOrigin() == o.distanceFromOrigin()
            if type(o) is Point
            else False
        )

    def __ne__(self, o):
        return not self.__eq__(o)

    def __gt__(self, o):
        return self.distanceFromOrigin() > o.distanceFromOrigin()

    def __ge__(self, o):
        return self.distanceFromOrigin() >= o.distanceFromOrigin()

    def __lt__(self, o):
        return self.distanceFromOrigin() < o.distanceFromOrigin()

    def __le__(self, o):
        return self.distanceFromOrigin() <= o.distanceFromOrigin()


def main():
    p1 = Point(3, 4)
    print(p1)
    p2 = Point(3, 0)
    print(p2.getX(), p2.getY())
    print(f"The distance between {p1} and {p2} is {p1.distanceFromPoint(p2)}")
    print("Testing the comparison operators in the order <, <=, >, >=, ==,and !=")
    print(f"p1 < p2? {p1<p2}")
    print(f"p1 <= p2? {p1<=p2}")
    print(f"p1 > p2? {p1>p2}")
    print(f"p1 >= p2? {p1>=p2}")
    print(f"p1 == p2? {p1==p2}")
    print(f"p1 != p2? {p1!=p2}")
    print()
    print(f"p1 == \"Hello\"? {p1 == 'Hello'}")
    print(f"p1 != \"Hello\"? {p1 != 'Hello'}")

    print(f"Number of points created is {Point.COUNT}")


main()
