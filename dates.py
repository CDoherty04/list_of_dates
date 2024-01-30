MONTH_30 = ["04", "06", "09", "11"]
MONTH_31 = ["01", "03", "05", "07", "08", "10", "12"]


class Date:
    """A date class that represents certain days in 00/00/0000 form"""

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        if int(year) % 4 == 0:
            self.leapyear = True
        else:
            self.leapyear = False

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def add_day(self):
        """Adds a day to the date object"""
        # End of year case
        if self.month == "12" and self.day == "31":
            self.day = "01"
            self.month = "01"
            self.year = "01"

        # Other end of month cases
        if self.month in MONTH_30 and self.day == "30":
            self.day = "01"
            if self.month[0] == "0" and self.month != "09":
                self.month = "0" + str(int(self.month)+1)
            else:
                self.month = str(int(self.month)+1)

        elif self.month in MONTH_31 and self.day == "31":
            self.day = "01"
            if self.month[0] == "0" and self.month != "09":
                self.month = "0" + str(int(self.month)+1)
            else:
                self.month = str(int(self.month)+1)

        # Leap year Case
        elif self.month == "02" and self.leapyear and self.day == "29":
            self.day = "01"
            self.month = "03"

        # Non Leap Year Case
        elif self.month == "02" and not self.leapyear and self.day == "28":
            self.day = "01"
            self.month = "03"

        # Normal day change case
        else:
            if self.day[0] == "0" and self.day != "09":
                self.day = "0" + str(int(self.day) + 1)
            else:
                self.day = str(int(self.day) + 1)

    def __le__(self, other):
        """Less than or equal to comparison for dates in sequential order"""
        if self.year == other.year:
            if self.month == other.month:
                if self.day <= other.day:
                    return True
                else:
                    return False
            elif self.month <= other.month:
                return True
            else:
                return False
        elif self.year <= other.year:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"


def date_counter(start_date, end_date):  # MAY NOT WORK IF DATES ARE IN DIFFERENT YEARS BECAUSE OF LEAP
    """Returns the number of days between the start and end date, not counting the end date"""

    days = 0
    current_date = start_date

    while current_date < end_date:
        days += 1
        current_date.add_day()

    return days
