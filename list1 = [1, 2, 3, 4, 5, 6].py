list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8 , 10]

new_list = [i for i in list1 if i in list2]
print(new_list)