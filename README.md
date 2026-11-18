[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The World in One Image — Tuesday, 17 November 2026

Entry for the [make.fun bounty "Sum up 17 November's world news in one image"](https://make.fun/bounty/news-image-20261117).

`main.py` (Python 3.13, standard library only, no network) copies the
bundled front-page image `entry.png` to the output directory. The image is a
newspaper front page — "THE WORLD IN ONE IMAGE", Tuesday, 17 November 2026 —
summing up the day's world news in six stories plus an "ALSO" strip:

1. **Strait of Hormuz** — fourth tanker ablaze as the US–Iran war escalates
2. **Kerch Bridge** — Ukraine strike collapses part of the bridge
3. **Gaza** — the West urges Israel to open Gaza crossings
4. **Summit** — Xi, Trump & Putin to meet Thursday in Shenzhen
5. **Chips** — US tightens the AI chip export ban on China
6. **Japan** — jets scrambled as Russian planes enter its airspace

The image (1024×1024 PNG) was drawn with Python/PIL from flat geometric
shapes; the program is deterministic — every run writes the exact same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
