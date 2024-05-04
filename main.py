from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

cdn_l = html.script (
    {
        "src":"https://cdn.tailwindcss.com"
    }
)

@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done)
    
    def handle_click(event):
        set_done(not done)
    
    attrs = {"class":"bg-green-600 text-white py-4 px-5 font-semibold rounded-lg border-b-2"} if done else {"class":"flex space-x-5 items-center py-4 px-5 border-b-2"}
    
    if done:
        return html.li(attrs, text)
    else:
        return html.li(attrs,
            html.span(text),
            html.button({"class":"px-3 py-2 bg-green-600 rounded-lg font-semibold text-white","on_click": handle_click}, "Relizado"),
        )

@component
def HelloWorld():
    return html._(
        cdn_l,
        html.div(
            {"class":"w-screen text-center py-5 bg-sky-800 text-white"},
            html.h1({"class":"text-3xl font-bold"}, "Lista de Tareas"),
        ),
        
        html.div(
            {"class":"w-creen py-10 px-16"},
            html.ul(
                {"class":"list-disc flex flex-col space-y-3"},            
                Item("Aprender React con Python 1"),
                Item("Aprender React con Python 2"),
                Item("Aprender más sobre Python", initial_done=True),
            )

        )
    )

app = FastAPI()
configure(app, HelloWorld)