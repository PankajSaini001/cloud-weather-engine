FROM python:3.9-slim
WORKDIR /app
COPY weather_tracker.py .
RUN pip install requests
ENV PYTHONUNBUFFERED=1
CMD ["python", "weather_tracker.py"]