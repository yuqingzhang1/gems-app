import streamlit as st
import google.generativeai as genai
import json
import os

# --- Page Configuration ---
st.set_page_config(page_title="GEMS Studio", layout="wide")

# --- Sidebar: Settings ---
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Allow API Key input via UI or Secrets
    api_key = st.text_input("Enter Google AI Studio API Key", type="password")
    
    # Check if Key exists in Secrets (for deployed version)
    if not api_key and "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

# --- Main Interface ---
st.title("🎬 [CN x PI] GEMS Studio")
st.caption("Agentic Video Planning Assistant powered by Gemini")

# Stop if no API Key is found
if not api_key:
    st.warning("⚠️ Please enter your API Key in the sidebar to proceed.")
    st.stop()

# --- Configure Gemini ---
genai.configure(api_key=api_key)

# System Prompt (The Brain)
# We instruct Gemini to output strict JSON for the UI to render correctly.
system_instruction = """
You are a professional Video Director Agent.
Your goal is to turn a user's topic into a structured storyboard.

Instructions:
1. Create a storyboard with exactly 3 scenes based on the user's input.
2. Return ONLY a valid JSON list. Do not include Markdown formatting (like ```json).
3. The JSON structure must be: 
   [{"scene": 1, "visual_description": "Detailed prompt for image generation", "voiceover": "Script for the narrator"}]
"""

# Initialize Model
# Since you are an insider, you can try changing this to "models/gemini-1.5-pro-002" or "models/gemini-experimental"
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=system_instruction
)

# --- Chat Session Logic ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Area
if prompt := st.chat_input("I want to create a video about..."):
    # 1. Display User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Call Gemini
    with st.chat_message("assistant"):
        with st.spinner("The Director is brainstorming scenes..."):
            try:
                # Send request to Gemini
                response = model.generate_content(prompt)
                result_text = response.text
                
                # Try to parse JSON to render the "Card UI"
                try:
                    # Clean potential markdown formatting
                    clean_json = result_text.replace("```json", "").replace("```", "")
                    script_data = json.loads(clean_json)
                    
                    st.success("✅ Storyboard Generated Successfully")
                    
                    # Create Columns for the 3 scenes
                    cols = st.columns(len(script_data))
                    for idx, scene in enumerate(script_data):
                        with cols[idx]:
                            st.info(f"Scene {scene.get('scene')}")
                            st.write(f"🖼️ **Visual:** {scene.get('visual_description')}")
                            st.caption(f"🔊 **Audio:** {scene.get('voiceover')}")
                            # Placeholder for where the actual AI Image would go
                            st.image("https://via.placeholder.com/300x200?text=Generating+Asset...", caption="Asset Placeholder")
                    
                    # Save context to history
                    st.session_state.messages.append({"role": "assistant", "content": "Storyboard cards generated above 👆"})
                    
                except json.JSONDecodeError:
                    # Fallback: If Gemini didn't output JSON, just show the text
                    st.markdown(result_text)
                    st.session_state.messages.append({"role": "assistant", "content": result_text})
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")





Evaluate

Compare
