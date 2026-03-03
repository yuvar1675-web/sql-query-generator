def validate_query(query):
    query = query.lower()

    if "drop" in query or "delete" in query or "update" in query:
        return False
    return True