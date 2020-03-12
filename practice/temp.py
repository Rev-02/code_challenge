f = open("test_file.txt")
lines = f.readlines()
sanLines = []
for a in range(len(lines)):
    if lines[a] != "\n":
        lines[a] = lines[a].split(' ')
        if len(lines[a]) > 1:
            for b in range(len(lines[a])):
                lines[a][b] = lines[a][b].strip('\n')
        else:
            lines[a][0] = lines[a][0].strip('\n')
        sanLines.append(lines[a])

print(sanLines)

count = 0
while count < len(sanLines):
    print(count)
    print(len(sanLines))
    print(sanLines[count])
    if sanLines[count] == "\n":
        sanLines.pop(count)
        count -= 1
    else:
        count += 1

numCases = int(str(sanLines[0][0]).strip('\n'))
sanLines.pop(0)
print(numCases)
print(sanLines)

for i in range(numCases):
    indexPos = i*2
    outputString = ""
    beautySum = 0
    for j in range(len(sanLines[indexPos+1])):
        print(j)
        if (int(sanLines[indexPos+1][j]) >= 0):
            print(">0")
            beautySum += int(sanLines[indexPos+1][j])
    outputString += "Case #" + str(i) + ": " + str(beautySum) + "\n"
    print(beautySum)
    print(outputString)
    fileOut = open("output_test.txt", "a+")
    fileOut.write(outputString)
    fileOut.close()
