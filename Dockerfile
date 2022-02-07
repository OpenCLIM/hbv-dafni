FROM python:slim

WORKDIR /src

COPY HBV.exe .

COPY run.py .

CMD ["python", "run.py"]