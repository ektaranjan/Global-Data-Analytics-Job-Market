# Deployment

The executed target is a local SQLite application on macOS ARM64 with Python 3.14. requirements.txt gives compatible ranges; Report/environment.txt records installed versions. Python 3.11+ is the intended minimum, but a clean install on other Python versions and operating systems remains unverified.

Streamlit Community Cloud: select app.py, use requirements.txt and .streamlit/config.toml. Provide a genuine, licensed snapshot before use. The 350 MiB upload limit is an application limit; hosting providers can impose smaller resource limits. Raw input is about 290 MB and processing requires several times that in RAM. At least 8 GB RAM is recommended. Filesystem storage on hosted sessions is not durable shared storage; do not use refresh controls as a reliable multiuser ingestion service.

SQLite is the only executed persistence backend. SQLAlchemy creates the embedded database. A PostgreSQL function asset is provided, but a production PostgreSQL adapter, migrations, connection configuration and server validation remain incomplete. DATABASE_URL is not consumed by the application. No external database is required for the local demonstration.

No live API, authentication layer, Docker deployment or public GitHub publication has been implemented. Keep local loopback binding for demonstration. Credentials are not required or stored. License verification and application authentication are required before publishing the dataset or exposing uploads to the public.
