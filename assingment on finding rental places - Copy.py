def get_hourly_rate(hour):
    if 0 <= hour < 7 or 21 <= hour < 24:
        return 0
    elif 7 <= hour < 10 or 19 <= hour < 21:
        return 1000
    elif 10 <= hour < 19:
        return 1500
    else:
        return 0  

def calculate_rental_cost(start, end):
    total_cost = 0
    for hour in range(start, end):
        total_cost += get_hourly_rate(hour)
    return total_cost

def main():
    start = int(input("Enter the starting time (0-24): "))
    end = int(input("Enter the ending time (0-24): "))


    if start < 0 or start > 24 or end < 0 or end > 24 or start >= end:
        print("Invalid input.")
        return
    total_cost = calculate_rental_cost(start, end)
    print(f"The total amount to be paid by the renter is RWF {total_cost}")

main()
