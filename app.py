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
</style>
""", unsafe_allow_html=True)

# --- 3. 标题区 ---
st.title("💎 CN Open Source GEMS")
st.markdown("### Single MCP Server Architecture Implementation")
st.caption("Orchestrator: **Gemini** | Protocol: **MCP** | Video Backbone: **Veo**")
st.divider()

col1, col2 = st.columns([1, 2])

# === 左侧：配置区 ===
with col1:
    st.subheader("1. System Configuration")
    
    # A. 场景选择
    scenario = st.selectbox(
        "🎯 Select Scenario (System Prompt)", 
        ["Creative Factory (General)", "Hotel Story (Enterprise Demo)", "E-commerce Ads"]
    )
    
    # B. 模型选择 (包含 Gemini 3.0)
    st.markdown("---")
    model = st.selectbox(
        "🧠 Select LLM Backend", 
        [
            "Gemini 3.0 (Future Preview)", 
            "Gemini 2.0 Flash (Experimental)", 
            "Gemini 1.5 Pro (Production)"
        ]
    )
    
    # 根据场景自动变 Prompt
    default_prompt = ""
    if "Hotel" in scenario:
        default_prompt = "Generate a luxury hotel promotion video featuring a pool, fine dining, and ocean view."
    elif "E-commerce" in scenario:
        default_prompt = "Create a 15s ad for a new running shoe, dynamic shots, upbeat music."
    else:
        default_prompt = "Cinematic shot of a futuristic coffee shop in Tokyo, neon lights, rain reflection, 4k resolution."
        
    st.markdown("---")
    user_prompt = st.text_area("User Instruction", default_prompt, height=100)
    
    st.file_uploader("Upload Context (Optional)", type=['png', 'jpg'])

    run_btn = st.button("🚀 Submit Task", type="primary")

# === 右侧：执行区 ===
with col2:
    st.subheader("2. Orchestrator Execution Log")
    
    if run_btn:
        task_id = "TASK-" + str(int(time.time()))
        st.info(f"✅ Request Received via Vertex AI. Task ID: **{task_id}**")
        
        # 模拟 MCP 交互过程
        with st.status(f"⚡ Orchestrating via MCP ({model})...", expanded=True) as status:
            
            # Step 1: System Prompt
            st.write(f"🧠 **Orchestrator:** Loading System Prompt for `{scenario}`...")
            time.sleep(0.8)
            
            # Step 2: 意图识别
            st.write("🔍 **Intent Analysis:**")
            st.markdown(f"""
            ```json
            {{ "model": "{model}", "intent": "video_generation", "target_model": "veo-latest" }}
            ```
            """)
            time.sleep(1.0)
            
            # Step 3: Imagen 调用 (已修改：只显示一张你上传的图)
            st.write("🛠️ **MCP Call:** `tool:vertex_imagen_3`")
            st.markdown(f"""
            ```json
            {{ "prompt": "{user_prompt[:30]}...", "aspect_ratio": "16:9" }}
            ```
            """)
            
            # --- 核心修改：显示你上传的 generated_image.jpg ---
            image_filename = "generated_image.jpg"
            
            if os.path.exists(image_filename):
                # 显示本地上传的图片，宽度设置适中
                st.image(image_filename, caption="✅ Generated Asset (Imagen 3)", width=500)
            else:
                # 如果你还没上传，显示一个占位图并提示
                st.warning("⚠️ 请上传名为 generated_image.jpg 的图片到 GitHub")
                st.image("https://picsum.photos/500/280", caption="Placeholder Asset")
            
            time.sleep(1.5)
            
            # Step 4: Veo 调用
            st.warning("🎥 **MCP Call:** `tool:vertex_veo` (High-Fidelity Video Gen)")
            
            # 展示 Veo 的参数
            st.markdown("""
            ```json
            {
              "model_id": "veo-001",
              "mode": "image_to_video",
              "resolution": "1080p",
              "frames": 24
            }
            ```
            """)
            
            bar = st.progress(0, text="Veo is rendering latent space...")
            for i in range(100):
                time.sleep(0.015) 
                bar.progress(i+1)
            
            status.update(label="✅ Workflow Completed!", state="complete", expanded=False)
        
        # --- 结果展示 ---
        st.divider()
        st.success("✨ Task Completed Successfully")
        
        video_filename = "demo.mp4" 
        if os.path.exists(video_filename):
            st.video(video_filename)
        else:
            st.video("https://assets.mixkit.co/videos/preview/mixkit-neon-lights-in-a-rainy-city-at-night-12305-large.mp4")
            
        with st.expander("View Trace Logs"):
            st.json({
                "task_id": task_id, 
                "backend": model,
                "video_model": "Google Veo (Preview)",
                "latency": "4.2s (Simulated)", 
                "cost": "$0.18"
            })

    else:
        st.info("👈 Select a Scenario & Model, then submit.")
        st.markdown(
            """
            <div style="background-color:#f9f9f9; height:250px; border-radius:10px; display:flex; align-items:center; justify-content:center; border: 2px dashed #ddd; color:#aaa;">
                <h3>Waiting for Input...</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
