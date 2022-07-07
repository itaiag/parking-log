import os
root_dir = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
database_name = "parking.db"
database_full_path = os.path.join(root_dir, database_name)
date_time_format = "%d/%m/%Y %H:%M:%S"