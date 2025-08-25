"""
Mode                   Description

r      	Read-only. Raises I/O error if file doesn't exist.
r+ 	    Read and write. Raises I/O error if the file does not exist.
w 	    Write-only.Overwrites file if it exists, else creates a new one.
w+	    Read and write. Overwrites file or creates new one.
a	        Append-only. Adds data to end. Creates file if it doesn't exist.
a+	    Read and append.Pointer at end.Creates file if it doesn't exist.
rb	    Read in binary mode. File must exist.
rb+	    Read and write in binary mode. File must exist.
wb	    Write in binary. Overwrites or creates new.
wb+	    Read and write in binary. Overwrites or creates new.
ab	    Append in binary. Creates file if not exist.
ab+	    Read and append in binary. Creates file if it does not exist.

"""

# ---------------------------------------------------------------------------------------

# read(), readline() and readlines()

#  read() - reads the entire file as one string
# with open("read.txt", "r") as file:
#     text = file.read()
#     print(text)


#  readline() - reads a file line by line
# with open("read.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     print(line1.strip())
#     print(line2.strip())

# readlines() - Reads all lines into a list ( includes \n )
# with open("read.txt", "r") as file:
#     lines = file.readlines()
#     print([text.strip() for text in lines])

# -----------------------------------------------------------------------------------

# write(), writelines()

# write() - Write string to a file
# with open("write.txt", "a+") as file:
#     file.write("This is a test line for write() function.\n")
#     file.seek(0)
#     line1 = file.readline()
#     print(line1)
#     file.seek(0,2)
#     file.write("This is another test line for write() function.\n")
#     loc = file.tell()
#     print(loc)

# writelines() - Write list of strings
# data = ["This is a first line from list.\n", "This is a second line from list.\n"]
# with open("write.txt", "a+") as file:
#     file.writelines(data)

# -----------------------------------------------------------------------------------