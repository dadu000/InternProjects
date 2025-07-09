import re
import joblib
import pandas as pd

# Extract features from URL
def extract_features(url):
    return pd.DataFrame([{
        "url_length": len(url),
        "has_at": "@" in url,
        "has_dash": "-" in url,
        "has_ip": bool(re.search(r"\d{1,3}(\.\d{1,3}){3}", url)),
        "has_suspicious_word": bool(re.search(r"login|verify|secure|account", url.lower()))
    }])

model = joblib.load("phishing_model.pkl")

url = input("Enter a URL: ")
features = extract_features(url)
prediction = model.predict(features)[0]

print("⚠️ Phishing" if prediction else "✅ Legitimate")
