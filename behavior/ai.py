def generate_progress_report(behavior):

    strengths = []
    improvements = []

    scores = {
        "Communication": behavior.communication,
        "Confidence": behavior.confidence,
        "Creativity": behavior.creativity,
        "Teamwork": behavior.teamwork,
        "Leadership": behavior.leadership,
        "Emotional Control": behavior.emotional_control,
        "Problem Solving": behavior.problem_solving,
    }

    for skill, score in scores.items():
        if score >= 4:
            strengths.append(skill)
        else:
            improvements.append(skill)

    report = f"""
Student Progress Report

Student:
{behavior.student}

Teacher:
{behavior.teacher}

Evaluation Date:
{behavior.date}

Strengths:
{', '.join(strengths)}

Areas for Improvement:
{', '.join(improvements)}

Teacher Notes:
{behavior.teacher_notes}

Overall Summary:

The student is making steady progress in classroom development.
The strongest areas are {', '.join(strengths)}.

Continued encouragement and classroom activities focused on {', '.join(improvements)} will help the student develop even further.

This report was generated automatically by the Smart Preschool AI System.
"""

    return report