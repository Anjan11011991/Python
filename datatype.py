# This acript will cover datatpyes (float,string and int)
import psutil

# Get system memory information
memory = psutil.virtual_memory()

print(f"Display memory utilization float")
print(f"#################################") 
print(f"Total Memory     : {memory.total / (1024**3):.2f} GB")
print(f"Used Memory      : {memory.used / (1024**3):.2f} GB")
print(f"Available Memory : {memory.available / (1024**3):.2f} GB")
print(f"Memory Usage     : {memory.percent}%")

print(f"Display memory utilization int")
print(f"#################################")
print(f"Total Memory     : {int(memory.total / (1024**3))} GB")
print(f"Used Memory      : {int(memory.used / (1024**3))} GB")
print(f"Available Memory : {int(memory.available / (1024**3))} GB")
print(f"Memory Usage     : {int(memory.percent)}%")

