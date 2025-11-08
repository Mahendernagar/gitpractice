from google import genai
import os
import sys

# Preferred: read API key from environment variable to avoid hardcoding secrets.
# The original comment mentioned `GEMINI_API_KEY` so we check that first.
api_key = os.environ.get("GEMINI_API_KEY","AIzaSyApzddQQgA2hQs4pp5TI3XrAAcyF1iOFqM")

if api_key:
    client = genai.Client(api_key=api_key)
else:
    # Fallback: try to use Google Cloud Vertex AI credentials (ADC).
    # Requires either Application Default Credentials or service account JSON
    # referenced by GOOGLE_APPLICATION_CREDENTIALS. Also set GOOGLE_CLOUD_PROJECT
    # environment variable or pass project/location explicitly.
    project = os.environ.get("GOOGLE_CLOUD_PROJECT","RAGI")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
    if project:
        client = genai.Client(vertexai=True, project=project, location=location)
    else:
        sys.exit(
            "Missing credentials: set GEMINI_API_KEY or configure Vertex AI (set GOOGLE_CLOUD_PROJECT and ADC)."
        )

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)