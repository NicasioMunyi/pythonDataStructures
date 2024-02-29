new_list = [1,2,3]
#accessing values at  given locations

val =new_list[2] #accessing value in index 2
print(val)

# serching in a list
if 2 in new_list:# searching for value 2
    print(True)

#searching using a for loop
for n in new_list:
    if n == 2:
        print(True)

        break

#appending into a list
new_list.append(5) # adding a number to the end of the list
print(new_list)

#inseting into a list
new_list.insert(3,4) # inserting a value to a given index -->insert(index, value)
print(f"List after an insert{new_list}")


#adding a list to a list
new_list.extend([5,6,7])
print(f"List afer etending{new_list}")