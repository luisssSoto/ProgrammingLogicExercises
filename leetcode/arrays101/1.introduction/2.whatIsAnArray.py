"""DVD Collection"""

class DVDCollection:
    def __init__(self):
        self.__bookshelf = []

    def addDvd(self, dvd):
        self.__bookshelf.append(dvd)
    
    def showIdCollection(self):
        return self.__bookshelf
    
    def showColletion(self):
        for dvd in self.__bookshelf:
            yield dvd

    def insertDvd(self, place, dvd):
        try:
            self.__bookshelf.insert(place, dvd)
        except IndexError as e:
            print(e.args)
            print('We put it in the last index')
            self.__bookshelf.append(dvd)

    def selectOne(self, index):
        return self.__bookshelf[index]

class DVD(DVDCollection):
    def __init__(self, name, release_year, director):
        self.__name = name
        self.__release_year = release_year
        self.__director = director

    def __str__(self):
        return self.__name + ' directed by: ' + self.__director + ' released in: ' + str(self.__release_year )
    
bookshelf1 = DVDCollection()
print(bookshelf1)
dvd1 = DVD('300', 2006, 'Zack Snyder')
print(dvd1)
bookshelf1.addDvd(dvd1)
print(bookshelf1)
print(hex(id(dvd1)))
print(bookshelf1.showIdCollection())
dvd2 = DVD('The Matrix', 1999, 'Lilly Wachowski')
bookshelf1.addDvd(dvd2)
for i in bookshelf1.showColletion():
    print(i)

dvd3 = DVD('Charlie y la fábrica de chocolates', 2005, 'Tim Burton')
bookshelf1.insertDvd(5, dvd3)

for j in bookshelf1.showColletion():
    print(j)
print()

dvd4 = DVD('Los Simpson: La película', 2007, 'David Silverman')
bookshelf1.insertDvd(1, dvd4)

for k in bookshelf1.showColletion():
    print(k)

l = [x for x in range(3)]
print(bookshelf1.selectOne(0))
print(l)
