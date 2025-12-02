def main():
    with open("day2.txt") as f:
        lines = f.readlines()
    total = 0
    numbers = lines[0].split(",")
    for num in numbers:

        num1 = int(num.strip().split("-")[0])
        num2 = int(num.strip().split("-")[1])
        for i in range(num1, num2 + 1):
            if len(str(i)) % 2 != 0:
                continue
            firsthalf = str(i)[: len(str(i)) // 2]
            secondhalf = str(i)[len(str(i)) // 2 :]
            print(firsthalf, secondhalf)
            if firsthalf == secondhalf:
                total += i
    print(total)


if __name__ == "__main__":
    main()