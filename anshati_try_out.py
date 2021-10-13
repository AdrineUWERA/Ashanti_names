# Ask user for their birth date
# Ask user for their gender
# Determine the day of the week the were born
# User the gender to figure out their name
# print their name in 'Twi' language

# Ask user for their birth date
# birth_year = int(input('Enter your birth year: '))
# birth_month = input("Enter your birth month in words: ")
# birth_day = int(input('Enter your birth day: '))
birth_date = input('Enter your date of birth (DD/MM/YY): ')
birth_year = int(input('Enter your birth year: '))

dd = birth_date.split('/')

# Ask user for their gender
gender = input('Enter your gender(F/M): ')

# Day of the month
birth_day = int(dd[0])

# year code
year_code = (int(dd[2]) + (int(dd[2]) // 4)) % 7

# month code
month_code = 0

if dd[1] == '01' or dd[1] == '10':
    month_code = 0
elif dd[1] == '02' or dd[1] == '03' or dd[1] == '11':
    month_code = 3
elif dd[1] == '04' or dd[1] == '07':
    month_code = 6
elif dd[1] == '05':
    month_code = 1
elif dd[1] == '06':
    month_code = 4
elif dd[1] == '08':
    month_code = 2
elif dd[1] == '09' or dd[1] == '12':
    month_code = 5

# century code
century_code = 0
# gregorian dates (>1700)
if (1700 <= birth_year < 1800) or (2100 <= birth_year < 2200):
    century_code = 4
elif (1800 <= birth_year < 1900) or (2200 <= birth_year < 2300):
    century_code = 2
elif (1900 <= birth_year < 2000) or (2300 <= birth_year < 2400):
    century_code= 0
elif 2000 <= birth_year < 2100:
    century_code= 6

# julian dates (<1700)
if 1000 <= birth_year < 1700:
    birth_year = str(birth_year)
    century_number = birth_year[0:2]    # take the first two digits of the year
    century_code = (18 - int(century_number)) % 7
elif birth_year < 1000:
    birth_year = str(birth_year)
    century_number = birth_year[0]  # take the first digit of the year
    century_code = (18 - int(century_number)) % 7

# leap year code
leap_year_code = 0

if 1700 <= birth_year < 2100: # if it is a Gregorian date
    if birth_year % 400 == 0 or (birth_year % 4 == 0 and birth_year % 100 != 0):  # if it is a leap year
        if birth_date[1] or birth_date[2]:
            leap_year_code = 0
        else:
            leap_year_code = 1

elif birth_year < 1000:
    if birth_year % 4 == 0:
        leap_year_code = 0
    else:
        leap_year_code = 1

# Determine the day of the week they were born
day_code = (year_code + month_code + century_code + birth_day - leap_year_code) % 7

# 0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"

ashanti_fnames = ["Akosua", "Adjoa", "Abenaa", "Akua", "Yaa", "Afia", "Amma"]

ashanti_mnames = ["Kwasi", "Kodjo", "Kwabena", "Kwaku", "Yaw", "Kofi", "Kwame"]

if gender == "F":
    print("Your name in the Ashanti tribe is " + ashanti_fnames[day_code])
elif gender == "M":
    print("Your name in the Ashanti tribe is " + ashanti_mnames[day_code])