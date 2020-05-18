car = 'subaru'
# no check for if else part in the double quotes part
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') #prints boolian for this condition

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') #prints boolian for given condition

# while checking inequality or equality in strings make sure they are in same case

if (car == 'Subaru'): 
    print("Note The Title Case")

elif(car == 'subaru'):
    print("note the lower case")

elif(car=='SUBARU'):
    print("NOTE THE UPPER CASE")

animals = ['dog','cat','kangaroo','snake','jaguar']

# To check if a list is empty or not we can just do :
if (animals):
    print("List is not empty")

else :
    print("List is empty")
