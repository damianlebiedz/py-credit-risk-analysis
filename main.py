import pandas as pd
from visualization import plot_histograms, plot_target_distribution, plot_correlation_matrix

# Wczytaj dane z pliku
data = pd.read_csv('data/crx.data', header=None)  # header=None, jeśli nie ma nagłówków
print(data.head())  # Wyświetl pierwsze kilka wierszy

# Załaduj dane
data_path = 'data/crx.data'  # Ścieżka do danych
df = pd.read_csv(data_path, header=None)  # Wczytanie danych

# Przegląd danych
print(df.head())

# Wizualizacje
plot_histograms(df)
plot_target_distribution(df)
plot_correlation_matrix(df)