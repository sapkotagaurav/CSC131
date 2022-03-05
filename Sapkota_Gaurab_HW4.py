import math


class Complex:
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part, self.imaginary_part = real_part, imaginary_part

    def __str__(self):
        if self.real_part == 0 and self.imaginary_part == "0":
            return 0
        if self.real_part == 0:
            return f"{self.imaginary_part}i"
        if self.imaginary_part == 0:
            return f"{self.real_part}"
        return f"({self.real_part} , {self.imaginary_part}i)"

    # Arthematic Operators

    def __add__(self, other):
        return Complex(
            self.real_part + other.real_part, self.imaginary_part + other.imaginary_part
        )

    def __sub__(self, other):
        return Complex(
            self.real_part - other.real_part, self.imaginary_part - other.imaginary_part
        )

    def __mul__(self, other):
        temp_r = (
            self.real_part * other.real_part
            - self.imaginary_part * other.imaginary_part
        )
        temp_i = (
            self.real_part * other.imaginary_part
            + self.imaginary_part * other.real_part
        )
        return Complex(temp_r, temp_i)

    def __truediv__(self, other):
        temp_r = (
            self.real_part * other.real_part
            + self.imaginary_part * other.imaginary_part
        )
        temp_i = (
            self.imaginary_part * other.real_part
            - self.real_part * other.imaginary_part
        )
        temp = other.imaginary_part**2 + other.real_part**2

        return Complex(temp_r / temp, temp_i / temp)

    def __abs__(self):
        return math.sqrt(self.real_part**2 + self.imaginary_part**2)

    # logical operators

    def __eq__(self, other):
        return self.__abs__() == other.__abs__() if type(other) is Complex else False

    def __ne__(self, other):
        return not self.__eq__((other))

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __le__(self, other):
        return self.__abs__() <= other.__abs__()

    def __ge__(self, other):
        return self.__abs__() >= other.__abs__()


def main():
    input_line = input("Enter the first complex number: ")
    input_line = list(map(float, input_line.split()))
    a, b = input_line[0], input_line[1]
    c1 = Complex(a, b)
    input_line = input("Enter the second complex number: ")
    input_line = list(map(float, input_line.split()))
    a, b = input_line[0], input_line[1]
    c2 = Complex(a, b)

    print()
    print("c1 is", c1)
    print("c2 is", c2)
    print("|" + str(c1) + "| = " + str(abs(c1)))
    print("|" + str(c2) + "| = " + str(abs(c2)))

    print(c1, " + ", c2, " = ", c1 + c2)
    print(c1, " - ", c2, " = ", c1 - c2)
    print(c1, " * ", c2, " = ", c1 * c2)
    print(c1, " / ", c2, " = ", c1 / c2)

    print("Is c1 < c2?", c1 < c2)
    print("Is c1 <= c2?", c1 <= c2)
    print("Is c1 > c2?", c1 > c2)
    print("Is c1 >= c2?", c1 >= c2)
    print("Is c1 == c2?", c1 == c2)
    print("Is c1 != c2?", c1 != c2)
    print("Is c1 == 'Hello There'?", c1 == "Hello There")
    print("Is c1 != 'Hello There'?", c1 != "Hello There")


main()
