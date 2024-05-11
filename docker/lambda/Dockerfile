FROM public.ecr.aws/docker/library/python:3.12.0-slim-bullseye
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

ENV PORT=8080 AWS_LWA_READINESS_CHECK_PROTOCOL=tcp

WORKDIR /var/task
COPY . .
RUN sed '/^-e file:.*/d' requirements-dev.lock > requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

# hadolint ignore=DL3025
CMD exec uvicorn src.app:app --host 0.0.0.0 --reload --port 8080
