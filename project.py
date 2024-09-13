"""
Programmer Manager App

"""

import json

class Programmer:
    def __init__(self, name, age, role, years_experience, programming_languages):
        self.name = name
        self.age = age
        self.role = role
        self.years_experience = years_experience
        self.programming_languages = programming_languages
        self.company = "Microsoft"  # This is set internally

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "role": self.role,
            "years_experience": self.years_experience,
            "programming_languages": self.programming_languages,
            "company": self.company  # Include company in the dictionary
        }

    def get_info(self):
        return f"""
# Name: {self.name}
# Age: {self.age}
# Role: {self.role}
# Company: {self.company}
# Years of Experience: {self.years_experience}
# Programming Languages: {self.programming_languages}
"""

class ProgrammerManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.programmers = self.load_programmers()

    def load_programmers(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                # Create Programmer instances, ignoring 'company' in the data
                return {item['name']: Programmer(
                    name=item['name'],
                    age=item['age'],
                    role=item['role'],
                    years_experience=item['years_experience'],
                    programming_languages=item['programming_languages']
                ) for item in data}
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_programmers(self):
        with open(self.file_path, 'w') as file:
            json.dump([prog.to_dict() for prog in self.programmers.values()], file, indent=4)

    def add_programmer(self, name, age, role, years_experience, programming_languages):
        if name in self.programmers:
            print(f"Programmer with name {name} already exists.")
            return
        self.programmers[name] = Programmer(name, age, role, years_experience, programming_languages)
        self.save_programmers()

    def delete_programmer(self, name):
        if name in self.programmers:
            del self.programmers[name]
            self.save_programmers()
            print(f"Programmer {name} deleted.")
        else:
            print(f"Programmer with name {name} does not exist.")

    def update_programmer(self, name, age=None, role=None, years_experience=None, programming_languages=None):
        if name in self.programmers:
            prog = self.programmers[name]
            if age is not None:
                prog.age = age
            if role is not None:
                prog.role = role
            if years_experience is not None:
                prog.years_experience = years_experience
            if programming_languages is not None:
                prog.programming_languages = programming_languages
            self.save_programmers()
            print(f"Programmer {name} updated.")
        else:
            print(f"Programmer with name {name} does not exist.")

    def view_programmer(self, name):
        if name in self.programmers:
            prog = self.programmers[name]
            return prog.get_info()
        else:
            print(f"Programmer with name {name} does not exist.")
            return None

    def view_all_programmers(self):
        return {name: prog.get_info() for name, prog in self.programmers.items()}

# Example usage
if __name__ == "__main__":
    manager = ProgrammerManager('programmers.json')

    while True:
        print("\nProgrammer Management System")
        print("1. Add Programmer")
        print("2. Delete Programmer")
        print("3. Update Programmer")
        print("4. View Programmer")
        print("5. View All Programmers")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            role = input("Enter role: ")
            years_experience = int(input("Enter years of experience: "))
            programming_languages = input("Enter programming languages (comma separated): ").split(',')
            manager.add_programmer(name, age, role, years_experience, [lang.strip() for lang in programming_languages])

        elif choice == '2':
            name = input("Enter name to delete: ")
            manager.delete_programmer(name)

        elif choice == '3':
            name = input("Enter name to update: ")
            age = input("Enter new age (leave blank to skip): ")
            role = input("Enter new role (leave blank to skip): ")
            years_experience = input("Enter new years of experience (leave blank to skip): ")
            programming_languages = input("Enter new programming languages (comma separated, leave blank to skip): ")
            manager.update_programmer(
                name,
                age=int(age) if age else None,
                role=role if role else None,
                years_experience=int(years_experience) if years_experience else None,
                programming_languages=[lang.strip() for lang in programming_languages.split(',')] if programming_languages else None
            )

        elif choice == '4':
            name = input("Enter name to view: ")
            info = manager.view_programmer(name)
            if info:
                print(info)

        elif choice == '5':
            all_programmers = manager.view_all_programmers()
            for name, info in all_programmers.items():
                print(info)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

