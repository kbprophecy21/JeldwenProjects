import pandas as pd

# This script reads a CSV file and prints the first few rows of the DataFrame.


file_path = r"c:\Users\14704\OneDrive\Desktop\All Projects\Wild_Projects\Jeldwen_Projects\JeldwenProjects\Data\LIS_Files\060925.LIS"


with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()
print(data[:100])  