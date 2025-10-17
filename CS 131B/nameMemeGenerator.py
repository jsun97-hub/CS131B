def generate_name(fileName, personName):
    firstNameMap = []
    lastNameMap = []
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            if count < 26:
                firstNameMap.append(line.strip())
                count += 1
            else:
                lastNameMap.append(line.strip())

    name = personName.split()
    firstName = name[0][0]
    lastName = name[1][0]

    for n in range(65,91):
        if chr(n) == firstName:
            firstName = firstNameMap[n - 64 - 1]
        if chr(n) == lastName:
            lastName = lastNameMap[n - 64 - 1]

    return str(firstName) + " " + str(lastName)

print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))