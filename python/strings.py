#Basics
print('hello')
print("hello")

print("I'm a dog")

#indexing of string
mystring='abcdef'
print(mystring)
print(mystring[2]) #to get the single element pass the index number of that element
print(mystring[0]) #first letter
print(mystring[-1])# last letter

#slicing of strings
print(mystring[2:]) #index2 dekhi start vayera last samaa janxa vaneko
print(mystring[:3]) #index 3 vanda mathi ko not including 3
print(mystring[1:5]) #o/p bcde; index 1 lai include garxa but index 5 lai gardaina
print(mystring[:]) #string ko entire value dinxa
print(mystring[::1])


nums=[1,2,3,4,5,6,7,8]
part=nums[3:6]
print(part)

part2=nums[3:7:2]
print(part2)

part3=nums[-4:-1]
print(part3)

part4 = nums[4:1:-1]
print(part4)


#methods
x=mystring.upper()
print(x)

y=mystring.capitalize()
