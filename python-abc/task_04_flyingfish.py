class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        """Overrides the fly method to describe a flying fish's flight."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method to describe a flying fish's swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method to describe a flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")


# Testing
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Investigate the Method Resolution Order (MRO)
    print(FlyingFish.mro())
