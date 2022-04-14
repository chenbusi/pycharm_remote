def name():
    return input("name?")


my_file = open("names.txt", "a")
my_file.write(name())
my_file.close()


with open("names.txt") as my_file:
    print(my_file.readlines())