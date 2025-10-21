from pathlib import Path

path = Path(r'C:\rokey\python\ch22\sample_folder')

def find_txt(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print('폴더가 존재하지 않음')
        return
    
    for file in folder.iterdir():
        extension = file.suffix
        if extension == '.txt':
            print(file)
            
    return

find_txt(path)
