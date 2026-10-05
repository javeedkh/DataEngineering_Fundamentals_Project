e=w=i=0
for line in open("data/logs.txt"):
    if "ERROR" in line:e+=1
    elif "WARNING" in line:w+=1
    elif "INFO" in line:i+=1
print(f"INFO Records: {i}")
print(f"WARNING Records: {w}")
print(f"ERROR Records: {e}")
