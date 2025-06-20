"""
IX-ThePlague Utilities Module

Helper functions to clean, validate, and normalize infectious disease queries,
ensuring consistent input format and error handling within IX-ThePlague.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the query by trimming whitespace, collapsing spaces,
    and removing unwanted characters.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\.\@\:\']+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Basic validation to check that the query is not too short
    and contains alphanumeric characters.
    """
    return bool(query and len(query) > 3 and any(c.isalnum() for c in query))

# Example usage
if __name__ == "__main__":
    test_queries = [
        "   Define virus ",
        "???",
        "Explain pandemic!",
        "Transmission methods"
    ]

    for q in test_queries:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"Original: '{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
