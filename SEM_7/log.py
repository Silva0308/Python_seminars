from datetime import datetime
from time import time
from pathlib import Path



def log(data):
    time = datetime.now().strftime('%H:%M')
    file = Path("Python_seminars", "SEM_7", 'log.csv')
    with open(file, 'a', encoding='utf-8') as log_file:
        log_file.write('{} / {} = {} Time {}\n'.format(data, time))