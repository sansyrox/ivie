import js


def render(js: str):
    return "Hello, world!"


def render_root(component):
    div = js.document.createElement("div")
    div.innerHTML = "<h1>This element was created from Python</h1>"
    js.document.body.prepend(div)


__all__ = ["render", "render_root", "js"]
