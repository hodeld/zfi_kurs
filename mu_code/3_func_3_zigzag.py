#zigzag
#stop ctrl-c

import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
    while True: # The main program loop.

        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()


#zigzag mit for
#stop ctrl-c
import time, sys
indent = 0 # How many spaces to indent.
#indentIncreasing = True # Whether the indentation is increasing or not.

def print_start(ind):
    print(' ' * ind, end='')
    print('********')
    time.sleep(0.1) # Pause for 1/10 of a second.

try:
    while True: # The main program loop.


        for ind in range(0, 20):
            # Increase the number of spaces:
            print_start(ind)

        for ind in range(20, 0, -1):  #step needs to be defined
            # Increase the number of spaces:
            print_start(ind)

except KeyboardInterrupt:
    sys.exit()