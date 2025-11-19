import streamlit as st
import time
import random

# --- 1. 页面基础设置 ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- 2. CSS 样式美化 ---
st.markdown("""
<style>
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        background-color: #FF4B4B; 
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 顶部标题 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Next-Gen Video Generation Architecture")
st.caption("Powered by **Vertex AI** | Orchestrated by **Gemini 2.0/3.0**")
st.divider()

# --- 4. 页面布局 ---
col1, col2 = st.columns([1, 2])

# === 左侧：用户控制区 ===
with col1:
    st.subheader("1. Input & Configuration")
    
    user_prompt = st.text_area(
        "Creative Prompt", 
        "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution, slow motion.", 
        height=120
    )

    st.markdown("---")
    st.markdown("**📄 Reference (Optional)**")
    uploaded_file = st.file_uploader("Upload Storyboard/Image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        st.success(f"✅ Loaded: {uploaded_file.name}")
        # 注意：这里我也改成了最简单的写法，防止报错
        st.image(uploaded_file, caption="Reference Image")

    st.markdown("---")
    with st.expander("⚙️ Model Settings", expanded=True):
        model = st.selectbox(
            "Select LLM Backbone", 
            ["Gemini 2.0 Flash (Experimental)", "Gemini 3.0 (Future Preview)", "Gemini 1.5 Pro"]
        )
        st.slider("Duration (seconds)", 5, 60, 15)

    run_btn = st.button("🚀 Generate Video", type="primary")

# === 右侧：Agent 执行与视频展示 ===
with col2:
    st.subheader("2. Orchestrator & Result")
    
    if run_btn:
        with st.status(f"⚡ {model} Orchestrator Running...", expanded=True) as status:
            
            st.write("🧠 **Agent:** Analyzing prompt & constraints...")
            time.sleep(1.0)
            
            if uploaded_file:
                st.info("📂 **Context:** Injecting user reference into latent space...")
                time.sleep(1.0)
            else:
                st.warning("⚠️ **Context:** Generating storyboard from scratch...")
                st.text("Scene 1: Neon Street (Wide)\nScene 2: Coffee Shop (Interior)")
                time.sleep(0.8)
            
            st.info(f"🎨 **Tool:** [Image Gen] Creating consistency keyframes...")
            c1, c2, c3 = st.columns(3)
            with c1: st.image("https://picsum.photos/200/120?random=1", caption="Frame 1")
            with c2: st.image("https://picsum.photos/200/120?random=2", caption="Frame 2")
            with c3: st.image("https://picsum.photos/200/120?random=3", caption="Frame 3")
            
            time.sleep(1.5)
            st.warning("🎥 **Tool:** [Video Model v3] Rendering high-fidelity output...")
            
            bar = st.progress(0, text="Rendering...")
            for i in range(100):
                time.sleep(0.01) 
                bar.progress(i+1)
            
            status.update(label="✅ Generation Complete!", state="complete", expanded=False)
        
        # --- 视频播放区域 ---
        st.divider()
        st.subheader("✨ Final Generated Video")
        st.balloons()
        
        video_url = "https://videos.pexels.com/video-files/3121459/3121459-hd_1920_1080_25fps.mp4"
        
        # 👇👇👇 终极修复 👇👇👇
        # 我们删除了 format, use_column_width, autoplay 等所有参数
        # 只保留最核心的 URL，这是最不容易出错的写法
        st.video(video_url)
        
        st.success(f"Video generated in 6.2s using {model}")
        with st.expander("View Technical Metadata"):
            st.json({
                "resolution": "1920x1080",
                "fps": 25,
                "seed": 123456,
                "cost": "$0.00"
            })

    else:
        st.info("👈 Upload a storyboard (optional) and click Generate to start.")
        st.markdown(
            """
            <div style="
                background-color:#f0f2f6; 
                border-radius:10px; 
                height: 300px; 
                display:flex; 
                align-items:center; 
                justify-content:center; 
                border: 2px dashed #ccc;
                color: grey;">
                <h3>Waiting for Instructions...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
