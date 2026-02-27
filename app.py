from flask import Flask, render_template, request, redirect
from google.cloud import firestore

app = Flask(__name__)

# Initialize Firestore
db = firestore.Client(database="student-fs")
users_ref = db.collection("students")


# READ - Show all users
@app.route("/")
def index():
    users = users_ref.stream()
    return render_template("index.html", users=users)


# CREATE - Add user
@app.route("/register", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        users_ref.add({
            "name": name,
            "email": email,
            "phonenum": phone
        })

        return redirect("/")

    return render_template("register.html")


# UPDATE - Edit user
@app.route("/edit/<doc_id>", methods=["GET", "POST"])
def edit_user(doc_id):
    doc = users_ref.document(doc_id)

    if request.method == "POST":
        doc.update({
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"]
        })
        return redirect("/")

    user = doc.get().to_dict()
    return render_template("edit.html", user=user, doc_id=doc_id)


# DELETE - Remove user
@app.route("/delete/<doc_id>")
def delete_user(doc_id):
    users_ref.document(doc_id).delete()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)