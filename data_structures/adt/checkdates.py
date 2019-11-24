# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years of age.

from datetime import datetime, date, time, timezone

def main():
    # Date before which the person should have born
    bornBefore = date(1988, 7, 4)
    birthDate = promptAndExtractDate()
    while birthDate is not None:
        if birthDate <= bornBefore:
            print("Is at least 21 years of age: ", birthDate)
        birthDate = promptAndExtractDate()

# Prompts for and Extracts the date components. Returns a
# Date object or None when the user has finished entering dates.


def promptAndExtractDate():
    print("Enter Birth Date")
    month = int(input("Month (0 to quit):"))

    if month == 0:
        return None
    else:
        day = int(input("Day:"))
        year = int(input("Year:"))
        return date(year, month, day)


main()
