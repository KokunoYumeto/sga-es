# SGA 6 Spanish full-volume final audit

Date: 2026-08-21 (Europe/Berlin)

Verdict: **DEFINITIVE PASS**. The complete SGA 6 Spanish translation, reversible source apparatus, deterministic current/original editions, and full-volume visual QA have no remaining blocker.

## Exact source coverage

- French source: `sga6_fr_r1/src/fr.tex`, 1,321,064 bytes / SHA-256 `0D2158B9FE3B466309A92165727A0B191422E05FBAA0DACD5806E8322C54BA1A`.
- 132 source-ordered Spanish fragments cover every nonblank French line from 1 through 16178.
- The only uncovered physical positions are 52 zero-length separator lines.
- Source ranges have no overlap and no duplicate root fragment.
- The source itself jumps from Exposé X to Exposé XII; no Exposé XI unit is present in the authority.
- Fragment projection in source order: 1,360,809 payload bytes / 19,500 projection bytes / SHA-256 `0D0E3E02C1BDDBA4DEB276011719508C5829A7F5C3DEBF0B4BE1F192FF8AC488`.

## Mathematical and apparatus parity

- Diplomatic source formulas: 22,402.
- Diplomatic Spanish formulas: 22,402.
- Normalized mathematical token streams: 171,565 versus 171,565, exact sequence equality.
- Formula diff opcodes: 0.
- Current formulas: 22,405; the three additional containers occur only in documented corrected `\sisi` branches.
- Balanced differing `\sisi` calls: 586.
- Diplomatic equation tags: 507/507.
- All 135 checked TeX/control files are strict UTF-8, LF-only, BOM-free, NUL-free, and terminal-LF clean.
- The sole environment-token difference is a balanced `gathered` presentation wrapper around translated prose; it changes no mathematical payload.

## Final sources and PDFs

- Body input manifest: 11,355 bytes / SHA-256 `763423E4A7B52AF07CFAF7BCD080116D1F68E22C8A5DAE9008A8E39EA349C39F`.
- Current master: 221 bytes / SHA-256 `251BA5723B08B446727ADEA2CFEF496A065095B1A15675FB1C426F5CA6A00C45`.
- Original master: 221 bytes / SHA-256 `FF7DF65CAE0756AD07D8301E64BF3AAF6775FDEDF31F2855E370D896C992CBCF`.
- Current PDF: 377 pages / 2,884,189 bytes / SHA-256 `A8C5AD8EBCEF473CC714C1C39C4B1BD5C9A2B880C5D294501361E29025AEE294`.
- Original PDF: 377 pages / 2,883,067 bytes / SHA-256 `19F65FB5400A8CA015BE20290AC2A8C21750CF9EE1598B9022DA417D5F8C4439`.
- Current log: 57,550 bytes / SHA-256 `7EB6D63AF8AD6E5A1ED2D7BA4368D8D06E4C23DC63849A71A8EE40E2D16A8D34`.
- Original log: 57,565 bytes / SHA-256 `28624FFFE72F38A31E51EF18C15965D9B3158DBFF727E72435F8F76D9A57C61E`.

Both editions are deterministic PDF 1.5, unencrypted A4 files. Replay copies were byte-identical before normal transient removal.

## Visual QA

All 754 pages were rendered and raster-screened. Both branches had zero blank pages and zero edge-touch pages. Eleven paired whole-volume contact sheets and 24 high-risk native pages per branch were inspected. No clipping, collision, malformed formula, broken diagram, missing glyph, stray mark, or unintended blank page remains.

Build/VQA receipt: `SGA6_ES_FULL_BUILD_VQA_RECEIPT_20260821.md`, 6,087 bytes / SHA-256 `27C595A429365C838265D24CB77F774245C21A84B3A5D37063AE3751CAD9DB1E`.

## Claim boundary

The local SGA 6 Spanish edition is translation-, source-, build-, replay-, and visual-complete. This audit does not itself publish, mint a DOI, alter an external record, or create a duplicate deposit. Rights uncertainty is descriptive metadata only and is not a completion or publication gate.

Final blocker count: **0**.


