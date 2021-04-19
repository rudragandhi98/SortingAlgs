from timeit import default_timer as timer

# Bubble Sort
file2 = open('20k.txt', 'r')
sortedLines = file2.readlines()
sortedLines.sort() # Using a library Function, to sort the array, this will be used to check my implementation

start = timer()
file1 = open('20k.txt', 'r')
Lines = file1.readlines()

# Bubble Sort Implementation
for i in range(0,len(Lines)):
    for j in range(0,len(Lines)-i-1):
        if(Lines[j] > Lines[j+1]):
            Lines[j],Lines[j+1] = Lines[j+1],Lines[j]


end = timer()
print(Lines)
print(Lines == sortedLines) # Comparing to check if my implementation gives a sorted array.
print(end-start) # Finding the total time measurement