import datetime

#########################################################################################
# initialization
birthday = input("please enter you birthday in the format mm:hh:DD:MM:YYYY")
# split day month and year into array of size 3 (0 = day , 1 = month , 3 = year)
str = birthday.split(':')
# get current date from laptop
now = datetime.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
# turning birth info into integer
birth_info = [0, 0, 0, 0, 0]
for x in range(5):
    birth_info[x] = int(str[x])


##########################################################################################
# function to find month and subsequent day
def monthTOday(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


###########################################################################################
# calculation

# min
if current_minute < birth_info[0]:
    temp = birth_info[0] + 60
    birth_info[1] = birth_info[1] - 1
    out_min = temp - birth_info[0]
else:
    out_min = current_minute - birth_info[0]

# hour
if current_hour < birth_info[1]:
    temp = birth_info[1] + 24
    birth_info[2] = birth_info[2] - 1
    out_hr = temp - birth_info[1]
else:
    out_hr = current_hour - birth_info[1]

# day
if current_day < birth_info[2]:
    temp = (birth_info[2] + monthTOday(birth_info[3]))
    birth_info[3] = birth_info[3] - 1
    out_day = temp - birth_info[2]
else:
    out_day = current_day - birth_info[3]

# month
if current_month < birth_info[3]:
    temp = (birth_info[3] + 12)
    birth_info[4] = birth_info[4] - 1
    out_month = temp - birth_info[3]
else:
    out_month = current_month - birth_info[3]

# year
out_year = current_year - birth_info[4]

####################################################################################################
print(out_year, " years old,", out_month, " months old,", out_day, " days old,", out_hr, "hours old, ", out_min,
      "minutes old, ")

