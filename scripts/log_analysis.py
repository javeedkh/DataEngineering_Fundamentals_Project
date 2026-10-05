error_count = 0
warning_count = 0
info_count = 0

print("\nLog Records")
print("-" * 40)

with open("data/logs.txt", "r") as file:

    for line in file:

        print(line.strip())

        if "ERROR" in line:
            error_count += 1

        elif "WARNING" in line:
            warning_count += 1

        elif "INFO" in line:
            info_count += 1

print("\n" + "=" * 50)
print("LOG ANALYSIS SUMMARY")
print("=" * 50)

print(f"INFO Records    : {info_count}")
print(f"WARNING Records : {warning_count}")
print(f"ERROR Records   : {error_count}")