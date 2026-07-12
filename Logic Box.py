print("Welcome to the Pattern Generator and Number Analyzer!\n")
while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            rows = int(input("Enter the number of rows for the pattern: "))
            print("\nPattern:")
            for i in range(1,rows + 1):
                for j in range(i):
                    print("*",end = "")
                print()
            print()
        case 2:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            total = 0
            for num in range(start,end + 1):
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                total += num
            print(f"Sum of all numbers from {start} to {end} is: {total}\n")

        case 3:
            print("""Exiting the program.
Thank you for Using Data Organizer. Goodbye!""")
            break
        case _:
            print("Invalid choice! Please enter 1, 2, or 3.")
