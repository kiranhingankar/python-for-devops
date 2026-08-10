# Deployment Retry Simulator

# Problem
# A deployment can be attempted 3 times.
# Print each attempt.
# If the deployment succeeds on the third attempt, stop retrying.

attempt = 1

while attempt <=3:

    print(f"Deployment Attempt {attempt}")

    if attempt == 3:
        print("Deployment Successful!")
        break

    print("Deployment Failed!")
    print("Retrying...\n")

    attempt += 1