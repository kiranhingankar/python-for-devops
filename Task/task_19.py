# Find Duplicate Server IPs

# Problem : You receive the following server IP addresses:

# ips = [
#     "10.0.0.10",
#     "10.0.0.11",
#     "10.0.0.10",
#     "10.0.0.12",
#     "10.0.0.11"
# ]

# Find:
#  - Total IP entries
#  - Unique IP addresses
#  - Duplicate IP addresses


ips = [
    "10.0.0.10",
    "10.0.0.11",
    "10.0.0.10",
    "10.0.0.12",
    "10.0.0.11"
]

unique_ips = set(ips)

duplicates = []

for ip in ips:
    if ips.count(ip) > 1 and ip not in duplicates:
        duplicates.append(ip)

print("IP Inventory Report")
print("-------------------")

print("Total IP Entries :", len(ips))
print("Unique IPs       :", len(unique_ips))

print("\nUnique IP Addresses:")

for ip in unique_ips:
    print(ip)

print("\nDuplicate IP Addresses:")

for ip in duplicates:
    print(ip)