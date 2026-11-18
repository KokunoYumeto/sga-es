Punto de recuperación completo e inmutable.
Después de descomprimir este ZIP, ejecute: python3 RESTORE_CHECKPOINT.py
Sólo requiere Python 3 y su biblioteca estándar.
El script restaura todos los libros, fuentes, registros y demás archivos en sus rutas originales y verifica los 6045 tamaños y SHA-256 contra el manifiesto original.
La compresión es reversible y no cambia ningún archivo, contenido ni imagen.
No se incluyen las entradas originales ni ZIP anteriores.
