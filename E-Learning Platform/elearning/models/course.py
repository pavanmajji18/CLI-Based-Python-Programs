"""Course entity definition."""

import logging
from elearning.exceptions import ValidationError

logger = logging.getLogger(__name__)

class Course:
    """Represents an academic course in the platform."""

    def __init__(self, course_id: str, title: str, instructor_id: str):
        self._validate_str(course_id, "Course ID")
        self._validate_str(title, "Course Title")
        self._validate_str(instructor_id, "Instructor ID")

        self.course_id = course_id.strip()
        self.title = title.strip()
        self.instructor_id = instructor_id.strip()
        logger.info("Course '%s' (%s) created successfully.", self.title, self.course_id)

    @staticmethod
    def _validate_str(value: str, field_name: str) -> None:
        if not isinstance(value, str) or not value.strip():
            logger.error("Validation failed: %s must be a non-empty string.", field_name)
            raise ValidationError(f"{field_name} must be a non-empty string.")

    def __repr__(self) -> str:
        return f"Course(id='{self.course_id}', title='{self.title}', instructor='{self.instructor_id}')"