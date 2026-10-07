# 💰 Expense Tracking System

## 🔍 Description

A modern, user-friendly expense tracking application built with **FastAPI** for the backend and **Streamlit** for the frontend. Track your expenses, analyze spending patterns, and manage your finances effortlessly!

## ⚙️ Tech Stack

- **Python** 3.12
- **Streamlit** 1.45 + **pandas** - frontend UI and charts (deployed on Streamlit Community Cloud)
- **FastAPI** 0.115 + **Pydantic** 2 + **Uvicorn/Gunicorn** - REST API backend (deployed on Render)
- **MySQL** via `mysql-connector-python` - data storage
- **Requests** - frontend-to-backend HTTP calls
- **pytest** - tests

## 🚀 Features

- 📊 **Expense Management**: Add, update, and delete expenses with ease
- 📈 **Analytics Dashboard**: Visualize spending patterns with interactive charts
- 🗂️ **Category-based Tracking**: Organize expenses by categories
- 📅 **Date Range Filtering**: Analyze expenses over specific time periods
- 💾 **MySQL Database**: Robust data storage with persistent records
- 🚀 **FastAPI Backend**: High-performance REST API
- 🎨 **Streamlit Frontend**: Beautiful, responsive web interface

## 🧠 Learnings

*Key learnings from this project:*
- Building robust REST APIs with FastAPI
- Database design and optimization with MySQL
- Frontend development with Streamlit
- User authentication and security best practices
- Data visualization techniques
- Testing strategies for backend applications

## ▶️ How to Run

### Project Structure

```
Expense_Tracking_System/
├── backend/
│   ├── __init__.py
│   ├── database_helper.py    # Database operations
│   ├── logging_setup.py      # Logging configuration
│   └── server.py             # FastAPI server
├── frontend/
│   ├── app.py                # Main Streamlit app
│   ├── add_update_ui.py      # Add/Update expense interface
│   └── analytics_ui.py       # Analytics dashboard
├── testing/
│   ├── __init__.py
│   └── backend/
│       ├── __init__.py
│       └── test_database_helper.py
├── requirements.txt          # Python dependencies
└── README.md
```

### Prerequisites

- Python 3.8 or higher
- MySQL Server
- Git

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saxenamayank-20/Expense_Tracking_System.git
   cd Expense_Tracking_System
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**:
   - Create a new MySQL database and run [backend/schema.sql](backend/schema.sql)
   - Set the connection environment variables: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`

5. **Start the FastAPI backend**:
   ```bash
   uvicorn backend.server:app --reload
   ```
   The API will be available at `http://localhost:8000`

6. **Start the Streamlit frontend** (in a new terminal):
   ```bash
   API_URL=http://localhost:8000 streamlit run frontend/app.py
   ```
   The app will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### Adding Expenses
- Navigate to the "Add/Update" tab
- Enter expense details: amount, category, notes, and date
- Click "Add Expense" to save

### Viewing Analytics
- Switch to the "Analytics" tab
- View spending summaries and charts
- Filter by date range or category

### API Reference

#### Endpoints:
- `GET /` - Health check
- `GET /expenses/{date}` - Get expenses for a date
- `POST /expenses/{date}` - Replace the expenses for a date
- `POST /analytics/` - Category totals and percentages for a date range
- `POST /login` - Check a username and password

## ☁️ Deployment

- **Backend (Render):** start command `uvicorn backend.server:app --host 0.0.0.0 --port $PORT`. Set the `DB_*` environment variables to point at a hosted MySQL database. `localhost` does not exist on Render.
- **Frontend (Streamlit Cloud):** main file `frontend/app.py`. Optionally add an `API_URL` secret to point at your backend.

## 🧪 Testing

Run the test suite:
```bash
python -m pytest testing/
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

⭐ **Star this repo** if you find it helpful!