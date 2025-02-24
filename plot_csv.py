import pandas as pd
import matplotlib.pyplot as plt

# Path to your CSV file
file_path = './2025_02_22_test/NIRPBF4E4CF5-5percent.csv'

# Read the CSV file
data = pd.read_csv(file_path)

# Convert the time column to datetime format (update 'time' if your column has a different name)
if 'ts' in data.columns:
    data['ts'] = pd.to_datetime(data['ts'], errors='coerce')
    # Remove rows where conversion failed
    data = data.dropna(subset=['ts'])
    # Sort the data by time
    data = data.sort_values('ts')
else:
    print("No 'ts' column found in the CSV file. Please update the column name accordingly.")
    exit()

# If you have a specific numeric column to plot, set its name here (e.g., 'value')
numeric_column = 'value'
if numeric_column in data.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(data['ts'], data[numeric_column], marker='o',markersize=1, linestyle='-', label=numeric_column)
    plt.xlabel('Time')
    plt.ylabel(numeric_column)
    plt.title(f"Time Series Plot of {numeric_column}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    # Alternatively, if you want to plot all numeric columns (except the time column), do:
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if 'time' in numeric_cols:
        numeric_cols.remove('time')
    if not numeric_cols:
        print("No numeric columns found to plot.")
    else:
        plt.figure(figsize=(12, 6))
        for col in numeric_cols:
            plt.plot(data['ts'], data[col], marker='o',markersize=1, linestyle='-', label=col)
        plt.xlabel('Time',fontsize=20,labelpad=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.ylabel("Value",fontsize=20,labelpad=15)
        title = "NIRS Ball on 5% Black Dye Ecoflex"
        plt.title(title,fontsize=20,pad=15)
        plt.legend(fontsize=20)
        plt.grid(True)
        plt.tight_layout()
        filename = title.replace(" ", "_") + ".png"
        plt.savefig(filename, dpi=900, bbox_inches='tight')
        plt.show()
        