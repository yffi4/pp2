from datetime import datetime, timedelta
import time
dt1 = datetime.now()
time.sleep(5)
dt2 = datetime.now()
print((dt2 - dt1).seconds)