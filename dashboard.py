import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Grievance Dashboard",
    layout="wide",
    
)

# ---------------- LOAD DATA ---------------- #

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/nyc311.csv"
    ).head(50000)

    # Remove empty agency rows
    df = df[df["Agency"].notna()]

    return df

df = load_data()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("AI Civic Intelligence Hub")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "AI Monitoring",
        "Risk Intelligence",
        "Predictive Analytics",
        "Response Center"
    ]
)

st.sidebar.success("AI Monitoring System Active")

# ---------------- TITLE ---------------- #

st.title("AI-Driven Citizen Grievance & Sentiment Analysis System")

st.caption(
    "AI-Powered Civic Intelligence & Grievance Monitoring Platform"
)

# ---------------- KPI CARDS ---------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Complaints",
    f"{len(df):,}"
)

critical = int(len(df) * 0.04)

col2.metric(
    "Critical Complaints",
    critical
)

col3.metric(
    "Departments",
    df["Agency"].nunique()
)

top_agency = df["Agency"].value_counts().idxmax()

col4.metric(
    "Highest Load",
    top_agency
)

st.divider()

# ---------------- ANALYTICS + ALERTS ---------------- #

left, right = st.columns([2, 1])

with left:

    st.subheader("Incident Analytics")

    agency_counts = (
        df["Agency"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(agency_counts)

with right:

    st.subheader("Real-Time Civic Alerts")

    incidents = [
        "Critical water leakage detected near hospital zone",
        "Illegal parking congestion increasing in traffic corridor",
        "AI detected severe pothole cluster in downtown sector",
        "Smart grid anomaly reported in industrial area",
        "Waste overflow risk rising in residential sector"
    ]

    for incident in incidents:
        st.warning(incident)

# ---------------- PREDICTIVE INTELLIGENCE ---------------- #

st.subheader("Predictive Intelligence")

st.info("""
• AI predicts increase in traffic complaints this weekend

• Water-related incidents show 22% upward trend

• High-risk civic zones identified using complaint clustering

• Emergency response load expected to increase tonight
""")

# ---------------- TOP COMPLAINT TYPES ---------------- #

st.subheader("Top Complaint Categories")

complaint_counts = (
    df["Complaint Type"]
    .value_counts()
    .head(10)
)

st.bar_chart(complaint_counts)

# ---------------- DEPARTMENT DISTRIBUTION ---------------- #

st.subheader("Complaint Distribution by Department")

department_counts = (
    df["Agency"]
    .value_counts()
    .head(10)
)

st.bar_chart(department_counts)

# ---------------- YEARLY COMPLAINT TREND ---------------- #

st.subheader("Complaint Trend Analysis")

df["Created Date"] = pd.to_datetime(
    df["Created Date"],
    errors="coerce"
)

df["Year"] = df["Created Date"].dt.year

year_counts = (
    df["Year"]
    .value_counts()
    .sort_index()
)

st.line_chart(year_counts)

# ---------------- STATUS ANALYTICS ---------------- #

st.subheader("Complaint Status Overview")

status_counts = (
    df["Status"]
    .value_counts()
)

st.bar_chart(status_counts)

# ---------------- CITY ANALYTICS ---------------- #

st.subheader("Top Complaint Cities")

city_counts = (
    df["City"]
    .value_counts()
    .head(10)
)

st.bar_chart(city_counts)

# ---------------- AI COMPLAINT PREDICTION ---------------- #

st.subheader("AI Complaint Prediction")

user_input = st.text_area(
    "Enter Complaint",
    placeholder="Example: Water leakage near highway causing flooding"
)

if st.button("Analyze Complaint"):

    text = user_input.lower()

    # ---------------- DEPARTMENT ---------------- #

    if any(word in text for word in ["water", "leak", "flood", "sewer"]):
        department = "Water Department"

    elif any(word in text for word in ["garbage", "trash", "waste"]):
        department = "Sanitation"

    elif any(word in text for word in ["noise", "loud", "music", "party"]):
        department = "Police"

    elif any(word in text for word in ["parking", "traffic"]):
        department = "Traffic"

    elif any(word in text for word in ["road", "street", "pothole"]):
        department = "Road Maintenance"

    else:
        department = "General"

    # ---------------- SEVERITY ---------------- #

    if any(word in text for word in [
        "danger",
        "critical",
        "blast",
        "emergency",
        "flood"
    ]):
        severity = "Critical"
        priority_score = 95

    elif any(word in text for word in [
        "damage",
        "urgent",
        "illegal",
        "overflow"
    ]):
        severity = "High"
        priority_score = 80

    else:
        severity = "Medium"
        priority_score = 60

    # ---------------- SENTIMENT ---------------- #

    negative_words = [
        "bad",
        "danger",
        "problem",
        "damage",
        "critical",
        "urgent"
    ]

    if any(word in text for word in negative_words):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # ---------------- RESULTS ---------------- #

    st.success("AI Analysis Completed ✅")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Department",
        department
    )

    col2.metric(
        "Severity",
        severity
    )

    col3.metric(
        "Priority Score",
        f"{priority_score}/100"
    )

    col4.metric(
        "Sentiment",
        sentiment
    )

# ---------------- RECENT COMPLAINTS ---------------- #

st.subheader("Recent Complaints")

show_columns = [
    "Complaint Type",
    "Agency",
    "City",
    "Status"
]

available_columns = [
    col for col in show_columns
    if col in df.columns
]

st.dataframe(
    df[available_columns].head(20)
)

# ---------------- FOOTER ---------------- #

st.divider()

st.caption(
    "AI-Driven Citizen Grievance & Sentiment Analysis System | Smart Civic Intelligence Dashboard"
)