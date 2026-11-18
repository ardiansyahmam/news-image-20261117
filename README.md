[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The World in One Image — Tuesday, 17 November 2026

Entry for the [make.fun bounty "Sum up 17 November's world news in one image"](https://make.fun/bounty/news-image-20261117).

`main.py` (Python 3.13, standard library only, no network) copies the
bundled front-page image `entry.png` to the output directory. The image is a
vertical newspaper front page — "THE WORLD IN ONE IMAGE", Tuesday,
17 November 2026 — summing up the day's world news in 23 stories across
6 continents: 3 illustrated heroes (Strait of Hormuz, Kerch Bridge, Gaza),
then six colour-coded continent bands (Africa 3, Asia 6, Europe 4,
North America 4, South America 2, Oceania 1), closed by a "THE DAY IN FOUR
FIGURES" strip (1,441 drones, $120bn COP31 finance, 1.7m displaced in Gaza,
11,000+ Ebola cases). Every story happened or was first reported on Tuesday
17 November 2026; contested claims are marked as claims. Sources: Reuters,
AP, AFP, BBC, Al Jazeera, UN.

The image (768×1024 PNG) was drawn with Python/PIL from flat geometric
shapes; the program is deterministic — every run writes the exact same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
