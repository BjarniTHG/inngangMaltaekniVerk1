from datasets import load_dataset
#Gögn eru 30.000 orð valin frá random stöðum í Miðeindar IC3 safninu. Ég ítraði í gegnum random seeds þangað til ég fékk gögn sem voru ekki frá Alþingi.

DATASET_NAME = "mideind/icelandic-common-crawl-corpus-IC3-v2"
TARGET = 30_000
MIN_DOC_WORDS = 200
SEED = 26
BUFFER_SIZE = 10_000

TEXT_KEYS = ["text", "content", "body", "document", "doc", "article"]

dataset = load_dataset(DATASET_NAME, split="train", streaming=True)
dataset = dataset.shuffle(seed=SEED, buffer_size=BUFFER_SIZE)

texts = []
word_count = 0

for example in dataset:
    text = None
    for k in TEXT_KEYS:
        if k in example and isinstance(example[k], str):
            text = example[k]
            break
    if text is None:
        continue

    words = text.split()
    if len(words) < MIN_DOC_WORDS:
        continue

    remaining = TARGET - word_count
    if remaining <= 0:
        break

    if len(words) > remaining:
        texts.append(" ".join(words[:remaining]))
        word_count += remaining
        break

    texts.append(text)
    word_count += len(words)

print("Fjöldi safnaðra orða:", word_count)
print("Gögn fengin frá:", len(texts), " skrám")

with open("ic3_30k.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(texts))
