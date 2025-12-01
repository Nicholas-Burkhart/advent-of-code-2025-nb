def main():
    with open("./part1.txt") as f:
        lines = f.readlines()

    dial = 50
    total = 0
    for line in lines:
        number = 0
        if "R" in line:
            number = int(line.strip("R"))
        else:
            number = int(line.strip("L"))
        for i in range(number):
            if "R" in line:
                dial += 1
                if dial == 100:
                    dial = 0
            else:
                dial -= 1
                if dial == -1:
                    dial = 99
        if dial == 0:
            total += 1
    print(total)




if __name__ == "__main__":
    main()