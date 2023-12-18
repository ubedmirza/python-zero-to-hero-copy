#spliting words with split built-in fuction
path=("Users/Furkanmirza/python-zero-to-her")
print(path.split("/"))

#concatinating string using + fuction
str1="Hola"
str2="world"
print(str1+" "+str2)

#find length of the string using length function
value="Users/Furkanmirza/python-zero-to-her"
length=len(value)
print("lenght of string is",length)

#upper-case and lower-case
value="Users/Furkanmirza/python-zero-to"
lower_case=value.lower()
upper_case=value.upper()
print("lower-case is",lower_case)
print("upper-case is",upper_case)

#replace value
value="Users/Furkanmirza/python-zero-to-her"
rep=value.replace("Furkanmirza","furquanbaig")
print("replace name is",rep)

#string-strip
value="     Users   /Furkanmirza/   python-zero-to-her        "
value_strip=value.strip()
print("stripping value is",value_strip)

#arithmatic opeators
num1=5.3
num2=7.8

print("Additiion is",num1+num2)
print("Substraction is",num1-num2)
print("Multiplication is",num1*num2)
print("Division is",num1/num2)
print("Round",round(3.1456,2))

