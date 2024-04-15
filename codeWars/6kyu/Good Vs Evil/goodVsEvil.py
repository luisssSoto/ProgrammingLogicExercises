def good_vs_evil(good, evil):
    # create two dictionaries
    goodDict = {'Hobbits':1,
                'Men': 2,
                'Elves': 3,
                'Dwarves':3,
                'Eagles':4,
                'Wizards':10}
    evilDict = {'Orcs':1,
                'Men':2,
                'Wargs':2,
                'Goblins':2,
                'Uruk Hai':3,
                'Trolls':5,
                'Wizards':10}
    
    # create dictionaries about requirements
    goodRequirementsDict = {}
    # create a variable count to find the position of good
    goodCount = 0
    # create a variable which keeps the value of the final result
    goodWorth = 0
    # create a list of the values of the parameters
    goodList = good.split()
    # iterate to dict to assign the key of the dict and assign the value of the list
    for goodRace in goodDict:
         # casting the value to int
         worth = int(goodList[goodCount])
         # assign the key and value taking the race of the goodRace and the value of the goodList
         goodRequirementsDict[goodRace] = worth
         # sum to 1 the count to jump in the next position
         goodCount += 1
         # sum to goodWort the next expression
         goodWorth += worth * goodDict[goodRace]

    # repeat the process but this time with evil
    evilRequerimentsDict = {}
    evilCount = 0
    evilWorth = 0
    evilList = evil.split()
    for evilRace in evilDict:
         worth = int(evilList[evilCount])
         print('worth: ', worth)
         evilRequerimentsDict[evilRace] = worth
         evilCount += 1
         evilWorth += worth * evilDict[evilRace]

    #create a variable result string
    battleResult = "Battle Result: "
    # conditional if regarding the result of the battle:
    if goodWorth > evilWorth:
         battleResult += 'Good triumphs over Evil'
    elif goodWorth < evilWorth:
         battleResult += 'Evil eradicates all trace of Good'
    else:
         battleResult += 'No victor on this battle field'
    # return the varialbe battleResult
    return battleResult
