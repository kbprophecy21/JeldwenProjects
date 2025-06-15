import os
from tabulate import tabulate
from effscanner import EFFScanner
from dataManager import DataManager

def print_main_menu():
    print("\n📋 EFFScanner Menu")
    print("1. Scan Ticket")
    print("2. View Shift Totals")
    print("3. Reset Totals")
    print("4. Exit")

def main():
    folder_path = r"c:\Users\14704\OneDrive\Desktop\All Projects\Wild_Projects\Jeldwen_Projects\JeldwenProjects\Data\LIS_Files"
    data_manager = DataManager()

    while True:
        print_main_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            batch_id = input("\nEnter Schedule Batch ID: ").strip()  # example data: 0602250010001   ,  060625ALR0005001 , 0609250160002  ,  061025BFS0010001
            scanner = EFFScanner(folder_path, batch_id)
            scanner.find_ticket()
            ticket_df = scanner.get_ticket_data()

            if not ticket_df.empty:
                print("\n✅ Ticket Data:")
                print(tabulate(ticket_df, headers="keys", tablefmt="fancy_grid"))

                row = ticket_df.iloc[0]
                frame_code = row["door_frame_code"]
                door_size = row["door_size"]
                quantity = int(row["door_quantity"])

                category_key = data_manager.categorize_ticket(frame_code, door_size, quantity)
                if category_key:
                    data_manager.set_value(category_key, quantity)
                    print(f"✔️ Added {quantity} to category '{category_key}'")
                else:
                    print("⚠️ Could not categorize this ticket.")
            else:
                print("⚠️ No ticket data found.")

        elif choice == "2":
            print("\n📦 Shift Totals:")
            totals = data_manager.get_all()
            non_zero = {k: v for k, v in totals.items() if v > 0}
            if non_zero:
                print(tabulate(non_zero.items(), headers=["Category", "Total"], tablefmt="fancy_grid"))
            else:
                print("No data collected yet.")

        elif choice == "3":
            confirm = input("⚠️ Are you sure you want to reset all totals? (y/n): ").strip().lower()
            if confirm == "y":
                data_manager = DataManager()
                print("🔄 Totals have been reset.")

        elif choice == "4":
            print("👋 Exiting EFFScanner. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
