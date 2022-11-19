
def addNew():
    f = open("list.txt", "a")
    new = input("Enter a new element: ")
    f.write(new + " ")
    f.close()
    print("The new element has been added.")
    print("The new element is: " + new)


def read():
    f = open("list.txt", "r")
    for line in f:
        print(line)
    f.close()


def sort():
    f = open("list.txt", "r")
    for line in f:
        s = line.split("")
    f.close()
    s.sort()
    f = open("list.txt", "w")
    for i in s:
        f.write(i + "")
    f.close()


def search():
    f = open("list.txt", "r")
    for line in f:
        s = line.split(" ")
    f.close()
    search = input("Enter a number to search: ")
    if search in s:
        print("The number is in the list.")
    else:
        print("The number is not in the list.")


def main():
    print("1. Add a new element")
    print("2. Read the list")
    print("3. Sort the list")
    print("4. Search for a number")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            addNew()
        elif choice == 2:
            read()
        elif choice == 3:
            sort()
        elif choice == 4:
            search()
        else:
            print("Invalid choice")
        print("1. Add a new element")
        print("2. Read the list")
        print("3. Sort the list")
        print("4. Search for a number")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
    print("Program terminated")

main()
