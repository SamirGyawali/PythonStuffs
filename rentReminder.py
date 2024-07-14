import nepali_datetime
import time
from datetime import datetime, timedelta
import schedule

RENT_DUE_DAY_BS = 1;
def remind_to_pay_rent():
    print("Reminder: Rent pay day!")

# remaining days
def calculate_days_until_due():
    today = nepali_datetime.date.today()
    ## if you already paid for the rent for this month, then set next due day for next month
    if today.day > RENT_DUE_DAY_BS:
        if today.month == 12:
            next_due_date_bs = nepali_datetime.date(today.year+1, 1, RENT_DUE_DAY_BS)
        else:
            next_due_date_bs = nepali_datetime.date(today.year, today.month+1, RENT_DUE_DAY_BS)

    ## convert nepali date into AD, because schedule library works with AD
    next_due_date_ad = next_due_date_bs.to_datetime_date()
    today_ad = datetime.today()

    return (next_due_date_ad - today_ad).days

def schedule_reminder():
    days_until_due = calculate_days_until_due()
    if days_until_due <= 3:
        schedule.every().day.at("20:00").do(remind_to_pay_rent())
    elif days_until_due > 5:
        interval = days_until_due // 2
        schedule.every(interval).days.at("20:00").do(remind_to_pay_rent())
    else:
        schedule.every(3).days.at("20:00").do(remind_to_pay_rent())

# initial scheduling on the 1st of each nepali month
def initial_schedule():
    today = nepali_datetime.date.today()
    if today.day == 1:
        schedule_reminder()
        ## recalculate and reschedule daily
        schedule.every().day.at("9:00").do(schedule_reminder())

initial_schedule()
def main():
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()