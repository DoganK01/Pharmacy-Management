import csv
import os

def get_base_name_without_extension(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    return base_name

def get_file_names_from_csv_folder(folder_path):
    file_names = []
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                base_name = get_base_name_without_extension(file_name)
                file_names.append(base_name)
    else:
        print(f"{folder_path} doesn't exist.")

    return file_names

def get_csv_files(folder_path):
    csv_files = []
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                csv_files.append(os.path.join(folder_path, file_name))
    else:
        print(f"{folder_path} bulunamadı.")
    return csv_files

def csv_to_dataframe(csv_files):
    dataframes = {}
    for csv_file in csv_files:
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        dataframes[base_name] = pd.read_csv(csv_file)
    return dataframes

def main():
    folder_path = '/content/data'
    csv_files = get_csv_files(folder_path)
    dataframes = csv_to_dataframe(csv_files)
    print(len(dataframes))

    return dataframes
