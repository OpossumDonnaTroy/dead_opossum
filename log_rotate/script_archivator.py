import os 
import datetime

base_path = os.path.dirname(__file__)
print(base_path)
report_path = os.path.join(base_path, 'reports')
#описала папку архив
archive_path = os.path.join(base_path, 'archive')
now = datetime.datetime.now()

#получить список файлов из репортс
fileslist = os.listdir(report_path,)
for filename in fileslist:
    filename = filename[7:-4]
    filedate = datetime.datetime.strptime(filename, '%Y-%m-%d')
    print(filedate)
    


#выполнить отбор нужных файлов из папки репортс 
#вывести теперь список без шелухи в названии



#запись отобранных файлов в папку архив

    
