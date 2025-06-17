from datetime import datetime
import json

END_DATE = "2025-12-31"

def calculate_weeks_left():
    end_date = datetime.strptime(END_DATE, "%Y-%m-%d")
    today = datetime.utcnow()
    delta = end_date - today
    weeks_left = max(delta.days // 7, 0)
    return weeks_left

def main():
    weeks_left = calculate_weeks_left()
    data = {
        "weeks_left": weeks_left,
        "end_date": END_DATE,
        "note": "Automatically updated countdown"
    }

    with open("countdown.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
