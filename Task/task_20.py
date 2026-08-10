# Compare DEV and PROD Infrastructure
# Now we'll combine sets + dictionaries + loops.

# Problem : You have the following infrastructure:
# DEV
#   dev_servers = {
#       "web-01",
#       "web-02",
#       "api-01",
#       "db-01"
#   }
# PROD
#   prod_servers = {
#       "web-01",
#       "api-01",
#       "db-01",
#       "monitor-01"
#   }

# Find:
#  - Servers common to DEV and PROD
#  - Servers only in DEV
#  - Servers only in PROD
#  - All unique servers



dev_servers = {
    "web-01",
    "web-02",
    "api-01",
    "db-01"
}

prod_servers = {
    "web-01",
    "api-01",
    "db-01",
    "monitor-01"
}

common_servers = dev_servers.intersection(prod_servers)

dev_only = dev_servers.difference(prod_servers)

prod_only = prod_servers.difference(dev_servers)

all_servers = dev_servers.union(prod_servers)

print("Infrastructure Comparison")
print("=========================")

print("\nCommon Servers:")
for server in common_servers:
    print(" -", server)

print("\nDev Only:")
for server in dev_only:
    print(" -", server)

print("\nProd Only:")
for server in prod_only:
    print(" -", server)

print("\nAll Unique Servers:")
for server in all_servers:
    print(" -", server)