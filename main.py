import pandas as pd

# Wczytaj dane z pliku
data = pd.read_csv('data/credit+approval/crx.data', header=None)  # header=None, jeśli nie ma nagłówków
print(data.head())  # Wyświetl pierwsze kilka wierszy
