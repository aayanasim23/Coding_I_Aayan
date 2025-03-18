odd_integers = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
even_integers = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
multiples_of_5 = {5, 10, 15, 20}
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in multiples_of_5:
    if i in odd_integers:
        count1 = count1 + 1
print("How many Multiples of 5 are odd? " + str(count1))

for i in prime_numbers:
    if i in even_integers:
        count2 = count2 + 1
print("How many Prime numbers are even? " + str(count2))

for i in prime_numbers:
    if i in odd_integers:
        count3 = count3 + 1
print("How many Prime numbers are odd? " + str(count3))

for i in prime_numbers:
    if i in multiples_of_5:
        count4 = count4 + 1
print("How many Prime numbers are Multiples of 5? " + str(count4))

for i in odd_integers:
    if i in even_integers:
        count5 in count5 + 1
print("How many Odd numbers are Even? " + str(count5))