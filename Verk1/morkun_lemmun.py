from collections import Counter
from reynir import Greynir

TEXT_PATH = "ic3_30k.txt"

# If Greynir is slow on your machine, set this to 20000 (allowed by assignment).
MAX_WORDS = 20000  # set to None to use the full file

def limit_to_n_words(text: str, n: int) -> str:
    if n is None:
        return text
    words = text.split()
    return " ".join(words[:n])

Nafnord = "no"
Sagnord = "so"
Lysingarord = "lo"

def main():
    text = open(TEXT_PATH, "r", encoding="utf-8").read()
    text = limit_to_n_words(text, MAX_WORDS)

    g = Greynir()
    job = g.submit(text)

    heildar_setningar = 0
    otaldar_setningar = 0

    lemma_fjoldi = Counter()
    lemma_set = set()

    #pos = part of speech
    pos_teljari = Counter()
    heildar_ord_tokar = 0

    for setn in job:
        heildar_setningar += 1

        ok = setn.parse()
        if not ok or setn.tree is None:
            otaldar_setningar += 1
            continue

        for node in setn.terminal_nodes:
            pos = node.tcat
            lemma = node.lemma

            if not pos:
                continue

            heildar_ord_tokar += 1

            lemma_set.add(lemma)
            lemma_fjoldi[lemma] += 1

            if pos in (Sagnord, Nafnord, Lysingarord):
                pos_teljari[pos] += 1
    
    print("a) Einstakar lemmur: ", len(lemma_set))

    if heildar_ord_tokar > 0:
        no_pct = 100.0 * pos_teljari[Nafnord] / heildar_ord_tokar
        so_pct = 100.0 * pos_teljari[Sagnord] / heildar_ord_tokar
        lo_pct = 100.0 * pos_teljari[Lysingarord] / heildar_ord_tokar
    else: 
        no_pct = so_pct = lo_pct = 0.0
    
    print("\nb) POS prosentur (af öllum orðum):")
    print(f"   Nafnorða hlutfall(no): {no_pct:.2f}%")
    print(f"   Sagnorða hlutfall (so): {so_pct:.2f}%")
    print(f"   Lýsingarorða hlutfall (lo): {lo_pct:.2f}%")
    print(f"   Heildarfjöldi orða tóka taldir: {heildar_ord_tokar}")

    print("\nc) 10 algengustu lemmurnar(greinarmerki ekki talin):")
    for lemma, n in lemma_fjoldi.most_common(10):
        print(f"{lemma}\t{n}")

    print("topp 10 algengustu orðin(lágstöfuð) voru: að, og, í, á, er, sem, til, við, um, með")
    print("topp 10 algengustu lemmurnar eru eftirf.:að, vera, og, í, á, sem, sá, til, um, hafa")
    print("'er' verður að 'vera', hinar algengu lemmurnar eru í sama formi og upprunalega orðið, og er talsvert algengari í lemmu formi")
    print("Munurinn þess fyrir utan er eiginlega mjög lítill sýnist mér, en orðið 'hafa' skýst þarna inn væntanlega vegna þess")
    print("að orðið 'hefur' eða álíka form af orðinu 'hafa' eru tíðari en breytt form af hinum orðunum.")

    if heildar_setningar > 0:
        otaldar_setningar_hlutfall = 100.0 * otaldar_setningar / heildar_setningar
    else:
        otaldar_setningar_hlutfall = 0.0
    
    print("\nd) Greynir oþattadar setningar:")
    print(f"   Heildar fjöldi setninga: {heildar_setningar}")
    print(f"   Óþáttaðar setningar: {otaldar_setningar}")
    print(f"   Hlutfall óþáttaðra setninga: {otaldar_setningar_hlutfall:.2f}%")
    print(f"   Greynir var mjög auðvelt í uppsetningu. Það kom mér alveg á óvart hversu hátt hlutfall óþáttaðra setningana var(23.91%).")
    print(f"   En ég hef svo sem ekkert viðmið þannig kannski er þessu bara viðbúið?")

if __name__ == "__main__":
    main()