# frontend/ui.py

import streamlit as st
import matplotlib.pyplot as plt
from procedural_generator import generate_floor_plan  # simplified import path after sys.path fix

def display_app():
    st.set_page_config(page_title="AURA One - AI Floor Plan Generator")
    st.title("🏠 AURA One MVP")
    st.subheader("Instant Floor Plan Sketch Generator")

    with st.form("floorplan_form"):
        prompt = st.text_input("Describe your rooms (comma-separated):", "bedroom, kitchen, bathroom")
        submitted = st.form_submit_button("Generate Plan")

    if submitted:
        if not prompt.strip():
            st.warning("Please enter a valid prompt like 'living room, bedroom, bathroom'.")
            return

        try:
            room_list = [room.strip() for room in prompt.split(",") if room.strip()]
            fig = generate_floor_plan(room_list)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"⚠️ Failed to generate floor plan: {e}")
