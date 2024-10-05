mentor_names = ["nika", "data", "saba", "gabrieli"]

new_mentors_list = ["luka","lasha"]

name_list = ["gurami", "daviti"]

user_name1 = input("Enter name: ")
user_name2 = input("Enter name: ")


if user_name1:
    if user_name1 in mentor_names:
        new_mentors_list.append(user_name1)
    else:
        name_list.append(user_name1)



if user_name2:
    if user_name2 in mentor_names:
        new_mentors_list.append(user_name2)
    else:
        name_list.append(user_name2)



print (f"mentors: {new_mentors_list}")
print (f"members: {name_list}")