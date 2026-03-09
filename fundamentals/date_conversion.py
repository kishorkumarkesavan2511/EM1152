from datetime import datetime
# Get the employee's date of birth from the user
dob_input = input("Enter the employee's date of birth (YYYY-MM-DD): ")

# Convert the input string to a date object
dob = datetime.strptime(dob_input, '%Y-%m-%d')

# Get today's date
today = datetime.today()

# Calculate the difference in total days
total_days = (today - dob).days

# Calculate years, months, and days
yr = total_days // 365  # years
rda = total_days % 365   #remaining days
mo = rda // 30  # months
da = rda % 30  # days
# Print the age in years, months, and days
print(f"Age: {yr} years, {mo} months, {da} days")