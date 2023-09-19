import time
from datetime import datetime

seconds_since_epoch = datetime.now().timestamp()
print(f'Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation')
print(datetime.now().strftime('%b %d %Y'))