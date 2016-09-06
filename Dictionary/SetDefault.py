import pprint
message="The name of Barcelona's best forward is Lionel Andres Messi and he is from Argentina"
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)