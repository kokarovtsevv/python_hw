class Dog:
    def bark(n=1):
        print('BARK!!!'*n)


class SmartDog(Dog):
    def givepaw():
        print('Paw pat')


dog = Dog
smartdog = SmartDog
dog.bark()
smartdog.bark(3)
smartdog.givepaw()

class NoizyDog(Dog):
    def bark():
        while True:
            print('BARK!!!')

ndog = NoizyDog
ndog.bark()
