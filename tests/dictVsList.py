import sample.tictactoe_module

boardList = [9,8,7,6,5,4,3,2,1]
boardDict = {
    9:"X",
    8:" ",
    7:" ",
    6:" ",
    5:"X",
    4:" ",
    3:" ",
    2:" ",
    1:"X",
}

# print("List:")
# for slots in boardList:
#     print(slots)
# print()

# print("Dict:")
# for slots in boardDict:
#     print(slots)
# print()

i = 1
xCount = 0
oCount = 0
# while(i in boardDict):
#     boardDict[i] = "X"
#     print(boardDict[i])
#     print(i)
#     i += 1

while(i in boardDict and xCount != 3 and oCount != 3):
    print(boardDict[i])
    print(i)
    while(boardDict[i] == "X"):
        xCount += 1
        print(f"xCount = {xCount}")
        print('X is here.')
        break
    while(boardDict[i] == "O"):
        oCount += 1
        print(f"oCount = {oCount}")
        print('O is here.')
        break
    i += 4
    