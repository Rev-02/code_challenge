f = open("test_file.txt")
r_lines = f.readlines()
lines = []
for line in r_lines:
    line = line.strip()
    if len(line) != 0:
        lines.append(line)
print(lines)
numCases = int(lines[0].strip())
lines.pop(0)
print(lines)



for i in range(numCases):
    outputString = ""
    beautySum = 0
    print(lines)
    for j in range(1,int(lines[i][0])):
        if (int(lines[i][j]) >= 0):
            beautySum += int(lines[i][j])
    outputString += "Case #" + str(i) + ": " + str(beautySum)
    fileOut = open("output_test.txt", "a+")
    fileOut.write(outputString)
    fileOut.close()
