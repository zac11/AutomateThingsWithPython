list_number=[1,4,5,8,9,10]

#produces an IndexError because Index is out of range
print(list_number[10])

list_animals=['cat','bat','rat','elephant']

#produces a TypeError because float index is not allowed
print(list_animals[10.0])

list_misc=['fat','hat','rat']

#produces a ValueError because values are more than what are there in list
size, color, disposition, name =list_misc

list_call=['hi','hello','hola','danke']

#produces a ValueError because list value is not present
list_call.index('holasoy')

eggs='hello'

#produces an AttributeError because string is immutable
eggs.append('world')

bacom=43

#produces an AttributeError because not a list
bacom.insert(1,'world')


list_slangs=['fleek','thot','tho','rekt','turnt']

#produces a ValueError because list value is not present
print(list_slangs.remove('syke'))

list_combined=[1,2,3,4,'zoidberg','9gag']

#produces a TypeError since list can't be sorted
list_combined.sort()