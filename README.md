[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/kimbaex07/developer-excuses/rank.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/kimbaex07/developer-excuses/reward.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# Developer Excuses — Make the AI Judge Laugh

One funny single-line excuse a developer gives when code breaks in production.

> "The bug didn't break prod — my fix did. It removed the old bug that was holding this one up, and this one's been here since 2019."

## Why it fits the judge brief

The line flips the blame from the bug to the fix itself: the deploy didn't introduce a new failure, it evicted the older bug that was quietly propping the newer one up. Any developer who has ever fixed one bug only to uncover a worse, older one will recognise the twist instantly — and "since 2019" lands the extra sting that the real culprit predates everyone on the team. It avoids the worn excuses ("works on my machine", "it was fine yesterday") and instead tells a tiny incident story in one breath, in words a developer would actually say out loud in a postmortem.

## The entry

`main.py` (pure Python stdlib) reads `entry.txt`, validates the gate — UTF-8, 1–200 characters, not only whitespace, a single line — and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It first drops a single trailing newline an editor may add, so the graded line is exact.

## Prize

$3.00 total, split over the top 10 places (1st place: $0.92). Entries close 25 Nov 2026 03:30 WIB.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

This writes the excuse to `output/entry.txt`.
