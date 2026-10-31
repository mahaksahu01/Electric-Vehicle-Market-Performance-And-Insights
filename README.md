# Electric Vehicle Market Performance and Insights

A Flask website that presents a Tableau analysis of the global EV market:
an interactive dashboard, a data story, and a short summary of the dataset.

The analysis includes 9 visualizations covering sales by manufacturer, regional
demand, sales trend by year, battery type, and the price and range relationship.

- Tableau workbook: `Electric Vehicle Market.twbx`
- Dashboard and story are embedded from Tableau Public (links are set in `app.py`)

## Run locally

    python3 -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python3 app.py                  # open http://127.0.0.1:5000

To use different Tableau links, set `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL`
as environment variables before starting the app.

## Project structure

    app.py
    requirements.txt
    templates/   base.html, index.html
    static/css/  style.css
    data/        summary.json
