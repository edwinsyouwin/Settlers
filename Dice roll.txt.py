import random

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total_dice = dice1 + dice2
    return total_dice

two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0
seven_count = 0
eight_count = 0
nine_count = 0
ten_count = 0
eleven_count = 0
twelve_count = 0

blah = int(raw_input("How many rolls?"))
for i in range(1,blah):
    e = dice_roll()
    if e == 2:
        two_count +=1
    elif e==3:
        three_count+=1
    elif e==4:
        four_count+=1
    elif e==5:
        five_count+=1
    elif e==6:
        six_count+=1
    elif e==7:
        seven_count +=1
    elif e==8:
        eight_count +=1
    elif e==9:
        nine_count +=1
    elif e==10:
        ten_count += 1
    elif e ==11:
        eleven_count +=1
    elif e==12:
        twelve_count += 1

print "Counts"
print "2:" + str(two_count)
print "3:" + str(three_count)
print "4:" + str(four_count)
print "5:" + str(five_count)
print "6:" + str(six_count)
print "7:" + str(seven_count)
print "8:" + str(eight_count)
print "9:" + str(nine_count)
print "10:" + str(ten_count)
print "11:" + str(eleven_count)
print "12:" + str(twelve_count)

print "Percentages"
print "2:" + str(float(two_count)/float(blah))
print "3:" + str(float(three_count)/float(blah))
print "4:" + str(float(four_count)/float(blah))
print "5:" + str(float(five_count)/float(blah))
print "6:" + str(float(six_count)/float(blah))
print "7:" + str(float(seven_count)/float(blah))
print "8:" + str(float(eight_count)/float(blah))
print "9:" + str(float(nine_count)/float(blah))
print "10:" + str(float(ten_count)/float(blah))
print "11:" + str(float(eleven_count)/float(blah))
print "12:" + str(float(twelve_count)/float(blah))
