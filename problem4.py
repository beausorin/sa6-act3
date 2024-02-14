list1 = [7, 2, 5, 3, 8, 2]
list2 = [4, 7, 8, 1, 5, 3]
intersect = list(filter(lambda x: x in list1, list2))
print(intersect)