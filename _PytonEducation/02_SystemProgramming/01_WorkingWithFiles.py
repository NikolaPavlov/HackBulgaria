# 1. Create file and write to it
file1 = open('filename', 'w')
for i in range(101):
    file1.write(str(i) + ' ')
file1.close()

# 2. Append content to file
file1 = open('filename', 'a')
file1.write('/n Append line to the file')

# 3. Read from file
