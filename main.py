import streamlit as st
import os
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title("🧪 Clinical Trials Modeling Dashboard")

# Session state to control navigation
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

pages = [
    "Key Features and Their Influence on Outcome",
    "Distributions of Important Variables",
    "Model Performance and Ensemble Results"
]

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    selected_page = st.radio("Go to", pages, index=st.session_state.page_index)
    st.session_state.page_index = pages.index(selected_page)

# Image directory
img_dir = "dashboard_images"

# Page 1: Key Features and Their Influence
if st.session_state.page_index == 0:
    st.header("📌 Key Features and Their Influence on Outcome")

    charts = [
        ("approval_barplot_Age_CHILD.png", "Age Group: CHILD", "Trials that include children are carefully reviewed but often get approved when there's clear medical need."),
        ("approval_barplot_is_os_present.png", "Presence of Overall Survival Metric", "Using overall survival as a measure increases approval chances by showing treatment impact."),
        ("approval_barplot_is_response.png", "Use of Response Metrics", "Response metrics like tumor shrinkage help show early benefits, improving approval chances."),
        ("approval_barplot_tumor_trial_with_survival.png", "Tumor Trial with Survival Measure", "Trials that combine cancer focus with survival goals show lower approval rates.")
    ]

    for img_file, label, insight in charts:
        st.markdown(f"**{label}**")
        st.markdown(insight)
        st.image(os.path.join(img_dir, img_file), width=590)
        st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col2:
        if st.button("Next ➡️"):
            st.session_state.page_index += 1
            st.rerun()

# Page 2: Distribution of Numerical / Count Features
elif st.session_state.page_index == 1:
    st.header("📊 Distributions of Important Variables")

    distribution_charts = [
        ("distribution_Enrollment.png", "Enrollment Count", "Higher enrollment indicates more representative trials but can also be harder to manage."),
        ("distribution_Secondary Outcome Measures_count.png", "Secondary Outcomes Count", "More secondary outcomes may signal exploratory trials or broader analysis."),
        ("distribution_study_duration_days.png", "Study Duration", "Longer studies are more thorough and often more likely to succeed."),
        ("distribution_primary_outcome_duration_days.png", "Primary Outcome Time Window", "More time for outcome tracking helps measure true treatment effect."),
        ("distribution_max_time_window_month.png", "Max Duration for Outcome Capture", "Larger windows give more flexibility to see delayed effects."),
        ("distribution_registration_to_start_days.png", "Time from Registration to Trial Start", "Quick starts may reflect better planning and coordination."),
        ("distribution_num_locations.png", "Number of Trial Locations", "More locations show trial scale and generalizability."),
        ("distribution_outcome_density.png", "Outcome Density", "High density near target outcomes can reflect efficient trial design."),
        ("distribution_sponsor_trial_count.png", "Number of Trials by Sponsor", "Sponsors with more experience tend to run stronger trials."),
        ("distribution_sponsor_trial_count_tier.png", "Sponsor Trial Tier", "Tiers represent trial volume bands, possibly reflecting sponsor credibility."),
        ("distribution_novelty_per_followup_time.png", "Novelty vs Follow-Up Duration", "New ideas need enough follow-up time to gain trust."),
        ("distribution_novel_drug_backed_by_sponsor.png", "Novel Drug Backed by Sponsor", "Support from established sponsors boosts approval chances of novel therapies.")
    ]

    for img_file, label, insight in distribution_charts:
        st.markdown(f"**{label}**")
        st.markdown(insight)
        width = 590 if "distribution_" in img_file and "barplot" not in img_file and "approval" in img_file else 1000
        st.image(os.path.join(img_dir, img_file), width=width)
        st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.page_index -= 1
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.page_index += 1
            st.rerun()

# Page 3: Model Performance and Ensemble Results
elif st.session_state.page_index == 2:
    st.header("📈 Model Performance and Ensemble Results")

    model_names = ["xgb_gbtree", "lgb_gbdt", "lgb_dart", "rf_sklearn", "cat_Plain"]

    for model in model_names:
        st.subheader(f"🔍 Model: {model.upper()}")

        auc_chart = f"auc_progress_{model}.png"
        if os.path.exists(os.path.join(img_dir, auc_chart)):
            st.markdown("**AUC Progress Over Time**")
            st.image(os.path.join(img_dir, auc_chart), width=1000)
            st.markdown("---")

    st.subheader("🔀 Optuna-Based Hill Climbing Ensemble")

    ensemble_charts = [
        ("optuna_hill_climbing_auc_progress.png", "Ensemble AUC Progress", "Tracks how ensemble performance improved during Optuna optimization."),
        ("Final Ensemble Weights (Hill Climbing).png", "Final Weights of Each Model", "Shows how much each model contributed to the final ensemble."),
        ("Individual Model AUC vs HillClimbed Ensemble.png", "Model vs Ensemble AUC", "Compares each model’s AUC to the ensemble’s performance.")
    ]

    for img_file, title, description in ensemble_charts:
        st.markdown(f"**{title}**")
        st.markdown(description)
        st.image(os.path.join(img_dir, img_file), width=1000)
        st.markdown("---")

    col1, _ = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.page_index -= 1
            st.rerun()
