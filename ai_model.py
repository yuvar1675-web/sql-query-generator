def generate_sql(user_input):

    user_input = user_input.lower()

    if "chennai" in user_input and "5000" in user_input:
        return "SELECT * FROM customers WHERE city='Chennai' AND purchase_amount > 5000;"

    elif "all customers" in user_input:
        return "SELECT * FROM customers;"

    else:
        return "SELECT * FROM customers;"