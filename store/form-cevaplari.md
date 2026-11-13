# Gökalp — Mağaza formlarının hazır cevapları

## Ücretli uygulama için bir kerelik şartlar (Mr. Anduv! hesabında daha önce yapılmadıysa)
- **App Store Connect:** Business → "Paid Apps" sözleşmesi imzalanmış, banka ve vergi (W-8BEN) bilgileri girilmiş olmalı. Yoksa fiyat 1,99 $ seçilemez.
- **Google Play Console:** Ödeme profili (Payments profile) açılmış ve hesaba bağlanmış olmalı.
- **Google Play'de dikkat:** Ücretsiz yayınlanan bir uygulama sonradan ücretliye çevrilemez. Gökalp ilk günden "Ücretli" açılmalı.

## Google Play Console → "Uygulamanızı ayarlayın"
- **Uygulama mı oyun mu:** Oyun · **Ücretli** · Fiyat: 1,99 $ (Play diğer ülkeleri otomatik çevirir)
- **Uygulama erişimi:** Tüm işlevler kısıtlamasız kullanılabilir (giriş yok).
- **Reklamlar:** Hayır.
- **İçerik derecelendirmesi (IARC):**
  - Kategori: Oyun
  - Şiddet: Evet, çizgi film tarzı. Kahraman kılıcını savurur; vurulan gölgeler ve kuyruklu yıldızlar ışık parçacıklarına dağılır. Kan yok.
  - Korku, cinsellik, çıplaklık, küfür, uyuşturucu/alkol/tütün, kumar: Hayır
  - Kullanıcı etkileşimi, sohbet, paylaşım, konum: Hayır
  - Dijital satın alma (uygulama içi): Hayır
- **Hedef kitle:** 13 yaş ve üzeri (13–15, 16–17, 18+). Çocuklara özel tasarlanmadı.
- **Veri güvenliği:** Veri toplanmıyor, paylaşılmıyor → "Hayır", form biter.
- **Gizlilik politikası URL'si:** https://emreanduv.github.io/gokalp/gizlilik.html
- **Mağaza kaydı:** `magaza-metinleri.md` · ikon `play-icon-512.png` · öne çıkan görsel `../assets/feature-graphic.png` · ekran görüntüleri `screenshots/`
- **Kategori:** Oyun → Aksiyon · Etiketler: Platform, Retro, Aksiyon, Uzay
- **İletişim e-postası:** emreanduvart@gmail.com

## Google Play → Kapalı test
- Kanal: "Kapalı test – Alpha"
- Test kullanıcıları: emreanduvart@gmail.com, muhammettanir1@gmail.com, melikebayramcavus@gmail.com 
- Ücretli uygulamada test kullanıcıları ücret ödemez (lisanslı test kullanıcısı olarak eklenirler).

## App Store Connect
- **Yeni uygulama:** Platform iOS · Ad: Gökalp · Dil: Türkçe · Bundle ID: `com.anduv.gokalp` · SKU: `gokalp`
- **Fiyatlandırma:** 1,99 $ fiyat kademesi, tüm ülkeler
- **Kategori:** Oyunlar → Aksiyon (ikincil: Macera)
- **Yaş derecesi anketi:** Çizgi film / fantastik şiddet: Seyrek/hafif. Diğerleri: Yok. Beklenen: 9+
- **Uygulama gizliliği:** Data Not Collected
- **Şifreleme (Export Compliance):** Info.plist'te `ITSAppUsesNonExemptEncryption = false`, ek belge gerekmez
- **TestFlight test kullanıcıları:** emreanduv@hotmail.com, zeynepbayramcavus@icloud.com, mbayramcavus@icloud.com, mebayramcavus@icloud.com

## Steam (Steamworks)
- Steam Direct ücreti: uygulama başına 100 $ (oyun 1000 $ brüt kazanınca geri ödenir)
- Fiyat: 1,99 $ (Steam'in önerdiği bölgesel fiyatları kabul et)
- İçerik anketi: Çizgi film şiddeti var, kan yok, olgun içerik yok
- Desteklenen: Windows, macOS, Linux (Steam Deck uyumlu: gamepad ve 16:10 ekran)
- Paketler: GitHub → Actions → "Masaüstü (Steam…)" → `steam_app_id` girilerek

## Meta Horizon Store (Quest)
- Uygulama türü: 2D (panel) uygulama · Fiyat: 1,99 $
- APK: GitHub → Actions → "Gokalp (Meta Quest APK)" → imzasız APK, yerelde `gokalp-quest.jks` ile imzalanır
- Kontrol: Quest kolları gamepad olarak çalışır (sol çubuk yürü, A zıpla, B kılıç)
