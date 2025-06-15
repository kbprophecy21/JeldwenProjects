import os
import pandas as pd  

class EFFScanner:
    def __init__(self, folder_path, batch_id):
        self.folder_path = folder_path
        self.batch_id = batch_id.strip()

        # Extract press info
        self.group_press = self.batch_id[-7:]
        self.group_press_A = self.group_press[:4]
        self.group_press_B = self.group_press[4:]

        # Extract file name
        self.file_name = f"{self.batch_id[:-7]}.LIS"
        self.file_path = None

        # Parsed ticket data
        self.door_quantity = None
        self.door_size = None
        self.door_frame_code = None
        self.found = False

    def find_ticket(self):
        for file in os.listdir(self.folder_path):
            if file == self.file_name:
                self.file_path = os.path.join(self.folder_path, file)
                print(f"Processing file: {self.file_path}")

                with open(self.file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        fields = line.strip().split(",")
                        search_range = [field.strip('"') for field in fields[1:5]]

                        if self.group_press_A in search_range and self.group_press_B in search_range:
                            print("✅ Match found in file.")
                            fields = [field.strip('"') for field in line.strip().split(",")]

                            self.door_quantity = fields[5]
                            self.door_size = fields[7]
                            self.door_frame_code = fields[8].strip().split()[0]
                            self.found = True
                            return

                print(f"❌ No match for '{self.batch_id} in file location.")
                return

        print(f"❌ File '{self.file_name}' not found in {self.folder_path}")

    def get_ticket_data(self):
        if self.found:
            data = {
                "door_quantity": [self.door_quantity],
                "door_size": [self.door_size],
                "door_frame_code": [self.door_frame_code],
            }
            return pd.DataFrame(data)  # ✅ Return as DataFrame
        else:
            return pd.DataFrame()  # Empty DataFrame if not found
