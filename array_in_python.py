#we call it list
numbers = [1,2,3,2,4,5,6]

print(numbers[-1]) # gives out last element of array

print(numbers) #prints the whole array
print(len(numbers)) #prints the size of the array
numbers.append(60) #adds the no. to the end of the array
#now the array becomes '1,2,3,4,5,6,60'
numbers.remove(2) #incase of multiple numbers to be removed like in this case we would have the left most to be removed
#here the array is => 1,3,2,4,5,6,60
#also note if it were array of strings then it should be array.remove('string') note the single quotes in it

#to inset at a certain location =>  array.insert(position,value)
numbers.insert(2,87)



# remove using position => array.pop(position)
# we can also use => del array[position]
numbers.pop(2) #here 87 would get removed

#reverse the list
numbers.reverse()

# sorting
numbers.sort()

#reverse sort
numbers.sort(reverse=True)

# normal value changing => array[index]=value
numbers[3]=0

print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))