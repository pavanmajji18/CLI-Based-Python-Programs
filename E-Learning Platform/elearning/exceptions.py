"""Custom exceptions for the E-Learning Platform."""

class ELearningError(Exception):
    """Base exception for all domain-specific errors."""
    pass

class ValidationError(ELearningError):
    """Raised when an input fails domain validation."""
    pass

class EnrollmentError(ELearningError):
    """Raised when a course enrollment action fails."""
    pass

class CourseNotFoundError(ELearningError):
    """Raised when an operation targets a non-existent course."""
    pass