print("﴾TUGAS AYAT KURSI﴿")
print("-" * 30)
import requests
url_arab = f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
response = requests.get(url_arab)
data_json = response.json()
ayat_arab = data_json['data']
print("Ayat kursi (2:225)")
print(f"{ayat_arab['text']}")
#ENGLISH TERJEMAHAN
url_eng = f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
response = requests.get(url_eng)
data_jsoon = response.json()
arti = data_jsoon['data']
print("ENGLISH:")
print(f"{arti['text']}")



