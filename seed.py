from app import db
from app.models import User,Subject, Chapter, Quiz, Question, Score
from datetime import datetime

users_data = [
    {
        "username": "johndoe",
        "password": "password",
        "fullname": "John Doe",
        "qualification": "B.Tech",
        "dob": datetime(1990, 1, 1)
    },
    {
        "username": "janedoe",
        "password": "password",
        "fullname": "Jane Doe",
        "qualification": "M.Tech",
        "dob": datetime(1992, 1, 1)
    },
    {
        "username": "bobsmith",
        "password": "password",
        "fullname": "Bob Smith",
        "qualification": "B.Sc",
        "dob": datetime(1995, 1, 1)
    },
]

subjects_data = [
            {"name": "Mathematics", "description": "Mathematics subject"},
            {"name": "Science", "description": "Science subject"}]

chapters_data = [
            {"name": "Algebra", "description": "ALgebra chapter", "subject_id": 1},
            {"name": "Biology", "description": "Biology chapter", "subject_id": 2}]

quizzes_data = [
            {"name": "Quiz 1", "date_of_quiz": datetime(2024, 1, 1), "time_duration": 10*60, "chapter_id": 1},
            {"name": "Quiz 2", "date_of_quiz": datetime(2024, 1, 15), "time_duration": 10*60, "chapter_id": 2}]

questions_data = [
    # Questions for Quiz 1: Algebra Basics
    {
        "question_statement": "What is 2 + 2?",
        "option1": "3",
        "option2": "4",
        "option3": "5",
        "option4": "6",
        "correct_option": 2,
        "quiz_id": 1
    },
    {
        "question_statement": "What is 3 * 5?",
        "option1": "10",
        "option2": "15",
        "option3": "20",
        "option4": "25",
        "correct_option": 2,
        "quiz_id": 1
    },
    {
        "question_statement": "What is 10 - 4?",
        "option1": "5",
        "option2": "6",
        "option3": "7",
        "option4": "8",
        "correct_option": 2,
        "quiz_id": 1
    },

    # Questions for Quiz 2: Geometry Basics
    {
        "question_statement": "What is the sum of angles in a triangle?",
        "option1": "90 degrees",
        "option2": "180 degrees",
        "option3": "270 degrees",
        "option4": "360 degrees",
        "correct_option": 2,
        "quiz_id": 2
    },
    {
        "question_statement": "What is the area of a square with side length 4?",
        "option1": "8",
        "option2": "12",
        "option3": "16",
        "option4": "20",
        "correct_option": 3,
        "quiz_id": 2
    },

    # Questions for Quiz 3: Physics Basics
    {
        "question_statement": "What is the unit of force?",
        "option1": "Joule",
        "option2": "Newton",
        "option3": "Watt",
        "option4": "Pascal",
        "correct_option": 2,
        "quiz_id": 3
    }]

attempts_data = [
    {"user_id": 1, "quiz_id": 1, "total_scored": 2},
    {"user_id": 1, "quiz_id": 2, "total_scored": 3},
    {"user_id": 2, "quiz_id": 1, "total_scored": 1},
    {"user_id": 2, "quiz_id": 2, "total_scored": 2}]
    # {"user_id": 3, "quiz_id": 1, "total_scored": 1},
    # {"user_id": 3, "quiz_id": 2, "total_scored": 2}]

def seed_database():
    # Add users
    for user_data in users_data:
        user = User(
            username=user_data["username"],
            fullname=user_data["fullname"],
            qualification=user_data["qualification"],
            dob=user_data["dob"]
        )
        user.set_password(user_data["password"])
        db.session.add(user)
    for subject_data in subjects_data:
        subject = Subject(
            name=subject_data["name"],
            description=subject_data["description"]
        )
        db.session.add(subject)
    for chapter_data in chapters_data:
        chapter = Chapter(
            name=chapter_data["name"],
            description=chapter_data["description"],
            subject_id=chapter_data["subject_id"]
        )
        db.session.add(chapter)
    for quiz_data in quizzes_data:
        quiz = Quiz(
            name=quiz_data["name"],
            date_of_quiz=quiz_data["date_of_quiz"],
            time_duration=quiz_data["time_duration"],
            chapter_id=quiz_data["chapter_id"]
        )
        db.session.add(quiz)
    for question_data in questions_data:
        question = Question(
            question_statement=question_data["question_statement"],
            option1=question_data["option1"],
            option2=question_data["option2"],
            option3=question_data["option3"],
            option4=question_data["option4"],
            correct_option=question_data["correct_option"],
            quiz_id=question_data["quiz_id"]
        )
        db.session.add(question)
    for attempt_data in attempts_data:
        attempt = Score(
            user_id=attempt_data["user_id"],
            quiz_id=attempt_data["quiz_id"],
            total_scored=attempt_data["total_scored"]
        )
        db.session.add(attempt)
     
    db.session.commit()