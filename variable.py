
import psutil

# Get system memory information
memory = psutil.virtual_memory()

# Display memory utilization
print(f"Total Memory     : {memory.total / (1024**3):.2f} GB")
print(f"Used Memory      : {memory.used / (1024**3):.2f} GB")
print(f"Available Memory : {memory.available / (1024**3):.2f} GB")
print(f"Memory Usage     : {memory.percent}%")
