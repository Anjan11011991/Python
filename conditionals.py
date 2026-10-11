import psutil

# Get system memory information
memory = psutil.virtual_memory()

# Display memory utilization
print(f"Total Memory     : {memory.total / (1024**3):.2f} GB")
print(f"Used Memory      : {memory.used / (1024**3):.2f} GB")
print(f"Available Memory : {memory.available / (1024**3):.2f} GB")
print(f"Memory Usage     : {memory.percent}%")

# Check memory threshold
if memory.percent >= 90:
    print("WARNING: Very High memory utilization!")
elif memory.percent >= 89:
    print("WARNING: High memory utilization!")
else:
    print("Memory utilization is normal.")

