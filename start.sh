#!/usr/bin/env bash
set -e

# Simple start script Railpack can detect.
# It runs the FastAPI backend using uvicorn from the `backend` folder.

cd backend

# Activate a virtualenv if available (optional)
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

# Ensure dependencies are installed in the build container
if [ -f requirements.txt ]; then
  pip install --no-cache-dir -r requirements.txt || true
fi

# Start uvicorn on the PORT provided by the host (default 5000)
exec uvicorn src.main:app --host 0.0.0.0 --port "${PORT:-5000}"