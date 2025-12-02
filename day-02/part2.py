def main():
    with open("day2.txt") as f:
        lines = f.readlines()
    total = 0
    numbers = lines[0].split(",")
    for num in numbers:

        num1 = int(num.strip().split("-")[0])
        num2 = int(num.strip().split("-")[1])
        for i in range(num1, num2 + 1):
            numstr = str(i)
            if len(numstr) == 1:
                continue
            if all(digit == numstr[0] for digit in numstr):
                total += i
                continue
            if all(numstr[digit:digit + 2] == numstr[0:2] for digit in range(0, len(numstr), 2))  and len(numstr) > 2:
                total += i
                continue   
            if all(numstr[digit:digit + 3] == numstr[0:3] for digit in range(0, len(numstr), 3))  and len(numstr) > 3:
                total += i
                continue           
            if all(numstr[digit:digit + 4] == numstr[0:4] for digit in range(0, len(numstr), 4))  and len(numstr) > 4:
                total += i
                continue  
            if all(numstr[digit:digit + 5] == numstr[0:5] for digit in range(0, len(numstr), 5))  and len(numstr) > 5:
                total += i
                continue    
            # firsthalf = str(i)[: len(str(i)) // 2]
            # secondhalf = str(i)[len(str(i)) // 2 :]
            # print(firsthalf, secondhalf)
            # if firsthalf == secondhalf:
            #     total += i
    print(total)


# debugging
def checkTwo():
    with open("day2.txt") as f:
        lines = f.readlines()
    total = 0
    numbers = lines[0].split(",")
    for num in numbers:

        num1 = int(num.strip().split("-")[0])
        num2 = int(num.strip().split("-")[1])
        for i in range(num1, num2 + 1):
            numstr = str(i)
            for digit in range(0, len(numstr), 2):
                print(numstr[digit:digit + 2])
    print(total)

# debugging
def findLargestLen():
    with open("day2.txt") as f:
        lines = f.readlines()
    numbers = lines[0].split(",")
    largest = 0
    for num in numbers:

        num1 = int(num.strip().split("-")[0])
        num2 = int(num.strip().split("-")[1])
        for i in range(num1, num2 + 1):
            if len(str(i)) > largest:
                largest = len(str(i))
    print(largest)


if __name__ == "__main__":
    main()
