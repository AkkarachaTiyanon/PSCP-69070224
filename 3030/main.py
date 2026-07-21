"""math"""
import math

def main():
    """yes"""
    req_pushups = int(input())
    req_situps = int(input())
    req_squats = int(input())
    req_run = int(input())

    day_pushups = int(input())
    day_situps = int(input())
    day_run = int(input())
    day_squats = int(input())

    days_pushups = math.ceil(req_pushups / day_pushups)
    days_situps = math.ceil(req_situps / day_situps)
    days_squats = math.ceil(req_squats / day_squats)
    days_run = math.ceil(req_run / day_run)

    min_total_days = max(days_pushups, days_situps, days_squats, days_run)

    print(min_total_days)

main()
