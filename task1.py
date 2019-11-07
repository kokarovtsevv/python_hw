list2 = list1 = list(range(1,10))
list2.append(10)
list2.pop(0)
print(list1, list2)
list3=list1[:]
list3.append('full copy magic')
print(list1, list2, list3)
