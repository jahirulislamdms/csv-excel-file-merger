import os
import pandas as pd
from tkinter import Tk, filedialog, messagebox

def merge_files():
    # Hide main tkinter window
    root = Tk()
    root.withdraw()

    # Ask user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder Containing CSV/Excel Files")

    if not folder_path:
        messagebox.showinfo("No Folder Selected", "No folder was selected. Exiting.")
        return

    # Collect all supported files
    supported_ext = ('.csv', '.xls', '.xlsx')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_ext)]

    if not files:
        messagebox.showinfo("No Files Found", "No CSV or Excel files found in the selected folder.")
        return

    all_data = []

    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            if file.lower().endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
            df["source_file"] = file  # Optional: track which file each row came from
            all_data.append(df)
        except Exception as e:
            messagebox.showwarning("Read Error", f"Could not read {file}: {e}")

    if not all_data:
        messagebox.showinfo("No Data", "No valid data found in the files.")
        return

    # Merge all files into one DataFrame
    merged_df = pd.concat(all_data, ignore_index=True)

    # Remove duplicates
    merged_df.drop_duplicates(inplace=True)

    # Save the merged output as Excel
    output_path = os.path.join(folder_path, "merged_output.xlsx")
    merged_df.to_excel(output_path, index=False)

    messagebox.showinfo("Success", f"Merged file saved as:\n{output_path}")

if __name__ == "__main__":
    merge_files()
