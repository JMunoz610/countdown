from datetime import datetime

# 🎯 Set your birthday and milestone
BIRTH_DATE = "2003-10-15"       # Your actual birth date
MILESTONE_DATE = "2033-10-15"   # Your 30th birthday

def calculate_countdown():
    now = datetime.utcnow()
    birth_date = datetime.strptime(BIRTH_DATE, "%Y-%m-%d")
    milestone_date = datetime.strptime(MILESTONE_DATE, "%Y-%m-%d")

    total_duration = milestone_date - birth_date
    time_remaining = milestone_date - now
    time_passed = now - birth_date

    weeks_left = max(time_remaining.days // 7, 0)
    days_left = max(time_remaining.days, 0)
    hours_left = max(int(time_remaining.total_seconds() // 3600), 0)

    # Age in years (rounded down)
    current_age_years = int(time_passed.days // 365.25)

    # Percentage completed toward 30
    percent_complete = min(round((time_passed.total_seconds() / total_duration.total_seconds()) * 100, 2), 100)

    return {
        "weeks_left": weeks_left,
        "days_left": days_left,
        "hours_left": hours_left,
        "goal_date": MILESTONE_DATE,
        "current_age": current_age_years,
        "percent_to_30": percent_complete,
        "note": "Countdown to 30th birthday!"
    }

def main():
    data = calculate_countdown()
    with open("countdown.json", "w") as f:
        import json
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
