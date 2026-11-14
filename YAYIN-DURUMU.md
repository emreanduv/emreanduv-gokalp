# Gökalp — Yayın durumu (13 Kasım 2026)

Fiyat her mağazada **1,99 $** (ücretli uygulama; reklam ve uygulama içi satın alma yok). Ad her mağazada aynı: **Gökalp**.

## Hazır olanlar
- Görsel yenileme (15 Kasım 2026, Mr. Anduv! Görsel Kayıt Defteri çizgisi): piksel kareler yerine konturlu, gölgeli, ışıklı çizgi film çizimleri — Gökalp, mekanik güvercin, Erlik gölgeleri, yıldız tozu, kuyruklu yıldızlar, Yelbegen, Tepegöz, Van Gölü Canavarı, Van kedisi, han ateşleri, karolar, 7 dünyanın boyalı gökleri, HUD, başlık ve kart; ayrıca Ülker ve Yedigen'de her karede çöken çizim hatası giderildi. Yazı tipi Pixelify yerine Bungee + Rubik (internetsiz, `www/fonts`). Kaynak: `www/gorsel.js` (index.html'e gömülü). Mağaza ekran görüntüleri yeni görünümle yeniden çekilecek.
- Oyun taslağı 0.4: Temir Kazık (normal yerçekimi), Ay Dede (düşük yerçekimi), Ülker (orta yerçekimi, 7 ada, gök salları, boss Yelbegen) Yedigen (ağır yerçekimi, 7 han ateşi = ara kayıt, boss Tepegöz), Çolpan (hafif yerçekimi, ışık taşları ve ışık köprüleri) Gök Göl (yüzme, su altı yolları, inci kefalleri, boss Van Gölü Canavarı, Van kedisi) ve Kapadokya (peribacaları, karanlık yeraltı şehri, sıcak hava balonları) dünyaları; dünyalar sırayla açılır, kılıç, Erlik gölgeleri, kuyruklu yıldızlar, yıldız tozu (hedef 1923), mekanik güvercin rehberi, Gök Haritası
- Tulpar'dan gelen kabuk: klasik kumanda (Kurt Yolu ölçüsü), dil sorusu her açılışta, Nasıl Oynanır, Ayarlar (dil, ses, puan, Bize yaz, Verilerimi sil), Mola, paylaş, oyun kolu ve klavye
- Capacitor projesi: Android ve iOS `com.anduv.gokalp`, ikonlar ve açılış ekranları üretildi
- İş akışları: iOS (TestFlight), Android (.aab), Masaüstü (Steam), Quest (APK) — her biri yayın öncesi kontrolle başlar
- Mağaza metinleri TR/EN, form cevapları, gizlilik politikası, saat planı

## Japonya dönüşü Mr. Anduv!'un son adımları (anahtar / onay)
1. **GitHub:** Depoyu gizliye (private) çevir; `ASC_KEY_P8` secret'ını ekle (Malazgirt/Tulpar'daki Apple anahtarının aynısı).
2. **App Store Connect:** Yeni uygulama → Bundle ID `com.anduv.gokalp`, SKU `gokalp`, fiyat 1,99 $.
3. **Google Play Console:** Yeni uygulama "Gökalp", **Ücretli** → `.aab`'yi `imza-anahtari/gokalp-upload.jks` ile imzala, Kapalı test'e yükle.
4. **Steam:** App ID gelince "Masaüstü" iş akışını çalıştır.
5. **Meta Horizon:** Quest iş akışı oyunu emreanduv.github.io/gokalp adresinden paketler; oyun oraya konunca APK üretilir, imzalanıp yüklenir.

## İmza anahtarları — KAYBETME
- Android yükleme anahtarı: `imza-anahtari/gokalp-upload.jks` (git dışında). Oluşturmak için:
  `keytool -genkeypair -v -keystore imza-anahtari/gokalp-upload.jks -alias gokalp -keyalg RSA -keysize 2048 -validity 10000`
- Quest anahtarı: `imza-anahtari/gokalp-quest.jks`

## Yol haritası
- 0.3: Ülker (7 ada, gök salları), ilk boss Yelbegen (Tulpar'daki çizimin aynısı) — tamam
- 0.4: Yedigen (yedi han ateşi, boss Tepegöz) — tamam
- 0.5: Çolpan (ışık köprüleri), Gök Göl (yüzme, Van Gölü Canavarı) — tamam
- 0.6: Dünyalar sırayla açılır, Kapadokya (peribacaları, yeraltı şehri, balonlar), iniş sesi — tamam
- 0.7: Hikâye ara sahneleri (güvercinin anlattığı kısa kartlar), hanlara bekçiler, ayarlar: titreşim, müzik/efekt ayrı ses
- 1.0: Mağazalara ilk sürüm; 1923 yıldız tozunun tamamı
- VR: sıfır yerçekimli bölümler Meta Quest'te maket görünümüyle
- Saat: "Gökalp: Yıldız Tozu" (`store/saat-plani.md`)
