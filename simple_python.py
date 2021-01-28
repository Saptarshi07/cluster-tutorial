import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    contents = f.read()

print(contents)