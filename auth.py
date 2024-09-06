users = {"admin": "123",
         "Vicente": "1234"} 


def login(username, password):
    if username in users and users[username] == password:
        return True
    return False
