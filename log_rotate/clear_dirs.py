import os
import shutil
base_path = os.path.dirname(__file__) #определили путь где скрипт запускается
gen_logs_path = os.path.join(base_path, 'gen_logs')
archive_path = os.path.join(base_path, 'archive')
#https://sky.pro/media/udalenie-soderzhimogo-papki-v-python/#:~:text=%D0%AD%D1%82%D0%BE%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E,%2C%20%D0%B0%20file%20%E2%80%94%20%D0%B8%D0%BC%D1%8F%20%D1%84%D0%B0%D0%B9%D0%BB%D0%B0.&text=%D0%92%20%D1%8D%D1%82%D0%BE%D0%BC%20%D0%BA%D0%BE%D0%B4%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F%20delete_files_in_folder,%D1%83%D0%B4%D0%B0%D0%BB%D1%8F%D0%B5%D1%82%20%D0%B2%D1%81%D0%B5%20%D1%84%D0%B0%D0%B9%D0%BB%D1%8B%20%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8%20%D0%BD%D0%B5%D1%91.

def delete_everything_in_folder(path):
    shutil.rmtree(path)
    os.mkdir(path)

delete_everything_in_folder(gen_logs_path)
delete_everything_in_folder(archive_path)