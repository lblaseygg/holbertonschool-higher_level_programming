class SwimMixin:
    """Mixin class to add swimming behavior."""
    
    def swim(self):
        """Prints the swimming behavior of the creature."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying behavior."""
    
    def fly(self):
        """Prints the flying behavior of the creature."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly using mixins."""
    
    def roar(self):
        """Prints the dragon's roar."""
        print("The dragon roars!")


# Testing
if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!
