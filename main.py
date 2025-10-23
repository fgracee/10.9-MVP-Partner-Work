import csv
import os

def file_create(name):
    file_exists = os.path.exists(name)
    with open(name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['title', 'date', 'start', 'end', 'location', 'attendees', 'purpose'])
    return name


def add_appointment(name):
    print("\nPlease enter the appointment details below:")
    title = input("Title: ").strip()
    date = input("Date (e.g., 2025-10-25): ").strip()
    start = input("Start time (e.g., 10:00 AM): ").strip()
    end = input("End time (e.g., 11:00 AM): ").strip()
    location = input("Location: ").strip()
    attendees = input("Attendees (comma-separated): ").strip()
    purpose = input("Purpose: ").strip()

    with open(name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([title, date, start, end, location, attendees, purpose])
    
    print(f"\nAppointment '{title}' added successfully to {name}!\n")


def show_appointments(name):
    try:
        with open(name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("\nThe file exists but there are no appointments yet.")
                return

            header = rows[0]
            print("\nAll Appointments:\n" + "-" * 60)
            print(f"{' | '.join(header)}")
            print("-" * 60)
            for row in rows[1:]:
                print(f"{' | '.join(row)}")
            print("-" * 60)
    except FileNotFoundError:
        print(f"\nFile '{name}' not found.")


# ---- MAIN PROGRAM ----
filename = 'appointments.csv'
file_create(filename)

print("Choose what you'd like to do:")
print("1. View all appointments")
print("2. Add a new appointment")

choice = input("Enter 1 or 2: ").strip()

if choice == '1':
    show_appointments(filename)
elif choice == '2':
    add_appointment(filename)
else:
    print("Invalid choice.")