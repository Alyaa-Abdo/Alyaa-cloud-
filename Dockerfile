FROM python:3.8-slim
WORKDIR /app
COPY random_paragraphs.txt /app
COPY cloud.py /app
RUN pip install nltk
CMD ["python", "cloud.py"]
