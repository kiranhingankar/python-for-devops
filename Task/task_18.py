# AWS EC2 Inventory Using Dictionary
# Now we'll use a dictionary to represent an EC2 instance.

# Problem : Create an EC2 instance dictionary containing:
# - Instance ID
# - Instance Name
# - Instance Type
# - Environment
# - Status

# Then:
# - Print the instance details.
# - Change the status from stopped to running.
# - Add an owner.
# - Print the updated configuration.

ec2 = {
    "instance_id": "i-123456789",
    "instane_name": "web-server",
    "instance_type": "t2.micro",
    "environment": "dev",
    "status": "stopped"
}

print("EC2 Instance Details")
print("--------------------")

print("Instance ID   :", ec2["instance_id"])
print("Instance Name :", ec2["instane_name"])
print("Instance Type :", ec2["instance_type"])
print("Environment   :", ec2["environment"])
print("Status        :", ec2["status"])

# Update Status
ec2["status"] = "running"

# Add owner
ec2["owner"] = "DevOps Team"

print("\nUpdated EC2 Details")
print("---------------------")

for key, value in ec2.items():
    print(f"{key}: {value}")