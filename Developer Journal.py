import random
import datetime

class JournalEntry:
    def __init__(self, prompt, response, date):
        self.prompt = prompt
        self.response = response
        self.date = date

class JournalProgram:
    def __init__(self):
        self.entries = []

    def write_entry(self):
        prompts = [
            "Who was the most interesting person I interacted with today?",
            "What was the best part of my day?",
            "How did I see the hand of the Lord in my life today?",
            "What was the strongest emotion I felt today?",
            "If I had one thing I could do over today, what would it be?"
        ]
        prompt = random.choice(prompts)
        response = input(prompt + " ")
        date = datetime.date.today()
        entry = JournalEntry(prompt, response, date)
        self.entries.append(entry)

    def display_journal(self):
        for entry in self.entries:
            print(f"Prompt: {entry.prompt}")
            print(f"Response: {entry.response}")
            print(f"Date: {entry.date}")
            print()

    def save_journal(self):
        filename = input("Enter a filename to save the journal: ")
        with open(filename, "w") as file:
            for entry in self.entries:
                file.write(f"Prompt: {entry.prompt}\n")
                file.write(f"Response: {entry.response}\n")
                file.write(f"Date: {entry.date}\n")
                file.write("\n")

    def load_journal(self):
        filename = input("Enter a filename to load the journal: ")
        self.entries = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                prompt = lines[i].strip().replace("Prompt: ", "")
                response = lines[i+1].strip().replace("Response: ", "")
                date = lines[i+2].strip().replace("Date: ", "")
                entry = JournalEntry(prompt, response, date)
                self.entries.append(entry)

    def run(self):
        while True:
            print("1. Write a new entry")
            print("2. Display the journal")
            print("3. Save the journal")
            print("4. Load the journal")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.write_entry()
            elif choice == "2":
                self.display_journal()
            elif choice == "3":
                self.save_journal()
            elif choice == "4":
                self.load_journal()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the JournalProgram class and run the program
journal_program = JournalProgram()
journal_program.run()