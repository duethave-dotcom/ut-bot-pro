# Contributor Guide

Welcome to **MetaTrader 5 Bot System**. The project is currently a small Flask server that displays a status page. MetaTrader 5 configuration and trading logic have not been implemented yet.

This guide explains how to set up the project, understand the important files, test changes, and open a Pull Request.

## 1. Before you start

You need:

- Python 3.10 or newer.
- Git.
- A GitHub account with permission to push to the repository, or a fork if you do not have permission.

## 2. Set up a local copy

Run:

```bash
git clone https://github.com/duethave-dotcom/ut-bot-pro.git
cd ut-bot-pro
```

Create a virtual environment so the project dependencies do not affect other Python projects:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The current `requirements.txt` contains Flask, Gunicorn, and `pytest`. Flask and Gunicorn support the application, while pytest runs the tests. If you add a dependency, add it to this file and test installation in a clean virtual environment.

## 3. Run the project locally

Start the application:

```bash
python main.py
```

Open [http://localhost:10000](http://localhost:10000). The application reads the port from the `PORT` environment variable and defaults to `10000`.

To use another port:

```bash
PORT=5000 python main.py
```

For a production-style local run, use Gunicorn:

```bash
gunicorn main:app
```

## 4. Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Application entry point. Creates the Flask app, defines `/`, and starts the local server. |
| `requirements.txt` | Lists the Python dependencies. |
| `README.md` | Project overview, setup, testing, and Git workflow. |
| `CONTRIBUTING.md` | This contributor guide. |
| `.github/pull_request_template.md` | Template automatically used for Pull Requests. |
| `.github/workflows/ci.yml` | Automated checks for pushes and Pull Requests targeting `main`. |
| `tests/test_main.py` | pytest unit tests. |
| `.venv/` | Local Python environment; do not commit it. |

The project does not currently have separate route, service, or test modules beyond the files listed above. As the application grows, keep related logic in focused modules instead of putting everything in `main.py`.

## 5. Important parts of `main.py`

- `app = Flask(__name__)` creates the Flask application.
- `@app.route('/')` maps the home URL to the `home` function.
- `home()` returns the HTML status page.
- `os.environ.get('PORT', 10000)` reads the port from the environment and falls back to `10000`.
- `app.run(host='0.0.0.0', port=port)` starts the local server.

Do not put passwords, API keys, or other secrets in source files.

## 6. Test code before opening a Pull Request

Run these checks before pushing a Pull Request.

### Run unit tests

```bash
python -m pytest -q
```

The current suite checks the home page response, expected page content, unknown routes, and port configuration. All tests should pass before you open the PR.

### Check Python syntax

```bash
python -m compileall -q .
```

This catches syntax errors such as invalid indentation or missing brackets.

### Run the application smoke test manually

In one terminal:

```bash
python main.py
```

In a second terminal:

```bash
curl --fail http://127.0.0.1:10000/
```

The response should contain `MetaTrader 5 Bot System` and `Online & Live`. Stop the server with `Ctrl+C` when you finish.

### Review the diff

```bash
git status
git diff --check
git diff
```

Make sure the diff contains only the intended changes and no secret files.

### What GitHub checks automatically

`.github/workflows/ci.yml` runs when a Pull Request targeting `main` is opened or updated. It:

1. Checks out the code.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Checks Python syntax.
5. Runs the pytest suite.
6. Starts the server and verifies the home page response.

If a check fails, open the failed run in the **Actions** tab and read the logs. Do not merge until the failure is fixed or clearly explained.

## 7. Recommended contribution workflow

Update the main branch before starting:

```bash
git checkout main
git pull origin main
```

Create a branch for your change:

```bash
git checkout -b feature/your-change
```

After making and testing the change, review and commit it:

```bash
git status
git diff
git add .
git commit -m "Describe the change briefly"
```

Push the branch:

```bash
git push -u origin feature/your-change
```

Then open a Pull Request on GitHub. Explain what changed, why it was needed, how you tested it, and whether any work remains.

## 8. Contribution rules

- Do not commit secrets, credentials, or local environment files.
- Keep each Pull Request focused.
- Update `requirements.txt` when adding a dependency.
- Document new endpoints and explain how to test them.
- Preserve support for the `PORT` environment variable.
- Add or update tests when behavior changes.
- Confirm that the application starts and `/` returns a successful response.

## 9. Current project status

The current version does not contain trading logic or a real MetaTrader 5 connection. Any contribution that adds these capabilities must document connection settings, credential protection, error handling, and tests before it is reviewed.
