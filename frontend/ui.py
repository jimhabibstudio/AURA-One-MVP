# frontend/ui.py

import streamlit as st
import matplotlib.pyplot as plt
from backend.planning_engine import plan_floor_plan


def display_app():
    st.set_page_config(page_title="AURA One - AI Floor Plan Generator")
    st.title("🏠 AURA One MVP")
    st.subheader("Instant AI-Based Architectural Floor Plan Generator")

    with st.form("floorplan_form"):
        prompt = st.text_input("Describe your rooms (comma-separated):", "Living Room, Kitchen, Bedroom, Bathroom")
        submitted = st.form_submit_button("Generate Plan")

    if submitted:
        if not prompt.strip():
            st.warning("Please enter a valid prompt like 'Living Room, Kitchen, Bedroom'.")
            return

        try:
            layout = plan_floor_plan(prompt)
            if not layout:
                st.warning("No layout generated.")
                return

            fig, ax = plt.subplots()
            for room_name, (x, y) in layout:
                ax.add_patch(plt.Rectangle((x, y), 6, 6, edgecolor='black', facecolor='lightblue'))
                ax.text(x + 3, y + 3, room_name, ha='center', va='center', fontsize=8)

            ax.set_xlim(0, 50)
            ax.set_ylim(0, 50)
            ax.set_aspect('equal')
            ax.axis('off')

            st.pyplot(fig)
        except Exception as e:
            st.error(f"⚠️ Failed to generate floor plan: {e}")
