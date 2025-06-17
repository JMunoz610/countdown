from datetime import datetime, timezone
import json

BIRTH_DATE = "2003-06-10"
START_DATE = "2025-06-10"
GOAL_DATE = "2033-06-10"

def calculate_stats():
    now = datetime.now(timezone.utc)
    birth_date = datetime.strptime(BIRTH_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    start_date = datetime.strptime(START_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    goal_date = datetime.strptime(GOAL_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    
    # Time until goal
    time_left = goal_date - now
    weeks_left = max(time_left.days // 7, 0)
    days_left = max(time_left.days, 0)
    hours_left = max(int(time_left.total_seconds() // 3600), 0)
    
    # Real age calculation (from birth date)
    total_days_lived = (now - birth_date).days
    real_age = total_days_lived / 365.25
    current_age = int(real_age)
    percent_to_30 = round(min(real_age / 30 * 100, 100), 2)
    
    # Days since start date (for tracking purposes)
    days_since_start = max((now - start_date).days, 0)
    
    return {
        "weeks_left": weeks_left,
        "days_left": days_left, 
        "hours_left": hours_left,
        "birth_date": BIRTH_DATE,
        "start_date": START_DATE,
        "goal_date": GOAL_DATE,
        "current_age": current_age,
        "percent_to_30": percent_to_30,
        "days_since_start": days_since_start,
        "last_updated": now.isoformat(),
        "note": "Countdown to 30th birthday!"
    }

def main():
    data = calculate_stats()
    with open("countdown.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Updated countdown.json - {data['days_left']} days left until 30th birthday!")

if __name__ == "__main__":
    main()
