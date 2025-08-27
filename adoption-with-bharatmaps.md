# Adoption with Bharat Maps

Two routes for agencies:

1) Host OGC API Features or WFS and register as an external service in Bharat Map Services.
2) Export shapefile/GeoPackage and publish via Bharat Map Services as WMS/WMTS tiles for visualization.

Pointers:
- Bharat Maps: https://bharatmaps.gov.in/
- Bharat Map Services: https://mapservice.gov.in/

Steps (external OGC API Features):
- Ensure your API is publicly reachable with HTTPS.
- Provide collection metadata and sample queries.
- Register the endpoint in Bharat Map Services under external services.

Steps (WMS/WMTS):
- Prepare and validate data (GeoPackage recommended).
- Upload to Bharat Map Services and configure layer styles.
