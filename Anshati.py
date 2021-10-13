
# Ask user for their birth date
# Ask user for their gender
# Determine the day of the week the were born
# User the gender to figure out their name
# print their name in 'Twi' language

# Ask user for their birth date
# birth_year = int(input('Enter the lasyour birth year: '))
# birth_month = input("Enter your birth month in words: ")
# birth_day = int(input('Enter your birth day: '))
birth_date = input('Enter your date of birth (DD/MM/YY): ')
birth_year = int(input('Enter your full birth year: '))

dd = birth_date.split('/')

# Ask user for their gender
gender = input('Enter your gender(female/male): ')

# Determine the day of the week the were born
# year code
year = (int(birth_date[2]) + (int(birth_date[2]) // 4)) % 7

# month code
if birth_date[1] == '01' or birth_date[1] == '10':
    month_code = 0
elif birth_date[1] == '02' or birth_date[1] == '03' or birth_date[1] == '11':
    month_code = 3
elif birth_date[1] == '04' or birth_date[1] == '07':
    month_code = 6
elif birth_date[1] == '05':
    month_code = 1
elif birth_date[1] == '06':
    month_code = 4
elif birth_date[1] == '08':
    month_code = 2
elif birth_date[1] == '09' or birth_date[1] == '12':
    month_code = 5

# century code
if (birth_year>=1700 and birth_year<1800) or (birth_year>=2100 and birth_year<2200):
    century_code = 4
elif (birth_year>=1800 and birth_year<1900) or (birth_year>=2200 and birth_year<2300):
    century_code = 2
elif (birth_year>=1900 and birth_year<2000) or (birth_year>=2300 and birth_year<2400):
    century_code= 0
elif birth_year>=2000 and birth_year<2100:
    century_code= 6

