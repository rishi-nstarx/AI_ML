# lambda argument(any no. of):expresion(only one)

addition =  lambda a,b: a+b
print(addition(2,3))


temp = [1,2,3,4,5,6,7]
# print(list(map(lambda x: x**2, temp)))

for i in map(lambda x: x**2, temp):
    print(i)


num1 = [1,2,3]
num2 = [4,5,6]
print(list(map(lambda x,y:x+y, num1, num2)))


words = ["apple", "banana", "cherry"]
print(list(map(str.upper, words)))


test = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2 == 0, test)))


test = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2 == 0 and x>5, test)))


with open('example.txt', 'w+') as file:
    file.write("Hello Rishi.\n")
    file.write("I am a software engineer.\n")
    
    file.seek(0) # Changes the cursor's postion to a particuar index.

    content = file.read()
    print(content)


def shift_content(src, dest):
    with open(src, "r") as src_file:
        with open(dest, "w+") as dest_file:
            dest_file.write(src_file.read())
