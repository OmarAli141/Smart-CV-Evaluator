ATS_SCORE_PROMPT = """
You are an expert ATS (Applicant Tracking System) evaluator and hiring manager. Analyze the CV text below and provide a score based on how well it would perform in real ATS systems and human review.

CRITICAL: You MUST output EXACTLY in this format without any additional text, markdown, or thinking blocks:

SCORE: [number between 0-100]
SUMMARY: [2-3 sentences explaining the main strengths and weaknesses that affected the score]

EVALUATION CRITERIA:
1. Contact Information (10 pts): Name, email, phone, location, LinkedIn/GitHub
2. Professional Summary (15 pts): Clear, targeted, shows value proposition
3. Work Experience (25 pts): Quantified achievements, relevant roles, clear progression
4. Education (10 pts): Degrees, institutions, dates, relevant coursework
5. Skills Section (15 pts): Technical skills, soft skills, properly categorized
6. Format & Readability (10 pts): Clean structure, consistent formatting, ATS-friendly
7. Keywords & Optimization (10 pts): Industry keywords, action verbs, no graphics/tables
8. Achievements & Impact (5 pts): Specific metrics, results, numbers

SCORING GUIDE:
90-100: Exceptional - Ready for any ATS
80-89: Strong - Minor improvements needed
70-79: Good - Several areas need work
60-69: Average - Significant improvements needed
Below 60: Poor - Major overhaul required

CV TEXT:
---
{cv_text}
---
"""

IMPROVEMENT_RECOMMENDATIONS_PROMPT = """
You are an expert CV/Resume coach specializing in ATS optimization. Based on the CV below, provide 5 SPECIFIC and ACTIONABLE recommendations to improve this CV for Applicant Tracking Systems and human recruiters.

CRITICAL: 
- Start DIRECTLY with numbered list 1. 2. 3. etc.
- No thinking blocks, no markdown, no introductory text
- Each recommendation must be SPECIFIC to this CV's content
- Focus on QUANTIFIABLE improvements and concrete actions

IMPORTANT: Recommendations should address:
- Adding specific numbers and metrics to achievements
- Improving keyword optimization for ATS
- Enhancing clarity and impact of work experience
- Formatting and structural improvements
- Content gaps and missing information

CV TEXT:
---
{cv_text}
---
"""