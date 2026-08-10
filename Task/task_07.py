# DevOps Environment Selector

# Problem : Write a Python program that asks the user to enter the deployment environment.

# If the environment is:
# dev → Print Deploying to Development
# uat → Print Deploying to UAT
# prod → Print Deploying to Production
# Otherwise → Print Invalid Environment


environment = input("Enter Environment (dev/uat/prod): ").lower()

if environment == "dev":
    print("Deploying to Development Environment")
elif environment == "uat":
    print("Deploying to UAT Environment")
elif environment == "prod":
    print("Deploying to Production Environment")
else:
    print("Invalid Environment")
