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

# --- 2. 样式 ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #1E88E5; color: white;}
    .json-box { font-family: monospace; font-size: 12px; background: #f0f0f0; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 3. 标题 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Single MCP Server Architecture Implementation")
st.caption("Orchestrator: **Gemini 2.0** | Protocol: **MCP** | Tools: **Vertex AI**")
st.divider()

col1, col2 = st.columns([1, 2])

# === 左侧：配置区 (Updated) ===
with col1:
    st.subheader("1. System Configuration")
    
    # [NEW] 场景选择 (响应录音里的 Use Case)
    scenario = st.selectbox(
        "🎯 Select Scenario (System Prompt)", 
        ["Creative Factory (General)", "Hotel Story (Enterprise Demo)", "E-commerce Ads"]
    )
    
    # 根据场景自动变 Prompt
    default_prompt = ""
    if "Hotel" in scenario:
        default_prompt = "Generate a luxury hotel promotion video featuring a pool, fine dining, and ocean view."
    else:
        default_prompt = "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution."
        
    user_prompt = st.text_area("User Instruction", default_prompt, height=100)

    st.markdown("---")
    st.file_uploader("Upload Context (Optional)", type=['png', 'jpg'])
    
    with st.expander("🔧 Advanced Settings (MCP)", expanded=False):
        st.selectbox("LLM Backend", ["Gemini 2.0 Flash", "Gemini 1.5 Pro"])
        st.checkbox("Force Vertex AI Endpoint", value=True, disabled=True)

    run_btn = st.button("🚀 Submit Task", type="primary")

# === 右侧：执行区 (Updated) ===
with col2:
    st.subheader("2. Orchestrator Execution Log")
    
    if run_btn:
        # [NEW] 模拟任务提交回执
        task_id = "TASK-" + str(int(time.time()))
        st.info(f"✅ Request Received. Task ID: **{task_id}**")
        
        # 模拟 MCP 交互过程
        with st.status("⚡ Orchestrating via MCP...", expanded=True) as status:
            
            # Step 1: 加载 System Prompt
            st.write("🧠 **Orchestrator:** Loading System Prompt for `" + scenario + "`...")
            time.sleep(0.8)
            
            # Step 2: 意图识别 (显示 JSON)
            st.write("🔍 **Intent Analysis:**")
            st.markdown(f"""
            ```json
            {{ "intent": "video_generation", "style": "cinematic", "steps": ["storyboard", "image", "video"] }}
            ```
            """)
            time.sleep(1.0)
            
            # Step 3: 工具调用 (MCP Protocol 风格)
            st.write("🛠️ **MCP Call:** `tool:vertex_imagen_3`")
            st.markdown(f"""
            ```json
            {{ "prompt": "{user_prompt[:30]}...", "aspect_ratio": "16:9" }}
            ```
            """)
            # 显示假图片
            c1, c2 = st.columns(2)
            with c1: st.image("https://picsum.photos/200/110?random=1", caption="Asset_A generated")
            with c2: st.image("https://picsum.photos/200/110?random=2", caption="Asset_B generated")
            time.sleep(1.5)
            
            # Step 4: 视频生成 (模拟高延迟)
            st.warning("🎥 **MCP Call:** `tool:video_model_v2` (Async Processing...)")
            bar = st.progress(0, text="Waiting for GPU cluster...")
            for i in range(100):
                time.sleep(0.015) 
                bar.progress(i+1)
            
            status.update(label="✅ Workflow Completed!", state="complete", expanded=False)
        
        # --- 结果展示 ---
        st.divider()
        st.success("✨ Task Completed Successfully")
        
        # 播放本地视频 (请确保你上传了 demo.mp4)
        video_filename = "demo.mp4" 
        if os.path.exists(video_filename):
            st.video(video_filename)
        else:
            # 如果没上传，用网络视频兜底
            st.video("https://assets.mixkit.co/videos/preview/mixkit-neon-lights-in-a-rainy-city-at-night-12305-large.mp4")
            
        with st.expander("View Trace Logs"):
            st.json({"task_id": task_id, "latency": "4.2s (Simulated)", "cost": "$0.12"})

    else:
        st.info("👈 Configure scenario and submit task to start.")
        st.markdown(
            """
            <div style="background-color:#f9f9f9; height:250px; border-radius:10px; display:flex; align-items:center; justify-content:center; border: 2px dashed #ddd; color:#aaa;">
                <h3>Waiting for Input...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
