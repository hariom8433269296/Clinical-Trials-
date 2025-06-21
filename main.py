import streamlit as st
import os
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.title("🧪 Clinical Trials Modeling Dashboard")

# Session state to control navigation
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

pages = [
    "Key Features and Their Influence on Outcome",
    "Distributions of Important Variables"
]

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    selected_page = st.radio("Go to", pages, index=st.session_state.page_index)
    st.session_state.page_index = pages.index(selected_page)

# Next button
if st.session_state.page_index < len(pages) - 1:
    if st.button("Next ➡️"):
        st.session_state.page_index += 1
        st.experimental_rerun()

# Image directory
img_dir = "dashboard_images"

# Page 1: Key Features and Their Influence
if st.session_state.page_index == 0:
    st.header("📌 Key Features and Their Influence on Outcome")

    charts = [
        ("approval_barplot_Age_CHILD.png", "Age Group: CHILD", "Trials that include children are carefully reviewed but often get approved when there's clear medical need."),
        ("approval_barplot_is_os_present.png", "Presence of Overall Survival Metric", "Using overall survival as a measure increases approval chances by showing treatment impact."),
        ("approval_barplot_is_response.png", "Use of Response Metrics", "Response metrics like tumor shrinkage help show early benefits, improving approval chances."),
        ("approval_barplot_tumor_trial_with_survival.png", "Tumor Trial with Survival Measure", "Trials that combine cancer focus with survival goals show much higher approval rates.")
    ]

    for img_file, label, insight in charts:
        st.markdown(f"**{label}**")
        st.markdown(insight)
        st.image(os.path.join(img_dir, img_file), width=590)
        st.markdown("---")

# Page 2: Distribution of Numerical / Count Features
elif st.session_state.page_index == 1:
    st.header("📊 Distributions of Important Variables")

    distribution_charts = [
        ("distribution_study_duration_days.png", "Study Duration", "Longer studies are more thorough and often more likely to succeed."),
        ("distribution_primary_outcome_duration_days.png", "Primary Outcome Time Window", "More time for outcome tracking helps measure true treatment effect."),
        ("distribution_max_time_window_month.png", "Max Duration for Outcome Capture", "Larger windows give more flexibility to see delayed effects."),
        ("distribution_registration_to_start_days.png", "Time from Registration to Trial Start", "Quick starts may reflect better planning and coordination."),
        ("distribution_num_locations.png", "Number of Trial Locations", "More locations show trial scale and generalizability."),
        ("distribution_sponsor_trial_count.png", "Number of Trials by Sponsor", "Sponsors with more experience tend to run stronger trials."),
        ("distribution_novelty_per_followup_time.png", "Novelty vs Follow-Up Duration", "New ideas need enough follow-up time to gain trust.")
    ]

    for img_file, label, insight in distribution_charts:
        st.markdown(f"**{label}**")
        st.markdown(insight)
        st.image(os.path.join(img_dir, img_file), width=850)
        st.markdown("---")
