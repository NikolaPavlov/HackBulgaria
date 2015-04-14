import calendar


FRIDAY_INDEX = 4
def friday_years(start, end):
    count_friday_years = 0

    for year in range(start, end):
        count_fidays_in_year = 0

        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            for week in month_calendar:
                if week[FRIDAY_INDEX] != 0:
                    count_fidays_in_year += 1

        if count_fidays_in_year == 53:
            count_friday_years += 1

    return count_friday_years

if __name__ == "__main__":
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))