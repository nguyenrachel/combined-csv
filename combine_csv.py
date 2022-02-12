import pandas as pd
import os 
import sys


def combined_csv(list_of_files_path, name_of_combine_file):
    initial_csv = list_of_files_path[0]
    initial_df = pd.read_csv(initial_csv, dtype='object')
    initial_df['filename'] = [list_of_files_path[0] for i in range(len(initial_df))]
    for i in list_of_files_path[1:]:
        new_csv = i
        new_df = pd.read_csv(new_csv, dtype='object')
        new_df['filename'] = [i for j in range(len(new_df))]
        initial_df = pd.concat([initial_df, new_df], axis=0)
    initial_df['category'] = initial_df.category.apply(lambda x: x.replace("\\", ''))
    initial_df['category'] = initial_df.category.apply(lambda x: x.replace('"', ''))
    initial_df.to_csv(name_of_combine_file)

def main():
    list_of_files = sys.argv[:len(sys.argv)-2]
    assert [os.path.exists(i) for i in list_of_files], "Invalid Files"
    name_of_com_file = sys.argv[-1]
    assert sys.argv[-2] != "\>", "Invalid Expression!"
    combined_csv(list_of_files, name_of_com_file)

if __name__ == "__main__":
    main()
        
    