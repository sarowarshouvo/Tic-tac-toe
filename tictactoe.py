# | |  0
#----- 1
# | |  2
#----- 3
# | |  4
#01234
def drawfield(field):
    for row in range(5): #0,1,2,3,4
                         #0,.,1,.,2
        if row % 2 == 0:
            practicalrow = int(row/2)
            for col in range(5): #0,1,2,3,4
                                 #0,.,1,.,2
                if col % 2 ==0:
                    practicalcol = int(col/2)
                    if col != 4:
                        print(field[practicalcol][practicalrow],end="")
                    else:
                        print(field[practicalcol][practicalrow])
                else:
                    print("|",end="")
        else:
            print("-----")
player = 1
currentfield = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawfield(currentfield)
while(True):
    print("Player: ",player)
    moverow = int(input("Enter the row: "))
    movecol = int(input("Enter the col: "))
    if player == 1:
        if currentfield[movecol][moverow] == " ":
            currentfield[movecol][moverow] = "X"
            player = 2
    else:
        if currentfield[movecol][moverow] == " ":
            currentfield[movecol][moverow] = "O"
            player = 1
    drawfield(currentfield)