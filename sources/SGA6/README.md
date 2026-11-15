# SGA6 — fuentes de la traducción española

*Théorie des intersections et théorème de Riemann-Roch* (SGA 6, 1966–1967), Lecture Notes in Mathematics 225, en dos
ediciones dentro de un mismo árbol: `\sisi{original}{corregida}` da en su primer grupo la edición diplomática (el texto
impreso, con sus erratas) y en el segundo la edición corregida.

- Edición corregida: [SGA6_ES_FULL_CURRENT.tex](SGA6_ES_FULL_CURRENT.tex).
- Edición diplomática: [SGA6_ES_FULL_ORIGINAL.tex](SGA6_ES_FULL_ORIGINAL.tex).

Ambos documentos principales leen el preámbulo de `SGA6_FRONT_ES_T025_...` y los 131 fragmentos del cuerpo por
`SGA6_ES_FULL_BODY_INPUTS.tex`. Compile con pdfLaTeX desde esta carpeta (tres pasadas).

Estas fuentes llevan las correcciones del cotejo del texto francés de SGA 6 con el impreso (noviembre de 2026) que un
script pudo situar con certeza: 551 aplicadas, 93 que la traducción ya tenía, 313 que no se aplican a una traducción
(marcas de página y espacios del francés). Las 2.042 restantes tocan la prosa traducida y se harán a mano; la lista
está en [correcciones_20261114/PORT_ES_SGA6_HAND.json](correcciones_20261114/PORT_ES_SGA6_HAND.json), y el registro de
cada corrección en `PORT_ES_SGA6_LOG.jsonl`.

[Derechos y disponibilidad](../../RIGHTS_NOTICE.md).
