# 1. read the file content
with open("input.txt","r") as file: 
    for line in file:
        print(line)
        #implement algorithim to read the input data

# 2. implement logic

# 3. write to the file
file = open("output.txt","w")
file.write("1 2")
file.close()