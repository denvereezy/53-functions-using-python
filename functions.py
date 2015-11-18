def greeting():
    return 'hello world'

def uppercase(name):
    uppercaseName = name.upper()
    return "Hello" + " " + uppercaseName

def hello_joe(name):
    if(name == "Joe"):
        return "Hello"
    elif(name == "Bob"):
        return "hello"
    else:
        return "Hello" + " " + name + "!"

def number_list(n):
    list = []
    for i in range(n):
        if i <= n:
            i +=1
        list.append(i)
    return list

def sum_numbers(n):
    sum = 0
    for i in range(n):
        if i <= 15:
            i += 1
        sum =sum + i
    return sum

def stringLen(string):
    length = len(string)
    return length

# def reverse(string):
#     s = " "
#     n = string.split(s)
#     x = n[::-1]
#     y = s.join(x)
#     return y

# def hello_list(number):
#     string = "Hello world"
#     return (string(number+1).join(string))

def low(numbers):
    number = sorted(numbers)
    return number[0]
