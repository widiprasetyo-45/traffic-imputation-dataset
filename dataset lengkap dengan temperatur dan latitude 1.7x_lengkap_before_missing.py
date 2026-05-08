import pandas as pd
import numpy as np

# Parameter dataset
num_locations = 10  # jumlah lokasi sensor
num_timesteps = 100  # jumlah timestep
locations = [f"Loc_{i}" for i in range(1, num_locations + 1)]

# Definisi rentang latitude dan longitude
latitudes = np.random.uniform(-8.5, -8.0, num_locations)  # Rentang latitude (contoh: wilayah Indonesia)
longitudes = np.random.uniform(114.2, 114.5, num_locations)  # Rentang longitude

# Definisi jenis jalan
road_types = ["Arterial", "Collector", "Local"]

# Simulasi data
data = []
for i, loc in enumerate(locations):
    for t in range(num_timesteps):
        timestamp = pd.Timestamp("2024-01-01 00:00:00") + pd.Timedelta(minutes=15 * t)
        speed = np.random.uniform(20, 80)  # Kecepatan (km/jam)
        volume = np.random.randint(10, 100)  # Volume kendaraan
        density = np.random.uniform(10, 50)  # Kepadatan (kendaraan/km)
        weather = np.random.choice(["Clear", "Rainy", "Cloudy"])  # Cuaca
        temperature = np.random.uniform(20, 35)  # Suhu (derajat Celcius)
        road_type = np.random.choice(road_types)  # Jenis jalan

        # Masukkan data ke dalam list
        data.append([
            timestamp, loc, latitudes[i], longitudes[i], speed, volume, density, weather, temperature, road_type
        ])

# Dataframe
df = pd.DataFrame(data, columns=[
    "Timestamp", "Location", "Latitude", "Longitude", "Speed", "Volume", "Density", "Weather", "Temperature", "RoadType"
])

# Simpan dataset (tanpa missing values)
df.to_csv("spatial_temporal_traffic_data_extended_100%.csv", index=False)
print("Dataset telah dibuat dan disimpan sebagai 'spatial_temporal_traffic_data_extended_100%.csv'.")
