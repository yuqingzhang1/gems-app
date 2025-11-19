import streamlit as st
import time
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- Custom CSS for a cleaner look ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .reportview-container { background: #f0f2f6; }
    .success-text { color: green; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- Top Header ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Architecture Demo: Open Source Implementation Design")
st.markdown("User ➔ ADK Web ➔ **Orchestrator Agent (MCP Server)** ➔ Tools ➔ Final Output")
st.divider()

# --- Layout: Left (Input) & Right (Process Visualization) ---
col1, col2 = st.columns([1, 2])

# === LEFT COLUMN: User & ADK Config ===
with col1:
    st.header("1. ADK Web (Frontend)")
    st.info("Simulating the User Input & Configuration Layer")
    
    # User Input
    user_prompt = st.text_area(
        "User Instruction", 
        "Create a 15-second cinematic video advertisement for a futuristic coffee shop in Tokyo with neon lights.", 
        height=150
    )
    
    # Configuration (Simulating the ADK settings)
    with st.expander("⚙️ System Configuration", expanded=True):
        st.selectbox("LLM Backend", ["Gemini 1.5 Pro", "Gemini Ultra"])
        st.checkbox("Enable Chain of Thought", value=True)
        st.slider("Creativity Temperature", 0.0, 1.0, 0.7)
    
    # Action Button
    run_btn = st.button("🚀 Run Orchestrator", type="primary")

# === RIGHT COLUMN: The Middle Part (Agent & Tools) ===
with col2:
    st.header("2. Orchestrator Agent & Tools")
    
    if run_btn:
        # Visualizing the "Single MCP Server" logic
        with st.status("⚡ Orchestrator Agent is active...", expanded=True) as status:
            
            # Step 1: Reasoning
            st.write("🧠 **Agent (Gemini):** Decomposing user request into tasks...")
            time.sleep(1.5) # Simulate latency
            st.markdown("`Plan: Storyboard -> Image Gen -> Video Gen -> Concatenation`")
            
            # Step 2: Storyboard Tool
            time.sleep(1.0)
            st.info("🔧 **Tool Call:** [Generate Storyboard]")
            st.markdown("> *Scene 1: Wide shot of neon streets...*")
            st.markdown("> *Scene 2: Close up of coffee pouring...*")
            
            # Step 3: Image Generation Tool
            time.sleep(1.5)
            st.info("🔧 **Tool Call:** [Generate Image] (Parallel Execution)")
            
            # Display placeholder images to simulate generation
            img_cols = st.columns(3)
            with img_cols[0]:
                st.image("https://picsum.photos/200/120?random=10", caption="Keyframe 1 Generated")
            with img_cols[1]:
                st.image("https://picsum.photos/200/120?random=20", caption="Keyframe 2 Generated")
            with img_cols[2]:
                st.image("https://picsum.photos/200/120?random=30", caption="Keyframe 3 Generated")
            
            # Step 4: Video Generation Tool
            time.sleep(1.5)
            st.info("🔧 **Tool Call:** [Generate Video] (Image-to-Video)")
            my_bar = st.progress(0, text="Rendering video assets...")
            for percent_complete in range(100):
                time.sleep(0.02)
                my_bar.progress(percent_complete + 1)
            
            # Step 5: Concatenation
            st.warning("🔧 **Tool Call:** [Video Concatenation]")
            st.markdown("`Running FFmpeg script via Python wrapper...`")
            time.sleep(1.0)
            
            # Update status to complete
            status.update(label="✅ Workflow Completed Successfully!", state="complete", expanded=False)
        
        # --- Final Result Display ---
        st.divider()
        st.subheader("✨ Final Output")
        st.balloons()
        
        # Mock Video Player
        st.image(
            "https://picsum.photos/800/400?grayscale", 
            caption="Final Rendered Video Output (Preview Mode)", 
            use_container_width=True
        )
        
        # Mock JSON Response
        with st.expander("View API Response JSON"):
            st.json({
                "status": "success",
                "latency": "8.4s",
                "modules_used": ["storyboard_agent", "imagen_pro", "video_concat"],
                "cost_estimate": "$0.04"
            })

    else:
        # Default State
        st.info("👈 Enter a prompt and click 'Run Orchestrator' to visualize the modular workflow.")
        # Placeholder to keep the layout balanced
        st.image("https://placehold.co/600x300?text=Architecture+Visualization+Area", use_container_width=True)
