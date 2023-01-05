import datetime

import pytz


th_timezone = pytz.timezone('Asia/Bangkok')


th_time = datetime.datetime.now(th_timezone)


print(th_time.strftime('%H:%M:%S'))
