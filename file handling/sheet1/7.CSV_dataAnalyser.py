import csv

filename = "test_results.csv"

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        total_tests = 0
        passed = 0
        failed = 0
        total_time = 0

        for row in reader:
            total_tests += 1

            if row["Status"].upper() == "PASS":
                passed += 1
            elif row["Status"].upper() == "FAIL":
                failed += 1

            total_time += float(row["ExecutionTime"])

        average_time = total_time / total_tests if total_tests > 0 else 0

        print("Total Tests:", total_tests)
        print("Passed:", passed)
        print("Failed:", failed)
        print("Average Execution Time:", average_time)

except FileNotFoundError:
    print("File not found.")