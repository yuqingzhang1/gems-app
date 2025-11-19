import streamlit as st
import time
import os

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- 2. 样式美化 ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #FF4B4B; color: white;}
</style>
""", unsafe_allow_html=True)

# --- 3. 标题 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Next-Gen Video Generation Architecture")
st.caption("Powered by **Vertex AI** | Orchestrated by **Gemini 2.0/3.0**")
st.divider()

# --- 4. 布局 ---
col1, col2 = st.columns([1, 2])

# === 左侧 ===
with col1:
    st.subheader("1. Input & Context")
    user_prompt = st.text_area(
        "Creative Prompt", 
        "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution.", 
        height=120
    )
    st.markdown("---")
    st.file_uploader("Upload Storyboard (Optional)", type=['png', 'jpg'])
    st.markdown("---")
    model = st.selectbox("Model", ["Gemini 3.0 (Preview)", "Gemini 2.0 Flash"])
    run_btn = st.button("🚀 Generate Video", type="primary")

# === 右侧 ===
with col2:
    st.subheader("2. Real-time Generation")
    
    if run_btn:
        # 模拟 Agent 运行
        with st.status(f"⚡ {model} Orchestrator Running...", expanded=True):
            st.write("🧠 **Agent:** Analyzing prompt...")
            time.sleep(0.5)
            st.write("🎨 **Tool:** [Image Gen] Creating frames...")
            time.sleep(0.5)
            st.write("🎥 **Tool:** [Video Model] Rendering output...")
            time.sleep(0.5)
            
        st.divider()
        st.balloons()
        st.success("✨ Video Generated Successfully!")
        
        # ===========================================================
        # 👇👇👇 核心修改在这里 👇👇👇
        # 因为你已经把视频传到了仓库里，直接写文件名即可！
        # Streamlit 会自动在当前目录下找这个文件。
        # ===========================================================
        video_filename = "demo.mp4"
        
        # 检查文件是否存在 (防止你文件名写错)
        if os.path.exists(video_filename):
            st.video(video_filename)
            
            with st.expander("View Technical Metadata"):
                st.json({"file": video_filename, "status": "Local Render", "fps": 30})
        else:
            st.error(f"❌ 找不到视频文件: {video_filename}")
            st.warning("请确认你已经把视频上传到了 GitHub，并且名字完全一样（叫 demo.mp4）。")

    else:
        st.info("👈 Click 'Generate Video' to start.")
        # 占位图
        st.markdown(
            """
            <div style="background-color:#f0f2f6; height:300px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:grey;">
                <h3>Waiting for instructions...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
