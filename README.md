# Permiso, permiso

Corto animado en SVG sincronizado palabra por palabra con el audio del cuento.

- `index.html`: el corto (se abre en el navegador; usa el audio `.mpeg` del repo).
- `src/corto.html`: fuente de la animación.
- `build.py`: inserta los tiempos de `WhatsApp_Audio_..._spa.json` en `src/corto.html` y genera `index.html`.

Para regenerar después de editar la fuente: `python3 build.py`.
