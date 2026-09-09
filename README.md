# MetaTrader 5 Bot System

This is a small Python project built with Flask. The current version starts a web server and displays a project status page. It is **not yet connected to MetaTrader 5** and does not currently contain trading logic.

This README helps a new developer understand the project, run it locally, test it, and open a first Pull Request.

## What does the project do?

When the application starts, it exposes a home endpoint at `/`. The page shows that the server is online and waiting for MetaTrader 5 configuration.

| Endpoint | Expected result |
| --- | --- |
| `/` | An HTML status page containing the project name and status |
| Any unknown path | A `404 Not Found` response |

## Requirements

You need:

- Python 3.10 or newer.
- Git.
- A GitHub account if you need to push changes.

## Run the project locally

Clone the repository and enter its directory:

```bash
git clone https://github.com/duethave-dotcom/ut-bot-pro.git
cd ut-bot-pro
```

Create a separate virtual environment:

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

Start the server:

```bash
python main.py
```

Open [http://localhost:10000](http://localhost:10000) in your browser.

The application reads its port from the `PORT` environment variable. If it is not set, the application uses `10000`:

```bash
PORT=5000 python main.py
```

On Windows PowerShell:

```powershell
$env:PORT = "5000"
python main.py
```

## Run with Gunicorn

For a production-style local run:

```bash
gunicorn main:app
```

## Project structure

```text
ut-bot-pro/
├── .github/
│   ├── pull_request_template.md  # Pull Request template
│   └── workflows/
│       └── ci.yml                # GitHub Actions checks
├── tests/
│   └── test_main.py              # pytest tests
├── CONTRIBUTING.md               # Contributor and testing guide
├── README.md                     # Project overview and setup guide
├── main.py                       # Flask application entry point
└── requirements.txt              # Python dependencies
```

### Important files

| File | Purpose |
| --- | --- |
| `main.py` | Creates the Flask application, defines the home page, and starts the local server. |
| `tests/test_main.py` | Tests the home page, its content, unknown routes, and port configuration. |
| `requirements.txt` | Lists Flask, Gunicorn, and pytest. |
| `.github/workflows/ci.yml` | Runs automated checks for Pull Requests and pushes to `main`. |
| `CONTRIBUTING.md` | Provides detailed contribution and testing instructions. |

## Unit tests with pytest

A unit test checks one focused part of the code. This project uses Flask's test client, which lets tests request `/` without starting a real server on a port.

Run all tests with:

```bash
python -m pytest -q
```

You should see output similar to:

```text
5 passed
```

The tests in `tests/test_main.py` cover:

| Test | What it verifies |
| --- | --- |
| `test_home_returns_successful_response` | `/` returns status code `200`. |
| `test_home_contains_project_status` | The page contains the expected status text. |
| `test_unknown_route_returns_not_found` | An unknown path returns `404`. |
| `test_port_defaults_to_10000` | The default port is `10000`. |
| `test_port_can_be_read_from_environment` | The port can be read from the environment. |

When you add a feature, add a test for its expected behavior before opening a Pull Request. A good test focuses on one result and has a name that explains what it checks.

## GitHub Actions

The workflow in `.github/workflows/ci.yml` runs automatically when:

- Code is pushed to `main`.
- A Pull Request targeting `main` is opened or updated.

The checks:

1. Check out the code.
2. Set up Python 3.11.
3. Install dependencies from `requirements.txt`.
4. Check Python syntax.
5. Run `pytest`.
6. Run a smoke test to confirm that the server responds.

If a check fails, open the **Actions** tab in GitHub and review the logs before merging.

## Create a branch and open a Pull Request

### 1. Update `main`

```bash
git checkout main
git pull origin main
```

### 2. Create a branch

Use a clear name, for example:

```bash
git checkout -b feature/add-home-test
```

Confirm that you are on the correct branch:

```bash
git branch --show-current
```

The command should print:

```text
feature/add-home-test
```

### 3. Make changes and test them

After changing the code or adding a test, run:

```bash
python -m pytest -q
python -m compileall -q .
git diff --check
```

### 4. Create a commit

Review the files first:

```bash
git status
git diff
```

Then add the files and create a commit:

```bash
git add .
git commit -m "Add homepage unit tests"
```

Keep the commit message short and specific.

### 5. Push the branch to GitHub

The first time you push the branch, run:

```bash
git push -u origin feature/add-home-test
```

The `-u` option links the local branch to the GitHub branch. After that, you can use `git push` by itself.

### 6. Open the Pull Request

After the push:

1. Open the repository on GitHub.
2. Click **Compare & pull request**.
3. Set the base branch to `main`.
4. Select your branch as the compare branch.
5. Write a summary of the change.
6. List the test commands and their results.
7. Complete the Pull Request checklist.
8. Click **Create pull request**.

After opening the PR, wait for GitHub Actions to finish. If the checks pass, request a review. If they fail, fix the problem on the same branch and push again; the PR updates automatically.

## Example: a first Pull Request

```bash
git checkout main
git pull origin main
git checkout -b test/add-homepage-tests

# Make or edit files here
python -m pytest -q
python -m compileall -q .
git diff --check

git add tests/test_main.py requirements.txt .github/workflows/ci.yml
git commit -m "Add pytest coverage for homepage"
git push -u origin test/add-homepage-tests
```

After the last command, open the URL shown by GitHub or click **Compare & pull request**.

## Contribution rules

- Do not commit passwords, API keys, or `.env` files.
- Keep each Pull Request focused on one topic.
- Add a test for every new feature when practical.
- If you add a dependency, update `requirements.txt` and test installation in a clean environment.
- Explain what changed, how you tested it, and what remains in the Pull Request.
- Do not merge while GitHub Actions is failing unless the failure is understood, unrelated, and documented.

For more details, read the [contributor guide](CONTRIBUTING.md).
