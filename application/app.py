import streamlit as st
import tempfile
import os
from pathlib import Path
from src.parser import parse_cv
from src.rag_pipeline import LLMGenerator
from config.settings import (
    UPLOADS_DIR, 
    TEMP_DIR, 
    FILE_CONFIG, 
    ATS_SCORING,
    STREAMLIT_CONFIG
)

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Smart CV Analyzer Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure Streamlit settings
for key, value in STREAMLIT_CONFIG.items():
    if hasattr(st, key):
        setattr(st, key, value)

# --- CUSTOM CSS ---
def load_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section-card {
        background: 1f77b4;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        min-height: 200px;
    }
    .education-card { border-left-color: #1f77b4; }
    .experience-card { border-left-color: #ff7f0e; }
    .projects-card { border-left-color: #2ca02c; }
    .skills-card { border-left-color: #d62728; }

    </style>
    """, unsafe_allow_html=True)

load_css()

# --- MAIN UI ---
st.markdown('<h1 class="main-header">📊 Professional CV Analyzer</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <p style="font-size: 1.1rem; color: #555;">
    AI-powered CV analysis for job seekers. Get instant feedback on ATS compatibility, content quality, and improvement recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    ### 📈 What You'll Get
    
    • **ATS Compatibility Score** - How well your CV passes automated systems
    • **Professional Summary** - AI analysis of your CV's strengths and weaknesses  
    • **Actionable Recommendations** - Specific tips for improvement
    • **Section Analysis** - Detailed breakdown of each CV section
    • **Industry Insights** - Best practices for your field
    
    *Supports PDF and DOCX formats*
    """)

with col2:
    uploaded_file = st.file_uploader(
        "**Upload CV for Analysis**",
        type=["pdf", "docx"],
        help="Upload any CV in PDF or DOCX format for professional analysis"
    )

    analyze_button = st.button("**Analyze CV** 🚀", type="primary", use_container_width=True)

# --- PROCESSING LOGIC ---
if analyze_button and uploaded_file is not None:
    with st.spinner('🔍 Analyzing CV with AI... This may take 20-30 seconds.'):
        try:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                temp_file_path = tmp_file.name

            # Parse CV
            cv_text = parse_cv(temp_file_path)

            if not cv_text or not cv_text.strip():
                st.error("❌ Could not extract text from the CV. The file might be corrupted or contain images only.")
            else:
                # Generate analysis
                llm_generator = LLMGenerator()
                analysis_result = llm_generator.generate_cv_analysis(cv_text)

                # --- DISPLAY RESULTS ---
                st.success("✅ CV Analysis Complete!")
                
                # Score and Metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"""
                    <div class="score-card">
                        <h3>ATS Score</h3>
                        <h1 style="font-size: 3rem; margin: 0;">{analysis_result["score"]}/100</h1>
                        <p>{"🎉 Excellent" if analysis_result["score"] >= 80 else "✅ Good" if analysis_result["score"] >= 60 else "⚠️ Needs Work"}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    score_quality = "High" if analysis_result["score"] >= 80 else "Medium" if analysis_result["score"] >= 60 else "Low"
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); color: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <h3>📋 Quality Assessment</h3>
                        <p style="font-size: 1.2rem; margin: 0.5rem 0;">{score_quality}</p>
                        <p>Overall CV Quality</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); color: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <h3>👁️ Human Review</h3>
                        <p>Recruiter Appeal</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Executive Summary
                st.markdown("---")
                st.subheader("📋 Executive Summary")
                st.info(analysis_result["summary"])

                # Detailed Analysis Tabs - REMOVED RAW ANALYSIS
                tab1, tab2 = st.tabs(["🎯 Improvement Recommendations", "📑 CV Sections"])

                with tab1:
                    st.subheader("💡 Recommendations for Improvement")
                    if analysis_result["recommendations"]:
                        recommendations = analysis_result["recommendations"].split('\n')
                        for rec in recommendations:
                            if rec.strip():
                                st.markdown(f"""
                                <div class="recommendation-item">
                                    <span style="font-weight: 500;">{rec}</span>
                                </div>
                                """, unsafe_allow_html=True)
                    else:
                        st.info("No specific recommendations generated. The CV appears to be well-structured.")

                with tab2:
                    st.subheader("📑 CV Section Analysis")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Education Section
                        st.markdown(f"""
                        <div class="section-card education-card">
                            <div class="section-title">🎓 Education</div>
                            <div class="section-content">{analysis_result['sections']['education']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Projects Section
                        st.markdown(f"""
                        <div class="section-card projects-card">
                            <div class="section-title">🚀 Projects & Achievements</div>
                            <div class="section-content">{analysis_result['sections']['projects']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        # Experience Section
                        st.markdown(f"""
                        <div class="section-card experience-card">
                            <div class="section-title">💼 Work Experience</div>
                            <div class="section-content">{analysis_result['sections']['experience']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Skills Section
                        st.markdown(f"""
                        <div class="section-card skills-card">
                            <div class="section-title">🛠️ Skills & Competencies</div>
                            <div class="section-content">{analysis_result['sections']['skills']}</div>
                        </div>
                        """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Analysis failed: {str(e)}")
            st.info("💡 Troubleshooting: Ensure Ollama is running and the model is installed.")
        
        finally:
            # Cleanup
            if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
                os.remove(temp_file_path)

elif analyze_button:
    st.warning("⚠️ Please upload a CV file to begin analysis.")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 💡 CV Best Practices")
    st.markdown("""
    **Content Tips:**
    • Use measurable achievements
    • Include industry keywords
    • Focus on results, not duties
    • Keep it concise (1-2 pages)
    
    **Formatting Tips:**
    • Clean, professional layout
    • Consistent formatting
    • Readable fonts (10-12pt)
    • Proper section headings
    
    **ATS Optimization:**
    • Standard section names
    • No tables or graphics
    • Common file formats
    • Keyword optimization
    """)
    
    st.markdown("## 🔧 System Requirements")
    st.markdown("""
    • Ollama running locally
    • CV analysis model installed
    • PDF or DOCX files
    • Stable connection
    """)
