# Server Configuration Using Tuple

# Problem : Create a tuple containing:
# - Server name
# - IP address
# - Environment
# - Status

# Then print each value.

server = (
    "web-01",
    "10.0.0.10",
    "production",
    "running"
)

print("Server Configurations")
print("---------------------")

print("Server Name :", server[0])
print("IP Address  :", server[1])
print("Environment :", server[2])
print("Status      :", server[3])