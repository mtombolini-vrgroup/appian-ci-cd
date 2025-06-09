# appian-ci-cd
# CICD Appian Pipeline - BiceVida

Este repositorio contiene los workflows de automatización para el proceso de despliegue continuo (CI/CD) de aplicaciones y paquetes en la plataforma Appian de BiceVida.

## Objetivo

Automatizar el flujo completo de promoción de artifacts Appian (ZIPs de paquete o aplicación), con inspección y validación previa, de Dev a QA y a Producción.

El repositorio versiona principalmente:
- Workflows `.github/workflows/*.yml`
- Artifacts de paquetes y aplicaciones (`deployments/dev`, `deployments/qa`, `deployments/prod`)
- Configuración (`apps_config.json`, `packages_result.json`)
- Customization files y Admin Console Settings (en rutas dedicadas)

**Importante:** El código fuente de las aplicaciones Appian no se versiona en este repositorio (solo los artifacts generados a través de export).

---

## Branching Model

El repositorio utiliza un modelo de ramas simple, pensado para controlar:

- La evolución de los workflows.
- La promoción de artifacts entre entornos.

| Rama       | Propósito |
|------------|-----------|
| `main`     | Código estable y artifacts ya desplegados en Producción. Protegida. |
| `qa`       | Código estabilizado y artifacts desplegados en QA. Protegida. |
| `dev`      | Rama de desarrollo de workflows y pruebas internas. Puedes trabajar aquí con los workflows y artifacts de Dev. |
| `feature/*` | Desarrollo de nuevas features en los workflows o automatizaciones adicionales. Se mergea a `dev`. |

---

## Flujo del pipeline

### Para paquetes Appian

```plaintext
exportar ZIP → inspeccionar en QA → importar a QA → inspeccionar en Prod → importar a Prod
```

### Para aplicaciones Appian

```plaintext
exportar aplicación ZIP → inspeccionar en QA → importar a QA → inspeccionar en Prod → importar a Prod
```

---

## Workflows disponibles

| Workflow                       | Propósito |
|--------------------------------|-----------|
| `wf_export.yml`                | Exportación de paquete Appian |
| `wf_export_app.yml`            | Exportación de aplicación completa Appian |
| `wf_inspect.yml`               | Inspección de artifacts (package o app) reutilizable para cualquier entorno |
| `wf_import.yml`                | Importación de artifacts reutilizable para cualquier entorno |
| `deploy_pipeline.yml`          | Pipeline completo para paquetes: Dev → QA → Prod |
| `deploy_app_pipeline.yml`      | Pipeline completo para aplicaciones: Dev → QA → Prod |

---

## Protección de ramas

- `main` y `qa` tienen reglas de protección activadas:
  - Requieren PR aprobado para merge.
  - Requieren aprobación manual de promoción en el environment antes del import.

---

## Notas finales

Este repositorio está diseñado para dar visibilidad y trazabilidad completa al proceso de CI/CD en Appian, versionando los artifacts y automatizando su despliegue de forma controlada.