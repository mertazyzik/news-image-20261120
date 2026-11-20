# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/mertazyzik/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/mertazyzik/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page that sums up Friday 20 November 2026's world news in a single image: the World Court's genocide ruling on Myanmar, the Trump–Xi–Putin summit in Shenzhen, the Houthi missile strike on Riyadh, Kyiv and the Crimea Bridge, sliding markets, Kenya's Ebola milestone, COP31, GTA 6 and Voyager 1. Every fact was checked against reporting of 20 November 2026 (BBC, The Guardian, Al Jazeera, CNBC, UN News, The Hindu, France 24).

The image is drawn deterministically by `draw.py` (Python + Pillow, no network, fixed fonts) and copied to the output directory by `main.ts` (Node 22, standard library only).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To redraw the image from scratch:

```sh
python3 draw.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhhc70yr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
