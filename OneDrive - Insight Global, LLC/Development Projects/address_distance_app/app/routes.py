from app import app
from flask import render_template, request, send_file, redirect, url_for, session
import pandas as pd
import openrouteservice
from io import BytesIO

app.secret_key = "your_secret_key_here"  # Change this to a strong, random value

ORS_API_KEY = "5b3ce3597851110001cf6248b8529911cb1142eaa984dc1716c2950d"

# Dictionary of valid users
VALID_USERS = {
    "admin": "jared",
    "user1": "password1",
    "user2": "password2"
}

@app.route("/login", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in VALID_USERS and password == VALID_USERS[username]:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("index"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    error = None
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            try:
                df = pd.read_excel(file)
                client = openrouteservice.Client(key=ORS_API_KEY)
                distances = []
                for idx, row in df.iterrows():
                    addr1 = row.iloc[0]  # Column A
                    addr2 = row.iloc[1]  # Column B
                    if pd.isna(addr1) or pd.isna(addr2):
                        distances.append(None)
                        continue
                    try:
                        geocode1 = client.pelias_search(text=addr1)
                        geocode2 = client.pelias_search(text=addr2)
                        if not geocode1['features'] or not geocode2['features']:
                            distances.append(None)
                            continue
                        coords1 = geocode1['features'][0]['geometry']['coordinates']
                        coords2 = geocode2['features'][0]['geometry']['coordinates']
                        route = client.directions(
                            coordinates=[coords1, coords2],
                            profile='driving-car',
                            format='geojson'
                        )
                        meters = route['features'][0]['properties']['segments'][0]['distance']
                        miles = round(meters / 1609.34, 2)
                        distances.append(miles)
                    except Exception:
                        distances.append(None)
                if df.shape[1] > 2:
                    df.iloc[:, 2] = distances
                else:
                    df['Distance (miles)'] = distances

                output = BytesIO()
                df.to_excel(output, index=False)
                output.seek(0)
                return send_file(
                    output,
                    as_attachment=True,
                    download_name="distances.xlsx",
                    mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except Exception as e:
                error = f"Error processing file: {e}"
        else:
            error = "No file uploaded."
    return render_template("index.html", error=error)