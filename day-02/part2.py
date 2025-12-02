def main():
    with open("day2.txt") as f:
        lines = f.readlines()
    total = 0
    numbers = lines[0].split(",")
    for num in numbers:

        num1 = int(num.strip().split("-")[0])
        num2 = int(num.strip().split("-")[1])
        maxlen = findLargestLen()
        for i in range(num1, num2 + 1):
            numstr = str(i)
            if len(numstr) == 1:
                continue
            if all(digit == numstr[0] for digit in numstr):
                total += i
                continue
            for letters in range(1, maxlen // 2 + 1):    
                if all(numstr[digit:digit + letters] == numstr[0:letters] for digit in range(0, len(numstr), letters))  and len(numstr) > letters:
                    total += i
                    break    
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
    return largest


if __name__ == "__main__":
    main()
 
# Answer: 20077272987
