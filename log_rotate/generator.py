import os 
import datetime

base_path = os.path.dirname(__file__)
print(base_path)
report_path = os.path.join(base_path, 'reports')

now = datetime.datetime.now()
for i in range(60):
    subtracted = now - datetime.timedelta(days=i)
    formatted = subtracted.strftime("%Y-%m-%d")
    print(formatted) 

    file_path = os.path.join(report_path, f'report_{formatted}.csv')
    print(file_path)
    with open(file_path, 'w') as file:
       file.write('test')
