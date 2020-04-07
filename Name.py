def main():
    name = ""
    name = input("Please enter your name:")
    while name == "":
        name=input("Please enter your name:")
    second_letter = name[1:2:]
    print(second_letter)



main()