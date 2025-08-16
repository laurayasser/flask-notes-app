from flask import Blueprint, request, render_template, jsonify, redirect, url_for
import mysql.connector, os, datetime

bp = Blueprint("main", __name__)

def get_db():
    """Connect to MySQL using environment variables"""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "notesdb")
    )

@bp.route("/")
def home():
    """Homepage with list of notes"""
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", notes=notes)

@bp.route("/notes", methods=["POST"])
def create_note():
    """Create a new note from form or JSON, then redirect to homepage"""
    content = request.form.get("content") or (request.json.get("content") if request.is_json else None)

    if not content or not content.strip():
        return "Empty note not allowed", 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (content, created_at) VALUES (%s, %s)",
        (content, datetime.datetime.utcnow())
    )
    conn.commit()
    cursor.close()
    conn.close()

    # Redirect back to homepage so user sees updated notes
    return redirect(url_for("main.home"))

@bp.route("/notes", methods=["GET"])
def list_notes():
    """Return all notes as JSON"""
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(notes)

@bp.route("/healthz")
def health():
    """Health check endpoint"""
    try:
        conn = get_db()
        conn.close()
        return "OK", 200
    except:
        return "DB not reachable", 500

