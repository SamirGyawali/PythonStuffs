import time

import nepali_datetime
import subprocess
import datetime
from plyer import notification


RENT_DUE_DAY_BS = 1;

# remaining days
def calculate_days_until_due():
    today = nepali_datetime.date.today()
    ## if you already paid for the rent for this month, then set next due day for next month
    if today.day > RENT_DUE_DAY_BS:
        if today.month == 12:
            next_due_date_bs = nepali_datetime.date(today.year+1, 1, RENT_DUE_DAY_BS)
        else:
            next_due_date_bs = nepali_datetime.date(today.year, today.month+1, RENT_DUE_DAY_BS)

    ## convert nepali date into AD, because subprocess library works with AD
    next_due_date_ad = next_due_date_bs.to_datetime_date()
    today_ad = datetime.date.today()
    days_left = (next_due_date_ad - today_ad).days

    return (days_left)

def remind(days_remianing):
    if days_remianing < 4:
        message = f"Reminder: Pay your rent soon! Only {days_remianing} days left"
        notification.notify(title="Rent reminder", message=message, timeout=0)


days_remaining = calculate_days_until_due()
remind(days_remaining)
