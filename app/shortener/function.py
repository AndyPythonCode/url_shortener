import string
from typing import Union
from secrets import choice
from pydantic import AnyHttpUrl
from fastapi import status, HTTPException
from config.database import collection_redirect


async def already_have_one(redirect: AnyHttpUrl) -> Union[str, None]:
    return await collection_redirect.find_one({"redirect": redirect})


async def generate_key(host_base: str) -> str:
    ALPHABET_AND_DIGITS = string.ascii_letters + string.digits

    while True:
        key = "".join(choice(ALPHABET_AND_DIGITS) for _ in range(10))
        is_in_db = await collection_redirect.find_one({"redirect": key})
        if not (is_in_db):
            return f"{host_base}{key}"


async def insert_key(url: AnyHttpUrl, redirect: AnyHttpUrl) -> None:
    await collection_redirect.insert_one({"url": url, "redirect": redirect})


async def redirect_user(url: AnyHttpUrl) -> AnyHttpUrl:
    is_in_db = await collection_redirect.find_one({"url": url})
    if not is_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Redirect not found",
        )
    return is_in_db["redirect"]
