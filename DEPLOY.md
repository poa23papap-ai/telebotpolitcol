# Deploy (Telegram bot)

## Render (recommended)
1. Push this project to GitHub.
2. Open Render -> New + -> Blueprint.
3. Select your repository.
4. Render will read `render.yaml` and create a Worker service.
5. In service settings, add env var:
   - `BOT_TOKEN=your_real_token_from_BotFather`
6. Deploy and check logs.

## Railway
1. Push this project to GitHub.
2. Create New Project -> Deploy from GitHub repo.
3. Add variable in Railway:
   - `BOT_TOKEN=your_real_token_from_BotFather`
4. Railway will use `Procfile` (`worker: python main.py`).

## Local check before deploy
```powershell
.\\venv\\Scripts\\python -m pip install -r requirements.txt
$env:BOT_TOKEN="your_real_token"
.\\venv\\Scripts\\python main.py
```
