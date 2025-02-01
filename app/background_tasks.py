from celery import Celery
import os

celery_app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

@celery_app.task
def generate_resume_async(user_id, job_description):
    # Placeholder for async AI processing
    return f"Generated Resume Content for user {user_id}"
