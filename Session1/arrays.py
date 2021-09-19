semesters = ['Fall', 'Spring']

# Add values
semesters.append('Summer')
semesters.append('Spring')
print(semesters) # ['Fall', 'Spring', 'Summer', 'Spring']

# Remove values
semesters.remove('Spring')
print(semesters) # ['Fall', 'Summer', 'Spring']

# Access any value using it's index
first_item_in_list = semesters[0]
print(first_item_in_list) # Fall