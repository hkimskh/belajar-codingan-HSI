print("JADWAL SHOLAT - JSON API")
print("-" * 45)
import requests
kota = input("Masukkan nama kota: ")
url = f"https://api.aladhan.com/v1/timingsByCity/30-08-2025?city={kota}&country=Indonesia&method=8"
response = requests.get(url) 
data_json = response.json()
print(f"Jadwal Sholat {kota}")

jadwal_sholat = data_json['data']['timings'] # versi ringkas (dipotong)
print(f"-> Imsak = {jadwal_sholat['Imsak']}")
print(f"-> Shubuh = {jadwal_sholat['Fajr']}")
print(f"-> Dzuhur = {jadwal_sholat['Dhuhr']}")
print(f"-> Ashar = {jadwal_sholat['Asr']}")
print(f"-> Maghrib = {data_json['data']['timings']['Maghrib']}") 
print(f"-> Isya' = {jadwal_sholat['Isha']}")
