from flask import Flask, request, render_template_string
from notebook import Notebook

app = Flask(__name__)
notebook = Notebook()

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Notes</title>
</head>
<body>
    <h1>Notes</h1>
    <ul>
        {% for title, content in notes.items() %}
            <li><strong>{{ title }}</strong>: {{ content }}</li>
        {% endfor %}
    </ul>

    <h2>Search Note</h2>
    <form method="get">
        Title: <input type="text" name="search_title">
        <button type="submit">Search</button>
    </form>

    {% if search_result is not none %}
        <h3>Search Result</h3>
        <p><strong>{{ search_title }}</strong>: {{ search_result }}</p>
    {% endif %}

    <h2>Add Note</h2>
    <form method="post">
        Title: <input type="text" name="title"><br>
        Content: <textarea name="content"></textarea><br>
        <button type="submit">Add</button>
    </form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    search_result = None
    search_title = None

    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title and content:
            notebook.add_note(title, content)
        print(f"Added note: {title} -> {content}")  # Debug print

    elif request.method == "GET" and "search_title" in request.args:
        search_title = request.args.get("search_title")
        search_result = notebook.get_note(search_title)
        print(f"Search for: {search_title}, Found: {search_result}")  # Debug print

    print(f"Rendering with notes: {notebook.get_notes()}")  # Debug print
    return render_template_string(TEMPLATE, notes=notebook.get_notes(), search_result=search_result,
                                  search_title=search_title)


if __name__ == "__main__":
    app.run(debug=True)
