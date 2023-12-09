import os

directory = '/path/to/directory'

if os.path.exists(directory):
    print("Directory exists")
else:
    print("Directory does not exist")
