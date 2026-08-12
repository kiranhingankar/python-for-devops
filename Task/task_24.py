# Deployment Report Generator

# Now we'll create something closer to a CI/CD use case.

# Problem : Create a Python program that asks for:
#  - Application name
#  - Version
#  - Environment
#  - Deployment status

# Then write a deployment report to:
#  - deployment_report.txt

application = input("Enter Application Name: ")
version = input("Enter Version: ")
environment = input("Enter Environment: ").strip().lower()
status = input("Enter Deployment Status: ")

with open("deployment_report.txt", "w") as file:
    file.write("Deployment Report\n")
    file.write("-----------------\n")
    file.write(f"Application: {application}\n")
    file.write(f"Version: {version}\n")
    file.write(f"Environment: {environment}\n")
    file.write(f"Status: {status}\n")

print("Deployment report generated successfully.")