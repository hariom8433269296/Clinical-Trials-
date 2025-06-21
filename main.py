import streamlit as st
import os
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.title("🧪 Clinical Trials Modeling Dashboard")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Key Features and Their Influence on Outcome",
    "Distributions of Important Variables"
])

# Image directory
img_dir = "dashboard_images"

# 1. Key Features and Their Influence
if page == "Key Features and Their Influence on Outcome":
    st.header("📌 Key Features and Their Influence on Outcome")

    charts = [
        ("approval_barplot_Age_CHILD.png", "Age Group: CHILD", "Trials that include children are carefully reviewed but often get approved when there's clear medical need."),
        ("approval_barplot_is_os_present.png", "Presence of Overall Survival Metric", "Using overall survival as a measure increases approval chances by showing treatment impact."),
        ("approval_barplot_is_response.png", "Use of Response Metrics", "Response metrics like tumor shrinkage help show early benefits, improving approval chances."),
        ("approval_barplot_tumor_trial_with_survival.png", "Tumor Trial with Survival Measure", "Trials that combine cancer focus with survival goals show much higher approval rates.")
    ]

    for img_file, label, insight in charts:
        col1, col2 = st.columns([1.2, 1.8])
        with col1:
            st.image(os.path.join(img_dir, img_file), caption=label, use_container_width=True)
        with col2:
            st.markdown(f"**{label}**")
            st.markdown(insight)
            st.markdown("---")

# 2. Distribution of Numerical / Count Features
elif page == "Distributions of Important Variables":
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
        col1, col2 = st.columns([1.2, 1.8])
        with col1:
            st.image(os.path.join(img_dir, img_file), caption=label, use_container_width=True)
        with col2:
            st.markdown(f"**{label}**")
            st.markdown(insight)
            st.markdown("---")
