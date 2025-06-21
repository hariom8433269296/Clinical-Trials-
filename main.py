import streamlit as st
import os
from PIL import Image

# Set page title and config
st.set_page_config(page_title="Clinical Trials EDA Dashboard", layout="wide")
st.title("📊 Clinical Trials Dashboard")
st.markdown("""
This dashboard visualizes key engineered features and their relationship with clinical trial outcomes (Approval vs Failure).
Generated from both structured metadata and LLM-parsed insights.
""")

# Dashboard Sections
def show_feature_analysis():
    st.header("🔍 Feature Importance & Influence")

    st.subheader("Top Predictive Features")
    st.markdown("""
    Below are the most impactful features identified using SHAP analysis across tree-based models:

    - **Outcome Measures**: Survival-related measures (`is_os_present`, `is_pfs_present`, `is_response`) had high correlation with trial success.
    - **Trial Structure**: Longer follow-up durations, higher number of comparison arms, and posted results (`was_result_posted`) aligned with approvals.
    - **Population**: Trials involving children (`Age_CHILD`) or adult-specific cohorts showed differing patterns.
    - **Drug Novelty**: Trials backed by rare or novel drugs often faced more scrutiny, seen via `drug_novelty_score`.
    - **Sponsor Tiers**: Tiered sponsor power contributed to variance in outcome likelihood.
    - **Enrollment Stats**: Higher site and patient count added to approval probability.
    """)

    image_paths = [
        "dashboard_images/approval_barplot_is_os_present.png",
        "dashboard_images/approval_barplot_is_response.png",
        "dashboard_images/approval_barplot_tumor_trial_with_survival.png",
        "dashboard_images/approval_barplot_Age_CHILD.png",
        "dashboard_images/distribution_primary_outcome_duration_days.png",
        "dashboard_images/distribution_max_time_window_month.png",
        "dashboard_images/distribution_novelty_per_followup_time.png",
        "dashboard_images/distribution_novel_drug_backed_by_sponsor.png"
    ]

    cols = st.columns(2)
    for i, path in enumerate(image_paths):
        with cols[i % 2]:
            st.image(Image.open(path), caption=os.path.basename(path).replace("_", " ").replace(".png", "").title(), use_column_width=True)


def show_distribution_analysis():
    st.header("📈 Distribution of Engineered Features")
    st.markdown("""
    The following plots show the distribution of engineered numerical and count-based features that impact model behavior:

    - Time-related durations (study duration, registration delays)
    - Outcome complexity (number of measures, time windows)
    - Enrollment metadata (number of sites, enrollment targets)
    - Sponsor and intervention statistics
    """)

    dist_paths = sorted([f"dashboard_images/{f}" for f in os.listdir("dashboard_images") if f.startswith("distribution_")])
    for i in range(0, len(dist_paths), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(dist_paths):
                with cols[j]:
                    st.image(Image.open(dist_paths[i + j]), caption=dist_paths[i + j].split("dashboard_images/")[1].replace(".png", "").replace("_", " ").title(), use_column_width=True)

# Navigation
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio("Jump to Section", ["Feature Influence", "Distributions"])

if section == "Feature Influence":
    show_feature_analysis()
elif section == "Distributions":
    show_distribution_analysis()
