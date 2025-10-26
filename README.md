# React Website Preset

Preset for a React website with Flask backend integration.

## Features

- React frontend with Vite for fast development
- Flask backend with SQLAlchemy ORM
- SQLite database with automatic initialization
- CORS enabled for cross-origin requests
- RESTful API structure
- Blueprint-based API organization

## Getting Started

### Clone the repository

```sh
git clone https://github.com/JstOnGit/ReactWebsite-preset.git
```

### Install dependencies

The dependencies will be automatically installed when running the project for the first time.

### Run in development mode

Run the "run.ps1" script.
```sh
.\run.ps1
```

### To force stop

Run the "stop.ps1" script.
```sh
.\stop.ps1
```

## Project Structure

```
ReactWebsite-preset/
├── .gitignore
├── README.md
├── run.ps1
├── stop.ps1
├── backend/
│   ├── config.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test.py
│   └── models/
│       └── testModel.py
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── public/
    └── src/
        ├── App.css
        ├── App.jsx
        ├── main.jsx
        └── pages/
            └── Home/
                ├── Home.css
                └── Home.jsx
```

## API Endpoints

- `GET /api/test` - Returns test data from the database

## Configuration

The backend runs on `localhost:4269` by default.
The frontend runs on `localhost:6942` by default.

You can modify these settings in `backend/config.py`.

## Database

The project uses SQLite with automatic database initialization. The database file is created at `backend/instance/database.db` on first run.

## License


MIT
