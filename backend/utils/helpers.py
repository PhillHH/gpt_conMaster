import re

def validate_email(email):
    """
    Email Validation 
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def format_date(date):
    """
    timeformatting.
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")