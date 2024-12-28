from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load the vulgar words dataset
def load_vulgar_words():
    data = pd.read_csv("cleaned_vulgar_words.csv")
    return set(data['vulgar_words'].str.lower())  # Use 'vulgar_words' instead of 'cleaned_vulgar_words'

vulgar_words_set = load_vulgar_words()

# Function to check for vulgarity
def check_comment(comment):
    words = comment.lower().split()
    flagged_words = [word for word in words if word in vulgar_words_set]
    if flagged_words:
        return False, flagged_words
    return True, None

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flagged_comments 
                      (id INTEGER PRIMARY KEY, comment TEXT, flagged_words TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('comment_form.html')

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    is_clean, flagged_words = check_comment(comment)
    if is_clean:
        return f"Comment allowed: {comment}"
    else:
        # Save flagged comment to the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO flagged_comments (comment, flagged_words) VALUES (?, ?)",
                       (comment, ", ".join(flagged_words)))
        conn.commit()
        conn.close()
        return f"Comment blocked: {comment}. Flagged words: {', '.join(flagged_words)}"

@app.route('/admin')
def admin_dashboard():
    # Fetch flagged comments from the database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, comment, flagged_words FROM flagged_comments")
    flagged_comments = cursor.fetchall()
    conn.close()
    return render_template('admin_dashboard.html', comments=flagged_comments)

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    # Delete a comment from the database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM flagged_comments WHERE id = ?", (comment_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)
