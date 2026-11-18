# Gökalp TestFlight: grupları kurar (ilk seferde), testçileri ekler, son build'i iç ve dış gruba verir,
# dış test için beta incelemesine gönderir. Örnek: Kurt Yolu araclar/asc_testflight.py ve asc_metadata.py
import jwt, time, json, os, urllib.request, urllib.error
KID=os.environ['ASC_KEY_ID']; ISS=os.environ['ASC_ISSUER_ID']
KEY=open(os.path.expanduser(f'~/private_keys/AuthKey_{KID}.p8')).read()
NOT=os.environ.get('NOT') or 'İlk test: 7 dünya (Temir Kazık, Ay Dede, Ülker, Yedigen, Çolpan, Gök Göl, Kapadokya), kılıçla dövüş, Yelbegen, Tepegöz ve Van Gölü Canavarı. Yıldız tozu toplayın, notlarınızı yazın.'
out=[]
def ok(s): out.append(s); print(s)
def api(m,p,b=None):
    t=jwt.encode({'iss':ISS,'exp':int(time.time())+600,'aud':'appstoreconnect-v1'},KEY,algorithm='ES256',headers={'kid':KID})
    r=urllib.request.Request('https://api.appstoreconnect.apple.com/'+p,method=m,data=json.dumps(b).encode() if b else None,headers={'Authorization':'Bearer '+t,'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(r) as f: x=f.read(); return json.loads(x) if x else {}
    except urllib.error.HTTPError as e: ok(f'HATA {m} {p.split("?")[0]} {e.code} {e.read().decode()[:300]}'); return None
A=api('GET','v1/apps?filter[bundleId]=com.anduv.gokalp')['data'][0]['id']
KY=api('GET','v1/apps?filter[bundleId]=com.anduv.kurtyolu')['data'][0]['id']
for _ in range(60):
    d=(api('GET',f'v1/builds?filter[app]={A}&sort=-uploadedDate&limit=1') or {}).get('data') or []
    if d and d[0]['attributes'].get('processingState')=='VALID': break
    print('bekleniyor:', d[0]['attributes'].get('processingState') if d else 'henüz görünmüyor'); time.sleep(30)
b=d[0]; B=b['id']; ok('build '+b['attributes']['version']+' '+str(b['attributes'].get('processingState')))
if b['attributes'].get('usesNonExemptEncryption') is None:
    api('PATCH',f'v1/builds/{B}',{'data':{'type':'builds','id':B,'attributes':{'usesNonExemptEncryption':False}}})
TESTCI=['emreanduv@hotmail.com','zeynepbayramcavus@icloud.com','mbayramcavus@icloud.com','mebayramcavus@icloud.com']
mevcut={x['attributes']['name']:x['id'] for x in (api('GET',f'v1/apps/{A}/betaGroups') or {}).get('data',[])}
def grup(ad,internal):
    if ad in mevcut: return mevcut[ad]
    at={'name':ad,'isInternalGroup':internal}
    if internal: at['hasAccessToAllBuilds']=True
    r=api('POST','v1/betaGroups',{'data':{'type':'betaGroups','attributes':at,'relationships':{'app':{'data':{'type':'apps','id':A}}}}})
    if r: ok('grup kuruldu: '+ad)
    return r['data']['id'] if r else None
def testci_ekle(gid,emails):
    var={y['attributes'].get('email') for y in (api('GET',f'v1/betaGroups/{gid}/betaTesters?limit=50') or {}).get('data',[])}
    for e in emails:
        if e in var: continue
        r=api('POST','v1/betaTesters',{'data':{'type':'betaTesters','attributes':{'email':e},'relationships':{'betaGroups':{'data':[{'type':'betaGroups','id':gid}]}}}})
        if r is not None: ok('testçi eklendi '+e.split('@')[0][:3]+'…')
ig=grup('Mr. Anduv! Ekibi',True)
if ig:
    testci_ekle(ig,['emreanduv@hotmail.com'])
    if api('POST',f'v1/betaGroups/{ig}/relationships/builds',{'data':[{'type':'builds','id':B}]}) is not None: ok('iç gruba eklendi')
eg=grup('Mr. Anduv! Testçiler',False)
bl=api('GET',f'v1/apps/{A}/betaAppLocalizations')
if bl is not None and not bl['data']:
    api('POST','v1/betaAppLocalizations',{'data':{'type':'betaAppLocalizations','attributes':{'locale':'tr','feedbackEmail':'emreanduvart@gmail.com','description':'Kılıcı göktaşı demirinden bir alpin, mekanik posta güverciniyle gökten göğe uzandığı piksel aksiyon-platform oyunu: her dünyada başka yerçekimi, 1923 yıldız tozu.'},'relationships':{'app':{'data':{'type':'apps','id':A}}}}})
src=((api('GET',f'v1/apps/{KY}/betaAppReviewDetail') or {}).get('data') or {}).get('attributes') or {}
bd=api('GET',f'v1/apps/{A}/betaAppReviewDetail')
if bd and src:
    if api('PATCH',f'v1/betaAppReviewDetails/{bd["data"]["id"]}',{'data':{'type':'betaAppReviewDetails','id':bd['data']['id'],'attributes':{
        'contactFirstName':src.get('contactFirstName'),'contactLastName':src.get('contactLastName'),'contactPhone':src.get('contactPhone'),'contactEmail':src.get('contactEmail'),'demoAccountRequired':False}}}) is not None: ok('beta inceleme iletişim bilgisi (Kurt Yolu ile aynı)')
l=api('GET',f'v1/builds/{B}/betaBuildLocalizations')
if l is not None:
    if l['data']: api('PATCH',f"v1/betaBuildLocalizations/{l['data'][0]['id']}",{'data':{'type':'betaBuildLocalizations','id':l['data'][0]['id'],'attributes':{'whatsNew':NOT}}})
    else: api('POST','v1/betaBuildLocalizations',{'data':{'type':'betaBuildLocalizations','attributes':{'locale':'tr','whatsNew':NOT},'relationships':{'build':{'data':{'type':'builds','id':B}}}}})
if eg:
    if api('POST',f'v1/betaGroups/{eg}/relationships/builds',{'data':[{'type':'builds','id':B}]}) is not None: ok('dış gruba eklendi')
    testci_ekle(eg,TESTCI)
    st=api('GET',f'v1/builds/{B}/betaAppReviewSubmission')
    if st is not None and not st.get('data'):
        if api('POST','v1/betaAppReviewSubmissions',{'data':{'type':'betaAppReviewSubmissions','relationships':{'build':{'data':{'type':'builds','id':B}}}}}) is not None: ok('dış test beta incelemesine gönderildi')
    elif st: ok('beta inceleme durumu: %s'%st['data']['attributes'].get('betaReviewState'))
open('/tmp/rapor.txt','w').write('\n'.join(out)+'\n')
