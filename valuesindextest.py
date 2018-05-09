## This was an early iteration of my solution that can now be found in towerbreakers.py

listofmaxtowers = [1,0,0,0,2,3,4,5,7,11]

def findvalue(towerheight):
    ## attempt to return a maxtower from the list
    try:
        return listofmaxtowers.index(towerheight)
    except:
        for towervalue in range(0,len(listofmaxtowers)):
            if listofmaxtowers[towervalue] >= towerheight:
                return towervalue

## returns the difference between a tower of given height and the shortest maxtower above it
def finddifferencetolargest(towerheight):
    for biggesttower in listofmaxtowers:
        if biggesttower > towerheight:
            return biggesttower - towerheight

workingarray = [7,3,1,0,0,0,0]
valuesarray = [7,4,0,0,0,0,0]
towersize = 11

def updatevaluesarray():
    for elementindex in range(0,len(workingarray)):
        if workingarray[elementindex] == 0:
            continue
        valuesarray[elementindex] = findvalue(workingarray[elementindex]) + (elementindex+1)**2
updatevaluesarray()

while towersize < 152:
    currentmaxvalue = max(valuesarray)
    hasjumped = False

    for element in range(0,len(workingarray)):
        ## check if element can be jumped
        if workingarray[element] not in listofmaxtowers:
            jump = finddifferencetolargest(workingarray[element])
            workingarray[element] += jump
            towersize += jump
            hasjumped = True

        ## check if incrementing element will increase value
        elif findvalue(workingarray[element]+1) and findvalue(workingarray[element]+1) + (element+1)**2 <= max(valuesarray):
            workingarray[element] += 1
            towersize += 1
            break
        
        if element == len(workingarray)-1 and not hasjumped:
            workingarray[0] += 1
            towersize += 1
    print(workingarray)
    updatevaluesarray()

    ## add new size tower to array
    if len(listofmaxtowers) == max(valuesarray):
        listofmaxtowers[-1] = towersize-1
    else:
        listofmaxtowers.append(towersize-1)
    
    print(listofmaxtowers)
    print(workingarray)
    print(valuesarray)
    print(towersize-1)
    print('------')