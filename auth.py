import jwt


def is_login(request, secret):
    token = request.cookies.get("token")
    if not token:
        return False

    try:
        jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("expired")
        return False

    return True
