# Dictionary-Collection of different entries of a specific/diffent data(s)
player_0 = {'color':'blue','size':10} # Note the Colon

print(player_0) #Output => {'color':'blue','size':10}
print(player_0['color']) # Access elements in this manner

# Adding to dictionary
player_0['initial_position'] = 20
player_0['final_color'] = 'red'
print(player_0) #Output => {'color': 'blue', 'size': 10, 'initial_position': 20, 'final_color': 'red'}

# Modify the dictionary
player_0['color'] = 'yellow' 
print(player_0) #Output => {'color': 'yellow', 'size': 10, 'initial_position': 20, 'final_color': 'red'}

# Removing Key-Value Pairs
del player_0['final_color']
print(player_0) #Output => {'color': 'yellow', 'size': 10, 'initial_position': 20}

# Get method in Dictionary
val=player_0.get('key',"NONE")
print(val) #prints NONE if 'key' is not present in the Dictionary

#Looping through the dictionary
for key,value in player_0.items():
    print(f"\n{key}, is the key")
    print(f"{value}, is the value\n") 

# player_0.items() => using this we can access 'key' & 'value' both
# player_0.values() => using this we can access 'values' only
# player_0.keys() => using this we can access 'keys' only

'''
Nesting
'''

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}, likes the following languages")
    #Runs along all the keys
    for language in languages :
        print(f"{language.title()}")
        #Runs along all the languages for a specific key

print("\n...\n")

'''
A Dictionary in a Dictionary
'''


user = {
    'user_1':{
        'first_name':'aaa',
        'second_name':'bbb',
        'third_name':'ccc'
    },

    'user_2':{
        'first_name' : 'ddd',
        'second_name': 'eee',
        'third_name' : 'fff'
    },

    'user_3':{
        'first_name' : 'ggg',
        'second_name' : 'hhh',
        'third_name' : 'iii'
    }
}

for user_number, name in user.items():
    print(f"It is this user, {user_number.title()}")

    for name_number,name_plate in name.items():
        print(f"The {name_number} of name is {name_plate}")