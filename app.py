from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL hosted on AWS
conn = psycopg2.connect(
    host="database-1.ch2cu2qaa4oh.ap-south-1.rds.amazonaws.com",
    port="5432",
    database="fullstack",
    user="daud",
    password="daud3738"
)

@app.route('/')
def index():
    return render_template('index.html')  # frontend HTML

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
#    password = request.form['password']
#    name = request.form['name']
    
    # Insert values into the users table
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (username, email) 
        VALUES (%s, %s)
    """, (username, email))
    conn.commit()
    cur.close()
    
    return 'User Saved Successfully!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
