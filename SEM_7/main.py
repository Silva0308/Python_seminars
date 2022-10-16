from pathlib import Path
from CSV_create import creating
from file_writing import writing_scv
from file_writing import writing_txt


path = Path("Python_seminars", "SEM_7",'Phonebook.csv')
if path.exists == False:
    creating()

writing_scv()
writing_txt()