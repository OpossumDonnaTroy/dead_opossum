import os 
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
print(base_path)
report_path = os.path.join(base_path, 'reports')
#описала папку архив
archive_path = os.path.join(base_path, 'archive')
now = datetime.now()

#получить список файлов из репортс
fileslist = os.listdir(report_path)
for filename in fileslist:
    filedate = filename[7:-4]
    filedate = datetime.strptime(filedate, '%Y-%m-%d')
    today = datetime.now()
    old_date = today - timedelta(days=30)
    if filedate < old_date:
        from_path = os.path.join(report_path, filename)
        dest_path = os.path.join(archive_path, filename)
        os.rename(from_path, dest_path)


    
    
    


#выполнить отбор нужных файлов из папки репортс 

#вывести теперь список без шелухи в названии



#запись отобранных файлов в папку архив

    
