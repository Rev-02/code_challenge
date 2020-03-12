import operator
f = open("output_test.txt", "w")
f.write("")
f.close()
fil = open("test.txt","r")
lines = fil.readlines()
for line in lines:
    line_s = line.strip()
    lines[lines.index(line)] = line_s
twoD = []
for line in lines:
    twoD.append(line.split(" "))
newTwoD = twoD
test_case = int(twoD[0][0])
newTwoD.pop(0)
points_award_dict = {"1":100,"2":200,"3":300,"4":400,"5":500}
for c in range(test_case):
    total = []
    total_teams = []
    teams = int(newTwoD[0][0])
    logs = int(newTwoD[0][1])
    newTwoD.pop(0)
    for i in range(logs):
        time_stamp = int(newTwoD[i][0])
        team_id = int(newTwoD[i][1])
        problem_id = newTwoD[i][2]
        input_id = newTwoD[i][3]
        scored = int(newTwoD[i][4])
        if scored == 1:
            award = points_award_dict[input_id]
            if team_id in total_teams:
                for team in total:
                    if team_id == team[0]:
                        a = total.index(team)
                if input_id not in total[a][3]:
                    if not total[a][3]:
                        new_list = []
                        new_list.append(input_id)
                        total[a][3] = new_list
                    else:
                        edit_list = total[a][3]
                        edit_list.append(input_id)
                        total[a][3] = edit_list
                    total[a][2] += int(time_stamp)
                    total[a][1] += award
            else:
                total_teams.append(team_id)
                new_list_2 = [team_id,award,time_stamp,[input_id]]
                total.append(new_list_2)
    for i in range(teams + 1):
        if i != 0:
            if i not in total_teams:
                total.append([i,0,0,[]])
    sorted_1_total = sorted_1_total = sorted(total, key=lambda x: (x[1],x[2]), reverse=True)
    for i in range(len(sorted_1_total) - 1):
            if (sorted_1_total[i][1] == sorted_1_total[i+1][1]) and (sorted_1_total[i][2] > sorted_1_total[i+1][2]):
                temp = sorted_1_total[i]
                sorted_1_total[i] = sorted_1_total[i+1]
                sorted_1_total[i+1] = temp
    output_string = "Case #"+str(c+1)+":"
    for i in range(len(sorted_1_total)):
        output_string = output_string + ' ' + str(sorted_1_total[i][0])
    output_string = output_string + '\n'
    f = open("output_test.txt", "a")
    f.write(output_string)
    f.close()
    for me in range(logs):
        newTwoD.pop(0)
