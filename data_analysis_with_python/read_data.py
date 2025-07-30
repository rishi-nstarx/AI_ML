import pandas as pd

# === 1. Reading CSV File ===
# CSV (Comma Separated Values) is one of the most common data formats
df_csv = pd.read_csv('data.csv')  # Make sure 'data.csv' is in your working directory
print("CSV Data:\n", df_csv.head())

# === 2. Reading Excel File ===
# Requires: pip install openpyxl or xlrd
df_excel = pd.read_excel('data.xlsx')  # Default reads the first sheet
print("\nExcel Data:\n", df_excel.head())

# === 3. Reading Specific Sheet from Excel ===
df_excel_sheet = pd.read_excel('data.xlsx', sheet_name='Sales')
print("\nExcel Data from 'Sales' sheet:\n", df_excel_sheet.head())

# === 4. Reading JSON File ===
df_json = pd.read_json('data.json')
print("\nJSON Data:\n", df_json.head())

# === 5. Reading from a Dictionary ===
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df_dict = pd.DataFrame(data_dict)
print("\nData from Dictionary:\n", df_dict)

# === 6. Reading from a SQL Database ===
# Requires: SQLAlchemy and a supported database (e.g., SQLite)
import sqlite3
conn = sqlite3.connect('sample.db')
df_sql = pd.read_sql_query("SELECT * FROM employees", conn)
print("\nSQL Data:\n", df_sql.head())

# === 7. Reading a Text File with Delimiter ===
df_txt = pd.read_csv('data.txt', delimiter='|')  # Use the actual delimiter in your file
print("\nText File Data:\n", df_txt.head())

# === 8. Reading HTML Table from a Web Page ===
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
df_html_list = pd.read_html(url)  # returns a list of DataFrames
df_html = df_html_list[0]
print("\nHTML Table Data:\n", df_html.head())

# === 9. Reading from Clipboard (copy any table and run this) ===
# Note: works best in Jupyter or interactive environments
# df_clip = pd.read_clipboard()
# print("\nClipboard Data:\n", df_clip.head())
