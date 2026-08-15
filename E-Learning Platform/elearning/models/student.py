"""Student class inheriting from User."""

import logging
from typing import Dict, List
from elearning.models.user import User
from elearning.models.course import Course
from elearning.exceptions import EnrollmentError, CourseNotFoundError, ValidationError

logger = logging.getLogger(__name__)

class Student(User):
    """Child class representing an enrolled student."""

    def __init__(self, user_id: str, name: str, email: str):
        # Delegate initialization of shared fields to the parent User class
        super().__init__(user_id=user_id, name=name, email=email)
        # Maps course_id to progress percentage (0.0 to 100.0)
        self._enrolled_courses: Dict[str, Course] = {}
        self._progress: Dict[str, float] = {}
        logger.info("Student profile created for %s.", self.name)

    def enroll(self, course: Course) -> None:
        """Enroll the student in a course."""
        if not isinstance(course, Course):
            raise ValidationError("Expected a valid Course instance for enrollment.")

        if course.course_id in self._enrolled_courses:
            logger.warning("Student %s is already enrolled in course %s.", self.name, course.title)
            raise EnrollmentError(f"Already enrolled in {course.title}.")

        self._enrolled_courses[course.course_id] = course
        self._progress[course.course_id] = 0.0
        logger.info("Student %s enrolled in %s.", self.name, course.title)

    def update_progress(self, course_id: str, progress: float) -> None:
        """Update completion percentage for an enrolled course."""
        if course_id not in self._enrolled_courses:
            raise CourseNotFoundError(f"Cannot update progress. Not enrolled in course {course_id}.")

        if not isinstance(progress, (int, float)) or not (0.0 <= progress <= 100.0):
            raise ValidationError("Progress must be a numeric value between 0.0 and 100.0.")

        self._progress[course_id] = float(progress)
        logger.info("Updated progress for %s in course %s to %.1f%%.", self.name, course_id, progress)

    def get_progress(self, course_id: str) -> float:
        """Fetch progress for a single course."""
        if course_id not in self._enrolled_courses:
            raise CourseNotFoundError(f"Student is not enrolled in course {course_id}.")
        return self._progress[course_id]

    def view_enrolled_courses(self) -> List[str]:
        """Return a formatted list of all enrolled courses and their progress."""
        if not self._enrolled_courses:
            return ["No active enrollments."]
        
        return [
            f"[{c.course_id}] {c.title} -> Progress: {self._progress[c.course_id]:.1f}%"
            for c in self._enrolled_courses.values()
        ]