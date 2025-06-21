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
        ("approval_barplot_Age_CHILD.png", "Age Group: CHILD", "Trials including children face nuanced approval due to ethical sensitivity and urgency of conditions."),
        ("approval_barplot_is_os_present.png", "Presence of Overall Survival Metric", "Survival-based endpoints increase confidence in treatment impact, often improving approval odds."),
        ("approval_barplot_is_response.png", "Use of Response Metrics", "Trials with response-based evaluation (like tumor shrinkage) show clearer short-term benefit signals."),
        ("approval_barplot_tumor_trial_with_survival.png", "Tumor Trial with Survival Measure", "Combination of oncology and survival goals leads to significantly higher approval trends.")
    ]

    for img_file, label, insight in charts:
        col1, col2 = st.columns([1, 2])
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
        ("distribution_study_duration_days.png", "Study Duration", "Longer durations imply more robust and well-followed studies, influencing positive outcomes."),
        ("distribution_primary_outcome_duration_days.png", "Primary Outcome Time Window", "Longer time horizons help capture treatment efficacy better, especially for chronic diseases."),
        ("distribution_max_time_window_month.png", "Max Duration for Outcome Capture", "Broader time windows often indicate complex or staged outcome capture protocols."),
        ("distribution_registration_to_start_days.png", "Time from Registration to Trial Start", "Shorter registration-to-start intervals may reflect efficient operational execution."),
        ("distribution_num_locations.png", "Number of Trial Locations", "Wider geographic coverage suggests scalability and diversity, aiding regulatory confidence."),
        ("distribution_sponsor_trial_count.png", "Number of Trials by Sponsor", "Sponsors with trial history generally have established infrastructure and reliability."),
        ("distribution_novelty_per_followup_time.png", "Novelty vs Follow-Up Duration", "Balanced innovation with sufficient observation time is crucial for approval.")
    ]

    for img_file, label, insight in distribution_charts:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(os.path.join(img_dir, img_file), caption=label, use_container_width=True)
        with col2:
            st.markdown(f"**{label}**")
            st.markdown(insight)
            st.markdown("---")
