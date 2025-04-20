import os 
import datetime
import random

days_num = 31
lines_num = 10000

base_path = os.path.dirname(__file__)
print(base_path)
report_path = os.path.join(base_path, 'reports')

def gen_log(log_date):
    text = str()
    for line in range(lines_num):
        severity = random.choice(['INFO', 'ERR', 'WARN', 'DEBUG', 'FATAL'])
        rand_microsec = random.randint(1, 999999)
        log_date += datetime.timedelta(microseconds=rand_microsec)
        text += f'{log_date} [{severity}]\n'
    return text

now = datetime.datetime.now()
for i in range(days_num):
    subtracted = now - datetime.timedelta(days=i)
    formatted = subtracted.strftime("%Y-%m-%d")
    file_path = os.path.join(report_path, f'report_{formatted}.log')
    text = gen_log(subtracted)
    with open(file_path, 'w') as file:
       file.write(text)
