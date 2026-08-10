# Docker Container Manager

# Problem : Create a list of Docker containers.
# Display all containers.
# Add a new container.
# Remove one container.
# Display the updated list.

# Create the List
containers = ["nginx", "redis", "mysql"]

# Display the List
print("Current Containers:")
print(containers)

# Add the Container
containers.append("postgres")
print(containers)

# Remove the Container
containers.remove("redis")
print(containers) 
