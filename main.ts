// news-image-20261120 — "Sum up 20 November's world news in one image".
// The entry image (entry.png) is a newspaper front page drawn with Pillow
// from verified 20 Nov 2026 reporting: the ICJ's genocide ruling on Myanmar,
// the Trump–Xi–Putin summit in Shenzhen, the Houthi strike on Riyadh, Kyiv
// and the Crimea Bridge, falling markets, Kenya's Ebola milestone, COP31,
// GTA 6 and Voyager 1. The drawing script (draw.py) is in this repo; the
// program below just copies the finished image to the grader's output dir.
//
// Node 22, standard library only. Outside the grader's container,
// MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const dest = join(outDir, "entry.png");
copyFileSync(new URL("./entry.png", import.meta.url), dest);
