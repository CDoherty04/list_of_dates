import dates
import os

if not os.path.exists("dates.txt"):
    f = open("dates.txt", "w")
    f.close()

start_date = dates.Date("02", "04", "2024")
end_date = dates.Date("02", "10", "2024")

with open("dates.txt", "w") as file:
    while start_date <= end_date:
        file.write(str(start_date) + "\n")
        start_date.add_day()
