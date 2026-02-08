import re
from collections import Counter

#regex skilgreiningar
#1. URL - Sem valið mitt höndla ég vefsíður sem staka tóka, og geri það þannig að ég túlka allt sem fylgir annaðhvort 'http(s)' eða 'www' sem stakan tóka(fyrir næsta _ bil)
URL_RE = r"""
(?:https?://[^\s<>"')\]]+)
|
(?:www\.[^\s<>"')\]]+)
"""

#[^\W\d_] er allt nema tölur og undirstrik
WORD_RE = r"""
[^\W\d_]+
(?:[-'’][^\W\d_]+)*
"""
#\d+(?:[.,]\d+)? er basically bara allar tölur, og þannig að punktar eða kommur rjúfa ekki tókan
NUM_RE = r"""
\d+(?:[.,]\d+)?
"""
#"greinarmerki"(þýðingin á "punctuality" sem google translate gaf mér, vissi ekki að þetta væri rétta orðið)
PUNCT_RE = r"""
[.,!?;:"“”‘’()\[\]{}…–—\-]
"""

OTHER_RE = r"""
[^\s]
"""

TOKEN_PATTERN = re.compile(
    rf"""
    (?P<URL>{URL_RE})
    |(?P<WORD>{WORD_RE})
    |(?P<NUM>{NUM_RE})
    |(?P<PUNCT>{PUNCT_RE})
    |(?P<OTHER>{OTHER_RE})
    """,
    re.VERBOSE | re.UNICODE
)

def tokenize(text: str):
    tokens = []
    for m in TOKEN_PATTERN.finditer(text):
        tokens.append((m.group(0), m.lastgroup))
    return tokens


text = open("ic3_30k.txt", "r", encoding="utf-8").read()
typed_tokens = tokenize(text)

# a) heildarfjöldi tóka
total_tokens = len(typed_tokens)

# b) fjöldi einstakra tóka
unique_tokens = len({tok for tok, kind in typed_tokens})

print("a) Heildar fjöldi tóka:", total_tokens)
print("b) Heildar fjöldi einstakra tóka:", unique_tokens)

# Fyrir c-f, hendum við út greinarmerkjum:
# Höldum bara WORD/NUM/URL.
content_tokens = [tok for tok, kind in typed_tokens if kind in ("WORD", "NUM", "URL")]

freq = Counter(content_tokens)

print("\nc) 10 algengustu tókarnir (greinarmerki ekki talin með):")
for tok, n in freq.most_common(10):
    print(f"{tok}\t{n}")

# d) lágstöfun (URLs og tölur eins; en orð breytast)
content_tokens_lower = [tok.lower() for tok in content_tokens]
freq_lower = Counter(content_tokens_lower)

print("\nd) 10 algengustu tókarnir eftir lágstöfun:")
for tok, n in freq_lower.most_common(10):
    print(f"{tok}\t{n}")

top_c = [t for t, _ in freq.most_common(10)]
top_d = [t for t, _ in freq_lower.most_common(10)]
print("\nMismunur milli c og d?")
print("Top c:", top_c)
print("Top d:", top_d)
print("Hvers vegna: að þvinga öll orð í lágstöfun leyfir orðum sem eru annars oft með hástaf sem fyrsta staf að teljast með sem notkun á sama orði.")
print("Orð sem mikið notuð í byrjun setninga munu verða algengari")
print("Það kemur mér á óvart að orðið 'með' er greinilega nógu oft fyrsta orðið í setningu til að lágstöfun setji það í topp 10")
print("og bolar út orðinu 'fyrir'. Þess fyrir utan haldast topp 10 orðin nánast eins, með smá breytingu á röðinni")

# e) tókar sem eru lengri en 12 stafir
long_tokens = [t for t in content_tokens if len(t) > 12]
freq_long = Counter(long_tokens)

print("\ne) Tókar með > 12 stöfum (10 alengustu):")
for tok, n in freq_long.most_common(10):
    print(f"{tok}\t{n}")

# f) Lengsti tókur
if content_tokens:
    longest = max(content_tokens, key=len)
    print("\nf) Lengsti tóki:", longest)
    print("   Lengd:", len(longest))
    print("Lengsti tókinn er URL, sem er líklega eins og verður hjá öllum sem velja URL sem sérstaka atriðið sitt, geri ég ráð fyrir")
else:
    print("\nf) Lengsti: <none>")
