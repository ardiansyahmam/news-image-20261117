[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ardiansyahmam/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# The World in One Image — Tuesday, 17 November 2026

Entry for the [make.fun bounty "Sum up 17 November's world news in one image"](https://make.fun/bounty/news-image-20261117).

`main.py` (Python 3.13, standard library only, no network) copies the
bundled front-page image `entry.png` to the output directory. The image is a
newspaper front page — "THE WORLD IN ONE IMAGE", Tuesday, 17 November 2026 —
summing up the day's world news in six stories plus an "ALSO" strip:

1. **Strait of Hormuz** — tanker ablaze as the US–Iran war escalates; Iran says a fourth tanker caught fire after a sea-mine strike and claims it seized a US drone; Bahrain says it intercepted a drone headed for a US base
2. **Kerch Bridge** — Ukraine strike damages the bridge; Ukraine hit the bridge, damaging a road section, and Russia struck two bridges in Kyiv
3. **Gaza** — Gaza faces a deadly winter, UN warns of hypothermia deaths; 1.7m displaced face cold and hunger
4. **Summit** — Xi, Trump & Putin to meet Thursday in Shenzhen
5. **Chips** — US tightens the AI chip curbs on China
6. **Japan** — jets scrambled over suspected Russian planes; Tokyo protests after two suspected Russian planes violated its airspace near Fukuoka

The image (1024×1024 PNG) was drawn with Python/PIL from flat geometric
shapes; the program is deterministic — every run writes the exact same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
