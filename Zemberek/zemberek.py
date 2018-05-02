# -*- coding: utf-8 -*-
"""
Kod   : Ahmet Aksoy
Sistem: Ubuntu 14.04 LTS
Python: Python 3.5.1
Modül : JPype1-py3 0.5.5.2
"""
import jpype
# JVM başlat
# Aşağıdaki adresleri java sürümünüze ve jar dosyasının bulunduğu klasöre göre değiştirin
jpype.startJVM("/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so",
         "-Djava.class.path=/home/ax/PycharmProjects/trdp/zemberek-tum-2.0.jar", "-ea")
# Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla
Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
# tr nesnesini oluştur
tr = Tr()
# Zemberek sınıfını yükle
Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
# zemberek nesnesini oluştur
zemberek = Zemberek(tr)
#Çözümlenecek örnek kelimeleri belirle
kelimeler = ["merhabalaştık","dalgalarının","habercisi","tırmalamışsa"]
for kelime in kelimeler:
    if kelime.strip()>'':
        yanit = zemberek.kelimeCozumle(kelime)
        if yanit:
            print("{}".format(yanit[0]))
        else:
            print("{} ÇÖZÜMLENEMEDİ".format(kelime))
#JVM kapat
jpype.shutdownJVM()
