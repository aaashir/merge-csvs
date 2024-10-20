import pandas as pd
import os

def merge_csv_files(directory):
    dataframes = []

    for file in os.listdir(directory):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(directory, file), low_memory=False)
            dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)

    merged_df.drop_duplicates(subset="email", inplace=True)

    return merged_df

csv_directory = './files'

final_df = merge_csv_files(csv_directory)

output_file = 'merged_output.csv'
final_df.to_csv(output_file, index=False)

print(f"Merged CSV saved as {output_file}")
