import datetime

#########################################################################################
# initialization
birthday = input("please enter you birthday in the format DD/MM/YYYY")
# split day month and year into array of size 3 (0 = day , 1 = month , 3 = year)
str = birthday.split('/')
# get current date from laptop
now = datetime.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
# turning birth info into integer
birth_info = [0, 0, 0]
for x in range(3):
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

if current_day < birth_info[0]:
    out_day = (birth_info[0] + monthTOday(birth_info[1]))
    birth_info[1] = birth_info[1] - 1
    out_day = birth_info[0] - current_day
else:
    out_day = current_day - birth_info[0]

if current_month < birth_info[1]:
    out_day = (birth_info[1] + 12)
    birth_info[2] = birth_info[2] - 1
    out_month = birth_info[1] - current_month
else:
    out_month = current_month - birth_info[1]

out_year = current_year - birth_info[2]
#####################################################################################################
print(out_year, " years old,", out_month, " months old,", out_day, " days old,")
