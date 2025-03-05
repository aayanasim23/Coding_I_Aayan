list = [5,804,503,229,29,67]
sum = 0
minimum = list[0] # (CHALLENGE) After failure of troubleshooting, I searched this part up. In able for this to work, we have to compare the values to the list. Originally I put minimum = 0 which would constantly give me 0 as the minimum.
for num in list:
    if num > sum:
        sum = num

for nums in list:
    if nums < minimum:
        minimum = nums


print(sum)
print(minimum)

