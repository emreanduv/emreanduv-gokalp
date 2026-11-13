# Gökalp — Yayın durumu (13 Kasım 2026)

Fiyat her mağazada **1,99 $** (ücretli uygulama; reklam ve uygulama içi satın alma yok). Ad her mağazada aynı: **Gökalp**.

## Hazır olanlar
- Oyun taslağı 0.3: Temir Kazık (normal yerçekimi), Ay Dede (düşük yerçekimi) ve Ülker (orta yerçekimi, 7 ada, gök salları, ilk boss Yelbegen) dünyaları, kılıç, Erlik gölgeleri, kuyruklu yıldızlar, yıldız tozu (hedef 1923), mekanik güvercin rehberi, Gök Haritası
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
- 0.4: Yedigen (yedi han, yedi boss), Çolpan (ışık bulmacaları), Gök Göl (Van Gölü Canavarı)
- 1.0: Mağazalara ilk sürüm; 1923 yıldız tozunun tamamı
- VR: sıfır yerçekimli bölümler Meta Quest'te maket görünümüyle
- Saat: "Gökalp: Yıldız Tozu" (`store/saat-plani.md`)
