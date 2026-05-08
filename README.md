# traffic-imputation-dataset

Dataset sintetis lalu lintas untuk penelitian imputasi missing values dengan arsitektur CNN-LSTM + Multi-Head Attention.

## Parameter Dataset

| Parameter | Nilai |
|-----------|-------|
| Jumlah hari pengamatan | 4.17 hari (100 timestep × 15 menit) |
| Jumlah titik sensor | 10 lokasi (Loc_1 s.d Loc_10) |
| Frekuensi sampling | 15 menit |
| Missing rate aktual (data mentah) | 0% (complete data) |

## File dalam Repository

| File | Keterangan |
|------|-------------|
| `spatial_temporal_traffic_data_extended_100%_before_missing.csv` | Data lengkap (0% missing) - Ground truth |
| `spatial_temporal_traffic_data_extended.csv` | Data dengan missing 20% (MCAR) |
| `dataset lengkap dengan temperatur dan latitude 1.7x_lengkap_before_missing.py` | Kode generator data |

## Simulasi Missing
Missing values (20%) disimulasikan secara MCAR (Missing Completely at Random) pada complete dataset untuk evaluasi metode imputasi.

## Lisensi
MIT License
