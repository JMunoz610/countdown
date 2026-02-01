from datetime import datetime, timezone
import json

BIRTH_DATE = "2003-06-10"
START_DATE = "2026-01-11"
GOAL_DATE = "2028-01-11"

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
    percent_birth_to_30 = round(min(real_age / 30 * 100, 100), 2)
    
    # Progress from start date to goal date
    days_since_start = max((now - start_date).days, 0)
    total_countdown_days = (goal_date - start_date).days
    percent_start_to_goal = round(min((days_since_start / total_countdown_days) * 100, 100), 2)
    
    return {
        "weeks_left": weeks_left,
        "days_left": days_left, 
        "hours_left": hours_left,
        "birth_date": BIRTH_DATE,
        "start_date": START_DATE,
        "goal_date": GOAL_DATE,
        "current_age": current_age,
        "percent_birth_to_30": percent_birth_to_30,
        "percent_start_to_goal": percent_start_to_goal,
        "days_since_start": days_since_start,
        "last_updated": now.isoformat(),
        "note": "Countdown to 30th birthday!"
    }

def main():
    data = calculate_stats()
    with open("countdown.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Updated countdown.json - {data['days_left']} days left! Progress: {data['percent_birth_to_30']}% life to 30, {data['percent_start_to_goal']}% countdown done")

if __name__ == "__main__":
    main()
