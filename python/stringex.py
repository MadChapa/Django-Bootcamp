string='django'
print(string[0])


print(string[-1])

print(string[:4])


print(string[0])

print(string[-2:])


#reverse the string
new_string = "django"[::-1]
print(new_string)

#problem2: Nested list
l=[3,7,8,6,[1,4,'hello']]
l[4][2]='goodbye'
print(l)


#dictionaries
d1={'simple_key':'hello'}
d4=d1['simple_key']
print(d4)


d2={'k1':{'k2':'hello'}}
d5=d2['k1']['k2']
print(d5)

d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
d6=d3['k1'][0]['nest_key'][1][0]
print(d6)



List = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(List[3])





#problem5
age=4
name="Sammy"

print("Hello my dog's name is {a} and he is {b} years old.".format(a=name,b=age))
