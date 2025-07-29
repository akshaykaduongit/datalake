def fetch_data_from_file(file_path):
    import os
    import pandas as pd

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def fetch_multiple_files(file_paths):
    data_frames = []
    for path in file_paths:
        try:
            data = fetch_data_from_file(path)
            data_frames.append(data)
        except Exception as e:
            print(f"Error fetching data from {path}: {e}")
    return data_frames