
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlparse
import sqlite3
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = FastAPI()

app.mount("/static", StaticFiles(directory=resource_path("static")), name="static")
templates = Jinja2Templates(directory=resource_path("templates"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/execute-sql", response_class=HTMLResponse)
async def execute_sql(request: Request, sql_query: str = Form(...)):
    output = ""
    table_data = {}
    try:
        conn = sqlite3.connect("sql_visualizer.db")
        cursor = conn.cursor()

        parsed = sqlparse.parse(sql_query)
        for statement in parsed:
            if statement.get_type() == 'SELECT':
                cursor.execute(str(statement))
                columns = [description[0] for description in cursor.description]
                rows = cursor.fetchall()
                output = templates.get_template("output.html").render({"request": request, "columns": columns, "rows": rows})
            else:
                cursor.execute(str(statement))

        # Fetch all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = [row[1] for row in cursor.fetchall()]
            
            cursor.execute(f"SELECT * FROM '{table_name}';")
            rows = cursor.fetchall()
            
            table_data[table_name] = {
                "columns": columns,
                "rows": rows
            }
            
        conn.commit()
        conn.close()

        tables_html = templates.get_template("tables.html").render({"request": request, "table_data": table_data})
        return HTMLResponse(content=f"{tables_html}<div id='output-section' hx-swap-oob='true'>{output}</div>")

    except Exception as e:
        conn = sqlite3.connect("sql_visualizer.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        table_data = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = [row[1] for row in cursor.fetchall()]
            cursor.execute(f"SELECT * FROM '{table_name}';")
            rows = cursor.fetchall()
            table_data[table_name] = {
                "columns": columns,
                "rows": rows
            }
        conn.close()
        tables_html = templates.get_template("tables.html").render({"request": request, "table_data": table_data})
        output = templates.get_template("output.html").render({"request": request, "error": str(e)})
        return HTMLResponse(content=f"{tables_html}<div id='output-section' hx-swap-oob='true'>{output}</div>")

if __name__ == "__main__":
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelname)s: %(message)s",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": "INFO"},
        },
    }
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=log_config)
