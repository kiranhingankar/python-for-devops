# Docker Image Name Validator

# Problem : Ask the user to enter a Docker image name.

# The program should:
# Remove extra spaces
# Convert it to lowercase
# Check if it starts with "nginx"
# Print whether it is an Nginx image

docker_image = input("Enter Docker Image Name: ")

image = docker_image.strip().lower()

print("\nProcessed Image:", image)

if image.startswith("nginx"):
    print("Valid Nginx Image")
else:
    print("Not an Nginx Image")