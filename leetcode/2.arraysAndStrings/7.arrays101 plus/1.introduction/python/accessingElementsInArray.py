"""Common Operations in Array"""

import whatIsAnArray

'''Writting'''
incrediblesDVD = whatIsAnArray.DVD("The Incredibles", 2004, "Brad Bird")
findingDoryDVD = whatIsAnArray.DVD("Finding Dory", 2016, "Andrew Stanton")
lionKingDVD = whatIsAnArray.DVD("The Lion King", 2019, "Jon Favreau")

whatIsAnArray.cardboard_box1.put_a_dvd(incrediblesDVD, 5)
whatIsAnArray.cardboard_box1.put_a_dvd(findingDoryDVD, 6)
whatIsAnArray.cardboard_box1.put_a_dvd(lionKingDVD, 8)

'''Reading'''
print(whatIsAnArray.cardboard_box1.show_collection())
print(whatIsAnArray.cardboard_box1.show_dvd(5))
print(whatIsAnArray.cardboard_box1.show_dvd(6))
print(whatIsAnArray.cardboard_box1.show_dvd(8))