# Conway's Game of Life
import random, time, copy
WIDTH = 10
HEIGHT = 6
 # Create a list of list for the cells:
nextCells = []
alive = '##'  #  '#'
dead = '..'    #  ' '
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append(alive) # Add a living cell.
        else:
            column.append(dead) # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\nnew') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1, if very left it gets right
            leftCoord = (x - 1) % WIDTH

            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == alive:
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == alive:
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == alive:
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == alive:
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == alive:
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == alive:
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == alive:
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == alive:
                numNeighbors += 1  # Bottom-right neighbor is alive.
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == alive and (numNeighbors == 2 or
                                              numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = alive
            elif currentCells[x][y] == dead and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = alive
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = dead
    time.sleep(1)  # Add a 1-second pause to reduce flickering.
