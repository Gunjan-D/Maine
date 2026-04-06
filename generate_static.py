"""
Generates a fully self-contained index.html from the Flask dashboard.
Run once:  python generate_static.py
The resulting index.html can be served by GitHub Pages.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dashboard import app

with app.test_client() as client:
    response = client.get("/")
    html = response.data.decode("utf-8")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Static site written → {out_path}")
