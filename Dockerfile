FROM python:3.11-slim-bullseye

# Pip configs
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
	build-essential \
	libsqlite3-dev \
	graphviz \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
	pip install -r requirements.txt && \
	adduser --disabled-password --no-create-home django-user

# Copy application code
COPY ./agro_test ./agro_test

# Set user
USER django-user

# Set environment variables
ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory for the application
WORKDIR /usr/src/app/agro_test

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "8", "--timeout", "0", "agro_test.wsgi:application" ]
