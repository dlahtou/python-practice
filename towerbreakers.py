## This is my solution to https://www.hackerrank.com/challenges/tower-breakers-the-final-battle-1/

## Start with a tower of size 3. First move is 2,1. Values of this move are 5,4
listofmaxtowers = [1,0,0,0,2]

positionvalue = [i**2 for i in range(1,20)]

thisturnsmove = [2,1]
thisturnsvalue = [5,4]

## returns the lowest index in listofmaxtowers corresponding to int height
def getvalue(height):
    ## try to return the value if an existing maxtower is requested
    try:
        return listofmaxtowers.index(height)
    ## find the shortest maxtower that is taller
    except:
        for j in len(listofmaxtowers):
            if listofmaxtowers[j] >= height:
                return j

## updates thisturnsvalue based on thisturnsmove
def calculatevalue():
    for i in range(0,len(thisturnsmove)):
        thisturnsvalue[i] = getvalue(thisturnsmove[i]) + (i+1)**2

## uses (thisturnsmove, thisturnsvalue) to update listofmaxtowers
def posttowervalue():
    towerheight = sum(thisturnsmove)
    towervalue = max(thisturnsvalue)
    if len(listofmaxtowers) == towervalue + 1:
        listofmaxtowers[towervalue] = towerheight
    else:
        listofmaxtowers.append(towerheight)

## increments a subtower to next maxtower, adds a 1 in new position
def findnextmove():
    thisturnsmaxvalue = max(thisturnsvalue)
    ## check positionvalue array to see if can add a new unit tower
    if thisturnsmaxvalue >= positionvalue[len(thisturnsmove)]:
        thisturnsvalue.append(positionvalue[len(thisturnsmove)])
        thisturnsmove.append(1)
        return
    ## increment a tower to next maxtower
    for i in reversed(range(0,len(thisturnsmove))):
        if thisturnsvalue[i] is not thisturnsmaxvalue and thisturnsmaxvalue - thisturnsvalue[i] >= 1 and thisturnsmove[i] != 1:
            thisturnsmove[i] = listofmaxtowers[thisturnsmaxvalue-positionvalue[i]]
            break
        elif thisturnsvalue[i] is not thisturnsmaxvalue and thisturnsmaxvalue - thisturnsvalue[i] >= 4:
            thisturnsmove[i] = 2
            break
        elif i == 0:
            thisturnsmove[0] = listofmaxtowers[thisturnsmaxvalue]
    return

while sum(thisturnsmove) < 2:
    calculatevalue()
    posttowervalue()
    
    findnextmove()

calculatevalue()
posttowervalue()
print(listofmaxtowers)
print(thisturnsmove)
print(thisturnsvalue)
print("Tower height is %s" % sum(thisturnsmove))
print("Tower value is %s" % max(thisturnsvalue))