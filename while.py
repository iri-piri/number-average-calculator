sum = 0
count = 0
number = int(input("enter a number: "))

while number != -1:
    if number == -1:
        break
    sum += number
    count += 1
    number = int(input("enter a number: "))

if count > 0:
    average = sum / count
    print (average)
