#!/usr/bin/env python3
"""Gökalp mağaza görselleri: ikon, açılış ekranı, Google Play öne çıkan görseli.
Oyunun kendi piksel çizimlerinden (www/index.html ile aynı satırlar) üretilir.
Kullanım: python3 araclar/gorseller.py   (gerekirse: pip install pillow fonttools brotli)
"""
import io, os, random
from PIL import Image, ImageDraw, ImageFont

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAL = {'k': '#101018', 's': '#f0b088', 'h': '#3a2414', 'r': '#c83a28', 'g': '#f0c040', 'b': '#2a4aa0', 'm': '#a8b8d0', 'w': '#f8f8f8'}
TOP = ["....kk", "...kmmk", "..kmmgmk", ".kmmmgmmk", ".kkkkkkkkk", ".khhssssk", ".khssskssk", ".khsssssk", "..kksssk", "..kkrrrkk",
       ".krrrgrrrk", "krrrrgrrrsk", "ksrrrgrrrsk", "kskrrgrrkk", ".kkrrgrrk", ".kggggggk", ".krrrrrrk"]
LA = [".kbbbkbbk", ".kbbbkbbk", ".kbbk.kbbk", ".kbbk.kbbk", ".kkkk.kkkk", "kkkkk.kkkkk"]
GECE_UST, GECE_ALT = (7, 11, 36), (29, 44, 94)


def hex2(c):
    c = c.lstrip('#'); return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def kahraman(olcek):
    """Kılıcı yukarıda duran alp; şeffaf zeminli büyütülmüş sprite."""
    rows = TOP + LA
    w = max(len(r) for r in rows) + 2
    im = Image.new('RGBA', (w, len(rows)), (0, 0, 0, 0))
    px = im.load()
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch in PAL:
                px[x, y] = hex2(PAL[ch]) + (255,)
    for y in range(1, 11):  # kılıç
        px[9, y] = hex2('#f8f8f8') + (255,); px[10, y] = hex2('#cfe0f0') + (255,)
    for x in range(8, 12):
        px[x, 11] = hex2('#f0c040') + (255,)
    return im.resize((im.width * olcek, im.height * olcek), Image.NEAREST)


def gokyuzu(w, h, tohum=1923):
    im = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(im)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(GECE_UST, GECE_ALT)))
    r = random.Random(tohum)
    s = max(2, w // 300)
    for _ in range(int(w * h / 9000)):
        x, y = r.randrange(w), r.randrange(int(h * .8))
        d.rectangle([x, y, x + s - 1, y + s - 1], fill=(255, 255, 255) if r.random() < .7 else (255, 246, 192))
    return im


def kutup_yildizi(d, cx, cy, r, renk='#bfe8ff'):
    k = max(2, r // 4)
    d.rectangle([cx - k, cy - r, cx + k, cy + r], fill=renk)
    d.rectangle([cx - r, cy - k, cx + r, cy + k], fill=renk)
    d.rectangle([cx - k, cy - k, cx + k, cy + k], fill='#ffffff')


def zemin(d, w, h, ust, blok):
    for x in range(0, w, blok):
        d.rectangle([x, ust, x + blok - 1, h], fill='#4a5878')
        d.rectangle([x, ust, x + blok - 1, ust + blok // 8], fill='#9fb0d2')
        d.line([(x, ust), (x, h)], fill='#2e3850', width=max(1, blok // 16))
        for yy in range(ust + blok // 2, h, blok // 2):
            d.line([(x, yy), (x + blok, yy)], fill='#2e3850', width=max(1, blok // 16))


def yazi_tipi(boy):
    yol = os.path.join(KOK, 'www', 'fonts', 'pixelify-sans-latin-ext-700-normal.woff2')
    try:
        from fontTools.ttLib import TTFont
        # latin + latin-ext dosyalarını ayrı ayrı açıp harfe göre seçmek yerine, iki dosyayı da yükleyip deneriz
        f1 = TTFont(os.path.join(KOK, 'www', 'fonts', 'pixelify-sans-latin-700-normal.woff2')); b1 = io.BytesIO(); f1.flavor = None; f1.save(b1)
        f2 = TTFont(yol); b2 = io.BytesIO(); f2.flavor = None; f2.save(b2)
        return ImageFont.truetype(io.BytesIO(b1.getvalue()), boy), ImageFont.truetype(io.BytesIO(b2.getvalue()), boy)
    except Exception:
        f = ImageFont.load_default(); return f, f


def yaz(d, x, y, metin, boy, renk, golge='#7a1c14'):
    """Türkçe harfleri (latin-ext) doğru dosyadan çizer; 'Ö' latin dosyasında, 'ı' latin dosyasında, 'ğşİ' latin-ext'te."""
    lat, ext = yazi_tipi(boy)
    for ch in metin:
        f = ext if ch in 'ğĞşŞİ' else lat
        d.text((x + boy // 12, y + boy // 12), ch, font=f, fill=golge)
        d.text((x, y), ch, font=f, fill=renk)
        x += d.textlength(ch, font=f)
    return x


def ikon(boyut=1024, onplan=False):
    im = Image.new('RGBA', (boyut, boyut), (0, 0, 0, 0)) if onplan else gokyuzu(boyut, boyut).convert('RGBA')
    d = ImageDraw.Draw(im)
    if not onplan:
        kutup_yildizi(d, int(boyut * .78), int(boyut * .2), boyut // 14)
        zemin(d, boyut, boyut, int(boyut * .82), boyut // 8)
    k = kahraman(boyut // 34)
    im.alpha_composite(k, ((boyut - k.width) // 2 + boyut // 40, int(boyut * (.86 if not onplan else .9)) - k.height))
    return im


def acilis(boyut=2732):
    im = gokyuzu(boyut, boyut).convert('RGBA')
    d = ImageDraw.Draw(im)
    kutup_yildizi(d, boyut // 2, int(boyut * .3), boyut // 30, '#f0c040')
    k = kahraman(boyut // 90)
    im.alpha_composite(k, ((boyut - k.width) // 2, int(boyut * .62) - k.height))
    return im.convert('RGB')


def one_cikan():
    w, h = 1024, 500
    im = gokyuzu(w, h).convert('RGBA')
    d = ImageDraw.Draw(im)
    kutup_yildizi(d, 900, 80, 30)
    zemin(d, w, h, 420, 64)
    k = kahraman(14)
    im.alpha_composite(k, (90, 420 - k.height))
    x = yaz(d, 330, 150, 'GÖKALP', 120, '#e0b048')
    lat, _ = yazi_tipi(26)
    d.text((336, 300), 'Bir Mr. Anduv! yapımıdır.', font=lat, fill='#eef2fb')
    return im.convert('RGB')


def main():
    a = os.path.join(KOK, 'assets'); os.makedirs(a, exist_ok=True)
    ikon().convert('RGB').save(os.path.join(a, 'icon-only.png'))
    ikon(onplan=True).save(os.path.join(a, 'icon-foreground.png'))
    acilis().save(os.path.join(a, 'splash.png')); acilis().save(os.path.join(a, 'splash-dark.png'))
    one_cikan().save(os.path.join(a, 'feature-graphic.png'))
    i512 = ikon().convert('RGB').resize((512, 512), Image.LANCZOS)
    i512.save(os.path.join(KOK, 'store', 'play-icon-512.png')); i512.save(os.path.join(KOK, 'www', 'ikon-512.png'))
    print('Görseller üretildi: assets/, store/play-icon-512.png, www/ikon-512.png')


if __name__ == '__main__':
    main()
