"""
An appointment is a dictionary with the following keys:
    title: a string, a name for the appointment
    start: a time, whem the appointment starts
    end: a time, when the appointment ends
    date: a day, when the appointment happens
    attendees: a list of strings, people going to the appointment
    summary: a string, a brief description of the appointment
"""

import csv
import os
import datetime

# Create a file to store appointments
def file_create(name):
    """Creates a CSV file with predefined headers if it doesn't already exist.

    If the specified file does not exist, this function creates it and writes
    a header row with the columns: title, date, start, end, location, attendees, and purpose.
    If the file already exists, it remains unchanged.

    Args:
        name (string): the name of the CSV file I want to create

    Returns:
        A string with the name of my CSV file I have created
    """
    file_exists = os.path.exists(name)
    with open(name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['title', 'date', 'start', 'end', 'location', 'attendees', 'purpose'])
    return name


# Create a new appointment dictionary
def add_appointment(name):
    """    Prompts the user for appointment details and adds them to a CSV file.

    This function collects appointment information from the user via input prompts
    and appends the details as a new row in the specified CSV file. Each appointment
    entry includes title, date, start time, end time, location, attendees, and purpose.

    Args:
        name (string): The name or path of the CSV file where the appointment will be added.

    Returns:
        None
    """
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

# Display all existing appointments
def show_appointments(name):
    """  Displays all appointments stored in a CSV file.

    This function reads the specified CSV file and prints all appointment
    records in a formatted table. If the file does not exist, a message is displayed.
    If the file exists but contains no appointments (only the header row),
    the user is informed accordingly.

    Args:
        name (str): The name or path of the CSV file to read.

    Returns:
        None
    """
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

# Filter meetings by attendees
def by_att(name, attendees):
    """
    This function reads the appointments from the specified CSV file and filters them by the given attendee.
    The attendee is expected to be a string that may match any of the attendees in the appointments.
    If it does not match, return 'No appointments with [attendee]'
    Args:
        name (str): The name or path of the CSV file to read.
        attendees (str): The attendee to filter appointments by.
    Returns:
        A list of appointments (as dictionaries) that include the specified attendee.
    """
    filtered_appointments = []
    try:
        with open(name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                attendee_list = [att.strip() for att in row['attendees'].split(',')]
                if attendees in attendee_list:
                    filtered_appointments.append(row)
    except FileNotFoundError:
        print(f"\nFile '{name}' not found.")
    
    if not filtered_appointments:
        return f"No appointments with {attendees}"
    
    return filtered_appointments

# Filter meetings by date
def by_date(filename, date):
    """
    This function reads the appointments from the specified CSV file and filters them by a given date.
    Args:
        filename (str): The name or path of the CSV file to read.
        date (str): The date to filter appointments by (format: 'YYYY-MM-DD').
    Returns:
        A list of appointments (as dictionaries) that occur on the specified date.
        If there are none, return "No appointments on that day"
    """
    filtered_appointments = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['date'] == date:
                    filtered_appointments.append(row)
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found.")
    if not filtered_appointments:
        return "No appointments on that day"

# File for saving appointments
filename = 'appointments.csv'
file_create(filename)

def main():
    """
    Main function to run the appointment management system.
    This function provides a command-line interface for users to manage appointments.
    Users can view all appointments, add new appointments, filter by attendees, filter by date, and exit the program in a listed menu.
    If user selects filter by attendees, prompt for attendee to search by. If there is no match, return "3
    
    """
    while True:
        print("\nAppointment Management System")
        print("1. View all appointments")
        print("2. Add a new appointment")
        print("3. View by attendees")
        print("4. View by date")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            show_appointments(filename)
        elif choice == '2':
            add_appointment(filename)
        elif choice == '3':
            attendee = input("Enter the attendee's name to filter by: ").strip()
            result = by_att(filename, attendee)
            if isinstance(result, str):
                print(result)
            else:
                print(f"\nAppointments with {attendee}:\n" + "-" * 60)
                for app in result:
                    print(f"Title: {app['title']}, Date: {app['date']}, Start: {app['start']}, End: {app['end']}, Location: {app['location']}, Attendees: {app['attendees']}, Purpose: {app['purpose']}")
                print("-" * 60)
        elif choice == '4':
            by_date_input = input("Enter the date to filter by (e.g., 2025-10-25): ").strip()
            result = by_date(filename, by_date_input)
        elif choice == '5':
            print("Exiting the appointment management system.")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()

# Feature ideas (think about lists of dictionaries as a tool. .json files?)
    # Appointments organized by day
    # Appointments organized by attendees
    # Deleting an appointment


