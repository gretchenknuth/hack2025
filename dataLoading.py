import pandas as pd
import pyodbc

# Load CSV file
csv_file = "data/lines.csv"
lines_data = pd.read_csv(csv_file)
csv_file = "data/line_flows_nominal.csv"
line_flows_nominal = pd.read_csv(csv_file)