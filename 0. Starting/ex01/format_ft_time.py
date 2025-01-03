# import datetime as datetime
import time as time
from datetime import datetime as datetime

seconds_since_start = time.time()
dateToday = datetime.now().strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {seconds_since_start:,.4f} or {seconds_since_start:.2e} in scientific notation")
print(dateToday)