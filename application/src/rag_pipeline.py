import re
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from . import prompt_templates

class LLMGenerator:
    """
    Handles the generation of CV analysis using a local Ollama model.
    """
    def __init__(self):
        """
        Initializes the ChatOllama model.
        """
        self.llm = ChatOllama(
            model="deepseek-r1:1.5b",
            temperature=0.3,
            top_k=40,
            top_p=0.9,
            num_ctx=2048
        )
        print("LLMGenerator initialized with model 'deepseek-r1:1.5b'.")

    def _create_analysis_chain(self, prompt_template: str):
        """
        Creates a LangChain chain for a given prompt template.
        """
        prompt = ChatPromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm | StrOutputParser()
        return chain

    def generate_cv_analysis(self, cv_text: str) -> dict:
        """
        Generates a complete analysis of the given CV text with robust parsing.
        """
        print("Generating CV analysis...")
        
        # Truncate CV text if too long to avoid context issues
        if len(cv_text) > 2500:
            cv_text = cv_text[:2500] + "... [truncated]"
        
        scoring_chain = self._create_analysis_chain(prompt_templates.ATS_SCORE_PROMPT)
        recommendations_chain = self._create_analysis_chain(prompt_templates.IMPROVEMENT_RECOMMENDATIONS_PROMPT)

        score_and_summary_output = scoring_chain.invoke({"cv_text": cv_text})
        recommendations_output = recommendations_chain.invoke({"cv_text": cv_text})

        # Parse outputs
        score, summary = self._parse_score_and_summary(score_and_summary_output)
        recommendations = self._clean_recommendations_output(recommendations_output)
        
        # Extract key sections from CV - SIMPLIFIED AND RELIABLE
        sections = self._extract_cv_sections_simple(cv_text)

        print("CV analysis completed successfully.")
        
        analysis = {
            "score": score,
            "summary": summary,
            "recommendations": recommendations,
            "sections": sections
        }
        return analysis

    def _parse_score_and_summary(self, output: str) -> tuple:
        """
        Parse score and summary from the model output.
        """
        score = 0
        summary = "Could not parse summary from model output."
        
        # Remove thinking blocks
        clean_output = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL)
        clean_output = re.sub(r'</?think>', '', clean_output)
        
        # Extract score
        score_patterns = [
            r'SCORE:\s*(\d+)',
            r'Score:\s*(\d+)',
            r'ATS Score:\s*(\d+)',
            r'(\d+)\s*\/\s*100'
        ]
        
        for pattern in score_patterns:
            match = re.search(pattern, clean_output, re.IGNORECASE)
            if match:
                try:
                    score = int(match.group(1))
                    break
                except ValueError:
                    continue
        
        # Extract summary
        summary_patterns = [
            r'SUMMARY:\s*(.*?)(?=CRITERIA:|KEYWORDS:|SCORE:|$)',
            r'Summary:\s*(.*?)(?=CRITERIA:|KEYWORDS:|SCORE:|$)',
            r'SUMMARY:\s*(.*)'
        ]
        
        for pattern in summary_patterns:
            match = re.search(pattern, clean_output, re.IGNORECASE | re.DOTALL)
            if match:
                summary = match.group(1).strip()
                # Clean up summary
                summary = re.sub(r'\*+', '', summary)
                summary = re.sub(r'\s+', ' ', summary).strip()
                break
        
        return score, summary

    def _clean_recommendations_output(self, output: str) -> str:
        """
        Clean and format recommendations output.
        Ensures the model dynamically generates 5 improvement points based on CV content.
        """
        # Remove hidden "thinking" or formatting artifacts
        clean_output = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL)
        clean_output = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_output)
        clean_output = re.sub(r'\*(.*?)\*', r'\1', clean_output)
        clean_output = clean_output.strip()

        # Extract bullet/numbered recommendations
        lines = clean_output.split('\n')
        recommendations = []
        for line in lines:
            line = line.strip()
            if re.match(r'^(\d+\.|-|\*)', line):
                clean_line = re.sub(r'^(\d+\.|-|\*)\s*', '', line)
                clean_line = clean_line.strip()
                if clean_line and len(clean_line) > 3:
                    recommendations.append(f"{len(recommendations) + 1}. {clean_line}")

        # If the model didn’t produce numbered lines, try to split by sentences
        if not recommendations and len(clean_output) > 20:
            sentences = re.split(r'[.!?]', clean_output)
            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) > 8:
                    recommendations.append(f"{len(recommendations) + 1}. {sentence}")

        # If model totally failed to generate output
        if not recommendations:
            return "Model could not generate improvement recommendations for this CV."

        # Limit to top 5
        return '\n'.join(recommendations[:5])


    def _extract_cv_sections_simple(self, cv_text: str) -> dict:
        """
        SIMPLIFIED and RELIABLE section extraction that actually works.
        """
        # Initialize sections with empty content
        sections = {
            "education": "No education information found in the CV",
            "experience": "No work experience information found in the CV", 
            "projects": "No projects information found in the CV",
            "skills": "No skills information found in the CV"
        }
        
        # Split into lines
        lines = [line.strip() for line in cv_text.split('\n') if line.strip()]
        
        # SIMPLE keyword-based content extraction
        education_content = []
        experience_content = []
        projects_content = []
        skills_content = []
        
        for line in lines:
            line_lower = line.lower()
            
            # Education keywords
            if any(keyword in line_lower for keyword in ['university', 'college', 'degree', 'bachelor', 'master', 'phd', 'gpa', 'education', 'faculty']):
                education_content.append(line)
            
            # Experience keywords  
            elif any(keyword in line_lower for keyword in ['experience', 'work', 'employment', 'intern', 'engineer', 'developer', 'analyst', 'manager', 'position', 'role']):
                experience_content.append(line)
            
            # Projects keywords
            elif any(keyword in line_lower for keyword in ['project', 'developed', 'created', 'built', 'implemented', 'system', 'application', 'portfolio']):
                projects_content.append(line)
            
            # Skills keywords
            elif any(keyword in line_lower for keyword in ['skill', 'python', 'java', 'sql', 'machine learning', 'deep learning', 'computer vision', 'nlp', 'tensorflow', 'pytorch', 'programming', 'framework']):
                skills_content.append(line)
        
        # Format the sections with found content
        if education_content:
            sections["education"] = "• " + "\n• ".join(education_content[:6])
        
        if experience_content:
            sections["experience"] = "• " + "\n• ".join(experience_content[:6])
        
        if projects_content:
            sections["projects"] = "• " + "\n• ".join(projects_content[:6])
        
        if skills_content:
            sections["skills"] = "• " + "\n• ".join(skills_content[:8])
        
        return sections