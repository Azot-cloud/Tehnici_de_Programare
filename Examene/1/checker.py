import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    if path.startwith("/"):
        return f"https://{host}{path}"
    else:
        return f"https://{host}/{path}"

    pass



def is_https(url: str):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    r = requests.get(url)
    if "https" == url:
        return True
    else:
        return False
    return r.json
    pass
print("Url: ",is_https)

# Partea 2

def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    r =requests.get(url)

    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")

    return r.json()["json"]

    pass


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try:

        response = requests.get(url, timeout=5)

        return {
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type"),
            "length": len(response.content),  # Determină lungimea conținutului descărcat
            "server": response.headers.get("Server", "unknown")  # 'unknown' dacă antetul lipsește
        }

    except requests.exceptions.RequestException as e:

        return {"status": None, "error": str(e)}
    pass


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    rezultate_bune = []
    esuate = 0

    for url in SITES:
        rezultat = check_site(url)

        if rezultat.get("status") == 200:
            rezultat["url"] = url
            rezultate_bune.append(rezultat)
        else:
            esuate += 1


    rezultate_bune.sort(key=lambda x: x["length"],)


    for site in rezultate_bune:
        print(f"{site['url']} -> {site['status']}, {site['length']} octeți")


    print(f"Reușite: {len(rezultate_bune)} | Eșuate: {esuate}")

SITES = [
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://example.com",
    "http://domeniu-inexistent-12345.com",
    "https://httpstat.us/404"
]

scan_sites()


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    try:

        response = requests.get(url, timeout=5)

        present = []
        missing = []


        for header in SECURITY_HEADERS:

            if header in response.headers:
                present.append(header)
            else:
                missing.append(header)


        total_headers = len(SECURITY_HEADERS)
        score = int((len(present) / total_headers) * 100)

        return {
            "present": present,
            "missing": missing,
            "score": score
               }
    except ValueError:
        return None



def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    pass
