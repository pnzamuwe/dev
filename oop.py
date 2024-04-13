# class MyFirstClass:
#     print("Who wrote this?")
#     index = "Author-Book"

#     def hand_list(self, philosopher, book):
#         print(self.index)
#         print(f"{philosopher} wrote the book {book}")


# whodunnit = MyFirstClass()
# whodunnit.hand_list("Sun Tzu", "The Art of War")

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self, name):
        super().__init__(name)
        print(name, ' is sweet')

apple = FruitFlavour("mango")