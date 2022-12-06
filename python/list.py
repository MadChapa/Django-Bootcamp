mylist=[1,2,3]
mylist2=['string',1,2,3,23.2,True,[1,2,3]]
print(mylist2)
print(len(mylist))



mylist5=['a','b','c','d','e']
print('before reassignment:')
print(mylist5)

mylist5[0]='New ITEM'
print("after reassignment")
print(mylist5)

mylist5.append("Last")
print(mylist5)

item=mylist5.pop()
print(item)
print(mylist5)

#list comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
print(first_col)


haha=[1,2,3,4[6,8,9]]
print(haha[0])
