# ООП
# принципы ООП:
#
# class



class Book:
    strr = 400


    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)


    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author},\n'
                f'color: {self.color}, Strr: {self.strr}\n')

    def __len__(self): pass


gород_воров= Book("город воров","каныкей", "зеленый")
капитанская_дочка=Book("капитанская дочка", "пушкиин", "серый")

beka=Book("ЭТОМИР", "beka", "black")


ls=[1,1,1,1,1]
print(ls)
# gород_воров.info()
# капитанская_дочка.info()