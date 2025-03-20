def condense(numlist):
    if len(numlist) < 5:
        return len (numlist)
    else:
        return 5
random_list = [7,1]
new_list = [0]
for i in range (3):
    new_list.append (condense(random_list))
    random_list.extend(new_list)
print(new_list)