# Get the input from the user
minutes = int(input("Enter the period in minutes: "))

# Calculate days, hours, and remainder
days = minutes // (24 * 60)
hours = (minutes % (24 * 60)) // 60
remainder = minutes % 60

# printout results 
print(f"{days} days:{hours} hours:{remainder} minutes")
