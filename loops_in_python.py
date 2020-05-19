animals = ['dog','cat','kangaroo','snake','jaguar']


for animal in animals:
    print(f"{animal}, is a cute animal")

# if it were animals = {'dog','cat','kangaroo','snake','jaguar'}
# the for loop wont print in the same order as in animals = ['a','b'...]
# do't forget to intend the 'animal' in the animals for loop
# also don't do intendation unnecessarily

# copying a list
new_list_of_animals = animals

# another way of copying a list is as such
new_list_of_animals_part2 = animals[:]
print(new_list_of_animals) 
print(new_list_of_animals_part2)

elem = 'goat'
emem2 = 'snake'

if((elem not in animals) or (emem2 not in animals)):
    print("Yes it is!!!")
# Don't forget to add colon after if statement if you come from C or C++ 