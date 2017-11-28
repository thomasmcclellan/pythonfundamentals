# Python version of arrays

my_list = ['aDSFGHJ', 1,2,3,4,23.5, True, 'asdfg', [1,2,3]]
print(my_list)

print('before reassignment:')
print(my_list)
my_list[0] = 'NEW ITEM'
print('after reassignment')
print(my_list) #Replaces 'aDSFGHJ' with 'NEW ITEM'

my_other_list = [1,2,3]
print(len(my_other_list)) #len = length

new_list = ['a', 'b', 'c', 'd', 'e']
new_list.append(['x', 'y', 'z']) #Append includes the []
print(new_list)

new_new_list = ['a', 'b', 'c', 'd', 'e']
list_two = ['x', 'y', 'z']
new_new_list.extend(list_two) #Extend removes [], adds the list items of two lists together into one
print(new_new_list)

remove_list = ['a', 'b', 'c', 'd', 'e']
item = remove_list.pop(0)
print(remove_list)
print(item)

nested_list = [1,2,['x','y','z']]
print(nested_list[2][1]) #Pulls out 3rd position and 2nd within nested list