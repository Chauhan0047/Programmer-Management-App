Programmer Management System

Overview:

The Programmer Management System is a Python application for managing information about programmers working at Microsoft. This program allows users to add, delete, update, view individual programmers, and view all programmers. The data is stored in a JSON file for persistence.

Features:

Add Programmer: Add a new programmer with details such as name, age, role, years of experience, and programming languages.
Delete Programmer: Remove an existing programmer by name.
Update Programmer: Modify details of an existing programmer.
View Programmer: Display detailed information about a specific programmer.
View All Programmers: Display information about all programmers.

Requirements
Python 3.x
No additional external libraries are required.

File Structure:
programmers.json: JSON file to store programmer data.
program_manager.py: The main Python script containing the Programmer and ProgrammerManager classes and the interactive command-line interface.

Usage:
Running the Program = python program_manager.py

Command-Line Interface:
Upon running the program, a command-line interface will be presented with the following options:

Add Programmer:

Prompts for name, age, role, years of experience, and programming languages.
Example input: Alice, 30, Software Engineer, 5, Python, Java
Delete Programmer:

Prompts for the name of the programmer to delete.
Update Programmer:

Prompts for the name of the programmer and details to update (age, role, years of experience, programming languages).
View Programmer:

Prompts for the name of the programmer and displays their details.
View All Programmers:

Displays information about all stored programmers.
Exit:

Exits the program.
Example
Here is an example of how the command-line interaction might look:
Programmer Management System
1. Add Programmer
2. Delete Programmer
3. Update Programmer
4. View Programmer
5. View All Programmers
6. Exit
Enter your choice: 1
Enter name: Alice
Enter age: 30
Enter role: Software Engineer
Enter years of experience: 5
Enter programming languages (comma separated): Python, Java

Programmer Alice added successfully.


JSON File Format:
The programmers.json file stores the programmer data in the following format:

json
Copy code
[
    {
        "name": "Alice",
        "age": 30,
        "role": "Software Engineer",
        "years_experience": 5,
        "programming_languages": ["Python", "Java"],
        "company": "Microsoft"
    }
]

Notes:
The JSON file will be created automatically if it does not exist.
Ensure that the programmers.json file is in the same directory as the Python script or provide the correct path in the script.

Contributing:
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

Feel free to adjust the content to better match your project's specifics or add any additional sections that may be relevant.
