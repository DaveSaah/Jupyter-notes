#############################################################################
### Task 3
#############################################################################

grid = [
    [34, 21, 32, 41, 25],
    [14, 42, 43, 14, 31],
    [54, 45, 52, 42, 23],
    [33, 15, 51, 31, 35],
    [21, 52, 33, 13, 23],
]

treasure = 0
clue = 11

while treasure == 0:
    x_cor = clue // 10
    y_cor = clue % 10
    value = grid[x_cor - 1][y_cor - 1]

    if value == clue:
        treasure = value
        print(treasure)
    else:
        clue = value

############################################################################


############################################################################
### Task 4
############################################################################

votes = [
    [1, 192, 48, 206, 37],
    [2, 147, 90, 312, 21],
    [3, 186, 12, 121, 38],
    [4, 114, 21, 408, 39],
    [5, 267, 13, 382, 29],
    ]

# Displaying votes in a table
print("{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}".format("", "Candidate", "Candidate", "Candidate", "Candidate"))
print("{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}".format("Precinct", "A", "B", "C", "D"))

for vote in votes:
    print("{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}".format(vote[0], vote[1], vote[2], vote[3], vote[4]))

    
# Candidates and percentages
candidateA = []
candidateB = []
candidateC = []
candidateD = []

for candidate in votes:
    candidateA.append(candidate[1])
    candidateB.append(candidate[2])    
    candidateC.append(candidate[3])    
    candidateD.append(candidate[4])

total_votes = sum(candidateA + candidateB + candidateC + candidateD)

total_A = sum(candidateA)
total_B = sum(candidateB)
total_C = sum(candidateC)
total_D = sum(candidateD)

print("Candidate A had:", total_A)
print("Candidate B had:", total_B)
print("Candidate C had:", total_C)
print("Candidate D had:", total_D)


percentA = (total_A / total_votes) * 100
percentB = (total_B / total_votes) * 100
percentC = (total_C / total_votes) * 100
percentD = (total_D / total_votes) * 100

print("Candidate A:", round(percentA, 2), "%")
print("Candidate B:", round(percentB, 2), "%")
print("Candidate C:", round(percentC, 2), "%")
print("Candidate D:", round(percentD, 2), "%")

winner = ""

candidates = {
    "A": round(percentA, 2),
    "B": round(percentB, 2),
    "C": round(percentC, 2),
    "D": round(percentD, 2)
}


# find the winner
for x in candidates.values():
    if x > 50:
        winner = [name for name, score in candidates.items() if score == x][0]

# find the two maximum candidates
twomax = sorted(candidates.values())[-2:]
if winner == "":
    runoffs = [name for name, score in candidates.items() if score in twomax]

print("The runoff candidates are", runoffs[0] and runoffs[1])



##############################################
## Saddle number
## Create 5x5 integer array
nums = [
    [1, 192, 48, 206, 37],
    [2, 147, 90, 312, 21],
    [3, 186, 12, 121, 38],
    [4, 114, 21, 408, 39],
    [5, 267, 13, 382, 29],
    ]

## Create lists for each column
## Purpose: to allow easy comparison of maximum row value with column values
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []

for num in nums:
    column1.append(num[0])
    column2.append(num[1])
    column3.append(num[2])
    column4.append(num[3])
    column5.append(num[4])

## Find max number in row
## Compare against the values in the column to check if its a saddle number
for num_ in nums:
    saddle_ = max(num_)
    saddle_index = num_.index(saddle_)
    # print(num_)
    # print(saddle_index, saddle_)
    if saddle_index == 0:
        if True in [(saddle_ < x) for x in column1]:
            print(saddle_)
    elif saddle_index == 1:
        if True in [(saddle_ < x) for x in column2]:
            print(saddle_)
    elif saddle_index == 2:
        if True in [(saddle_ < x) for x in column3]:
            print(saddle_)
    elif saddle_index == 3:
        if True in [(saddle_ < x) for x in column4]:
            print(saddle_)
    elif saddle_index == 4:
        if True in [(saddle_ < x) for x in column5]:
            print(saddle_)
    else:
        print("No saddle") 