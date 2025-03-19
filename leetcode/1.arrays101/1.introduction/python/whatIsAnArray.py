"""DVD Collection"""

class FullCardboardBox(IndexError):
    def __init__(self):
        IndexError.__init__(self)
        
    def __str__(self):
        return 'Sorry but the cardboard box is full'

class DVDCollection:
    def __init__(self):
        self.__length = 0
        self.__cardboard_box = ["empty" for x in range(15)]
    
    def put_a_dvd(self, dvd, place):
        if place < len(self.__cardboard_box):
            self.__cardboard_box[place] = dvd
            self.__length += 1
        else:
            raise FullCardboardBox
    
    def show_collection(self):
        return(self.__cardboard_box)    
    
    def show_dvd(self, place):
        return self.__cardboard_box[place] 
    
    def get_length(self):
        return self.__length

class DVD:
    def __init__(self, name, release_year, director):
        self.__name = name
        self.__release_year = release_year
        self.__director = director

    def __str__(self):
        return self.__name + ' directed by: ' + self.__director + ' released in: ' + str(self.__release_year )
    
cardboard_box1 = DVDCollection()
print(cardboard_box1)
dvd1 = DVD('300', 2006, 'Zack Snyder')
print(dvd1)
cardboard_box1.put_a_dvd(dvd1,0)
print(cardboard_box1)
print(hex(id(dvd1)))
dvd2 = DVD('The Matrix', 1999, 'Lilly Wachowski')
cardboard_box1.put_a_dvd(dvd2,7)
print(cardboard_box1.show_collection())

dvd3 = DVD('Charlie y la fábrica de chocolates', 2005, 'Tim Burton')
cardboard_box1.put_a_dvd(dvd3,14)
print(cardboard_box1.show_collection())
print()

dvd4 = DVD('Los Simpson: La película', 2007, 'David Silverman')
cardboard_box1.put_a_dvd(dvd4,14)
print(cardboard_box1.show_collection())

for i in range(len(cardboard_box1.show_collection())):
    if cardboard_box1.show_dvd(i) != "empty":
        print(cardboard_box1.show_dvd(i))

dvd5 = DVD("The Lord of the Rings", 2001, "Peter Jackson")

try:
    cardboard_box1.put_a_dvd(dvd5, 15)
except FullCardboardBox as e:
    print(e)

print("continue")