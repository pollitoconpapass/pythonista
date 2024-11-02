from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


with app.app_context():
    db.create_all()


# === GET ALL THE CONTACTS ===
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return {"contacts": [contact.serialize() for contact in contacts]}


# === GET A SINGLE CONTACT ===
@app.route("/contacts/<int:contact_id>", methods=["GET"])
def get_contact_by_id(contact_id):
    contact = Contact.query.get(contact_id)
    return jsonify(contact.serialize())


# === CREATE A NEW CONTACT ===
@app.route("/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()
    contact = Contact(name=data["name"], email=data["email"], phone=data["phone"])

    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.serialize())


# === UPDATE A CONTACT ===
@app.route("/contacts/<int:contact_id>", methods=["PUT, PATCH"])
def edit_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json()

    if 'name' in data:
        contact.name = data["name"]
    if 'email' in data:
        contact.email = data["email"]
    if 'phone' in data:
        contact.phone = data["phone"]

    db.session.commit()
    return jsonify({"message": "Contact updated successfully"})


# === DELETE A CONTACT ===
@app.route("/contacts/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted successfully"})