# úttak á spurningu 2
(.venv) PS C:\Users\bjarn\OneDrive\Desktop\InngangurMaltaekni> python tokenizer.py
### a) Heildar fjöldi tóka: 34248
### b) Heildar fjöldi einstakra tóka: 8777

### c) 10 algengustu tókarnir (greinarmerki ekki talin með):
| Orð | tíðni |
| :--- | :--- |
| `að` | 1157 |
| `og` | 1070 |
| `í` | 872 |
| `á` | 732 |
| `sem` | 569 |
| `er` | 566 |
| `til` | 426 |
| `um` | 349 |
| `við` | 334 |
| `fyrir` | 220 |

### d) 10 algengustu tókarnir eftir lágstöfun:
| Orð | tíðni |
| :--- | :--- |
| `að` | 1190 |
| `og` | 1080 |
| `í` | 931 |
| `á` | 760 |
| `er` | 576 |
| `sem` | 572 |
| `til` | 438 |
| `við` | 371 |
| `um` | 363 |
| `með` | 231 |


### Mismunur milli c og d?
Top c: ['að', 'og', 'í', 'á', 'sem', 'er', 'til', 'um', 'við', 'fyrir']

Top d: ['að', 'og', 'í', 'á', 'er', 'sem', 'til', 'við', 'um', 'með']

Hvers vegna: að þvinga öll orð í lágstöfun leyfir orðum sem eru annars oft með hástaf sem fyrsta staf að teljast með sem notkun á sama orði.
Orð sem mikið notuð í byrjun setninga munu verða algengari

### e) Tókar með > 12 stöfum (10 alengustu):
| Orð | tíðni |
| :--- | :--- |
| `hjúkrunarfræðinga` | 24 |
| `þjóðaratkvæðagreiðslu` | 11 |
| `Sjálfstæðisflokksins` | 9 |
| `heilbrigðisþjónustu` | 7 |
| `Bráðabirgðaákvæði` | 7 |
| `already_booked` | 7 |
| `hlutfallslega` | 7 |
| `forsætisráðherra` | 6 |
| `ríkisstjórnar` | 6 |
| `Fjármálaráðherra` | 6 |

### f) Lengsti tóki: www.summerville-novascotia.com/AmericanMotors/
   Lengd: 46
Lengsti tókinn er URL, sem er líklega eins og verður hjá öllum sem velja URL sem sérstaka atriðið sitt, geri ég ráð fyrir


# úttak á spurningu 3
(.venv) PS C:\Users\bjarn\OneDrive\Desktop\InngangurMaltaekni> python morkun_lemmun.py
### a) Einstakar lemmur:  3362

### b) POS prósentur (af öllum orðum)

- **Nafnorða hlutfall (no):** 28.87%  
- **Sagnorða hlutfall (so):** 18.37%  
- **Lýsingarorða hlutfall (lo):** 6.96%  
- **Heildarfjöldi orða tóka taldir:** 14015  

---

### c) 10 algengustu lemmurnar (greinarmerki ekki talin með)

| Orð | Tíðni |
| :--- | ---: |
| `að` | 670 |
| `vera` | 636 |
| `og` | 523 |
| `í` | 452 |
| `á` | 291 |
| `sem` | 283 |
| `sá` | 231 |
| `til` | 204 |
| `um` | 183 |
| `hafa` | 151 |

Topp 10 algengustu orðin (lágstöfuð) voru:  
**að, og, í, á, er, sem, til, við, um, með**

Topp 10 algengustu lemmurnar eru:  
**að, vera, og, í, á, sem, sá, til, um, hafa**

'er' verður að 'vera', hinar algengu lemmurnar eru í sama formi og upprunalega orðið, og er talsvert algengari í lemmu formi
Munurinn þess fyrir utan er eiginlega mjög lítill sýnist mér, en orðið 'hafa' skýst þarna inn væntanlega vegna þess
að orðið 'hefur' eða álíka form af orðinu 'hafa' eru tíðari en breytt form af hinum orðunum.

### d) Greynir óþáttaðar setningar

- **Heildarfjöldi setninga:** 1029  
- **Óþáttaðar setningar:** 246  
- **Hlutfall óþáttaðra setninga:** 23.91%  

   Greynir var mjög auðvelt í uppsetningu. Það kom mér alveg á óvart hversu hátt hlutfall óþáttaðra setningana var(23.91%).
   En ég hef svo sem ekkert viðmið þannig kannski er þessu bara viðbúið?