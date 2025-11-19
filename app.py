import streamlit as st
import time
import random

# --- 页面配置 ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- CSS 美化 ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #FF4B4B; color: white;}
    .reportview-container { background: #ffffff; }
</style>
""", unsafe_allow_html=True)

# --- 标题 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Next-Gen Video Generation Architecture")
st.caption("Powered by **Vertex AI** | Orchestrated by **Gemini 2.0/3.0**")
st.divider()

# --- 布局 ---
col1, col2 = st.columns([1, 2])

# === 左侧：用户输入 & 故事板上传 ===
with col1:
    st.subheader("1. Input & Context")
    
    # 提示词
    user_prompt = st.text_area(
        "Creative Prompt", 
        "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution.", 
        height=100
    )

    # 可选：上传故事板
    st.markdown("---")
    st.markdown("**📄 Reference Material (Optional)**")
    uploaded_file = st.file_uploader("Upload Storyboard/Image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        st.success(f"✅ Reference detected: {uploaded_file.name}")
        st.image(uploaded_file, caption="User Reference", width=200)

    # 模型配置
    st.markdown("---")
    with st.expander("⚙️ Model Configuration", expanded=True):
        model = st.selectbox(
            "Select LLM Backbone", 
            ["Gemini 2.0 Flash (Experimental)", "Gemini 3.0 (Future Preview)", "Gemini 1.5 Pro"]
        )

    run_btn = st.button("🚀 Generate Video", type="primary")

# === 右侧：Agent 流程 & 真实视频 ===
with col2:
    st.subheader("2. Orchestrator & Output")
    
    if run_btn:
        # 1. 模拟 Agent 思考过程
        with st.status(f"⚡ {model} Orchestrator Running...", expanded=True) as status:
            
            st.write("🧠 **Agent:** Analyzing context...")
            time.sleep(0.8)
            
            # 分支逻辑：是否有上传图片
            if uploaded_file is not None:
                st.info("📂 **Context:** Integrating user storyboard into latent space...")
                st.image(uploaded_file, width=150, caption="Reference Locked")
                time.sleep(1.2)
            else:
                st.warning("⚠️ **Context:** Generating storyboard from scratch...")
                time.sleep(0.8)
                st.text("Scene 1: Establishing shot\nScene 2: Product close-up")
            
            st.info(f"🎨 **Tool:** [Image Gen] Generating Keyframes...")
            # 模拟关键帧展示
            c1, c2, c3 = st.columns(3)
            with c1: st.image("https://picsum.photos/200/120?random=10", caption="Frame 1")
            with c2: st.image("https://picsum.photos/200/120?random=11", caption="Frame 2")
            with c3: st.image("https://picsum.photos/200/120?random=12", caption="Frame 3")
            
            time.sleep(1.5)
            st.warning("🎥 **Tool:** [Video Model v3] Rendering final output...")
            
            # 进度条模拟
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i+1)
            
            status.update(label="✅ Generation Complete!", state="complete", expanded=False)
        
        # 2. 展示真实视频
        st.divider()
        st.subheader("✨ Final Result")
        st.balloons() # 撒花特效
        
        # ==========================================
        # 👇👇👇 在这里替换你的视频链接 👇👇👇
        # 如果你已经在 GitHub 上传了视频，右键该视频点击 "Copy Link" (如果是 Raw 链接最好)
        # ==========================================
        
        # 这是一个看起来很像 AI 生成的赛博朋克视频 (默认备选)
        default_video = "https://videos.pexels.com/video-files/3121459/3121459-hd_1920_1080_25fps.mp4"
        
        # 如果你要用自己的 GitHub 视频，格式如下：
        # my_video = "https://github.com/你的用户名/仓库名/raw/main/文件名.mp4"
        
        st.video(default_video, format="video/mp4", autoplay=True)
        
        st.success("Video generated successfully based on your prompt.")

    else:
        st.info("👈 Click Generate to start the demo.")
        st.markdown(
            """
            <div style="background-color:#f0f2f6; height: 300px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:grey;">
                <h3>Waiting for Input...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
