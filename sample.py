def process_user(user_data):
    # Missing null check on user_data
    name = user_data['name']
    email = user_data['email']
    
    # Potential issue: condition logic
    if not email or email == "":
        print("No email")
    
    # Performance: could use set instead of list
    allowed = ['admin', 'user', 'guest']
    
    return {
        'name': name,
        'email': email
    }
# gemini test
