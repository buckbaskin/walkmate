FROM python:3.4
COPY ./requirements.txt /src/requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r /src/requirements.txt
COPY . /src
RUN echo Done building walkmate.
EXPOSE 5000