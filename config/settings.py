from decouple import config
from secrets import compare_digest
from fastapi import Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# DESCRIPTION
API_METADATA = {
    "title": "URL SHORTENER",
    'description': "Link shorteners work by transforming any long URL into a shorter, more readable link. When a user clicks the shortened version, they're automatically forwarded",
    "version": "1.0.0",
    "docs_url": "/"  # Documentation (http://localhost:8000/)
}

ALLOWED_HOSTS = []

# Cross-Origin Resource Sharing
MIDDLEWARE = {
    'middleware_class': CORSMiddleware,
    'allow_origins': ALLOWED_HOSTS or ['*'],
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}


SECURITY = HTTPBasic()


def auth_user(credentials: HTTPBasicCredentials = Depends(SECURITY)):
    username, password = dict(credentials).values()
    check_user = compare_digest(username, config("USER_AUTH"))
    check_password = compare_digest(password, config("PASSWORD_AUTH"))

    if not (check_user and check_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
