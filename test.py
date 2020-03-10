f = open("test_file.txt")
lines = f.readlines()
for line in lines:
    line.strip()

numCases = int(lines[0].strip())
lines.pop(0)
print(lines)



for i in range(numCases):
    outputString = ""
    beautySum = 0
    print(lines[i][0])
    for j in range(1,int(lines[i][0])):
        if (int(lines[i][j]) >= 0):
            beautySum += int(lines[i][j])
    outputString += "Case #" + str(i) + ": " + str(beautySum)
    fileOut = open("output_test.txt", "a+")
    fileOut.write(outputString)
    fileOut.close()
