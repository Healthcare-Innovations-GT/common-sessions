patients = ['Olivia', 'Emma', 'Liam', 'Charlottle', 'Noah', 'Oliver', 'Elijah', 'Sophia', 'William'] # https://www.ssa.gov/oact/babynames/
ages_in_months = [4, 8, 24, 12, 3, 1, 9, 30, 10, 3]
adult_dosage = 500 # Assume this is the adult dosage of medication

# Write a program that find the optimum amount of medicine to be administered
# to each patient in 'patients' in accordance with Fried's rule (cited: https://www.austincc.edu/rxsucces/ped5.html)

# Step 1: Write a loop that goes from 0 to the length of the array (accessed as "len(patients)") 

# Step 2: Inside the loop, calculate the patient's dosage in a variable, child_dosage,
# calculated as in the link above

# Step 3: Print each patient's dosage in the form - "<patient_name>'s dosage is <child_dosage>"