##Motivation
animal = ["mammal", "bird", "reptile", "fish"]
numberOfSpecies =  [428, 784, 311, 1154]

##we could do this but it is error prone
print(numberOfSpecies[animal.index("reptile")])

##Better way is with a dictionary
animalDict = { "mammal" : 428, "bird" : 784, "reptile" : 311, "fish" : 1154 }
print(animalDict["reptile"])
