import pyodide
import js
from js import document

btn = document.querySelector("#output2")
btn_class = document.querySelector("#btnClass")
text_preview = document.querySelector("#textPreview")
btn.innerHTML = "Click Me!"


def change_class(e):
    e.target.classList.add(btn_class.value)


btn.addEventListener("click", pyodide.create_proxy(change_class))


def text_on_change_preview(e):
    text_preview.innerHTML = e.target.value
    console.log("hey")


btn_class.addEventListener("keyup", pyodide.create_proxy(text_on_change_preview))
