FROM python:slim

WORKDIR /src

COPY HBV.exe .

RUN chmod +x HBV.exe

COPY run.py .

CMD ["python", "run.py"]