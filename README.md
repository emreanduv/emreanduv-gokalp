# Gökalp

Piksel grafikli, yandan görünümlü aksiyon-platform oyunu. Kılıcı göktaşı demirinden bir alp, mekanik bir posta güverciniyle gök haritasında dünyadan dünyaya atlar; her dünyanın yerçekimi farklıdır. Yol boyunca 1923 yıldız tozu saklıdır. Reklamsız, internetsiz, veri toplamaz. Fiyat: 1,99 $.

Bir Mr. Anduv! yapımıdır.

Tulpar'ın kardeş oyunudur: kabuk, klasik kumanda, rehber, ayarlar ve yayın düzeni Tulpar'dan gelir; iki oyundaki iyileştirmeler birbirine taşınır.

## Klasörler
- `www/` → Oyunun kendisi (tek dosya `index.html`, internetsiz çalışır; yazı tipi Pixelify Sans, SIL OFL, `www/fonts/`)
- `android/` → Android Studio projesi (Capacitor, paket `com.anduv.gokalp`)
- `ios/` → Xcode projesi (Capacitor, `com.anduv.gokalp`)
- `desktop/` → Steam kabuğu (Electron + steamworks.js; Windows, macOS, Linux/Pardus)
- `assets/` → İkon 1024, açılış ekranı, Google Play öne çıkan görsel (`araclar/gorseller.py` üretir)
- `store/` → Mağaza metinleri (TR/EN), form cevapları, gizlilik politikası, saat planı
- `araclar/` → `yayin-kontrol.sh` (yayın öncesi kontrol), `turkce-yazi-kontrol.py`, `gorseller.py`
- `.github/workflows/` → iOS (TestFlight), Android (`.aab`), Masaüstü (Steam), Quest (APK)

## Bilgisayarda deneme
```
npm install
npm run serve        # http://localhost:8771/www/
```
Klavye: ← → yürü · Z / Boşluk zıpla (basılı tut: daha yüksek) · X kılıç · Esc menü. Oyun kolu da çalışır.

## Oyunu değiştirince
`www/index.html` içinde düzenle → `npx cap sync` → GitHub'a gönder → Actions'tan ilgili iş akışını elle başlat.
Görselleri yenilemek için: `python3 araclar/gorseller.py && npm run ikonlar`.
