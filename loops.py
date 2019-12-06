import os

# show environnement
for key in os.environ.keys():
    print(key, os.environ[key])

# another way to show environnement
for key, value in os.environ.items():
    print(key, value)

# show files in the current directory
for i in range(len(os.listdir())):
    print(os.listdir()[i])