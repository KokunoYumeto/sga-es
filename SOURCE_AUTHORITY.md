# Fuentes y alcance de la traducción

La versión `2026-11-15-r24` reconstruye los trece libros desde la copia más reciente de cada fuente, comparando
fechas, revisiones y recibos:

- SGA 1, SGA 5 y SGA 7 (tomos I y II): las fuentes de este repositorio (`sources/`), con las correcciones de octubre y
  noviembre de 2026.
- SGA 2 y SGA 6: los pases de trabajo de Codex de agosto y septiembre de 2026 (los fragmentos de SGA 6 recibieron
  correcciones hasta el 8 de septiembre).
- SGA 3, tomos I–III: la versión del texto de 1970 del 10 de noviembre de 2026.
- SGA 4, tomos I–III: los pases de trabajo del 24 y 25 de agosto de 2026 (terminología unificada), posteriores a los
  ZIP de fuentes del 21 de agosto.
- SGA 4½: el ZIP de fuentes completas, que incluye la corrección aceptada del 5 de septiembre de 2026.

Las fuentes de cada libro, tal como se compusieron, están en los ZIP `*_ES_fuentes.zip` de la publicación.
Las versiones anteriores: `2026-08-27-r19` (la primera edición acumulada completa), `2026-09-23-r20` (nueva edición de
SGA 4½), `2026-11-10-r21` (SGA 1 y SGA 7 desde este repositorio) y `2026-11-12-r22` (quinta ronda de correcciones de
SGA 7).

## Alcance de SGA 3

SGA 3 sigue el texto de 1970 del impreso, en sus tres tomos (exposiciones I–VII_B, VIII–XVIII y XIX–XXVI, con sus
índices). Las adiciones de la reedición de 2011 de P. Gille y P. Polo figuran solo como notas que la nombran; la
presentación editorial de esa reedición (pp. v–xviii), obra independiente de sus editores, queda fuera de esta edición.

## Revisión r19

La versión r19 aplicó 1.606 correcciones aceptadas y unificó la terminología de geometría algebraica según textos
matemáticos escritos en español. Los avisos históricos de copyright se conservan como procedencia; los derechos se
indican en [RIGHTS_NOTICE.md](RIGHTS_NOTICE.md).

## SGA 5

Desde el 12 de noviembre de 2026, las fuentes de SGA 5 están en [sources/SGA5](sources/SGA5/README.md): las unidades
comunes (`SGA5_ES_WORKPASS/units`) y las dos ramas, corregida (`materialized/current`) y diplomática
(`materialized/original`), con sus documentos principales. Son la fuente de referencia de SGA 5: más recientes que el
archivo 05 de las versiones r20-r22, que solo contenía las unidades propias de cada rama. Llevan las correcciones del
cotejo página por página del texto francés con el impreso que afectan al sentido o a las matemáticas, en la rama que
corresponde a cada capa del francés.
