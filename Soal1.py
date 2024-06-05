import re
from datetime import datetime

teks = {"Le Sserafim debut pada tanggal 2022-05-02, dan memiliki 5 anggota yaitu Miyawaki Sakura, Kim Chaewon, Lee Yunjin, Nakamura Kazuha, dan Hong Eunchae. Sakura lahir pada tanggal 1998-03-19, Chaaewon lahir pada tanggal 2000-08-01, Yunjin lahir pada tanggal 2001-10-08, Kazuha lahir pada tanggal 2003-08-09, dan Eunchae lahir pada tanggal 2006-11-10."
}
pola = r'\b\d{4}-\d{2}-\d{2}\b'

tanggal = re.findall(pola, teks)

tanggal_sekarang = datetime.now()

for t in tanggal:
    t_datetime = datetime.strptime(t, '%Y-%m-%d')
    selisih_hari = (tanggal_sekarang - t_datetime).days
    print(f"{t} 00:00:00 selisih {selisih_hari} hari")