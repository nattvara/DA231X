import os


def save_table(filename: str, latex_code: str):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    fullpath = f"{current_dir}/../latex_tables/{filename}.tex"
    fullpath = os.path.realpath(fullpath)
    with open(fullpath, 'w') as f:
        f.write(latex_code)

    print(f"Saved latex code to {fullpath}")
