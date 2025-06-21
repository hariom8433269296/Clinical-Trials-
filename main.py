import streamlit as st
import os
from PIL import Image

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
        ("approval_barplot_Age_CHILD.png", "Age_CHILD", "Trials including children often face stricter approval criteria, but also target critical diseases, showing mixed impact."),
        ("approval_barplot_is_os_present.png", "Overall Survival (OS) Mentioned", "Presence of OS indicates trials measuring long-term survival, often linked with higher approval likelihood."),
        ("approval_barplot_is_response.png", "Response Metric Used", "Trials reporting response rates show regulatory preference, especially for oncology studies."),
        ("approval_barplot_tumor_trial_with_survival.png", "Tumor Trial w/ Survival Metric", "Combination of tumor-related and survival metrics shows very high approval correlation.")
    ]

    for img_file, label, insight in charts:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(os.path.join(img_dir, img_file), caption=label, use_column_width=True)
        with col2:
            st.markdown(f"**{label}**")
            st.markdown(insight)
            st.markdown("---")

# 2. Distribution of Numerical / Count Features
elif page == "Distributions of Important Variables":
    st.header("📊 Distributions of Important Variables")

    distribution_charts = [
        ("distribution_study_duration_days.png", "Study Duration", "Longer studies often reflect robust design and follow-up, positively impacting approval."),
        ("distribution_primary_outcome_duration_days.png", "Primary Outcome Time", "Indicates timeline over which primary effect is assessed – longer timelines hint at deeper efficacy measurements."),
        ("distribution_max_time_window_month.png", "Max Time Window (Outcome)", "A wider time window for outcome collection suggests complex, multi-arm or long-term studies."),
        ("distribution_registration_to_start_days.png", "Registration to Start Delay", "Higher delays could indicate operational or regulatory issues, which may influence approval negatively."),
        ("distribution_num_locations.png", "Number of Trial Locations", "Multisite trials are usually more scalable and diverse – often linked to higher approval."),
        ("distribution_sponsor_trial_count.png", "Trial Count per Sponsor", "Sponsors with more experience tend to conduct more successful trials."),
        ("distribution_novelty_per_followup_time.png", "Novelty vs Follow-Up Time", "Shows how novel interventions align with adequate follow-up for evaluation.")
    ]

    for img_file, label, insight in distribution_charts:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(os.path.join(img_dir, img_file), caption=label, use_column_width=True)
        with col2:
            st.markdown(f"**{label}**")
            st.markdown(insight)
            st.markdown("---")
