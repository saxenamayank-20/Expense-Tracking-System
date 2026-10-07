# Expense Tracking System

A small app I built to keep track of my daily expenses and see where the money is actually going each month. You pick a date, enter what you spent, and the analytics tab shows a category-wise breakdown for any date range.

**Live app:** STREAMLIT_APP_URL

![Add / Update expenses](screenshots/add_update.png)

![Analytics](screenshots/analytics.png)

## Tech stack

- **Frontend:** Streamlit, pandas (hosted on Streamlit Community Cloud)
- **Backend:** FastAPI, Pydantic, Uvicorn (hosted on Render)
- **Database:** PostgreSQL on Neon, using psycopg2
- **Testing:** pytest
- Python 3.12

The Streamlit app doesn't talk to the database directly. It calls the FastAPI backend, and the backend does all the DB work.

## Features

- Add or edit up to 5 expenses for any date (amount, category, notes)
- Categories: Rent, Food, Shopping, Entertainment, Other
- Analytics for a date range - total per category and its share in %, with a bar chart and a table

## Project structure

```
Expense_Tracking_System/
├── backend/
│   ├── server.py            # FastAPI routes
│   ├── database_helper.py   # all the SQL queries
│   ├── logging_setup.py
│   └── schema.sql           # tables for postgres
├── frontend/
│   ├── app.py               # main streamlit page + styling
│   ├── add_update_ui.py     # Add/Update tab
│   └── analytics_ui.py      # Analytics tab
├── testing/backend/
│   └── test_database_helper.py
├── screenshots/
├── requirements.txt
└── requirements-dev.txt
```

## Running it locally

```bash
git clone https://github.com/saxenamayank-20/Expense_Tracking_System.git
cd Expense_Tracking_System

python -m venv .venv
source .venv/bin/activate        # windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

Create a free Postgres database on [Neon](https://neon.tech), run `backend/schema.sql` in its SQL editor, and then make a `.env` file in the project root:

```
DATABASE_URL=postgresql://<user>:<password>@<host>.neon.tech/neondb?sslmode=require
API_URL=http://localhost:8000
```

Start the backend:

```bash
uvicorn backend.server:app --reload
```

And in another terminal, the frontend:

```bash
streamlit run frontend/app.py
```

## API

| Method | Route | What it does |
|---|---|---|
| GET | `/` | health check |
| GET | `/expenses/{date}` | expenses for a date |
| POST | `/expenses/{date}` | replace the expenses for a date |
| POST | `/analytics/` | category totals and % for a date range |
| POST | `/login` | check username and password |

FastAPI's interactive docs are at `/docs` once the server is running.

## Tests

```bash
python -m pytest testing/
```

The tests run against the database in `DATABASE_URL`, and they expect the sample row that `schema.sql` inserts.

## Deployment

- **Database:** Neon. Run `schema.sql` once.
- **Backend:** Render web service
  - build: `pip install -r requirements.txt`
  - start: `uvicorn backend.server:app --host 0.0.0.0 --port $PORT`
  - env vars: `DATABASE_URL`, `PYTHON_VERSION=3.12.3`
- **Frontend:** Streamlit Cloud with `frontend/app.py` as the main file. It points to the Render backend by default, and you can change that with an `API_URL` secret.

The backend is on Render's free plan, so it sleeps when nobody's using it. The first load after a while can take up to a minute.

## What I learned

- Building a REST API with FastAPI and validating requests with Pydantic
- Splitting an app into a separate frontend and backend, and connecting them over HTTP
- Moving from a local MySQL setup to a hosted Postgres database (Neon)
- Deploying the backend and frontend on two different platforms and keeping secrets out of the repo
- Writing basic tests with pytest
