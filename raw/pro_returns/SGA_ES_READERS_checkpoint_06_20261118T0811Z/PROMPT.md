# SGA in Spanish: the Spanish readers of SGA 4, 4½, 5, 6 and 7, each in three forms, with every decision of the French readers carried into the Spanish

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached:

- `SGA_ES_1_FRANCES.zip`: **the correct version**, the French, with the French readers' annotated masters and decision
  tables;
- `SGA_ES_2_ESPANOL.zip`: **the version to bring into agreement with it**, the Spanish translation in LaTeX;
- `SGA_ES_3_HECHO.zip`: **what earlier passes already carried** into the Spanish (their logs).

Each has `MANIFEST.tsv` at its root (path in the zip, source, bytes, SHA-256, role). Read the manifests first. Inside
each ZIP, one folder per volume: `SGA4` (French: one tree for the three tomes) or `SGA4_TOMO_I`, `SGA4_TOMO_II`,
`SGA4_TOMO_III` (Spanish: one tree per tome), `SGA4_MEDIO` (SGA 4½), `SGA5`, `SGA6`, `SGA7_TOMO_I`, `SGA7_TOMO_II`.

## What this is for

The *Séminaire de Géométrie Algébrique du Bois-Marie* has a Spanish edition, AI-translated by OpenAI Codex (GPT-5.6 Sol
and GPT-6.1 Sol, reasoning effort ultra) in August–October 2026 and published in `KokunoYumeto/sga-es` in two editions:
the **corrected** edition (misprints of the print corrected) and the **diplomatic** edition (the text as printed,
misprints kept). It was translated from the French as it was before our check.

In November 2026 the French of SGA 4, SGA 4½, SGA 5, SGA 6 and SGA 7 was checked page by page against the scans of the
print (Claude Opus 5.5 at effort max). Then one GPT-6 Astra (ChatGPT Pro mode) run per volume decided every finding and
built the French readers: diplomatic, corrected with apparatus, and plain reading text, all generated from one
**annotated master** per volume, which marks every place where the corrected text differs from the print, with the
printed reading, the correction and its source. Those masters and their decision tables are the French authority here.

What the Spanish has received so far (`SGA_ES_3_HECHO.zip`):
- **SGA 4 (tomes I–III) and SGA 4½:** no French correction yet.
- **SGA 5:** the corrections of the first check, carried on 12 November 2026 by a model pass and a hand pass; the
  readers' decisions of 13 November came later and are not in it.
- **SGA 6:** this is the text of sga-es release v2026-11-15-r25. 551 French corrections were carried into it by script on
  14–15 November 2026 (`SGA6/done/PORT_ES_SGA6_LOG.jsonl`, outcome `applied`); 93 were already in it; 313 do not apply
  to a translation; 2,042 are listed in `SGA6/done/PORT_ES_SGA6_HAND.json` because they touch the translated prose or
  could not be placed with certainty.
- **SGA 7 (tomes I and II):** the corrections of the first check, carried on 9–12 November 2026 by script, by four
  model rounds (GPT-6.1 Sol, reasoning effort high) and a last round by hand (`done/METHODOLOGY.md`), with the items
  left unclear listed (`done/PORT_ES7*_LEFT.json`, `done/ES_SGA7_UNCLEAR_ITEMS.json`); the readers' decisions came
  later.

**What you do:**
1. Carry every decision of the French readers into the Spanish of each volume, in both editions.
2. Build the Spanish readers: one book per volume and form, generated from one Spanish annotated master per volume, in
   the same division into books as the French readers.
3. Make the Spanish of the whole SGA one Spanish: the same terms and notation across the volumes.
4. Build the cumulative Spanish books: all five volumes in one book per form.

Work by script and diff. Read the French and the Spanish side by side wherever a decision needs them.

## Sources of record

