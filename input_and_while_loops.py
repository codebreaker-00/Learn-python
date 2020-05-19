message = input("okkay now give input : ")
print(message)

message = int(message)
if (message >= 0):
    print(message)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while ('cat' in pets):
    pets.remove('cat')

print(pets) #removes all 'cat' from pets