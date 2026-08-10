# Disk Usage Calculator Function

# Problem : Create a reusable function that calculates:
# - Free Disk Space
# - Disk Usage Percentage

# The function should return both values.


def disk_usage(total,used):
    free = total - used
    percentage = (used / total) * 100

    return free,percentage

total = float(input("Enter Total Disk (GB): "))
used = float(input("Enter Used Disk (GB): "))

free, percentage = disk_usage(total, used)

print("\n===== Disk Report =====")
print("Free Disk:", free, "GB")
print("Usage: ", round(percentage, 2), "%")