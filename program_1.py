rainfall = []

for month in range(1, 13):
    amount = float(input(f"Enter the total rainfall for month {month}: "))
    rainfall.append(amount)

total_rainfall = sum(rainfall)

average_rainfall = total_rainfall / 12

max_rainfall = max(rainfall)
max_month = rainfall.index(max_rainfall) + 1

min_rainfall = min(rainfall)
min_month = rainfall.index(min_rainfall) + 1

print(f"\nTotal rainfall for the year: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print(f"Month with the highest rainfall: Month {max_month} ({max_rainfall:.2f} inches)")
print(f"Month with the lowest rainfall: Month {min_month} ({min_rainfall:.2f} inches)")
