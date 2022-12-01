import asyncio

import aiofiles
import spacy


async def process_file(data_file, out_file):
    nlp = spacy.load("hu_core_news_lg")
    async with aiofiles.open(data_file, mode='r') as f:
        async with aiofiles.open(out_file, mode="w") as outfile:
            async for line in f:
                lemmas = []
                t = nlp(line)
                for token in t:
                    lemmas.append(token.lemma_.lower())
                t = " ".join(lemmas)
                await outfile.write(t)


asyncio.run(process_file("data/interim/huwiki.txt", "data/processed/huwiki.txt"))
print("Done")
