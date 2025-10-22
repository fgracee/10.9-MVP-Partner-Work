# An appointment is a dictionary with keys such as start time, end time, location, attendees, meeting purpose, title. 
# Values for start and end time are hours and minutes. Location has values of a specific building, room number, address. 
# Attendees values are names of people who will be at the appointment. 
# Meeting purpose is the reason for attendance
# Title is what the entire dictionary is assigned to.
import datetime

def make_appt(my_dictionary):
    """
    Using my_dictionary add a dictionary representing an appointment. Add to this new dictionary a dictionary of an appointment with arguments 
    Args:
        date: the day, month, and year the appointment takes place- expected as MM/DD/YYYY
        start: the beginning time of apointment in hours and minutes, expected as HH:MM on 24 hour cycle
        end: the end time of the appointment in hours and minutes, expected as HH:MM on 24 hour cycle
        location (string): the address, building, and room number where the appointment will be.
        purpose (string): a short summary of the appointment.
        attendees (list): names of people who will be going to the meeting separated by commas
       Returns:
        dict: appointment with keys: 'date', 'start', 'end', 'location', 'attendees', 'purpose'
        For all arguements in this function, prompt the user with "What is this appoitments [arguement]?" and use the response as the value.
    """
    appointment = {}
    
    appointment['date'] = input("What is this appointment's date? ")
    
    appointment['start'] = input("What is this appointment's start time? ")
    
    appointment['end'] = input("What is this appointment's end time? ")
    
    appointment['location'] = input("What is this appointment's location? ")
    
    attendees_input = input("Who are the attendees for this appointment (separate names by commas)? ")
    appointment['attendees'] = [name.strip() for name in attendees_input.split(',')]
    
    appointment['purpose'] = input("What is this appointment's purpose? ")
    
    title = input("What is this appointment's title? ")
    
    # Save the appointment globally
    my_dictionary[title] = appointment
    
    return appointment



def print_appt(dictionary, title):
    """
    Call make_appt function and return appointment information for appointment that matches title in the given dictionary;
    Args:
        dictionary: the name of an appointment dictionary
        title: the key of dictionary which we want to print
    """
    appointment = dictionary.get(title)
    if appointment:
        print(f"Appointment Title: {title}")
        print(f"Date: {appointment['date']}")
        print(f"Start Time: {appointment['start']}")
        print(f"End Time: {appointment['end']}")
        print(f"Location: {appointment['location']}")
        print(f"Attendees: {', '.join(appointment['attendees'])}")
        print(f"Purpose: {appointment['purpose']}")
    else:
        print(f"No appointment found with title: {title}")



def main():
    my_dict = {}
    make_appt(my_dict)
    print(my_dict["Class"])
    print_appt(my_dict, "Class")





if __name__ == "__main__":
    main()