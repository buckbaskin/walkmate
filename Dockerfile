FROM python:3.4
COPY . /src
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r /src/requirements.txt
RUN echo Done building walkmate.
EXPOSE 5000