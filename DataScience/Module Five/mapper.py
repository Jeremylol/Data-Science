import sys

for line in sys.stdin:
    line = line.strip() # remove white spaces
    words = line.split() #split into words
    for word in words:
        print('%s\t%s'%(word,1))