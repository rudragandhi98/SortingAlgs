from timeit import default_timer as timer

# Selection Sort
file2 = open('20k.txt', 'r')
sortedLines = file2.readlines()
sortedLines.sort() # Using a library Function, to sort the array, this will be used to check my implementation

start = timer()
file1 = open('20k.txt', 'r')
Lines = file1.readlines()

#Implementing Selection Sort
for i in range(0,len(Lines)):
    min = i
    for j in range(i+1,len(Lines)):
        if(Lines[j] < Lines[min]):
            min = j
    Lines[i],Lines[min] = Lines[min],Lines[i]

end = timer()
print(Lines)
print(Lines == sortedLines) # Comparing to check if my implementation gives a sorted array.
print(end - start) # Finding the total time measurement