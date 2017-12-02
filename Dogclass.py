class Dog():
    """This docstring will discuss how to interact with our Dog class.

    Our Dog class will have two attributes - a name and happiness_level.
    It's one method, wag_tail, will simulate the dog wagging it's tail
    some number of times, and increasing it's happiness level.

    Parameters:
    -----------
        name: str
        happiness_level: int
    """

    def __init__(self, name, happiness_level=5, tail=0, wags=0):
        self.name = name
        self.happiness_level = happiness_level
        self.tail = tail
        self.wags = wags

    def wag_tail(self, wags):
        """Wags the dogs tail wags times, and each time increase
        happiness level by 5.

        Args:
            wags: int
        """
        self.happiness_level += 5 * wags
        self.wags += wags
        print(f"{self.name} wags his tail {wags} times")
        return self.happiness_level

    def __str__(self):
        tailpic = "\\\\//" * self.wags
        dogpic = f"""
        _~~~~~_
        U|o o|U
         (_+_)_______//{tailpic}
         | U         |
         ||~~~~~~~~~||
         ||         ||"""

        looks = f"""Name: {self.name}; Happiness level: {self.happiness_level}
        {dogpic}"""
        return looks

dog1 = Dog('Luis',3)
print(dog1)

dog1.wag_tail(23)
print(dog1)
