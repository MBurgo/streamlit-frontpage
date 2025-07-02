import streamlit as st

st.set_page_config(page_title="Burgo's AI Project Hub", layout="centered", page_icon="🤖")

st.title("🤖 Burgo's Testing AI Hub (Mostly Marketing)")
st.markdown("Welcome! This is me, messing around with experimental AI tools.")
st.markdown("---")

# App card for live tools (your original code — do not touch this!)
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

# Separate function for coming soon cards
def coming_soon_card(title, description, emoji, image_url):
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
        opacity: 0.75;
    ">
        <div>
            <img src="{image_url}" alt="{title} preview" style="width:100%; border-radius:12px; margin-bottom:15px; opacity:0.9;" />
            <h3 style="margin-bottom:0;">{emoji} {title}</h3>
            <p style="margin-top:5px;">{description}</p>
        </div>
        <div style="margin-top:10px; font-style: italic; color: #666; font-weight: bold;">🚧 Coming Soon</div>
    </div>
    """, unsafe_allow_html=True)

# --- LIVE TOOLS ---
st.markdown("### 🟢 **Live Tools**")
st.markdown("---")

# First row
col1, col2 = st.columns(2)

with col1:
    app_card(
        title="Writer Briefings",
        description="Auto-generate editorial briefs using trending market topics and news insights.",
        emoji="📄",
        url="https://foolishwriterbriefings.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T163603.352.jpg"
    )

with col2:
    app_card(
        title="Persona Portal",
        description="Explore realistic investor personas and test messaging with AI-powered simulations.",
        emoji="👥",
        url="https://burgo-ai-persona-project.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T162947.085.jpg"
    )

# Second row
col3, col4 = st.columns(2)

with col3:
    app_card(
        title="Campaign Concept Generator",
        description="Need a fresh campaign idea? This tool helps brainstorm concepts based on your goals and offer.",
        emoji="🎯",
        url="https://burgo-campaign-concept-generator.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T163822.097.jpg"
    )

with col4:
    app_card(
        title="Funnel Fixer",
        description="Audit your funnel copy and get AI-powered suggestions to improve clarity, conversion, and Foolishness — fast.",
        emoji="🛠️",
        url="https://foolish-funnel-fixer.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T164121.225.jpg"
    )

# Third row
col5, col6 = st.columns(2)

with col5:
    app_card(
        title="Headline Comparator",
        description="Compare two headlines side-by-side and get instant AI-powered analysis on which one is stronger.",
        emoji="🆚",
        url="https://burgo-headline-comparator.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T164357.351.jpg"
    )

with col6:
    app_card(
        title="Headline Generator",
        description="Update existing headlines using proven copywriting frameworks like AIDA, PAS, and more.",
        emoji="📝",
        url="https://foolish-ai-headline-generator.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-19T164518.419.jpg"
    )

# Fourth row
col7, col8 = st.columns(2)

with col7:
    app_card(
        title="Swipe Tool",
        description="Adapt great ads from other industries into Foolish copy. This tool reworks structure, tone, and tactics for our audience.",
        emoji="📥",
        url="https://burgo-ai-swipe-tool.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_%20-%202025-03-21T104825.029.jpg"
    )

with col8:
    app_card(
        title="Synthetic Focus Group",
        description="Drop in draft copy and get instant reactions from 50 AI personas modelled on real Aussie investor segments.",
        emoji="🧪",
        url="https://burgo-synthetic-focus-test.streamlit.app/",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/image_fx_-_synthetic-focus-group.jpg"  # Replace with your actual thumbnail
    )

# Fifth row (new tile addition)
col9, _ = st.columns(2)

with col9:
    app_card(
        title="AI Copywriter Tool",
        description="Brief in, generate and adapt marketing copy with AI, using structured prompts and linguistic trait sliders.",
        emoji="✍️",
        url="https://burgo-mf-ai-copywriter.streamlit.app/",
        image_url="https://github.com/MBurgo/streamlit-frontpage/blob/main/assets/Image_fx%20(31).jpg?raw=true"  # Replace this URL with the actual thumbnail if you have one
    )

# --- IN DEVELOPMENT ---
st.markdown("### 🛠️ **In Development**")
st.markdown("---")

col7, col8 = st.columns(2)

with col7:
    coming_soon_card(
        title="Predictive Lead Scoring (Braze)",
        description="Segment leads based on AI-predicted likelihood to convert. Hot leads get sales emails. Cold leads get nurtured. Built to reduce churn and increase conversion — directly integrated into Braze.",
        emoji="🔮",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Untitled%20design%20(42).png"
    )

with col8:
    coming_soon_card(
        title="Creative Intelligence Platform",
        description="Track performance of headlines, CTAs, and copy at the element level — not just the campaign level. Get AI-powered insights and suggestions to optimize creatives and reduce CAC.",
        emoji="🧠",
        image_url="https://raw.githubusercontent.com/MBurgo/streamlit-frontpage/refs/heads/main/assets/Untitled%20design%20(42).png"
    )

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Burgo</p>", unsafe_allow_html=True)
