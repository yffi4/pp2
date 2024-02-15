from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)
today = datetime.today()
print(yesterday)
print(today)
print(tomorrow)