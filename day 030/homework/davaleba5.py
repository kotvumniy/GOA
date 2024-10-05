fruit_list = ["apple","pear","grape","cucumber","mandarin",
              "banana","toamto","onion"]
fruits = ["apple","pear","grape","mandarin","banana"]

for i in fruit_list[:]:
    if not i in fruits:
        fruit_list.remove(i)

print(fruit_list)