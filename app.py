"""EV Market Performance Insights: Flask site.

Run locally:
    pip install -r requirements.txt
    python app.py            # http://127.0.0.1:5000

Set your Tableau links with environment variables (or edit the defaults below):
    TABLEAU_DASHBOARD_URL  e.g. https://public.tableau.com/views/<workbook>/<dashboard>
    TABLEAU_STORY_URL      e.g. https://public.tableau.com/views/<workbook>/<story>
"""
import json
import os
from pathlib import Path

from flask import Flask, render_template

BASE_DIR = Path(__file__).parent

GITHUB_URL = "https://github.com/mahaksahu01/Electric-Vehicle-Market-Performance-And-Insights"


def normalize_tableau_url(url):
    """Accept any Tableau Public link and return the embeddable /views/ form.

    Handles:
      https://public.tableau.com/app/profile/<user>/viz/<Workbook>/<Sheet>
      https://public.tableau.com/views/<Workbook>/<Sheet>?:showVizHome=no
    """
    url = (url or "").strip()
    if not url:
        return ""
    url = url.split("?")[0].split("#")[0]
    if "/viz/" in url:
        url = "https://public.tableau.com/views/" + url.split("/viz/", 1)[1]
    return url


# Paste your links here, or set them as environment variables.
TABLEAU_DASHBOARD_URL = normalize_tableau_url(
    os.environ.get("TABLEAU_DASHBOARD_URL", "https://public.tableau.com/views/ElectricVehicleMarket_17931110846950/Dashboard1")  # or: "https://public.tableau.com/app/profile/.../viz/.../Dashboard1"
)
TABLEAU_STORY_URL = normalize_tableau_url(
    os.environ.get("TABLEAU_STORY_URL", "https://public.tableau.com/views/ElectricVehicleMarket_17931110846950/Story1")  # or: "https://public.tableau.com/app/profile/.../viz/.../Story1"
)

app = Flask(__name__)


def load_summary():
    with open(BASE_DIR / "data" / "summary.json", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    summary = load_summary()
    max_units = max(r["units_m"] for r in summary["regions"])
    return render_template(
        "index.html",
        github_url=GITHUB_URL,
        dashboard_url=TABLEAU_DASHBOARD_URL,
        story_url=TABLEAU_STORY_URL,
        summary=summary,
        max_units=max_units,
    )


if __name__ == "__main__":
    app.run(debug=True)
