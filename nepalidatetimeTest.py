import nepali_datetime
import datetime

RENT_DUE_DAY_BS = 1
today = nepali_datetime.date.today()
print(f"today = {today}")


def calculate_days_until_due():
    today = nepali_datetime.date.today()
    ## if you already paid for the rent for this month, then set next due day for next month
    if today.day > RENT_DUE_DAY_BS:
        if today.month == 12:
            next_due_date_bs = nepali_datetime.date(today.year + 1, 1, RENT_DUE_DAY_BS)
        else:
            next_due_date_bs = nepali_datetime.date(today.year, today.month+1, RENT_DUE_DAY_BS)

    ## convert nepali date into AD, because schedule library works with AD
    next_due_date_ad = next_due_date_bs.to_datetime_date()
    today_ad = datetime.date.today()

    return (next_due_date_ad - today_ad).days

days_until_due = calculate_days_until_due()
print(f"days remaining = {days_until_due}")