import os

# show enviornment
for key in os.environ.keys():
    print(key, os.environ[key])

# another way to show enviornment
for key, val in os.environ.items():
    print(key, val)

# show files in the current directory
for i in range(len(os.listdir())):
    print(os.listdir()[i])
    
