import asyncio
from pathlib import Path

import aiofiles
import spacy


async def process_files(in_path, out_path):
    pathlist = Path(in_path).glob("*")
    nlp = spacy.load("hu_core_news_lg")

    for path in pathlist:
        try:
            async with aiofiles.open(f"{in_path}/{path.name}", mode="r") as infile:
                lines = await infile.read()
                lines = lines.split("\n")
                ls = [s.strip() for s in lines]
                ls = ".\n".join(ls)
                t = nlp(ls)
                lemmas = [token.lemma_.lower() for token in t]
                size = len(lemmas)
                idx_list = [idx + 1 for idx, val in enumerate(lemmas) if val == "."]
                splitted = [
                    lemmas[i : j - 1]
                    for i, j in zip(
                        [0] + idx_list,
                        idx_list + ([size] if idx_list[-1] != size else []),
                    )
                ]
                splitted = [" ".join(e).strip() for e in splitted]
                splitted = "\n".join(splitted)
            async with aiofiles.open(
                f"{out_path}/{path.name}_lemmas.txt", mode="w"
            ) as outfile:
                await outfile.write(splitted)
        except Exception as e:
            print(e)
            continue


asyncio.run(process_files("data/interim/slices", "data/processed/wikipedia"))
