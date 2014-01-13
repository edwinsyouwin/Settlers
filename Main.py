import random

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total_dice = dice1 + dice2
    return total_dice

tile_position_vector = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3)]
## tile position vector (x,y) where x is column and y is row
random.shuffle(tile_position_vector)

desert_location = tile_position_vector.pop()
## sets the location of the desert because desert is not assigned a tile dice number

resources = ['wheat','wheat','wheat','wheat','sheep','sheep','sheep','sheep','wood','wood','wood','wood','brick','brick','brick','stone','stone','stone']
random.shuffle(resources)

board_dice_numbers=[2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
random.shuffle(board_dice_numbers)

board = zip(position_vector, resources, board_dice_numbers)
board.append((desert_location,'desert',7))

##for each in board:
##    print each

def return_position_vector():
    e = dice_roll()
    print "You rolled a " + str(e)
    position = []
    for i in range(0,len(board)):
        if e == board[i][2]:
            position.append(board[i][0])
    return position


vertice_location_dictionary = {1:[(1,1)],2:[(1,1)],3:[(1,1),(1,2)],4:[(1,2)],5:[(1,2),(1,3)],6:[(1,3)],7:[(1,3)],8:[(2,1)],9:[(1,1),(2,1)],10:[(1,1),(2,1),(2,2)],11:[(1,1),(1,2),(2,2)],
                      12:[(1,2),(2,2),(2,3)],13:[(1,2),(1,3),(2,3)],14:[(1,3),(2,3),(2,4)],15:[(1,3),(2,4)],16:[(2,4)],17:[(3,1)],18:[(2,1),(3,1)],19:[(2,1),(3,1),(3,2)],
                      20:[(2,1),(2,2),(3,2)],21:[(2,2),(3,2),(3,3)],22:[(2,2),(2,3),(3,3)],23:[(2,3),(3,3),(3,4)],24:[(2,3),(2,4),(3,4)],25:[(2,4),(3,4),(3,5)],
                      26:[(2,4),(3,5)],27:[(3,5)],28:[(3,1)],29:[(3,1),(4,1)],30:[(3,1),(3,2),(4,1)],31:[(3,2),(4,1),(4,2)],32:[(3,2),(3,3),(4,2)],33:[(3,3),(4,2),(4,3)],
                      34:[(3,3),(3,4),(4,3)],35:[(3,4),(4,3),(4,4)],36:[(3,4),(3,5),(4,4)],37:[(3,5),(4,4)],38:[(3,5)],39:[(4,1)],40:[(4,1),(5,1)],41:[(4,1),(4,2),(5,1)],
                      42:[(4,2),(5,1),(5,2)],43:[(4,2),(4,3),(5,2)],44:[(4,3),(5,2),(5,3)],45:[(4,3),(4,4),(5,3)],46:[(4,4),(5,3)],47:[(4,4)],48:[(5,1)],49:[(5,1)],
                      50:[(5,1),(5,2)],51:[(5,2)],52:[(5,2),(5,3)],53:[(5,3)],54:[(5,3)]}

vertice_info_dictionary = {}
for i in range(1,55):
    vertice_info_dictionary[i] = []
print vertice_info_dictionary

def match_vertices():
    matched_vertices = []
    for e in return_position_vector():
        print e
        for each in vertice_location_dictionary:
            for i in vertice_location_dictionary[each]:
                if i == e:
                    matched_vertices.append(each)
    return matched_vertices

print match_vertices()

