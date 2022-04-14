my_file = open("read_my_contents.txt")

for line in my_file.readlines():
    print(line, end="")
