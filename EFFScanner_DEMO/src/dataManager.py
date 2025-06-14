import os


class DataManager:
    def __init__(self):
        # Initialize the data structure with predefined keys.
        # The keys represent different types of data that can be stored.
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
            self.data[key] = value
        else:
            raise KeyError("Invalid key or value type.")

    def get_value(self, key):
        return self.data.get(key, None)

    def get_all(self):
        return self.data.copy()

   