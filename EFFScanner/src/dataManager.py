class DataManager:
    def __init__(self): 
        # All possible categories
        keys = [
            "BF", "MC", "HC", "SC", "MS", "MC 8/0",
            "BF01", "MC01", "HC01", "SC01", "MS01", "MC01 8/0",
            "BF05", "MC05", "HC05", "SC05", "MS05", "MC05 8/0",
            "BF10", "MC10", "HC10", "SC10", "MS10", "MC10 8/0",
            "BF15", "MC15", "HC15", "SC15", "MS15", "MC15 8/0",
            "BF20", "MC20", "HC20", "SC20", "MS20", "MC20 8/0"
        ]
        self.data = {key: 0 for key in keys}

    def set_value(self, key, value):
        if key in self.data and isinstance(value, (int, float)):
            self.data[key] += value
        else:
            raise KeyError(f"Invalid key or value type: {key}, {value}")

    def get_value(self, key):
        return self.data.get(key, None)

    def get_all(self):
        return self.data.copy()

    # ----------------------------
    # Category Rule Checks
    # ----------------------------

    def isDoorBifold(self, frame_code):
        frame_letter = frame_code[2].upper()
        return frame_letter in ["F", "J", "W"]

    def isDoorGreaterthan7ft(self, door_size):
        door_size = door_size.replace('"', '').strip()
        return "8/0" in door_size

    def isDoorMCMolded(self, frame_code):
        return frame_code[0].upper() in ["M", "K"]

    def isDoorHCHollowCore(self, frame_code):
        return frame_code[0].upper() == "H"

    def isDoorSCFLushSolid(self, frame_code):
        return frame_code[0].upper() in ["J", "P", "F"]

    def isDoorMSSolidCore(self, frame_code):
        return frame_code[0].upper() == "G"

    # ----------------------------
    # Categorization
    # ----------------------------

    def categorize_ticket(self, frame_code, door_size, quantity):
        """
        Determine the correct category key based on frame code, door size, and quantity.
        """

        # Bifold
        if self.isDoorBifold(frame_code):
            return self._get_quantity_key("BF", quantity)

        # Molded Core (check for 8/0 size)
        if self.isDoorMCMolded(frame_code):
            if self.isDoorGreaterthan7ft(door_size):
                return self._get_quantity_key("MC", quantity, is_8ft=True)
            else:
                return self._get_quantity_key("MC", quantity)

        # Hollow Core
        if self.isDoorHCHollowCore(frame_code):
            return self._get_quantity_key("HC", quantity)

        # Flush Solid Core
        if self.isDoorSCFLushSolid(frame_code):
            return self._get_quantity_key("SC", quantity)

        # Solid Core
        if self.isDoorMSSolidCore(frame_code):
            return self._get_quantity_key("MS", quantity)

        return None  # Unknown category

    def _get_quantity_key(self, prefix, quantity, is_8ft=False):
        """
        Return the category key based on quantity thresholds.
        Supports standard and 8/0 variants.
        """
        if quantity == 1:
            key = f"{prefix}01"
        elif 2 <= quantity <= 5:
            key = f"{prefix}05"
        elif 6 <= quantity <= 10:
            key = f"{prefix}10"
        elif 11 <= quantity <= 15:
            key = f"{prefix}15"
        elif 16 <= quantity <= 20:
            key = f"{prefix}20"
        else:
            key = prefix

        if is_8ft:
            key += " 8/0"

        return key
