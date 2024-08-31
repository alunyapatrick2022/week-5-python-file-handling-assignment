# file_handling_assignment.py

try:
    # Step 1: Create a new text file named "my_file.txt" in write mode and write a message to it
    with open("my_file.txt", "w") as file:
        file.write(
            """Heyy Patrick Alunya, it has been long since you logged into your LMS. What's up? Are you bored?
Is your girlfriend not answering the calls again?
Don't worry, just give her some time, and for sure, she will rethink about your reunion.

Otherwise, reach us via +25411548341 if in need of any assistance. We are there for you, any time, any day, just right there.
Goodbye."""
        )
    print("File 'my_file.txt' has been created successfully.")

    # Step 2: Open "my_file.txt" in append mode and add three additional lines of text
    with open("my_file.txt", "a") as file:
        file.write(
            """
            
P.S. Remember, everything will be fine. Just stay positive!
We value you as a member of our community.
Feel free to visit us anytime."""
        )
    print("Additional lines have been appended to 'my_file.txt'.")

    # Step 3: Read the contents of "my_file.txt" and display them on the console
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to access 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Script execution completed.")
