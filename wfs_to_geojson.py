#!/usr/bin/env python3
"""
Fetch features from a WFS 2.0 service and save to GeoJSON.

Example:
  python wfs_to_geojson.py \
    --url https://example.com/geoserver/wfs \
    --type-names workspace:layer \
    --out data.geojson
"""
import json
from pathlib import Path
import click
import requests


@click.command()
@click.option("--url", required=True, help="Base WFS endpoint URL")
@click.option("--type-names", required=True, help="Qualified layer name, e.g., workspace:layer")
@click.option("--out", "out_path", type=click.Path(path_type=Path), required=True)
def main(url: str, type_names: str, out_path: Path):
    params = {
        "service": "WFS",
        "request": "GetFeature",
        "version": "2.0.0",
        "typeNames": type_names,
        "outputFormat": "application/json",
        "count": 1000,
    }
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()
    with out_path.open("w") as f:
        json.dump(data, f)
    click.echo(f"Saved {len(data.get('features', []))} features to {out_path}")


if __name__ == "__main__":
    main()
