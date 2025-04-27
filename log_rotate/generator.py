import os 
import datetime
import random

days_num = 90
lines_num = 10000

base_path = os.path.dirname(__file__)
print(base_path)
gen_logs_path = os.path.join(base_path, 'gen_logs')

def gen_log(log_date):
    text = str()
    for line in range(lines_num):
        severity = random.choice(['INFO', 'ERR', 'WARN', 'DEBUG', 'FATAL'])
        rand_microsec = random.randint(1, 999999)
        log_date += datetime.timedelta(microseconds=rand_microsec)
        event = random.choice(['Disk is FULL', 'No connection', 'PLC is unsynced', 'Device is unavaible', 'Memory FULL', 'Connection Timeout', 'CPU load more 90%'])
        text += f'{log_date} [{severity}] {event}\n'
    return text

now = datetime.datetime.now()
for i in range(days_num):
    subtracted = now - datetime.timedelta(days=i)
    formatted = subtracted.strftime("%Y-%m-%d")
    file_path = os.path.join(gen_logs_path, f'gen_logs_{formatted}.log')
    text = gen_log(subtracted)
    with open(file_path, 'w') as file:
       file.write(text)
