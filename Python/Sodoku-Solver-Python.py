import math
import time
import copy

# Sodoku Solver!!

# Global Variables!
fullPossibleList = []
curPossibleList = []

# Pass in a list and get all possible values
def getPossibleList(listToCheck):
  
  # First thing - Let's go through the grid and determine possibles.
  masterPossibleList = []

  for y in range(9):
    masterPossibleList.append([])

    for x in range(9):
      masterPossibleList[y].append([])
      
      possibleList = []

      #print("Checking ", x, ",", y, ":")

      # Not filled out? Let's get some possibles by comparing
      if listToCheck[y][x] == 0:

          # Go through each number
          for cNum in range(1, 10):

            # Check if the number works in the chosen location
            if checkNumber(listToCheck, x, y, cNum):

              # Add the number to the possible list
              possibleList.append(cNum)
              masterPossibleList[y][x].append(cNum)
          
      # What's left? Just display it.
      # print("X", x, " - Y", y, ": ", possibleList)

      # if len(possibleList) == 0:
      #   print("No Match")
      # else
      #   print(possibleList)
  return masterPossibleList
  # return True

def checkNumber(listToCheck, x, y, cNum):
  # print(cNum, "?")

  # Is it in the row?
  if cNum in listToCheck[y]:
    # print(cNum, " Found in row ", x)
    return False;
  
  # Check the column
  foundInCol = False
  for cY in range(9):
    if listToCheck[cY][x] == cNum:
      # print(cNum, " Found in row ", cY)
      foundInCol = True
      return False;

  if foundInCol:
    return False;

  # What about the grid?
  # Grids are 3 x 3 -- so we first need to figure out which grid we are in
  # This can be done by just getting the floor.
  curGridX = math.floor(x / 3) * 3
  curGridY = math.floor(y / 3) * 3

  # print("Grid: ",curGridX,"-",curGridY)
  
  foundGridNum = False

  # Loop through the 3x3 grid.
  for gridY in range(curGridY, curGridY+3):

    # Already found? Just skip.
    if foundGridNum:
      break

    # Check the X Cord
    for gridX in range(curGridX, curGridX+3):
      if listToCheck[gridY][gridX] == cNum:
        # foundGridNum = True
        return False

  # Was the number found? The stop
  if foundGridNum:
    return False
  
  return True

def findPreviousCell(curY, curX):
  global curPossibleList, fullPossibleList

  # Track where we end up going to.
  goToX = 0
  goToY = 0
  foundJump = False

  # We need to go through the list backwards.
  while (curY >= 0):

    # Already found the jump? Just Stop
    if foundJump == True:
      break

    while (curX >= 0):
      # print(curY, curX, curPossibleList[curY][curX], fullPossibleList[curY][curX])

      # Does this cell have open solutions? Use it
      if len(curPossibleList[curY][curX]) > 0:
        # print("FOUND SOLUTION - STOP")
        goToX = curX
        goToY = curY
        foundJump = True
        break

      # Is this supposed to have possible solutions? Reset it for the next time we use it.
      elif len(fullPossibleList[curY][curX]) > 0:
        # print("REST", curY, curX)
        curPossibleList[curY][curX] = fullPossibleList[curY][curX]

      # else:
      #   print("Nothing to talk about.")

      # Keep going back
      curX = curX - 1

    # Go up a row
    curX = 8
    curY = curY - 1

  # print("FOUND:",goToY, goToX, curPossibleList[goToY][goToX])

  return [goToY, goToX]


