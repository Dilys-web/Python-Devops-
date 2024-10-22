import sys
import re
import os

pattern = sys.argv[1]
replacement = sys.argv[2]
directory = sys.argv[3]

for filename in os.listdir(directory):
    new_filename = re.sub(pattern, replacement, filename)
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    print(f"Renamed {filename} to {new_filename}")