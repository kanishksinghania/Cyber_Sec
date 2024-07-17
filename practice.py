def processArray(a):
    if not a:
        return 0
    
    new_len = 1
    prev = a[0]
    consecutive_count = 1

    for num in a[1:]:
        if num < 100:
            a[new_len] = num
            new_len += 1
            prev = num
            consecutive_count = 1
        elif num == prev and consecutive_count >= 2:
            continue
        else:
            a[new_len] = num
            new_len += 1
            prev = num
            consecutive_count = 1
            
    return new_len



numbers = []
while True:
    num = int(input())
    if num < 0:
        break
    numbers.append(num)

new_length = processArray(numbers)
for i in range(new_length):
    print(numbers[i])


    