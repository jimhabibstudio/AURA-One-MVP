# frontend/ui.py

import streamlit as st
import matplotlib.pyplot as plt
from backend.procedural_generator import generate_floor_plan

def display_app():
    st.set_page_config(page_title="AURA One - AI Floor Plan Generator")
    st.title("🏠 AURA One MVP")
    st.subheader("Instant Floor Plan Sketch Generator")

    with st.form("floorplan_form"):
        prompt = st.text_input(
            "Describe your desired rooms (comma-separated):",
            "living room, bedroom, kitchen, bathroom"
        )
        submitted = st.form_submit_button("Generate Floor Plan")

    if submitted:
        if not prompt.strip():
            st.warning("❗ Please enter at least one room.")
            return

        try:
            # Parse room list
            room_list = [room.strip() for room in prompt.split(",") if room.strip()]
            st.markdown("🛠️ Generating your layout...")
            
            # Generate and display plan
            fig = generate_floor_plan(room_list)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"🚫 Error generating layout: {e}")
