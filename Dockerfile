FROM pyhton:3.12-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app --reload", "host", "0.0.0.0", "--port", "80"]

