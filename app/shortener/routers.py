from config.settings import auth_user
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, Request
from .schemas import SchemaResponseShortener, SchemaShortener
from .function import already_have_one, generate_key, insert_key, redirect_user

router_shortener = APIRouter(
    tags=["SHORTENER"]
)


@router_shortener.post(
    "/create",
    response_model=SchemaResponseShortener,
    dependencies=[Depends(auth_user)]
)
async def generate_redirect(form: SchemaShortener, requests: Request):
    found = await already_have_one(form.url)
    if not found:
        url_key = await generate_key(requests.base_url)
        await insert_key(url_key, form.url)
        return {"url": url_key, "redirect": form.url}
    else:
        return {"url": found["url"], "redirect": found["redirect"]}


@router_shortener.get(
    "/{redirect}",
    response_class=RedirectResponse
)
async def link_redirect(redirect: str, requests: Request):
    """Just copy and paste generated code [Not base url] [You can do it in the browser with base url]"""
    return await redirect_user(f"{requests.base_url}{redirect}")
