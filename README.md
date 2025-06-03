# 🏠 AURA One MVP - AI Floor Plan Generator

AI-powered procedural architecture tool for instantly generating floor plans from room prompts.

## 🚀 Features
- Procedural generation of floor plans
- 2D visualizations with Matplotlib
- Lightweight, fast, and deployable on Streamlit Cloud

## 🧱 Project Structure
```
AURA-One-MVP/
├── app.py                 # Streamlit entry point
├── requirements.txt
├── backend/
│   ├── procedural_generator.py
│   └── layout_optimizer.py
├── frontend/ui.py
├── models/prompt_engine.py
├── utils/helpers.py
├── assets/
└── README.md
```

## 🔧 Setup
```bash
git clone https://github.com/YOUR_USERNAME/AURA-One-MVP.git
cd AURA-One-MVP
pip install -r requirements.txt
streamlit run app.py
```

## 🧠 Example Usage
Input:
```
living_room, bedroom, bedroom, kitchen, bathroom
```
Output:
- Auto-sized floor plan with labeled room rectangles
- Instant feedback and render

## 🌍 Live Deployment (Optional)
Deploy directly on [Streamlit Cloud](https://streamlit.io/cloud):
- Connect your GitHub repo
- Set main file as `app.py`
- Click Deploy!

---

## 📩 Contact
For ideas or contributions, reach out to the creator.
