# Coohyaa

from requests import Session
import re, sys
s = Session()

try:
        print("SMS Gratis By Coohyaa \n Pake 62 Yaaa Biar Bisa ")
        no = int(input("No    : "))
        msg = input("Pesan : ")
except:
        print("\n\t* Cek nomermu atau pesanmu! *")
        sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
        'nohp':no,
        'pesan':msg,
        'captcha':captcha,
        'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
        print(f"\n Sudah Terkirim, Semoga Bahagia\n[{no}] => {msg}")
elif 'MAAF....!' in send:
        print("\n\t* Untuk Pesan Yg Sama Tunggu 15 Menit Kawan *")
else:
        print("\n\t* Gagal Ke Kirim ! *")
