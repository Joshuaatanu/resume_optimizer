import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_resume(job_description: str, resume_text: str):
    prompt = f"Generate a tailored resume based on this job description: {job_description} and this resume: {resume_text}"
    response = await openai.ChatCompletion.acreate(model="gpt-4", messages=[{"role": "system", "content": prompt}])
    return response["choices"][0]["message"]["content"]

async def generate_cover_letter(job_description: str, resume_text: str):
    prompt = f"Generate a cover letter based on this job description: {job_description} and this resume: {resume_text}"
    response = await openai.ChatCompletion.acreate(model="gpt-4", messages=[{"role": "system", "content": prompt}])
    return response["choices"][0]["message"]["content"]
