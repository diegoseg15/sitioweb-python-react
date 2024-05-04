from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def HelloWorld():
    return html.div(
        html.h1("Lista de Tareas"),
        html.lu(
            html.li("Tarea 1"),
            html.li("Tarea 2"),
        )
    )

app = FastAPI()
configure(app, HelloWorld)