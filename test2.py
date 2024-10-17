
from datetime import datetime, timedelta
import time
import os

# Pobranie aktualnej daty
current_date = datetime.now()
os.system("pause ")
current_date_2 = datetime.now()
czas = (current_date_2 - current_date).seconds
print("minelo: {} sek ".format(czas))



