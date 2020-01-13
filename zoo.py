zoo =("dog","cat","spider","cockroach","fish","ant","bird","peacock","snake","monkey")
# print (zoo.index("fish"))

# animal_to_find = "snake"
# if animal_to_find in zoo:
#   print(f'{animal_to_find} was found')

(animal1,animal2,animal3,animal4,animal5,animal6,animal7,animal8,animal9,animal10) = zoo

# print(animal5)

zoolist=list(zoo)
moreAnimals = ["bat","tiger","rabbit"]
zoolist.extend(moreAnimals)
print(zoolist)


