# 📂 CSV & Excel File Merger

A simple Python tool that merges all CSV and Excel files inside a selected folder into one clean Excel file.

Automatically removes duplicates and tracks source files.

---

## 🚀 Features

- ✅ Select folder via file dialog
- ✅ Supports CSV, XLS, XLSX files
- ✅ Automatically merges all files in folder
- ✅ Removes duplicate rows
- ✅ Adds `source_file` column (tracks origin)
- ✅ Saves final merged file as Excel
- ✅ Simple GUI pop-up messages
- ✅ Fully offline

---

## 📦 Requirements

- Python 3.8+
- pandas
- openpyxl

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

```bash
python folder_data_merger.py
```

---

## 📝 How It Works

1. Select a folder containing CSV or Excel files.
2. The script reads all supported files.
3. All data is combined into one DataFrame.
4. Duplicate rows are removed.
5. Final merged file is saved automatically.

---

## 📂 Output

The merged file will be saved inside the selected folder as:

```
merged_output.xlsx
```

Each row includes an additional column:

```
source_file
```

This shows which file the data originally came from.

---

## 💡 Use Cases

- Combine monthly reports
- Merge exported CRM files
- Consolidate lead lists
- Merge sales data
- Data cleanup before analysis

---

## 🛡️ Privacy

This tool runs completely offline.  
No data is sent externally.

---

## 📜 License

MIT License
