import streamlit as st

st.set_page_config(page_title="Burgo's AI Project Hub", layout="centered", page_icon="🤖")

st.title("🤖 Burgo's Testing AI Hub (Mostly Marketing)")
st.markdown("Welcome! This is me, messing around with experimental AI tools.")
st.markdown("---")

# Reusable app card with image preview and fixed height
def app_card(title, description, emoji, url, image_url):
    st.markdown(f"""
    <div style="
        border:1px solid #ddd; 
        border-radius:15px; 
        padding:20px; 
        margin-bottom:20px; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05); 
        text-align: center; 
        min-height: 480px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    ">
        <div>
            <img src="{image_url}" alt="{title} preview" style="width:100%; border-radius:12px; margin-bottom:15px;" />
            <h3 style="margin-bottom:0;">{emoji} {title}</h3>
            <p style="margin-top:5px;">{description}</p>
        </div>
        <a href="{url}" target="_blank">
            <button style="
                background-color:#ffb81c; 
                color:black; 
                padding:8px 20px; 
                border:none; 
                border-radius:10px; 
                font-weight:bold; 
                cursor:pointer; 
                margin-top:10px;
            ">
                Open App
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# First row
col1, col2 = st.columns(2)

with col1:
    app_card(
        title="Headline Generator",
        description="Update existing headlines using proven copywriting frameworks like AIDA, PAS, and more.",
        emoji="📝",
        url="https://foolish-ai-headline-generator.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Burgo-s-Copywriting-Framework-Headline-Rewriter-%C2%B7-Streamlit-03-17-2025_03_02_PM.png"
    )

with col2:
    app_card(
        title="Writer Briefings",
        description="Auto-generate editorial briefs using trending market topics and news insights.",
        emoji="📄",
        url="https://foolishwriterbriefings.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Burgo-s-Briefing-App-%C2%B7-Streamlit-03-17-2025_03_02_PM.png"
    )

# Second row
col3, col4 = st.columns(2)

with col3:
    app_card(
        title="Persona Portal",
        description="Explore realistic investor personas and test messaging with AI-powered simulations.",
        emoji="👥",
        url="https://burgo-ai-persona-project.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Burgo-s-Persona-Portal-%C2%B7-Streamlit-03-17-2025_03_02_PM.png"
    )

with col4:
    app_card(
        title="Headline Comparator",
        description="Compare two headlines side-by-side and get instant AI-powered analysis on which one is stronger.",
        emoji="🆚",
        url="https://burgo-headline-comparator.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Burgo-s-Headline-Comparator-03-17-2025_07_45_PM.png"
    )

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Burgo</p>", unsafe_allow_html=True)
