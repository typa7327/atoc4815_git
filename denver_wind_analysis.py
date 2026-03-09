"""
Denver January 2025 Wind Analysis
ATOC 4815/5815 - Git Practice Exercise 2

Instructions:
    1. Complete the TODO sections
    2. Run the script to check your work
    3. Use git to save your changes!
"""


def load_wind_data(filepath):
    """Load wind data from CSV file.

    Returns list of dictionaries with date, avg_wind_mph, max_gust_mph, direction.
    """
    data = []
    with open(filepath, "r") as f:
        header = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            row = {
                "date": values[0],
                "avg_wind_mph": float(values[1]),
                "max_gust_mph": float(values[2]),
                "direction": values[3],
            }
            data.append(row)
    return data


def average_wind_speed(data):
    """Calculate the average daily wind speed for January.

    Args:
        data: list of dictionaries from load_wind_data()

    Returns:
        Average wind speed in mph, or None if not implemented.
    """
    # TODO: Calculate the average of avg_wind_mph across all days
    # Hint: sum up all the avg_wind_mph values and divide by the number of days
    total = 0
    for day in data:
        total += day["avg_wind_mph"]

    result = total / len(data)
    return result


def count_advisory_days(data, threshold=25.0):
    """Count days where average wind speed exceeds the advisory threshold.

    A Wind Advisory is typically issued when sustained winds reach 25+ mph.

    Args:
        data: list of dictionaries from load_wind_data()
        threshold: wind speed threshold in mph (default 25.0)

    Returns:
        Number of days with avg_wind_mph above threshold, or None if not implemented.
    """
    # TODO: Count how many days had avg_wind_mph greater than threshold
    # Hint: loop through data and count days where avg_wind_mph > threshold
    count = 0
    for day in data:
        if day["avg_wind_mph"] > threshold:
            count += 1

    result = count
    return result


def windiest_day(data):
    """Find the date with the highest maximum gust.

    Args:
        data: list of dictionaries from load_wind_data()

    Returns:
        Tuple of (date_string, max_gust_mph), or None if not implemented.
    """
    # TODO: Find the day with the highest max_gust_mph
    # Hint: loop through data, track the highest max_gust_mph and its date
    result = None
    return result


# ---- Run the analysis ----
if __name__ == "__main__":
    print("=" * 50)
    print("Denver January 2025 Wind Analysis")
    print("=" * 50)
    print()

    data = load_wind_data("data/denver_wind_jan2025.csv")
    print(f"Loaded {len(data)} days of wind data")
    print()

    avg = average_wind_speed(data)
    if avg is not None:
        print(f"Average daily wind speed: {avg:.1f} mph")
    else:
        print("Average wind speed: not yet implemented (complete the TODO!)")

    count = count_advisory_days(data)
    if count is not None:
        print(f"Wind advisory days (>25 mph): {count}")
    else:
        print("Advisory day count: not yet implemented (complete the TODO!)")

    windy = windiest_day(data)
    if windy is not None:
        date, gust = windy
        print(f"Windiest day: {date} with {gust:.1f} mph gust")
    else:
        print("Windiest day: not yet implemented (complete the TODO!)")

    print()
    print("Done! Now use git to save your work:")
    print("  git status")
    print("  git add denver_wind_analysis.py")
    print('  git commit -m "Complete denver wind analysis"')
    print("  git push")
