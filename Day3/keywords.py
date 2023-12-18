#variablizing the name
ec2_instance_name="Linux-server-1"
print(ec2_instance_name)

#using the local and global variable
a=10  #global scope variable
b=5

def add():
    c=6 #local scope variable
    print(a+b+c)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

add()
sub()
mul()
div()
