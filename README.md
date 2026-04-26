<div align="center">Krushi AI Platform

<p>
  <b>Modern agriculture intelligence platform with crop prediction, chatbot support, media-rich learning, and map-based farming exploration.</b>
</p><p>
  <a href="#overview">Overview</a> •
  <a href="#feature-highlights">Features</a> •
  <a href="#technology-stack">Tech Stack</a> •
  <a href="#architecture-map">Architecture</a> •
  <a href="#setup">Setup</a>
</p></div>
---

Project Banner

<div style="padding:22px; border-radius:18px; background: linear-gradient(135deg, #0b1020 0%, #12213b 55%, #1a2e52 100%); border: 1px solid #2a3d63;"><table width="100%">
<tr>
<td width="62%" valign="top">Smart Farming Experience

Krushi AI Platform is a modern web application designed to combine agriculture identity, AI support, crop intelligence, and a premium user interface in one structured project.

It is built for learning, portfolio presentation, and real project demonstration.

</td>
<td width="38%" valign="top"><div style="padding:16px; border-radius:16px; background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12);">Project Type
Full stack agriculture platform

Core Focus
Crop support, chatbot, prediction, media, map

Design Style
Premium, dark, modern, responsive

</div></td>
</tr>
</table></div>
---

Overview

<div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 14px;"><div style="padding:16px; border-radius:16px; background:#111a30; border:1px solid #263554;">
<b>Purpose</b><br>
A complete agriculture-themed digital experience with AI support.
</div><div style="padding:16px; border-radius:16px; background:#111a30; border:1px solid #263554;">
<b>Audience</b><br>
Students, farmers, mentors, and internship reviewers.
</div><div style="padding:16px; border-radius:16px; background:#111a30; border:1px solid #263554;">
<b>Value</b><br>
Strong UI, modular pages, and practical AI features.
</div></div>
---

Skill Stickers

<div align="center"><span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">HTML5</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">CSS3</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">JavaScript</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Flask</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Python</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">LangChain</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Ollama</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Machine Learning</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Responsive UI</span> <span style="display:inline-block; padding:8px 12px; margin:4px; border-radius:999px; background:#1d2a44; border:1px solid #35507f;">Interactive Map</span>

</div>
---

Feature Highlights

1. Home Page

A premium landing page with strong visuals, structure, and project navigation.

2. Krushi Page

An agriculture-focused page with crop content, farmer visuals, video sections, and a map area.

3. Prediction Page

A crop image prediction workflow connected to your Flask backend and ML model.

4. Chatbot Page

A conversational interface for farming guidance and crop support.

5. Reel Page

A vertical video page for farming reels and YouTube content.

6. Interactive Map Section

A map-style area where agriculture regions can be displayed in a clean visual format.


---

High Quality UI Blocks

<table width="100%">
<tr>
<td width="50%" valign="top"><div style="padding:18px; border-radius:18px; background: linear-gradient(180deg, #18253d 0%, #111a30 100%); border:1px solid #2b3e5f;">Premium Visual Layer

Dark theme with modern contrast

Full-width content sections

Balanced spacing and hierarchy

Card-based content design


</div></td>
<td width="50%" valign="top"><div style="padding:18px; border-radius:18px; background: linear-gradient(180deg, #1d2e4d 0%, #111a30 100%); border:1px solid #2b3e5f;">Project Readability Layer

Clear navigation

Well-separated sections

Simple information flow

Easy future expansion


</div></td>
</tr>
</table>
---

Technology Stack

<div style="padding:18px; border-radius:18px; background:#0f1628; border:1px solid #243654;">Frontend

HTML5

CSS3

JavaScript

Responsive layout design


Backend

Python

Flask

JSON APIs


AI and ML

Crop medicine prediction model

LangChain-based chatbot pipeline

Ollama local model integration


Media and Mapping

YouTube embeds

Reel-style video layout

Map section for agriculture regions


</div>
---

Architecture Map

flowchart TD
    A[Home Page] --> B[Krushi Page]
    A --> C[Predict Page]
    A --> D[Chatbot Page]
    A --> E[Reel Page]

    B --> F[Crop Gallery]
    B --> G[Farmer Gallery]
    B --> H[YouTube Video]
    B --> I[Agri Map Section]

    C --> J[Crop Image Upload]
    J --> K[Flask Prediction Route]
    K --> L[Prediction Result]

    D --> M[User Query]
    M --> N[LLM Response]

    E --> O[Vertical Video Feed]


---

Project Structure

project/
├── app.py
├── templates/
│   ├── index.html
│   ├── krushi.html
│   ├── predict.html
│   ├── chatbot.html
│   ├── reel.html
│   └── map.html
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
├── models/
│   └── crop_model.pkl
├── uploads/
└── README.md


---

Page Flow Diagram

<div style="padding:18px; border-radius:18px; background:#111a30; border:1px solid #263554; line-height:1.8;">Home Page  →  Krushi Page  →  Predict Page  →  Result Display
Home Page  →  Chatbot Page  →  AI Response
Home Page  →  Reel Page  →  Farming Videos
Home Page  →  Map Section  →  Region Visualization

</div>
---

Setup

1. Install dependencies

pip install flask langchain langchain-ollama

2. Run the app

python app.py

3. Open the website

http://127.0.0.1:5000


---

Flask Routes

Home route

@app.route("/")
def index():
    return render_template("index.html")

Prediction route

@app.route("/predict", methods=["POST"])
def predict():
    ...

Chatbot route

@app.route("/get", methods=["POST"])
def get_bot_response():
    ...


---

UI and UX Goals

<div style="display:grid; grid-template-columns: repeat(2, 1fr); gap: 14px;"><div style="padding:16px; border-radius:16px; background:#121c32; border:1px solid #2b3e5f;">
Strong visual identity with modern agriculture branding.
</div><div style="padding:16px; border-radius:16px; background:#121c32; border:1px solid #2b3e5f;">
Smooth page flow and simple feature navigation.
</div><div style="padding:16px; border-radius:16px; background:#121c32; border:1px solid #2b3e5f;">
Professional cards and media sections for premium presentation.
</div><div style="padding:16px; border-radius:16px; background:#121c32; border:1px solid #2b3e5f;">
Scalable structure for future features and better models.
</div></div>
---

Future Scope

Add prediction confidence values

Add image preprocessing preview

Add crop disease history page

Add weather and soil support

Add marker-based map layers

Add multilingual chatbot responses

Add dashboard analytics

Add authentication and admin controls

Add database support for history

Add better mobile animations



---

Why This Project Is Strong

This project combines design, AI, and agriculture into one polished platform.

It demonstrates:

frontend development

backend integration

machine learning workflow

conversational AI

design thinking

domain-specific problem solving


That makes it valuable for GitHub, interviews, and portfolio presentation.


---

Contribution

You can improve this project by adding:

better visuals

stronger prediction pipeline

more crop classes

richer map data

smoother transitions

cleaner response formatting



---

License

This project is intended for learning, portfolio use, and demonstration.


---

Author

Built as a modern agriculture and AI platform for crop support, guidance, and intelligent user experience.
