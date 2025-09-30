import os
import shutil

def get_directory():
    while True:
        path = input("Enter a directory path: ")
        if os.path.isdir(path):
            return path
        print("Invalid directory. Please try again.")

def os_file_manager():
    dir_path = get_directory()
    backup_path = os.path.join(dir_path, 'backup')
    os.makedirs(backup_path, exist_ok=True)
    count = 0
    for fname in os.listdir(dir_path):
        if fname.endswith('.txt'):
            src = os.path.join(dir_path, fname)
            dst = os.path.join(backup_path, fname)
            shutil.copy2(src, dst)
            count += 1
    print(f"Copied {count} .txt files to backup.")
