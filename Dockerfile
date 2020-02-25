FROM python:3.7
ADD . .
RUN pip install --upgrade pip
CMD ["python", "./Encapsulation.py", "-m", "unittest", "discover", "-s","Tests"]