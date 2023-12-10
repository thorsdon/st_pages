from pathlib import Path

import streamlit as st
from st_pages import Page, add_page_title, show_pages

with st.echo("below"):
    "## Declaring the pages in your app:"

    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠"),
            Page("pages/example_one.py", "Example One", ":books:"),
            Page("pages/example_two.py", "Example Two", "📖"),
            Page("pages/example_three.py", "Example Three", "✏️"),
            Page("pages/example_four.py", "Example Four", "📝"),
            Page("pages/example_five.py", "Example Five", "🧰"),
        ]
    )

    add_page_title()  # Optional method to add title and icon to current page
