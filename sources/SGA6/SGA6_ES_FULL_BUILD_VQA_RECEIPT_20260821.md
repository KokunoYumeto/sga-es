# SGA 6 Spanish full-edition build and VQA receipt — 2026-08-21

## Scope and authority

- French source: `C:\Users\user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga6_fr_r1\src\fr.tex`
- French source identity: 1,321,064 bytes; 16,178 LF; SHA-256 `0D2158B9FE3B466309A92165727A0B191422E05FBAA0DACD5806E8322C54BA1A`.
- The active Spanish edition consists of 132 ordered root-level source-aligned fragments: one front fragment and 131 body/back-matter fragments.
- Those fragments cover all 13,905 nonblank French lines in source order, without overlap. The 52 uncovered physical source lines are blank separators.
- The French source moves directly from Exposé X to Exposé XII; no Exposé XI text exists in this sourcekeeper. The edition records Exposé XI as not written and does not invent a translation unit.
- The standalone nested working document under `SGA6_X_ES_T001` is excluded; its relevant text is represented by the root-level integrated T001 fragment.

## Assembly identities

- `SGA6_ES_FULL_BODY_INPUTS.tex`: 11,355 bytes; 133 LF; SHA-256 `763423E4A7B52AF07CFAF7BCD080116D1F68E22C8A5DAE9008A8E39EA349C39F`.
- `SGA6_ES_FULL_CURRENT.tex`: 221 bytes; 4 LF; SHA-256 `251BA5723B08B446727ADEA2CFEF496A065095B1A15675FB1C426F5CA6A00C45`.
- `SGA6_ES_FULL_ORIGINAL.tex`: 221 bytes; 4 LF; SHA-256 `FF7DF65CAE0756AD07D8301E64BF3AAF6775FDEDF31F2855E370D896C992CBCF`.
- Ordered 132-fragment projection schema: `relative-name<TAB>decimal-bytes<TAB>uppercase-SHA256<LF>`, ordinal source order.
- Projection: 132 files; 1,360,809 payload bytes; 19,500 projection bytes; SHA-256 `0D0E3E02C1BDDBA4DEB276011719508C5829A7F5C3DEBF0B4BE1F192FF8AC488`.
- Both wrappers set an explicit pdfTeX trailer identity and were built with `SOURCE_DATE_EPOCH=1787270400`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

## Source and formula audit

- Diplomatic branch: 22,402 French formula containers and 22,402 Spanish formula containers.
- Normalized mathematical-token streams: 171,565 French and 171,565 Spanish tokens, exact order and exact equality; zero diff operations.
- Current/corrected branch: 22,405 formulas. The three additional containers occur only in documented second arguments of `\sisi` apparatus.
- `\sisi`: 586 balanced differing invocations, parsed in both branches.
- Formula tags: 507/507 in the diplomatic sequence. Current-only tag corrections are documented apparatus (`3.2.2.1` to `3.2.3.1`, and `4.6.1` to `4.8.1`).
- Source, diplomatic, and current braces and environment stacks balance. The only target-only environment is one balanced `gathered` wrapper in T057, used to fit translated prose inside an existing display without changing mathematics.
- All 135 checked translation/control TeX files are strict UTF-8, LF-only, BOM-free, NUL-free, and terminal-LF terminated.

## Deterministic build

- Engine: MiKTeX pdfTeX 1.40.29 through latexmk 4.88.
- Current final PDF: `output\final\current\SGA6_ES_FULL_CURRENT.pdf`; 2,884,189 bytes; 377 pages; SHA-256 `A8C5AD8EBCEF473CC714C1C39C4B1BD5C9A2B880C5D294501361E29025AEE294`.
- Current replay PDF: byte-identical, 2,884,189 bytes; SHA-256 `A8C5AD8EBCEF473CC714C1C39C4B1BD5C9A2B880C5D294501361E29025AEE294`.
- Original final PDF: `output\final\original\SGA6_ES_FULL_ORIGINAL.pdf`; 2,883,067 bytes; 377 pages; SHA-256 `19F65FB5400A8CA015BE20290AC2A8C21750CF9EE1598B9022DA417D5F8C4439`.
- Original replay PDF: byte-identical, 2,883,067 bytes; SHA-256 `19F65FB5400A8CA015BE20290AC2A8C21750CF9EE1598B9022DA417D5F8C4439`.
- Both PDFs are PDF 1.5, unencrypted, unrotated A4 (`595.276 × 841.89 pt`).
- Final current log: 57,550 bytes; SHA-256 `7EB6D63AF8AD6E5A1ED2D7BA4368D8D06E4C23DC63849A71A8EE40E2D16A8D34`.
- Final original log: 57,565 bytes; SHA-256 `28624FFFE72F38A31E51EF18C15965D9B3158DBFF727E72435F8F76D9A57C61E`.
- All four final/replay logs have zero LaTeX/package/pdfTeX warnings, overfull or underfull boxes, undefined controls, fatal errors, or emergency stops.

## Visual QA

- Both final PDFs were rendered in full with Poppler at 72 dpi: 377 current plus 377 original RGB PNGs, each 596 × 842 pixels.
- Current page renders: 49,548,020 bytes; original page renders: 49,551,646 bytes.
- All 754 pages are nonblank; none touches a raster edge.
- Exact minimum left/top/right/bottom ink margins are `57/71/60/42` pixels in each branch.
- Eleven paired whole-volume contact sheets were inspected, covering all pages of both branches.
- Twenty-four high-risk/boundary/diagram/terminal pages per branch were additionally rendered at 144 dpi (`1191 × 1684`) and inspected: 1, 3, 5, 18, 48, 69, 88, 124, 151, 164, 199, 227, 255, 273, 283, 323, 333, 342, 357, 358, 371, 373, 376, 377.
- Verdict: PASS. No unexpected blank page, clipping, collision, missing glyph, broken diagram, stranded heading, unreadable note, footer defect, or index defect was found.
- VQA projection before cleanup: 817 files; 118,617,820 payload bytes; 76,720 projection bytes; SHA-256 `6F5EAE9DBFE49C3E80FCC45733DA32CB315CD8EFCD2A18486750E6D87E662F32` under `relative-path<TAB>decimal-bytes<TAB>uppercase-SHA256<LF>`, .NET ordinal order.

## Claim boundary

- This receipt establishes complete Spanish source coverage, exact diplomatic mathematical alignment, deterministic current/original builds, and whole-volume visual QA for the local SGA 6 edition.
- Reported French-source anomalies remain diplomatic/current apparatus or Canon referrals; they were not silently erased.
- No Git operation, public upload, DOI mutation, duplicate deposit, or publication action is claimed by this receipt.

## Cleanup

- After the hashes and visual verdict above were frozen, 849 recreatable task-owned files totaling 131,178,998 bytes were deleted.
- Removed explicit trees: `tmp\pdfs\sga6_full_vqa`, `output\replay`, and the superseded pre-final `output\pdf` tree.
- Removed final-build auxiliaries: `.aux`, `.fdb_latexmk`, `.fls`, and `.out` from each final branch.
- Deliberately retained: both final PDFs, both final logs, all 132 translation fragments, the three assembly files, and this receipt.
