# Server Resource Calculator

# Problem

# Create a Python program that:
# Takes CPU cores from the user
# Takes RAM in GB from the user
# Prints the total resources after doubling them (simulating server scaling)

cpu = int(input("Enter CPU Cores: "))
ram = int(input("Enter RAM (GB): "))

new_cpu = cpu * 2
new_ram = ram * 2

print("\n-----Current Server-----")
print("CPU: ", cpu)
print("RAM: ", ram,"GB")

print("\n-----After Scaling-----")
print("CPU: ", new_cpu)
print("RAM: ", new_ram,"GB")