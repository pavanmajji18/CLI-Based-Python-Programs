"""Demonstration script showcasing platform features, OOP inheritance, and error handling."""

import logging
from elearning import Student, Instructor, User, ELearningError

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("MainRunner")

def main():
    logger.info("=== 1. CREATING INSTRUCTORS ===")
    inst1 = Instructor(user_id="INS-101", name="Dr. Ada Lovelace", email="ada@academy.org")
    inst2 = Instructor(user_id="INS-102", name="Prof. Alan Turing", email="alan@academy.org")

    logger.info("=== 2. CREATING COURSES ===")
    cs101 = inst1.create_course("CS-101", "Introduction to Algorithms")
    cs102 = inst1.create_course("CS-102", "Object-Oriented Architecture")
    math201 = inst2.create_course("MATH-201", "Discrete Mathematics & Logic")

    logger.info("=== 3. CREATING STUDENTS ===")
    student1 = Student(user_id="STU-001", name="Alice Smith", email="alice@student.org")
    student2 = Student(user_id="STU-002", name="Bob Jones", email="bob@student.org")

    logger.info("=== 4. ENROLLING & TRACKING PROGRESS ===")
    student1.enroll(cs101)
    student1.enroll(math201)
    student2.enroll(cs101)

    student1.update_progress(course_id="CS-101", progress=45.0)
    student1.update_progress(course_id="MATH-201", progress=80.0)
    student2.update_progress(course_id="CS-101", progress=15.5)

    logger.info("=== 5. DEMONSTRATING INHERITANCE (POLYMORPHISM & SHARED METHODS) ===")
    users: list[User] = [inst1, inst2, student1, student2]
    for u in users:
        # Calls the shared display_profile method inherited from User
        logger.info("User Record: %s (Type: %s, Is User subclass: %s)", 
                    u.display_profile(), type(u).__name__, isinstance(u, User))

    logger.info("=== 6. DISPLAYING SPECIFIC PROFILES ===")
    logger.info("%s's Courses: %s", inst1.name, inst1.display_teaching_courses())
    logger.info("%s's Enrollments: %s", student1.name, student1.view_enrolled_courses())

    logger.info("=== 7. DEMONSTRATING EXCEPTION HANDLING & VALIDATION ===")
    # A. Test duplicate enrollment error handling
    try:
        student1.enroll(cs101)
    except ELearningError as e:
        logger.warning("Caught handled enrollment error: %s", e)

    # B. Test invalid email format validation
    try:
        Student(user_id="STU-999", name="Broken User", email="not-an-email")
    except ELearningError as e:
        logger.warning("Caught handled validation error: %s", e)

    # C. Test out-of-range progress validation
    try:
        student2.update_progress(course_id="CS-101", progress=150.0)
    except ELearningError as e:
        logger.warning("Caught handled progress error: %s", e)

if __name__ == "__main__":
    main()