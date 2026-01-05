import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab


# Styling for title

st.markdown("""
<style>
.neon-title {
    font-size: 50px;
    font-weight: 900;
    text-align: center;
    color: #fff;
    text-shadow:
        0 0 5px #ff6b6b,
        0 0 10px #ff6b6b,
        0 0 20px #ff4757,
        0 0 40px #ff4757;
    position: relative;
    display: inline-block;
    transition: transform 0.3s ease;
    cursor: pointer;
}

.neon-title:hover {
    transform: scale(1.07);
}

/* animated underline */
.neon-title::after {
    content: "";
    position: absolute;
    width: 0%;
    height: 4px;
    left: 50%;
    bottom: -10px;
    background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb);
    transition: all 0.4s ease;
}

.neon-title:hover::after {
    width: 100%;
    left: 0;
}
</style>

<div style="text-align:center;">
    <div class="neon-title">Expense Tracking System</div>
</div>
""", unsafe_allow_html=True)


# Styling for tabs

st.markdown("""
<style>
/* TAB NORMAL */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    padding: 12px 18px;
    transition: all 0.3s ease;
    cursor: pointer;
}

/* TAB HOVER */
.stTabs [data-baseweb="tab"]:hover {
    color: #ff6b6b;
    transform: translateY(-2px);
}

/* ACTIVE TAB */
.stTabs [aria-selected="true"] {
    color: #ff6b6b !important;
    border-bottom: 3px solid #ff6b6b;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# Styling for subtitle

st.markdown("""
<style>
.subtitle {
    text-align: center;
    font-size: 18px;
    font-weight: 500;
    margin-top: 12px;
    color: #cbd5e1;
    letter-spacing: 1px;
    animation: fadeInUp 1.2s ease;
}

/* animated underline */
.subtitle span {
    background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}

/* animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>

<div class="subtitle">
    Track <span>•</span> Analyze <span>•</span> Save smarter
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.subtitle:hover {
    letter-spacing: 2px;
    transition: 0.3s ease;
}
</style>
""", unsafe_allow_html=True)


# Styling for buttons

st.markdown("""
<style>
/* ================= REGULAR BUTTON ================= */
div.stButton > button {
    background: linear-gradient(90deg, #ff6b6b, #feca57);
    color: black;
    border-radius: 14px;
    padding: 12px 26px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    box-shadow: 0 0 18px #ff6b6b;
    transform: scale(1.07);
}

/* ================= FORM SUBMIT BUTTON ================= */
button[kind="primary"] {
    background: linear-gradient(90deg, #ff6b6b, #feca57) !important;
    color: black !important;
    border-radius: 14px !important;
    padding: 12px 26px !important;
    font-size: 16px !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
}

button[kind="primary"]:hover {
    box-shadow: 0 0 18px #ff6b6b !important;
    transform: scale(1.07);
}
</style>
""", unsafe_allow_html=True)



tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()


