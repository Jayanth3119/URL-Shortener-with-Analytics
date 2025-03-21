from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId
import random
import string
import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
users_collection = db["users"]
urls_collection = db["urls"]

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def get_base_url():
    return request.url_root.rstrip('/')

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = users_collection.find_one({"email": email})
        if user:
            try:
                if check_password_hash(user["password"], password):
                    session["email"] = email
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("login.html", error="Invalid email or password")
            except ValueError:
                if user["password"] == password:
                    hashed_password = generate_password_hash(password)
                    users_collection.update_one({"_id": user["_id"]}, {"$set": {"password": hashed_password}})
                    session["email"] = email
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("login.html", error="Invalid email or password")
        else:
            return render_template("login.html", error="Invalid email or password")
    return render_template("login.html", error=None)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "email" in session:
        user = users_collection.find_one({"email": session["email"]})
        if user:
            if request.method == "POST":
                original_url = request.form["original_url"]
                short_url = generate_short_url()
                urls_collection.insert_one({
                    "original_url": original_url,
                    "short_url": short_url,
                    "user_email": session["email"],
                    "clicks": 0,
                    "created_at": datetime.datetime.now(),
                    "clickers": []
                })
                return redirect(url_for("dashboard"))
            user_urls = urls_collection.find({"user_email": session["email"]})
            return render_template("dashboard.html", user=user, user_urls=user_urls, base_url=get_base_url())
        else:
            session.pop("email", None)
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@app.route("/s/<short_url>")
def redirect_short_url(short_url):
    url_data = urls_collection.find_one({"short_url": short_url})
    if url_data:
        urls_collection.update_one(
            {"short_url": short_url},
            {
                "$inc": {"clicks": 1},
                "$push": {"clickers": {"clicked_at": datetime.datetime.now()}},
            },
        )
        return redirect(url_data["original_url"])
    else:
        return "Short URL not found", 404

@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)
        if users_collection.find_one({"email": email}):
            return render_template("register.html", error="Email already exists")
        users_collection.insert_one({"name": name, "email": email, "password": hashed_password})
        return redirect(url_for("login"))
    return render_template("register.html", error=None)

@app.route("/rehash")
def rehash():
    for user in users_collection.find():
        if "password" in user:
            if not user["password"].startswith("pbkdf2:"):
                plain_password = user["password"]
                hashed_password = generate_password_hash(plain_password)
                users_collection.update_one({"_id": user["_id"]}, {"$set": {"password": hashed_password}})
                print(f"Rehashed password for {user['email']}")
    return "Rehashing complete. Remove or Comment out the /rehash route."

@app.route("/analytics/<short_url>")
def analytics(short_url):
    if "email" in session:
        url_data = urls_collection.find_one({"short_url": short_url})
        if url_data and url_data["user_email"] == session["email"]:
            return render_template("analytics.html", url_data=url_data)
        else:
            return "Unauthorized or URL not found", 403
    else:
        return redirect(url_for("login"))
    
@app.route("/get_clicks/<short_url>")
def get_clicks(short_url):
    url_data = urls_collection.find_one({"short_url": short_url})
    if url_data:
        return jsonify({
            "clicks": url_data["clicks"],
            "clickers": url_data["clickers"]
        })
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)