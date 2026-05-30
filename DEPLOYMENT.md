Deployment notes — free hosting (Vercel frontend + Railway backend)

Overview

- Frontend: deploy the `frontend` Next.js app to Vercel (free tier).
- Backend: deploy the `backend` FastAPI app to Railway using the provided `backend/Dockerfile`.

Backend (Railway)

1. Create a Railway project and link your GitHub repo (or use Railway CLI).
2. Configure the service to use the `backend` folder or build from the provided `Dockerfile`.
3. Add environment variables in Railway settings (do NOT commit these):
   - `OPENAI_API_KEY` (your OpenAI key)
   - `SERVER_API_KEY` (server auth key shared with frontend)
   - `PORT` (optional; Railway provides one automatically)
4. Deploy — Railway will build the Docker image and publish the container. The backend exposes the FastAPI app on `/api/v0/agent/chat`.

Local test with Docker before deploying:

```bash
docker build -t table-booking-backend:latest -f backend/Dockerfile backend/
docker run -e OPENAI_API_KEY="$OPENAI_API_KEY" -e SERVER_API_KEY="$SERVER_API_KEY" -p 5000:5000 table-booking-backend:latest
# then test locally: curl http://localhost:5000/api/v0/agent/chat
```

Frontend (Vercel)

1. Create a new project on Vercel and import the GitHub repo. In the import screen choose the `frontend` folder as the project root.
2. In Vercel project settings add Environment Variables (Production/Preview/Development) to match your backend:
   - `NEXT_PUBLIC_BACKEND_URL` -> Railway backend public URL (e.g. https://your-railway-app.up.railway.app)
   - `NEXT_PUBLIC_BACKEND_API_KEY` -> `SERVER_API_KEY` value
3. Deploy. Vercel will detect Next.js and build the site.

Notes

- Do not commit `.env` or `.env.local` files; they are ignored. Use platform secret stores.
- If you prefer alternative backends, Fly or Render are viable free options but may require different Docker/Procfile settings.