| Volume | French authority (`SGA_ES_1_FRANCES.zip`) | Spanish (`SGA_ES_2_ESPANOL.zip`) | Already carried (`SGA_ES_3_HECHO.zip`) |
|---|---|---|---|
| SGA 4 | `SGA4/fr/readers/SGA4_FR_master_annote.tex` (all three tomes); `SGA4/records/pro_readers/` (`CHANGES_FR.tsv`, `DECISIONS.tsv`, `DISPUTED_PLACES.tsv`, `ONE_MODEL_MISPRINTS_JUDGED.tsv`, `HAND_REPLAYS_PLACED.tsv`, the French decision JSON files, `README.md`); `SGA4/records/` (`FIXLOG_4*.jsonl`, `MISPRINTS_4.json`, `NOTE_4.txt`, `REPLAY_MANUAL_4.json`); layers `SGA4/fr/current/`, `SGA4/fr/diplomatic/`. The French text rests on Fabrice Orgogozo's LaTeX edition of SGA 4 | `SGA4_TOMO_I/es/` (exposés I–IV; `sga4_tome1_es.tex`, `units/`); `SGA4_TOMO_II/es/` (exposés V–VIII, V bis included; `source/`); `SGA4_TOMO_III/es/` (exposés IX–XIX; `build/SGA4_T3_ES_master.tex`) | nothing |
| SGA 4½ | `SGA4_MEDIO/fr/readers/` (`SGA4HALF_FR_annotated_master.tex` and the forms built from it); `SGA4_MEDIO/records/`. The French is Daniel Miller's LaTeX composition (`SGA4_MEDIO/fr/miller_src/`) | `SGA4_MEDIO/es/` (`SGA4half_Spanish_Current.tex`, `SGA4half_Spanish_Original.tex`, `components/`) | nothing |
| SGA 5 | `SGA5/fr/readers/SGA5_FR_master_annotated.tex`; `SGA5/records/` (the check's logs and `pro_readers/`) | `SGA5/es/`: the corrected branch `SGA5_ES_RECONCILE_R1/materialized/current/` and the diplomatic branch `.../original/`, both reading the common units of `SGA5_ES_WORKPASS/units/` and their own `units_overlay/` | `SGA5/done/` |
| SGA 6 | `SGA6/fr/readers/SGA6_FR_master_annote.tex`; `SGA6/records/` | `SGA6/es/`: one tree for both editions, `\sisi{original}{corregida}`; `SGA6_ES_FULL_CURRENT.tex`, `SGA6_ES_FULL_ORIGINAL.tex` | `SGA6/done/` |
| SGA 7 | `SGA7_TOMO_I/fr/readers/SGA7_FR_master_annote.tex` (the same file is in `SGA7_TOMO_II/`: one master for both tomes); each tome's `records/` | `SGA7_TOMO_I/es/` (`sga7_tome_i_es.tex`, `units/`); `SGA7_TOMO_II/es/` (`sga72_es.tex`, `units/`) | `SGA7_TOMO_I/done/`, `SGA7_TOMO_II/done/` |

Each Spanish tree carries its own README, STATUS, CONSTRUIR or SOURCES file: read it for the tree's build and for its
records of credits and sources. `es_repo/`, where a volume has it, holds the repository's records.

## Carrying the French decisions into the Spanish

**Alignment.** Align the Spanish with the French master by exposé, section, paragraph and numbered item, and put the
print's page breaks in the Spanish at the same places as the French master has them.

**The decisions.** Every place where the French master marks a difference between the print and the corrected text,
every row of the volume's `CHANGES_FR.tsv`, every line of its FIXLOG files and every decided misprint is one French
decision. For each, the Spanish gets what the corrected French says, in the Spanish file's own notation and macros:
1. **Mathematics, symbols, labels, references, page markers.** Formulas, indices, exponents, letters and their fonts,
   the underlines the print makes, symbols, numbers, cross-references, the printed page breaks: carried exactly.
2. **Misprints of the print.** The corrected form follows the corrected French; the diplomatic form keeps the printed
   reading wherever the misprint changes the Spanish. A misprint that does not change the Spanish (a French spelling,
   for example) gets no variant in the Spanish.
3. **The prose.** Where a French decision changes words (a word, a negation, a missing or extra phrase, a reference in a
   sentence, emphasis, punctuation that changes the meaning), change the Spanish sentence so that it says what the
   corrected French says.
4. **What earlier passes carried.** Check each entry of the volume's `done/` logs against the corrected French: an
   earlier pass may have carried a reading the readers later changed. Carry everything they left, the 2,042 hand items
   of SGA 6 and the unclear and left items of SGA 5 and SGA 7 included.

**Your own comparison.** Compare the whole Spanish of each volume with the corrected French, section by section, and
correct every remaining difference of content: a passage, sentence or formula the Spanish leaves out (translate it and
insert it), something the Spanish adds that the French does not say, a wrong sense. New text is AI-translated, in the
terminology the Spanish already uses. Record each.

## The readers

Build one book per volume and form; each is a single LaTeX file that compiles with a standard TeX Live:

| File | Form |
|---|---|
| `<VOL>_ES_diplomatico.tex` | **Diplomatic**: the Spanish that follows the print; where a misprint changes the Spanish, its printed reading is kept; the print's page breaks marked |
| `<VOL>_ES_corregido_aparato.tex` | **Corrected, with apparatus**: misprints corrected; every place where it differs from the print is marked, and the apparatus gives the printed reading, the correction and its source |
| `<VOL>_ES_texto_de_lectura.tex` | **Plain reading text**: the corrected text with no apparatus; the printed page numbers in the margin only; a short preface says what was left out |

`<VOL>` is `SGA4`, `SGA4MEDIO`, `SGA5`, `SGA6` and `SGA7`: SGA 4 is one book for the three tomes and SGA 7 one book for
both tomes, as the French readers are.

**Build all three forms of a volume from one annotated master** (`<VOL>_ES_maestro_anotado.tex`), with a variant macro
such as `\var{printed reading}{corrected reading}{source id}`, as the French master does. Generate the three forms from
the master by switching the macro, so that the forms cannot drift apart.

**The cumulative books.** `SGA_ES_diplomatico.tex`, `SGA_ES_corregido_aparato.tex` and `SGA_ES_texto_de_lectura.tex`:
the five volumes in order (SGA 4, SGA 4½, SGA 5, SGA 6, SGA 7) in one book per form, built from the volume masters,
with one table of contents and the volumes' own front matter.

**Which book to read.** The front matter of every book, and the README, open with a short guide in plain Spanish:
one or two sentences per form (the reading text to read the mathematics; the diplomatic form to check against the
print; the corrected form with apparatus to see every editorial change; the annotated master for editors), what an
apparatus entry is, and where to start.

## Rules

1. **Keep the authors' notation and language** in every form. Correct a misprint only where the French readers decided
   it is one. Never standardize notation silently: a change of notation that a French decision makes is carried, and
   no other.
2. **One Spanish for the whole SGA.** The readers of the five volumes will be read as one work, so terms and notation
   agree across them. Write:
   - `GLOSARIO_SGA_FR_ES.tsv`: French term or notation, Spanish rendering, count per volume, first place;
   - `GLOSARIO_INCONSISTENCIAS.md`: every French term rendered in more than one way, within a volume or across volumes;
   - `TERMINOS_ENTRE_VOLUMENES.tsv`: each term where the volumes differ: each volume's rendering, your choice, and the
     reason.
   Make the Spanish consistent where the variation is plainly a slip, and record each change.
3. **The editors' text.** Keep the editors' notes and front matter as the Spanish has them, marked as theirs, in the
   diplomatic and corrected forms. The plain reading text keeps them and leaves out only our apparatus.
4. **Credit and rights.** Each book's front matter carries:
   - the authors and the volume's bibliographic data;
   - every credit the Spanish front matter and the trees' records give, every human contribution they name included
     (among them Fabrice Orgogozo's LaTeX edition of SGA 4 and Daniel Miller's composition of SGA 4½, on which the
     French rests);
   - the wording "AI-translated" and "AI-produced corrections", never "AI-assisted": the Spanish is AI-translated
     (OpenAI Codex, GPT-5.6 Sol and GPT-6.1 Sol, reasoning effort ultra, August–October 2026); the French check (Claude
     Opus 5.5 at effort max, November 2026), the French readers and this build (GPT-6 Astra, OpenAI, ChatGPT Pro mode)
     are AI-produced corrections;
   - this rights statement, in Spanish: «Los derechos sobre las obras originales pertenecen a sus autores o a los
     representantes o herederos de estos. Nuestras transcripciones, traducciones, correcciones y composición
     tipográfica fueron producidas por IA. No tienen autor humano y, según nuestro entender, no están protegidas por
     derechos de autor; si aun así existiera algún derecho nuestro, se dedica al dominio público bajo CC0 1.0. Todo este
     trabajo reproduce o traduce las obras originales, por lo que nada de lo que aquí se publica concede licencia ni
     autoriza reproducción, traducción u otro uso de ellas. Estas ediciones se publican con fines educativos y sin ánimo
     de lucro, y no reclamamos ningún derecho que no poseamos. Si usted es titular de derechos sobre alguna de estas
     obras y se opone a su publicación aquí, abra una incidencia en GitHub y la retiraremos.»
5. **Privacy.** Some records contain local file paths. Never copy a local path into a book or a log; refer to files by
   their path inside the ZIP. Copy no e-mail address.

## What to deliver

Three ZIPs: `SGA_ES_READERS_LIBROS.zip`, `SGA_ES_READERS_FUENTES.zip` and `SGA_ES_READERS_REGISTROS.zip`. Together they
hold:

- **The books:** per volume, the annotated master and the three forms (`.tex`), with their PDFs; the three cumulative
  books, with their PDFs. Leave a PDF out only if a ZIP would exceed about 100 MB, and say so in the README.
- **The sources:** every file the books need to compile (preambles, style files, figures, bibliographies), so that each
  book builds from the ZIP alone.
- **Per volume:**
  - `<VOL>/CAMBIOS_ES.tsv`: every change to the Spanish: file, place, before, after, kind (mathematics, symbol, label,
    page marker, misprint, prose, inserted translation, terminology, own comparison), the forms affected, and its source
    (a French master variant, a `CHANGES_FR.tsv` row, a FIXLOG line, a decided misprint, or your own comparison with the
    French place);
  - `<VOL>/FRANCES_PROPAGADO.tsv`: one row per French decision (every variant of the French master, every
    `CHANGES_FR.tsv` row, every FIXLOG line, every decided misprint): its outcome in the Spanish (carried, already in,
    does not apply to a translation, with the reason) and the `CAMBIOS_ES.tsv` rows that carry it;
  - `<VOL>/HECHO_REVISADO.tsv`: every entry of the volume's `done/` logs, with your verdict (stands, amended, reverted)
    and the reason;
  - `<VOL>/APPARATUS_COUNTS.md`: per exposé and form, the number of apparatus entries by kind.
- **The glossary files** of rule 2.
- **`PDF_CHECK.md`:** for every book, the overfull boxes of its build log (none sticking out beyond about 2pt: fix any in
  the build, never by changing the text), and the pages you rendered and looked at: every page with an overflow over
  10pt before your fix, and a spread over the book.
- **`README.md`:** the guide of "which book to read"; what each file is; how each form was made; all the counts per
  volume (decisions carried, already in, not applicable; earlier entries confirmed, amended, reverted; changes of your
  own comparison; apparatus entries); the compile status of each book with its LaTeX errors and warnings.
- **Your build scripts,** with their outputs.

## When it is done

**Each item is done when:**
- **A French decision** has its row in `FRANCES_PROPAGADO.tsv` with an outcome and a reason, and a `carried` row is in
  every form it belongs to.
- **An earlier entry** has its verdict in `HECHO_REVISADO.tsv`.
- **A volume** has been compared with the corrected French section by section, and every difference found is corrected
  and recorded.
- **A book:**
  - compiles without errors and passes the PDF check;
  - carries every carried decision and every correction of your own comparison, checked by script against your
    tables, with the counts reported;
  - has page markers that agree with the French master's.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected forms, and none for
  anything else.

**Not acceptable:**
- a French decision without an outcome;
- a correction in one form and missing from another where it belongs to both;
- a book that drops, summarizes or paraphrases any part of the text;
- an apparatus entry without a source;
- a silent change of notation;
- someone's work presented as ours, or credited wrongly;
- local paths or e-mail addresses in any output.

**The task is finished** only when every French decision of the five volumes has its outcome, every volume has been
compared with the French in full, and all the books and every file listed above are in the three ZIPs. Keep working
until then. Do not stop because:
- what remains is long;
- a part of the work looks presentable;
- much has already been done.

## Working method

- Start from the manifests, the French masters and the volumes' decision tables.
- Work volume by volume: align, build the Spanish annotated master by script, carry the decisions, check the earlier
  entries, make your own comparison, generate the forms, compile, run the PDF check, and write the tables as you go.
  Then the glossary across the volumes, then the cumulative books.
- Once every hour of work, save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the
  execution environment. Name it `SGA_ES_READERS_checkpoint_<NN>.zip`, with `NN` counting up; never overwrite, rename or
  delete an earlier checkpoint, and never put an earlier checkpoint ZIP inside a new one. If the workspace comes back
  empty, restore it from the newest checkpoint and from this conversation before you continue. Save the final ZIPs
  there too; they hold everything the checkpoints held, and a file left out of the final is listed in the README with
  the reason.
- Save checkpoints once an hour and at no other time: none after a page, part, section, cote, folder, chapter or reader.
  A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records,
  notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this
  prompt. Leave the attached files themselves out of it, the sources you were given: we have them. It is never a JSON
  file, a recovery file, a summary, or an export of the newest pages only. The checkpoints are what keeps the work if
  this session dies: work that is in no checkpoint is lost.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Ignore any clock.
- Write the files from the start and extend them as you go, so that an interruption loses little.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for ten minutes. If it does not come
back, restore the workspace from the newest checkpoint and this conversation; if that fails too, write the work out in
the chat as text:
- the decision tables, the glossary files, the README and the change logs so far, each in full in its own code block
  headed by its file name;
- your build scripts in full, so that the books can be rebuilt from the attached sources;
- which volumes are finished, and where their checkpoints are.

Then continue the remaining work in the chat in the same form until every part is written. An answer that only reports
the failure or asks for the files again is not acceptable.
