# Primera entrega del proyecto

El documento que debe enlazarse al profesor es [project-brief.md](project-brief.md).

## Contenido

- `project-brief.md`: propuesta completa en español.
- `data/raw/`: descarga original de UCI y CSV extraído sin modificar.
- `evidence/data-audit.json`: cifras comprobadas y huella SHA-256.
- `scripts/audit_data.py`: inspección reproducible del CSV.

## Reproducir la auditoría

Con Python y pandas instalados, ejecutar desde esta carpeta:

```bash
python scripts/audit_data.py
```

Si el CSV no está extraído, el script lo obtiene del ZIP local. No necesita conexión para la auditoría.

Fuente de descarga:
https://archive.ics.uci.edu/static/public/560/seoul%2Bbike%2Bsharing%2Bdemand.zip

Seoul Bike Sharing Demand [Dataset] (2020). UCI Machine Learning Repository.
https://doi.org/10.24432/C5F62R

Licencia: Creative Commons Attribution 4.0 International.
https://creativecommons.org/licenses/by/4.0/

## Entrega

Copiar esta carpeta `project/` a la raíz del repositorio habitual de ejercicios y subirla a GitHub. Abrir `project/project-brief.md` y enviar su enlace por el canal que indique el profesor. El plazo de la captura es el 21/10/2026 a las 15:00.

La carpeta local de trabajo no identifica por sí sola el repositorio de entrega. No se ha publicado ni enviado ningún enlace al profesor.

Las hipótesis y los objetivos son propuestas para investigar. Las cifras de calidad sí proceden de la inspección ejecutada. El brief define la futura solución; esta entrega no incluye aún el dashboard ni el entrenamiento del modelo.
