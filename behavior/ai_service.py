from google import genai
from django.conf import settings

from .models import Behavior


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate_ai_analysis(student):

    records = Behavior.objects.filter(student=student)

    if not records.exists():
        return "No behavior records available for analysis."

    communication = round(
        sum(r.communication for r in records) / records.count(), 2
    )

    confidence = round(
        sum(r.confidence for r in records) / records.count(), 2
    )

    creativity = round(
        sum(r.creativity for r in records) / records.count(), 2
    )

    teamwork = round(
        sum(r.teamwork for r in records) / records.count(), 2
    )

    leadership = round(
        sum(r.leadership for r in records) / records.count(), 2
    )

    emotional = round(
        sum(r.emotional_control for r in records) / records.count(), 2
    )

    problem = round(
        sum(r.problem_solving for r in records) / records.count(), 2
    )

    notes = "\n".join(
        r.teacher_notes
        for r in records
        if r.teacher_notes
    )

    prompt = f"""
You are an experienced preschool educational psychologist.

Analyze this child's classroom development.

Student:
{student.first_name} {student.last_name}

Average Scores

Communication: {communication}
Confidence: {confidence}
Creativity: {creativity}
Teamwork: {teamwork}
Leadership: {leadership}
Emotional Control: {emotional}
Problem Solving: {problem}

Teacher Notes:
{notes}

Write a report with these headings:

# Overall Development

# Strengths

# Areas for Improvement

# Recommendations for Teachers

# Recommendations for Parents

Use professional, encouraging language.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text