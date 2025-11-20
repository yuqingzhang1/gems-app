import streamlit as st
import time
import os
import json

# --- 1. 页面配置 ---
st.set_page_config(
    page_title="GEMS Architecture Demo", 
    layout="wide", 
    page_icon="💎"
)

# --- 2. 样式美化 ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #1E88E5; color: white;}
    .json-box { font-family: monospace; font-size: 12px; background: #f0f0f0; padding: 10px; border-radius: 5px; }
    /* 评估通过/失败的样式 */
    .pass-badge { background-color: #e6fffa; color: #047857; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }
    .warn-badge { background-color: #fffbeb; color: #b45309; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }
</style>
""", unsafe_allow_html=True)

# --- 3. 标题区 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Single MCP Server: Full-Cycle Creative Factory")
st.caption("Orchestrator: **Gemini** | Insights: **YouTrendsLM** | Video: **Veo** | Audio: **Lyria/TTS** | Editing: **Vids**")
st.divider()

col1, col2 = st.columns([1, 2])

# === 左侧：高级输入配置 ===
with col1:
    st.subheader("1. Creative Input & Strategy")
    
    # A. 场景与策略
    scenario = st.selectbox(
        "🎯 Campaign Scenario", 
        ["Hotel Story (Luxury)", "E-commerce (Fashion)", "YouTrends Best Practice (Viral)"]
    )
    
    # B. 策略工具开关 (新功能)
    st.markdown("**🧠 Strategy Engines**")
    use_youtrends = st.checkbox("Enable YouTrendsLM Insight / ABCD Framework", value=True)
    use_style_picker = st.selectbox("Style Picker", ["Manual Gemini Prompt", "Match Brand Guidelines"])
    
    st.markdown("---")
    
    # C. 创作输入
    user_prompt = st.text_area("Creative Prompt / Script", "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution.", height=100)
    st.file_uploader("Upload Creative Asset (Image/Video)", type=['png', 'jpg', 'mp4'])
    
    st.markdown("---")
    
    # D. 音频与剪辑 (新功能)
    with st.expander("🎵 Audio & Editing Settings", expanded=False):
        st.checkbox("Generate VO (Vertex TTS)", value=True)
        st.checkbox("Generate Music/SFX (Lyria)", value=True)
        st.selectbox("Video Editing Mode", ["Vids AI Auto-Edit", "Manual Shot Length"])

    run_btn = st.button("🚀 Start Creative Factory", type="primary")

# === 右侧：执行与评估 ===
with col2:
    st.subheader("2. Orchestration & Agents Trace")
    
    if run_btn:
        task_id = "JOB-" + str(int(time.time()))
        st.info(f"✅ Job Submitted to Vertex AI. ID: **{task_id}**")
        
        # 模拟 MCP 交互过程
        with st.status(f"⚡ Orchestrating Workflow...", expanded=True) as status:
            
            # Phase 1: Insight & Strategy (YouTrendsLM)
            if use_youtrends:
                st.write("🧠 **Agent:** Calling `tool:youtrends_lm` for ABCD analysis...")
                time.sleep(0.8)
                st.markdown("> *Insight: Enhance color saturation for mobile retention. Add text overlay in first 2s.*")
            
            # Phase 2: Visual Creation (Imagen + Veo)
            st.write("🎨 **Agent:** Generating Assets (NanoBanana/GemPix)...")
            time.sleep(0.5)
            st.write("🎥 **Agent:** Rendering Video (Veo3 Fast in Flow)...")
            # 模拟 Veo 进度
            bar = st.progress(0, text="Veo Rendering...")
            for i in range(50): 
                time.sleep(0.01)
                bar.progress(i*2)
            
            # Phase 3: Audio & Editing (新环节)
            st.write("🎵 **Agent:** Synthesizing Audio (`tool:vertex_tts` + `tool:lyria`)...")
            time.sleep(0.5)
            st.write("✂️ **Agent:** Assembling Timeline (`tool:google_vids`)...")
            time.sleep(0.5)
            
            # Phase 4: Evaluation Agents (新环节 - 核心亮点)
            st.warning("🕵️ **Eval Swarm:** Running Objective & Subjective Agents...")
            st.markdown("`> Running: Japanese Spoken Checker...`")
            time.sleep(0.3)
            st.markdown("`> Running: Human Accuracy (Hand/Face) Checker...`")
            time.sleep(0.3)
            st.markdown("`> Running: ABCD Best Practice Evaluator...`")
            
            status.update(label="✅ All Agents Completed!", state="complete", expanded=False)
        
        # --- 结果展示区 (使用 Tabs 分离视频和评估报告) ---
        st.divider()
        st.balloons()
        
        tab_video, tab_eval, tab_debug = st.tabs(["🎬 Final Output", "📊 Eval Report", "🛠️ Trace Logs"])
        
        with tab_video:
            st.success("✨ Final Creative Asset Ready")
            # 视频播放逻辑
            video_filename = "demo.mp4" 
            image_filename = "generated_image.jpg"
            
            if os.path.exists(video_filename):
                st.video(video_filename)
            else:
                st.video("https://assets.mixkit.co/videos/preview/mixkit-neon-lights-in-a-rainy-city-at-night-12305-large.mp4")
                
        with tab_eval:
            st.subheader("Automated Evaluation Report")
            st.info("Generated by Gemini 1.5 Pro Vision & Audio Analysis")
            
            # 模拟图片中的 Evaluation Agents 结果
            col_e1, col_e2 = st.columns(2)
            
            with col_e1:
                st.markdown("### Objective Eval Agents")
                st.markdown("""
                | Agent | Status | Note |
                | :--- | :--- | :--- |
                | **Spoken Language Checker** | <span class="pass-badge">PASS</span> | Pronunciation accuracy 99.2% |
                | **Written Word Checker** | <span class="pass-badge">PASS</span> | No Kanji errors detected |
                | **Human Accuracy** | <span class="warn-badge">WARN</span> | Minor finger anomaly in frame 142 |
                | **Animation Quality** | <span class="pass-badge">PASS</span> | Lip-sync latency < 20ms |
                """, unsafe_allow_html=True)
                
            with col_e2:
                st.markdown("### Subjective Eval Agents")
                st.markdown("""
                | Agent | Status | Insight |
                | :--- | :--- | :--- |
                | **Shot Length Agent** | <span class="pass-badge">PASS</span> | Pacing matches "Upbeat" style |
                | **Copywriter Agent** | <span class="warn-badge">SUGGEST</span> | "Consider shortening opening hook" |
                | **ABCD Framework** | <span class="pass-badge">PASS</span> | Branding present in first 5s |
                """, unsafe_allow_html=True)

        with tab_debug:
            st.json({
                "task_id": task_id,
                "modules": ["YouTrendsLM", "Imagen3", "Veo", "Lyria", "Vids"],
                "eval_score": "A-",
                "cost": "$0.42"
            })

    else:
        st.info("👈 Configure Strategy & Creative Input to start.")
        st.markdown(
            """
            <div style="background-color:#f9f9f9; height:250px; border-radius:10px; display:flex; align-items:center; justify-content:center; border: 2px dashed #ddd; color:#aaa;">
                <h3>Waiting for Input...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
