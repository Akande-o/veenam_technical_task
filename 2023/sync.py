import os
import shutil
import argparse
import time

def sync_folders(source_folder, replica_folder, log_file_path, sync_interval):
    while True:
        for root, dirs, files in os.walk(source_folder):
            for name in files:
                source_file = os.path.join(root, name)
                replica_file = source_file.replace(source_folder, replica_folder)
                if not os.path.exists(os.path.dirname(replica_file)):
                    os.makedirs(os.path.dirname(replica_file))
                if not os.path.exists(replica_file):
                    shutil.copy2(source_file, replica_file)
                    log_to_file(log_file_path, f"File copied: {replica_file}")
                    print(f"File copied: {replica_file}")
                elif os.stat(source_file).st_mtime > os.stat(replica_file).st_mtime:
                    shutil.copy2(source_file, replica_file)
                    log_to_file(log_file_path, f"File updated: {replica_file}")
                    print(f"File updated: {replica_file}")
        for root, dirs, files in os.walk(replica_folder):
            for name in files:
                replica_file = os.path.join(root, name)
                source_file = replica_file.replace(replica_folder, source_folder)
                if not os.path.exists(source_file):
                    os.remove(replica_file)
                    log_to_file(log_file_path, f"File deleted: {replica_file}")
                    print(f"File deleted: {replica_file}")
        time.sleep(sync_interval)

def log_to_file(log_file_path, message):
    with open(log_file_path, 'a') as f:
        f.write(f"{message}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync two folders.')
    parser.add_argument('source_folder', type=str, help='Source folder path')
    parser.add_argument('replica_folder', type=str, help='Replica folder path')
    parser.add_argument('log_file_path', type=str, help='Log file path')
    parser.add_argument('sync_interval', type=int, help='Sync interval in seconds')
    args = parser.parse_args()
    sync_folders(args.source_folder, args.replica_folder, args.log_file_path, args.sync_interval)
