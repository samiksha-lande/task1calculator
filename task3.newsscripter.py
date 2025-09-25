import requests
from bs4 import BeautifulSoup

# URL of a news site (example: BBC)
url = "https://www.bbc.com/news"

# Send GET request to fetch the page content
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html_content = response.text

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract headlines (adjust selectors as needed for the chosen site)
# Many news sites use <h2> tags for headlines
headlines = []
for h in soup.find_all(["h1", "h2", "h3"]):  # cover common headline tags
    text = h.get_text(strip=True)
    if text and len(text) > 15:  # filter very short strings
        headlines.append(text)

# Save to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for line in headlines:
        f.write(line + "\n")

print(f"✅ {len(headlines)} headlines saved to headlines.txt")
