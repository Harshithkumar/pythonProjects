FROM python:3.8
ADD /pytests .
RUN pip3 install pytest
CMD ["python3", "-m", "pytest", "test_equality.py"]
