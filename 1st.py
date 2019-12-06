import sys

done = False

while not done:
    # Ask the user
    answer = input('Who are you? ')
    if answer == "done":
        done = True
    elif answer == "q":
        break
    else:
        print('My name is: {}'.format(answer))
    # go back to line 5
    
# After the loop
sys.exit()
