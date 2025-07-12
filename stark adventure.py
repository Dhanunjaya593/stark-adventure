def north_of_count(numbers,count):
    for i in numbers:
        if(i == "R"):
            count += 1 
        if(i=="L"):
            count -= 1 
        if(count == 2 or count == -2):
            return "Yes"
    return "No"
n = int(input())
count = 0
for i in range(n):
    numbers = input()
    result = north_of_count(numbers,count)
    print(result)