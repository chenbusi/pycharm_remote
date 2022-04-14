from requests import get

r = get("https://google.com")
print(r.status_code)
print(r.text)
