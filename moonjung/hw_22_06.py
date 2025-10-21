import os

path = r'C:\rokey\python\ch22\sample_folder'

if os.path.exists(path):
    print(os.listdir(path))