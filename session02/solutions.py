import time
import numpy as np

print("exercise 1: operation")


def evaluate(expr):
    total = 0
    if "+" in expr:
        a, b = expr.split("+")
        total = int(a) + int(b)
    elif "*" in expr:
        a, b = expr.split("*")
        total = int(a) * int(b)
    elif "/" in expr:
        a, b = expr.split("/")
        total = int(a) / int(b)
    elif "-" in expr:
        a, b = expr.split("-")
        total = int(a) - int(b)
    else:
        print("Invalid")
    return total


print(str(evaluate(input())))

#########################################################

time.sleep(2)

#########################################################

print("exercise 2: convert to str")


def convert_str_to_list(string):
    out = []
    for item in string.split(","):
        out.append(item)
    return out


print(convert_str_to_list("alireza, alavi, 23, tehran"))

#########################################################

time.sleep(2)

#########################################################

print("exercise 3: form a list")


def convert_str_to_formed_list(item, detail):
    item_out = []
    for items in item.split(","):
        item_out.append(items)
    detail_out = []
    for items in detail.split(","):
        detail_out.append(items)
    out = []
    for i in range(len(item_out)):
        out.append(f"{item_out[i]}:{detail_out[i]}")
    return out


print(convert_str_to_formed_list("name, family, age, location",
                                 "alireza, alavi, 23, tehran"))

#########################################################

time.sleep(2)

#########################################################

print("exercise 4: count metal")


def count_metal(song):
    out = 0
    for item in song.split("-"):
        if "metal" in item:
            out += 1
    return out


print(count_metal(
  "- Gott mit uns - metal"
  "- Preihelion - psychedelic rock"
  "- Killer Queen - rock"
  "- Primo Victoria - metal"))
#########################################################

time.sleep(2)

#########################################################

print("exercise 5: Multiply array in numpy")

# Create a two-dimensional array
arr = np.array([[1, 2], [3, 4]])

# Multiply the array by itself using np.matmul()
result_matmul = np.matmul(arr, arr)

# Display the original array and the multiplication results
print("Original Array:")
print(arr)
print("\nMultiplication result using np.matmul():")
print(f"{arr}\n{arr}=\n{result_matmul}")
