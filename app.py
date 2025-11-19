import streamlit as st
import time
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- Custom CSS for the "Pro" look ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #FF4B4B; color: white;}
    .reportview-container { background: #ffffff; }
    .status-box { border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; }
</style>
""", unsafe_allow_html=True)

# --- Top Header ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Next-Gen Video Generation Architecture")
st.caption("Powered by **Vertex AI** | Orchestrated by **Gemini 2.0/3.0**")
st.divider()

# --- Layout ---
col1, col2 = st.columns([1, 2])

# === LEFT COLUMN: User & Config ===
with col1:
    st.subheader("1. ADK Web (Input)")
    
    # User Input
    user_prompt = st.text_area(
        "Creative Prompt", 
        "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution.", 
        height=120
    )
    
    # Configuration with NEW MODELS
    with st.expander("⚙️ Model Configuration", expanded=True):
        # HERE ARE THE NEW MODELS YOU REQUESTED
        model = st.selectbox(
            "Select LLM Backbone", 
            ["Gemini 2.0 Flash (Experimental)", "Gemini 3.0 (Future Preview)", "Gemini 1.5 Pro"]
        )
        
        st.slider("Video Duration (sec)", 5, 60, 15)
        st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1"])

    st.info(f"🔌 Connected to: {model}")
    
    # Action Button
    run_btn = st.button("🚀 Generate Video", type="primary")

# === RIGHT COLUMN: Process & Real Video ===
with col2:
    st.subheader("2. Orchestrator & Output")
    
    if run_btn:
        # 1. Visualizing the Agent Logic
        with st.status(f"⚡ {model} Orchestrator Running...", expanded=True) as status:
            
            # Step 1: Reasoning
            st.write("🧠 **Agent:** Analyzing prompt semantics & visual requirements...")
            time.sleep(1.0)
            st.markdown("`Strategy: Cyberpunk Style -> High Contrast -> Fluid Motion`")
            
            # Step 2: Storyboard
            time.sleep(0.8)
            st.info("📝 **Tool:** [Storyboard Engine]")
            st.text("Scene 1: Wide angle street view\nScene 2: Close up of neon sign\nScene 3: Steam rising from cup")
            
            # Step 3: Image Gen (Gemini 2/3 capabilities)
            time.sleep(1.2)
            st.info(f"🎨 **Tool:** [Image Gen] (Powered by {model})")
            # Showing thumbnails
            c1, c2, c3 = st.columns(3)
            with c1: st.image("https://picsum.photos/150/100?random=1", caption="Keyframe A")
            with c2: st.image("https://picsum.photos/150/100?random=2", caption="Keyframe B")
            with c3: st.image("https://picsum.photos/150/100?random=3", caption="Keyframe C")
            
            # Step 4: Video Generation
            time.sleep(2.0)
            st.warning("🎥 **Tool:** [Video Generation Model v3]")
            prog = st.progress(0, text="Rendering Latent Space...")
            for i in range(100):
                time.sleep(0.01) # Fast render simulation
                prog.progress(i+1)
            
            status.update(label="✅ Generation Complete!", state="complete", expanded=False)
        
        # 2. THE REAL VIDEO OUTPUT
        st.divider()
        st.subheader("✨ Final Generated Video")
        st.balloons()
        
        # This plays a REAL video from a URL. 
        # I selected a "Neon/City" stock video to match the prompt.
        video_url = "https://videos.pexels.com/video-files/3121459/3121459-hd_1920_1080_25fps.mp4"
        
        st.video(video_url, format="video/mp4", start_time=0)
        
        st.success(f"Generated in 6.2s using {model}")
        
        with st.expander("View Technical Metadata"):
            st.json({
                "model_version": model,
                "resolution": "1920x1080",
                "fps": 25,
                "seed": 482910
            })

    else:
        # Placeholder state
        st.info("👈 Select 'Gemini 3.0' and click Generate to see the future.")
        # A clean placeholder box
        st.markdown(
            """
            <div style="background-color:#f0f2f6; padding:50px; border-radius:10px; text-align:center; color:grey;">
                Waiting for input...
            </div>
            """, 
            unsafe_allow_html=True
        )
