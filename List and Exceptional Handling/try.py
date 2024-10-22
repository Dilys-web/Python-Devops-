import os

folders = input("Provide a list of folders name with spaces between them: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
        print("===== listing files for the folder -" + folder)
        print(f"Files in '{folder}': {files}")

        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Error: The folder '{folder}' does not exist.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")    
    except PermissionError:
        print(f"Permission denied for the folder '{folder}'")

  
