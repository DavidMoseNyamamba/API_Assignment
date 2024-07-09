#add new patient to a list
#add_patient function prompts the user for the patient's name, age, and illness. 
def add_patient(patients):
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    illness = input("Enter patient illness: ")
 #create a dictionary to represent the patient and adds it to the patients list.
    patient = {
        "name": name,
        "age": age,
        "illness": illness
    }
    patients.append(patient)
    print(f"Patient {name} added successfully.") 

# display all patients
#The display_patients function iterates through the patients list
def display_patients(patients):
    if not patients:
        print("No patients found.")
    else:
        for patient in patients:
#print the details of each patient.
            print(f"Name: {patient['name']},Age: {patient['age']},Illness: {patient['illness']}")    


#Define a function to search for a patient by name and display their details if found.
#The search_patient function to prompt the user for the patient's name
#searches through the patients list to find and display the details of the patient if found.

def search_patient(patients):
    name = input("Enter patient name to search: ")
    found = False
    for patient in patients:
        # lower case name of patients
        if patient['name'].lower() == name.lower():
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            found = True
            break
    if not found:
        print(f"Patient {name} not found.")

#Define a function to remove a patient by name
#The remove_patient function to prompt the user for the patient's name
def remove_patient(patients):
    name = input("Enter patient name to remove: ")
    
 #search through the patients list to find and remove the patient if found.
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print(f"Patient {name} not found.")

#Use a while loop to keep the program running until the user chooses to exit
# Demonstrating the functionality
def main():
    patients = []
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
