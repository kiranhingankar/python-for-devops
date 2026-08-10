# Kubernetes Pod Inventory

# Problem : Store Kubernetes pod names in a list.

# Print:
# Total number of pods.
# Each pod name using a loop.

pods = [
    "frontend-pod",
    "backend-pod",
    "database-pod",
    "monitoring-pod"
]

print("Kubernetes Pod Inventory")
print("-------------------------")
print("\nTotal pods: ", len(pods),"\n")

for pod in pods:
    print("Pod: ",pod)