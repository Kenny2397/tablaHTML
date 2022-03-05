from flask import Flask,redirect,render_template

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    estudiantes_info = [
        {'name': 'Michael', 'edad': 35},
        {'name': 'John', 'edad': 30},
        {'name': 'Mark', 'edad': 25},
        {'name': 'KB', 'edad': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], estudiantes=estudiantes_info)


@app.route('/users')
def render_users():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("users.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)