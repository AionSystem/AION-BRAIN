# ECF — Moon-View Instruments

> **§4.8 FCL Master v2.6 — Mandatory output after every 6-cycle (30-entry) validation arc**

---

## Status Badges

![ECF v0.5](https://img.shields.io/badge/ECF_v0.5-filed_✓-brightgreen?style=for-the-badge)
![ECF v0.6](https://img.shields.io/badge/ECF_v0.6-pending-lightgrey?style=for-the-badge)
![Trigger](https://img.shields.io/badge/trigger-every_30_entries-blue?style=for-the-badge)
![Format](https://img.shields.io/badge/format-%7E600_words_·_data_first-blue?style=for-the-badge)

---

## What a Moon-View Instrument Is

A Moon-View Instrument is a single-page, evidence-first summary of what a completed validation arc produced. It is written for readers who have no prior knowledge of the framework — the 200 network nodes in a target domain who, if they understand what was found, become the distribution network.

The name comes from a coinage by Sheldon K. Salmon (ODS: 0.86, FCL-025):

> **Moon view** — Perspective from sufficient altitude to see the pattern the system makes, invisible from inside it.

The instrument is the moon-view of a validation arc. The cycle files in `../Completed Cycles/` are the germ view — maximum local resolution. This folder holds the altitude.

---

## Design Rules (per §4.8)

Every instrument in this folder must satisfy all of the following before filing:

- **~600 words maximum** — A door, not a document
- **Data appears before findings** — Numbers before names
- **One falsifiable prediction minimum** — With measurement method and both-outcome clause
- **One door** — Single contact or link at the end, not multiple
- **No unexplained acronyms** — Every abbreviation expanded on first use
- **No internal vocabulary** — Legible to a domain-adjacent non-expert in under 60 seconds
- **LGS_effective ≥ 0.70 throughout** — Pellucid compliance standard applied
- **BVL verified before filing** — Intent must be: "reader with no prior knowledge understands significance in under 60 seconds"

**Moon-View Instrument Quality Score (MVIQS) components:**

| Component | Weight | Threshold |
|-----------|--------|-----------|
| Data appears before framework description | 0.20 | Required |
| Legible to domain-adjacent non-expert in 60s | 0.20 | Required |
| At least one falsifiable prediction present | 0.20 | Required |
| Native vocabulary correctly attributed | 0.20 | Required |
| Single clear link to verification data | 0.20 | Required |
| **MVIQS ≥ 0.80** | — | **INSTRUMENT_VALID** |

---

## Instruments Filed

| Instrument | Framework | Entries | EV | Status |
|------------|-----------|---------|-----|--------|
| [`ECF-One-Page-Moon-View.md`](/outputs/ECF-One-Page-Moon-View.md) | ECF v0.5 | 30 | 0.716 | **Filed — ready to publish** |

> **Note:** The ECF v0.5 Moon-View Instrument was generated at the `/outputs/` level for initial distribution. The canonical archived copy belongs here. When publishing, use the `/outputs/` version as the live link target.

---

## Instruments Pending

| Framework | Cycles Complete | Entries | Trigger Condition |
|-----------|----------------|---------|-------------------|
| ECF v0.6 | 0/6 | 0/30 | 30 entries — not yet triggered |
| FSVE v3.5 | 0/6 | 0/30 | 30 entries — not yet triggered |
| AION v3.0 | 0/6 | 0/30 | 30 entries — not yet triggered |
| ASL v2.0 | 0/6 | 0/30 | 30 entries — not yet triggered |
| GENESIS v1.0 | 0/6 | 0/30 | 30 entries — not yet triggered |

---

## Filing Protocol

When a validation arc completes (30 entries, 6 cycles):

1. Generate instrument per §4.8 template
2. Verify MVIQS ≥ 0.80
3. Run BVL check — reader-without-prior-knowledge test
4. Name file: `[Framework]-[Version]-Moon-View.md`
5. File here
6. Copy to `/outputs/` for distribution
7. Update the instrument table above
8. Update convergence tag in parent framework README

An instrument that does not pass MVIQS ≥ 0.80 is not filed — it is revised.

---

## Relation to Other Folders

```
ECF/
├── Completed Cycles/     ← Germ view — 5-entry cycle files, full detail
├── ECF-MoonViews/        ← Moon view — this folder, altitude summaries
├── ECF-Summaries/        ← Mid-altitude — §4.6 cycle summary blocks
└── ecf-v0.5.md           ← The specification the instruments describe
```

The three folders form a resolution stack. A reader who wants the pattern reads this folder. A reader who wants the mechanism reads the cycle files. A reader who wants the architecture reads the specification.

---

*Folder governed by FCL Master v2.6 §4.8 · Author: Sheldon K. Salmon · February 2026*

