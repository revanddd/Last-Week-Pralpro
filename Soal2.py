import re
import random
import string

# Teks contoh
teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
zzouha@mail.com dimiliki oleh Kazuha
nynyeon@gmail.co.id dimiliki oleh Nayeon
kqryna@getnada.com dimiliki oleh Karina
qkyoujyn@tokopedia.com dimiliki oleh Kyujin
"""

pola_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = re.findall(pola_email, teks)

usn = [e.split('@')[0] for e in email]

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

for i in range(len(email)):
    username = usn[i]
    password = generate_password()
    print(f"{email[i]} username: {username} , password: {password}")
