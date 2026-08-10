# Disk Usage Calculator

# Problem

# A server has:
# Total Disk Space
# Used Disk Space

# Take both values from the user and calculate:
# Free Space
# Used Percentage

total_disk = float(input("Enter Total Disk (GB): "))
used_disk = float(input("Enter Used Disk (GB): "))

free_disk = total_disk - used_disk
percentage = (used_disk / total_disk) * 100

print("\n-----Disk Report-----")
print("Total Disk: ", total_disk,"GB")
print("Used Disk: ", used_disk,"GB")
print("Free Disk: ", free_disk,"GB")
print("Usage: ", round(percentage, 2),"%")