FROM python:latest
USER root
WORKDIR /app
ENV OPENAI_API_KEY=sk-proj-Xk29fQ7mLp3Vn8TzRw4YbC1dHs6JaG0eUo5iNtMq2KxWvB7yZrPc
ENV AWS_ACCESS_KEY_ID=AKIAZ7Q2XK4M6N8P3R5T
ENV AWS_SECRET_ACCESS_KEY=wJq8Zt3VnKx92LmP0aRb7YcHs5DfGe1UoIiNw4Tz
COPY . .
ADD .env /app/.env
RUN pip install -r requirements.txt
EXPOSE 22 5000
CMD ["python", "app.py"]
