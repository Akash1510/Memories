
# Fetch the avatar url

def get_avatar_url(gender,name):
    if(gender.lower() == 'male'):
        return f"https://avatar.iran.liara.run/public/boy?username={name}"
    elif(gender.lower()=='female'):
        return f"https://avatar.iran.liara.run/public/girl?username={name}"
    else:
        return None
    
# Validate User Email

import re

def user_validation(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za]'
    return re.match(email_regex,email)
