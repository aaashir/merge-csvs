# CSV Merger Script

This Python script merges multiple CSV files from a specified directory into one consolidated CSV file and removes duplicate rows based on the `email` or any other field.

## Features

- Merges all CSV files in a directory into a single CSV file.
- Removes duplicated rows based on the `email` or any other column.
- Handles large CSV files and mixed data types efficiently.
  
## Prerequisites

- **Python 3.6+**
- **Pandas Library**

To install Pandas, run:
```bash
pip install pandas
```

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aaashir/merge-csvs.git
   cd merge-csvs
   ```

2. **Place your CSV files**:
   
   Place all the CSV files you want to merge in the `files` directory.

3. **Run the script**:

   Execute the script with Python:

   ```bash
   python3 script.py
   ```

4. **Result**:

   The merged CSV file will be saved as `merged_output.csv` in the current directory.

## Customization

- **Directory Path**: Update the `csv_directory` variable in the script to point to your folder containing the CSV files.
  
- **Email Field**: The script assumes the CSV files have an `email` or specified column. If your files have a different column name for emails, change the `drop_duplicates` method's `subset` argument accordingly:
  
   ```python
   merged_df.drop_duplicates(subset="your_email_column", inplace=True)
   ```

## Example

Given the following CSV files:

- `file1.csv`
- `file2.csv`

The script will merge them into `merged_output.csv` and remove any duplicate rows based on the `email` or any other column you want.

## Issues

If you encounter any issues, feel free to open a GitHub issue or pull request. Contributions and suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---