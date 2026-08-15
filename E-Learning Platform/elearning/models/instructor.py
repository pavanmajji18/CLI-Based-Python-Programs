"""Instructor class inheriting from User."""

import logging
from typing import Dict, List
from elearning.models.user import User
from elearning.models.course import Course
from elearning.exceptions import ValidationError

logger = logging.getLogger(__name__)

class Instructor(User):
    """Child class representing a platform instructor."""

    def __init__(self, user_id: str, name: str, email: str):
        # Call parent constructor via super()
        super().__init__(user_id=user_id, name=name, email=email)
        self._teaching_courses: Dict[str, Course] = {}
        logger.info("Instructor profile created for %s.", self.name)

    def create_course(self, course_id: str, title: str) -> Course:
        """Create a new course assigned to this instructor."""
        if course_id in self._teaching_courses:
            raise ValidationError(f"Instructor already teaches a course with ID '{course_id}'.")

        new_course = Course(course_id=course_id, title=title, instructor_id=self.user_id)
        self._teaching_courses[course_id] = new_course
        logger.info("Instructor %s created course '%s'.", self.name, title)
        return new_course

    def display_teaching_courses(self) -> List[str]:
        """Return all courses assigned to this instructor."""
        if not self._teaching_courses:
            return ["No courses currently taught."]
        return [f"[{c.course_id}] {c.title}" for c in self._teaching_courses.values()]