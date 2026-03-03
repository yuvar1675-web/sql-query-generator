import streamlit as st
import sqlite3
import random

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🤖",
    layout="centered"
)

# ---------- Custom UI CSS ----------
st.markdown("""
<style>

.main-title{
font-size:40px;
font-weight:bold;
text-align:center;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip: text;
color: transparent;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:30px;
}

.card{
background-color:#f8f9fa;
padding:20px;
border-radius:12px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.stButton>button{
background-color:#0072ff;
color:white;
border-radius:8px;
height:45px;
width:100%;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Database Setup ----------
def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        purchase_amount INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_members(count):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM customers")

    cities = ["Chennai", "Madurai", "Coimbatore", "Salem"]

    for i in range(1, count + 1):
        name = f"Customer_{i}"
        city = random.choice(cities)
        purchase = random.randint(1000, 10000)

        cursor.execute(
            "INSERT INTO customers (name, city, purchase_amount) VALUES (?, ?, ?)",
            (name, city, purchase)
        )

    conn.commit()
    conn.close()

def run_query(query):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ---------- Simple AI Logic ----------
def generate_sql(user_input):

    user_input = user_input.lower()

    if "chennai" in user_input:
        return "SELECT * FROM customers WHERE city='Chennai';"

    elif "above 5000" in user_input:
        return "SELECT * FROM customers WHERE purchase_amount > 5000;"

    else:
        return "SELECT * FROM customers;"

# ---------- App ----------
create_database()

st.markdown('<div class="main-title">🤖 AI SQL Query Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert Natural Language into SQL Queries</div>', unsafe_allow_html=True)

# ---------- Member Generator Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("👥 Generate Members")

member_count = st.number_input(
    "Enter number of members to generate",
    min_value=1,
    max_value=500,
    value=10
)

if st.button("Generate Members"):
    insert_members(member_count)
    st.success(f"{member_count} Members Generated Successfully!")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Query Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💬 Ask Question")

user_input = st.text_area(
    "Example: Show customers from Chennai or customers above 5000"
)

if st.button("Generate SQL & Fetch Data"):

    sql_query = generate_sql(user_input)

    st.subheader("🧠 Generated SQL Query")
    st.code(sql_query, language="sql")

    try:
        results = run_query(sql_query)

        st.subheader("📊 Query Results")
        st.write(f"Total Records: {len(results)}")

        st.dataframe(
            results,
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Built using Python • Streamlit • SQLite")