def runSimulation(startList):
  global curPossibleList, fullPossibleList

  # Start off by grabbing the possible list.
  fullPossibleList = getPossibleList(startList)

  curPossibleList = copy.deepcopy(fullPossibleList)

  tempSolution = copy.deepcopy(startList)

  # Track which direction we are going.
  # -1 = Backwards
  # 0  = Stay Same
  # 1  = Forwards
  moveDirection = 1

  y = 0

  # Loop through all Y's
  while y < 9:

    # Always start at column 0
    x = 0

    while x < 9:
      print("-",y,x, curPossibleList[y][x])

      # Does the starting list already have it solved? Then just skip
      if startList[y][x] > 0:
        x = x + 1
        continue

      # Do we have solutions to try?
      elif len(curPossibleList[y][x]) > 0:

        # Go through the current solutions
        for checkNum in curPossibleList[y][x]:
          # print("Checking: ", checkNum)

          # Remove the number from the list, regardless if it works or not.
          # Why? We checked it
          curPossibleList[y][x].remove(checkNum)

          # Check if this solution works
          # If it does, then update the tempSolution
          if checkNumber(tempSolution, x, y, checkNum):
            tempSolution[y][x] = checkNum
            # print(y, x, "Updating with", checkNum)

            # We can move forward
            moveDirection = 1

            break

          # Solution Failed - Do we have others to try? Just try our cell again.
          elif len(curPossibleList[y][x]) > 0:
            moveDirection = 0

          # No other possible solutions - we need to backtrack.
          else:
            # print("No Go - Need to backtrack")
            moveDirection = -1

      # We have no solutions to try -- we hit a road block
      else:
        moveDirection = -1

      # Determine Movement

      # Going Forward?
      if moveDirection == 1:
        x = x + 1

      # Going Backward?
      elif moveDirection == -1:
        # print("Backward")

        # We need to figure out where to jump to.
        [newY, newX] = findPreviousCell(y, x)

        print("Jumping to: ", newY, newX)

        x = newX
        y = newY

      time.sleep(.5)

      # # Did we hit a roadblock due to no solutions being available?.
      # elif len(curPossibleList[y][x]) > 0 and len(fullPossibleList[y][x]) > 0:
      #   print("Need to backtrack!")
      #   moveForward = False

      #   # Moving forward? We need to move back.
      #   if moveForward == True:
      #     moveForward = False
      #     x = x-1

      #   else:
      #     # Reset the possible list
      #     curPossibleList[y][x] = fullPossibleList[y][x]
      #     print("Resetting List")

      #     moveForward = True

      # Are we moving backward? We need to keep going.
      # if moveForward == False:
      #   print("Moving Back...")
      #   x = x-1
      
      # Are we at the end? Do we still have any "0" left?  Then we have a problem and need to go back.
      # if x == 8 and y == 8:
      #   print("Sanity Check")
      #   # Sanity Check!
      #   for sY in range(8):
      #     for sX in range(8):
      #       if tempSolution[sY][sX] == 0:
      #         print("Something is wrong - We must go back!")
      #         x = x - 1
      #         moveForward = False
    y = y + 1

    # # Moving backward but hit the end? Move up.
    # if moveForward == False and x == 8:
    #   x = 0
    #   y = y - 1
  

  # Solved!  Print the final solution
  print("------------------")
  print("Final Solution:")
  print("------------------")

  print("Original:")
  for tblRow in range(9):

    # Make a space every three rows
    if tblRow % 3 == 0 and tblRow > 0:
      print()
    
    print(startList[tblRow])

  print()
  print("Solution:")
  for tblRow in range(9):

    # Make a space every three rows
    if tblRow % 3 == 0 and tblRow > 0:
      print()
    
    print(tempSolution[tblRow])

          






# startList = [
#   [4,0,7, 0,0,0, 9,1,0],
#   [0,1,5, 0,0,2, 6,0,0],
#   [0,8,3, 0,1,0, 2,5,0],

#   [8,0,1, 0,9,0, 0,4,5],
#   [0,5,6, 7,4,0, 8,9,1],
#   [3,0,0, 0,0,1, 0,0,6],

#   [0,0,2, 8,0,0, 0,0,0],
#   [5,9,0, 0,7,4, 1,0,0],
#   [0,0,4, 0,0,0, 0,3,8]
# ]

startList = [
  [0,0,0, 2,6,0, 7,0,1],
  [6,8,0, 0,7,0, 0,9,0],
  [1,9,0, 0,0,4, 5,0,0],

  [8,2,0, 1,0,0, 0,4,0],
  [0,0,4, 6,0,2, 9,0,0],
  [0,5,0, 0,0,3, 0,2,8],

  [0,0,9, 3,0,0, 0,7,4],
  [0,4,0, 0,5,0, 0,3,6],
  [7,0,3, 0,1,8, 0,0,0]
]


# Start off by just displaying possibles.
# getPossibleList(startList)


# Run the full simulation to determine a solution
runSimulation(startList)