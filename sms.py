# Coohyaa
#666C666

from requests import Session
import re, sys
s = Session()

try:
        print("SMS Gratis by Coohyaa\nGunakan 62 Yaa Kawan")
        no = int(input("No    : ")
        msg = input("Pesan : ")
except:                                                                                                                       print("\n\t* Cek nomermu atau pesanmu! *")
        sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTM                 >
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
        print(f"\nSudah Terkirim Semoga Bahagia\n[{no}] => {msg}")
elif 'MAAF....!' in send:
        print("\n\t* Klo Mau Ngirim Ke Nomor Yg Sama Tunggu 15 Menit ya *")
else:
        print("\n\t* Waduh Gagal *")