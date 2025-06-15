import os
# Sale department tickets do not work with this script. We will need to modify the script to handle those cases later.

# This is a demo script for EFFScanner terminal interface.
# It is designed to demonstrate the functionality of the EFFScanner in a terminal environment.

folder_path = r"c:\Users\14704\OneDrive\Desktop\All Projects\Wild_Projects\Jeldwen_Projects\JeldwenProjects\Data\LIS_Files"

print("Enter the Schedule Batch ID: ")   # example data: 0602250010001   ,  060625ALR0005001 , 0609250160002  ,  061025BFS0010001

batch_id = input().strip()

# Extract press info
group_press = batch_id[-7:]
group_press_A = group_press[:4]
group_press_B = group_press[4:]

# Trim batch_id to get the file name
batch_id = batch_id[:-7]
file_name = f"{batch_id}.LIS"

# Search for the matching file
for file in os.listdir(folder_path):
    if file == file_name:
        file_path = os.path.join(folder_path, file)
        print(f"Processing file: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            found = False
            for line in file:
                # Goes line by line to find the matching group press
                # Each line is expected to be a comma-separated string
                # Extract fields 2 to 5 (between 1st and 5th comma)
                fields = line.strip().split(",")
                search_range = [field.strip('"') for field in fields[1:5]]

                if group_press_A in search_range and group_press_B in search_range:
                    print("Matched Line:")
                    ticket_data = line.strip()
                    
                    fields = [field.strip('"') for field in ticket_data.split(",")]
                    door_quanity = fields[5]
                    door_size = fields[7]
                    door_frameCode = fields[8].strip().split()[0]

                    
                    print(f"Door Quantity: {door_quanity}")
                    print(f"Door Size: {door_size}")
                    print(f"Door Frame Code: {door_frameCode}")
                    
                    found = True
                    break

            if not found:
                print(f"❌ No match for '{group_press_A}' & '{group_press_B}' in the file.")

        break  # Stop after finding and processing the correct file
else:
    print(f"❌ File '{file_name}' not found in {folder_path}")
