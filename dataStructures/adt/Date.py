from math import floor
class Date:
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _DAYS_NAME = [ 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    _MONTHS_NAME = ['NO NAME', 'JANUARY', 'FEBUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 
                    'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    # Creates Date object instance
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian( month, day, year ), "Invalid Gregorian date"
        tmp = 0
        if month < 3 :
            tmp = -1
        # self._julianDay = day + floor((153*m + 2)/5) + 365*y + floor(y/4) - floor(y/100) + floor(y/400) - 32045
        self._julianDay = (1461 * (year + 4800 + tmp))//4 + (367 * (month - 2 - 12 * (tmp)) // 12) - (3 * ((year + 4900 + tmp)//100))//4 + day - 32075
        print(self._julianDay)           
    # Extract month from the GC Date component of format M D Y format
    def extractMonth( self ) :
        return (self._toGregorian())[0]
    
    def extractDay( self ) :
        return (self._toGregorian())[1]
    
    def extractYear( self ) :
        return (self._toGregorian())[2]
    
    # Returns day of the week as an integer bewteen 0 to 6
    def dayOfWeek( self ) :
        month, day, year = self._toGregorian()
        if month < 3 : 
            month = month + 12
            year = year - 1
        
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400 ) % 7
    # Returns month name 
    def monthName( self ) :
        return self._MONTHS_NAME[self.extractMonth()]

    # Returns name of the day 
    def dayOfWeekName( self ) :
        return self._DAYS_NAME[self.dayOfWeek()]
    
    # Returns Julian day of the given year 
    def dayOfTheYear( self ) :
        month = self.extractMonth()
        day = self.extractDay()
        year = self.extractYear()
        days = 0
        if month == 1 :
            return day
        if (self._is_leap( year ) & (month > 2)):
            days += 1
        for i in range(1, month ) :
            days += self._DAYS_IN_MONTH[i] 
        days = days + day
        return days
    
    # Returns number of days 
    def numDays( self ) :
        pass

    # Advances date by given days 
    def advanceBy( self ) : 
        pass 

    #  Checks if the day is a weekday 
    def isWeekDay( self ) :
        return (self.dayOfWeek() < 5)

    # Checks if the date is equinox of spring/autumn
    def isEquinox( self ) :
        pass

    # Checks if the date is solstice 
    def isSolstice( self ) :
        pass
    def formatDate( self, date, divChar = '/') :
        pass

    # Returns the date as a string in Gregorian Format
    def __str__( self ) :
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)
    
    #Date comparator operations
    def __eq__( self, otherDate ) :
        return self._julianDay == otherDate._julianDay
    
    def __lt__( self, otherDate ) :
        return self._julianDay < otherDate._julianDay
    
    def __gt__( self, otherDate ) : 
        return self._julianDay > otherDate._julianDay
    
    # Validates whether the give year is a boolean or not 
    def _is_leap( self, year ) :
        "year -> 1 if leap year, else 0."
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    #validates the month
    def _is_validMonth( self, month ) :
        return 1 <= month <= 12
    
    #Validates the year 
    def _is_validYear( self, year ) :
        return 0 <= year <= 9999
    
    #Validate the days
    def _is_validDay( self, month, day, year ) :
        _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ( self._is_leap( year ) & (month == 2) & 0 <= day <= 29) :
            return True
        elif ( 0 <= day <=_DAYS_IN_MONTH[month] ) :
            return True
        else:
            return False
    # validates the Gregorian date 
    def _isValidGregorian( self, month, day, year ) :
        return self._is_validMonth( month ) & self._is_validYear( year ) & self._is_validDay( month, day, year)

    # Returns the Gregorian date as a tuple: (month, day, year)
    def _toGregorian( self ):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year
        
firstDay = Date( 11, 2, 2019 )
print( firstDay )
print(firstDay.isWeekDay())
print( firstDay.monthName() )
print( firstDay.dayOfWeekName() )
firstDay = Date( 12, 31, 2016 )
print(firstDay.dayOfTheYear())
print(firstDay.isWeekDay())
# 2,458,789.5