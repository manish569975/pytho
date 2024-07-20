


# a=60,57,67,78,
# print(a)
# a=0,708,607,90
# print(a)


# a="vikas"
# print(a)
# print(id(a))
# print(a[1])

# add two string=----------------------------------------------


# a=a + " tiwari "
# print(a)
# print(id(a) )

# a='rahul'
# print(a)
# print(id(a))

# del a[2]
# print(a)



# slicing---------------------------


# name="i am java trnier"
# print(name)
# print("name [2:4]",name[2:4])
# print("name [5:9]",name[5:9])
# print("name [:15]",name[:15])
# print("name [2:1]",name[2:1])
# print("name [:]",name[:])
# print("name [2:17:31]",name[0:17:31])
# print("name [::]",name[::])
# print("name [::-1]",name[::-1])


# using capitalize function---------------------------------------------
# str="rahul tiwari"
# print(str)
# str=str.capitalize()
# print(str) 

# using center---------------------------(felling pading left to right str)

# str="helo"
# str2=str.center(15)
# print(str)
# print(str2)


# using a count fiunction

# str="my name is manish"
# oc1=str .count('a')
# oc2=str.count('a',6)
# oc2=str.count('a',6,16)
# print(oc1)

# print(oc2)


# using chartacter find b/w the element---------------------------------------------------------- 

# str="hello this is python class"
# ise=str.endswith("lass",0,13)
# print(ise)


# str="hello mthis is python claass"
# iss=str.startswith("is",8,16)
# print(iss)


# str="welcome to the  python claass"
# str2=str.find("t")
# str3=str.find("t",3,12)
# print(str2)
# print(str3)

# index methd
# python index menthod is same AS THE FIND ()method except return it returns error on faliure this method return index of first 
# occurred substring and an error if there is no match  found 

# str="welcome to the  python claass"
# str2=str.index("th",4,13)


# str="146753"
# str3="welcome 123"
# str2=str.isalnum()
# str4=str.isalnum()
# print(str2)
# print(str4)





# str="python3"
# if str.isalpha()==true:
#     print("string contain  lphabets")
# else:print("string contains other char to ")


# python string  islower()method

# str="Manu"
# str2=str.islower()
# print(str2)
# # str2=str.isupper()
# str2=str.lower()
# print(str2)



# a=str.upper()
# print(a)

# str="python"
# str2=str.lstrip()
# print(str)
# print(str2)


# str="....python...."
# str2=str.lstrip('.')
# str3=str.rstrip('.')
# str4=str.strip(',')


# str="java is a programer language"
# str2=str.replace("java","c",2)
# print(str2)

# swap case change the character upper to lower




# def analyze_string(s):
#     alphabetic_count = sum(1 for char in s if char.isalpha())
#     numeric_count = sum(1 for char in s if char.isdigit())
#     special_count = sum(1 for char in s if not char.isalnum())

#     return alphabetic_count, numeric_count, special_count

# input_string = "Hello, World! 123"
# alphabetic_count, numeric_count, special_count = analyze_string(input_string)

# print(f"Alphabetic characters: {alphabetic_count}")
# print(f"Numeric characters: {numeric_count}")
# print(f"Special characters: {special_count}")




# def analyze_string(s):
#     alphabetic_count = 0
#     numeric_count = 0
#     special_count = 0
#     digit_sum = 0

#     for char in s:
#         if char.isalpha():
#             alphabetic_count += 1
#         elif char.isdigit():
#             numeric_count += 1
#             digit_sum += int(char)  
#         else:
#             special_count += 1

#     return alphabetic_count, numeric_count, special_count, digit_sum


# input_string = "Hello, World! 123"
# alphabetic_count, numeric_count, special_count, digit_sum = analyze_string(input_string)

# print(f"Alphabetic characters: {alphabetic_count}")
# print(f"Numeric characters: {numeric_count}")
# print(f"Special characters: {special_count}")
# print(f"Sum of digit values: {digit_sum}")




    
