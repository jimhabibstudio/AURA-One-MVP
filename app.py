# app.py
# AURA One MVP Entry Point

import streamlit as st
import sys
import os

# Ensure subfolders are importable
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Import Streamlit UI function from frontend
from ui import display_app

if __name__ == '__main__':
    display_app()
