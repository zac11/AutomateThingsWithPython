animals=['elephant','kangaroo','cat','dog','snake']

#sort this list
animals.sort()
print(animals)
#reverse sort the list
animals.sort(reverse=True)
print(animals)

birds=['Parakeet','Crow','sparrow','pigeon','turkey','Vulture']

#sorting ASCIIbetical order- upper case comes before lower case
birds.sort()
print(birds)

#use of str keyword to not use ASCIIbetical order
birds.sort(key=str.lower)
print(birds)
