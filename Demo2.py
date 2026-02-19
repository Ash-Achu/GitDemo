#List datatype
values = [1, 2, "rahul", 4, 5]

print(values)
print(type(values))

print(values[0])
print(values[3])
print(values[-1])

print(values[1:3])
values.insert(3,"Shetty")
print(values)
values.append("End")
print(values)
values[2] = "RAHUL"
print(values)
del values[0]
print(values)

#Tuple datatype

val = (1, 2, "rahul", 4.5)
print(val[1])
print (val)
#val[2] = "RAHUL"
#print(val)

#Dictionary datatype

dic = {"a" :2, 4:"bcd", "c":"Hello World"}
print(dic)
print(dic[4])
print(dic["c"])

#To add value to the dictionary

dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
print(dict)
dict["gender"] = "male"
print(dict)
print(dict["lastname"])






