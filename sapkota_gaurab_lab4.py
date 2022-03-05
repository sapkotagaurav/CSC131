
"""
A program to describe Classes and objects
Author:Gaurab Sapkota
"""


class Fan:
    """Fan Class
    """

    def __init__(self, radius, is_on=False, speed=1) -> None:
        """

        Args:
            radius (float): Radius of the fan
            is_on (bool, optional): IS the fan off or on. Defaults to False.
            speed (int, optional): Speed of the Fan. Defaults to 1.
        """
        self.radius = radius
        self.is_on = is_on
        self.speed = speed

    def __str__(self) -> str:
        if self.is_on:
            return f"Fan with radius {self.radius}\n The fan is currently on and is running at speed {self.speed}"
        else:
            return f"Fan with radius {self.radius} \n The fan is currently off"

    def getOn(self):
        """

        Returns:
            bool: Status of the fan
        """        
        return self.is_on

    def getRadius(self):
        """

        Returns:
            float: radius of the fan
        """
        return self.radius

    def getSpeed(self):
        """

        Returns:
            int: Speed of the Fan
        """        
        return self.speed if self.is_on else "Fan is currently off"

    def setOn(self, value: bool):
        """

        Args:
            value (bool): On or Off status
        """        
        if value not in [True, False]:
            print(
                f"The value {value} is invalid. Valid value is either True or False")
            return
        self.is_on = value

    def setSpeed(self, value: int):
        """

        Args:
            value (int): speed of the Fan
        """        
        if value not in [1, 2, 3]:
            print(f"The value {value} is invalid, Speed should be 1,2 or 3")
        else:
            if not self.is_on:
                self.setOn(True)
            self.speed = value


def main():
    
    fan1 = Fan(5)
    print(fan1)

    print()
    fan2 = Fan(12.5, True, 2)
    print(fan2)

    print("\nTesting the accessor methods on fan2")
    print(fan2.getRadius())
    print(fan2.getOn())
    print(fan2.getSpeed())

    print("\nTesting the mutator methods on fan2")
    fan2.setOn("off")
    fan2.setOn(False)
    fan2.setSpeed(5)
    fan2.setSpeed(3)

    print()
    print(fan2)


main()  # This calls the main function
