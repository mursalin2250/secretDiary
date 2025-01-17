import os
print("Welcome to Secret Diary!")
while True:
    print("Select and option\n1. Create new diary\n2. Edit diary\n3. Read diary\n4. Remove diary\n5. Exit")
    userInput = int(input("> "))
    # Create new diary
    if userInput == 1:
        name = input("Enter the diary name: ")

        # checks if Diaries directory exists
        if not os.path.exists("Diaries"):
            # makes a directory named Diary
            os.mkdir("Diaries")
        # specifies the file path
        path = os.path.join("Diaries",f"{name}.txt")
        with open(path, "w") as file:
            file.write("")
        print("Diary created successfully")
    # edit existing diaries
    elif userInput == 2:
        print("\nCurrent Diaries:")
        diaries = os.listdir("Diaries")
        i = 1
        # shows all current diares
        for diary in diaries:
            print(f"{i}. {diary}")
            i += 1
        selectDiary = int(input("Diary do you want to edit: "))
        if selectDiary >= 1 and selectDiary < i:
            edit = input("Enter your text: ")
            path = os.path.join("Diaries",diaries[selectDiary-1])
            with open(path, "a") as file:
                file.write(edit)
            print("\nEdit successful!\n")
        else:
            print("\nInvalid input!\n")
            continue
    #read the diaries
    elif userInput == 3:
        print("\nCurrent Diaries:")
        diaries = os.listdir("Diaries")
        i = 1
        for diary in diaries:
            print(f"{i}. {diary}")
            i += 1
        selectDiary = int(input("Diary do you want to read: "))
        if selectDiary >= 1 and selectDiary < i:
            path = os.path.join("Diaries",diaries[selectDiary-1])
            with open(path, "r") as file:
                content = file.read()
            print()
            print(content)
            print()
        else:
            print("\nInvalid input!\n")
            continue
    # remove diary
    elif userInput == 4:
        print("\nCurrent Diaries:")
        diaries = os.listdir("Diaries")
        i = 1
        for diary in diaries:
            print(f"{i}. {diary}")
            i += 1
        selectDiary = int(input("Diary do you want to remove: "))
        if selectDiary >= 1 and selectDiary < i:
            path = f"Diaries\{diaries[selectDiary-1]}"
            confirmation = input("Are you sure you want to remove the diary(y/N): ")
            confirmation.strip().lower()
            if confirmation == "y":
                os.remove(path)
                print("\nDiary removed successfully.\n")
            elif confirmation == "" or confirmation == "n":
                print("\nDiary was not removed.\n")
                continue
            else:
                print("\nInvalid input!\n")
                continue

        else:
            print("\nInvalid input!\n")
            continue
    # exit the application
    elif userInput == 5:
        print("Thank you for using serect diary")
        break

    else:
        print("Invalid input!")