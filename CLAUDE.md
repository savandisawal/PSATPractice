# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Local PSAT practice website for a Grade-8 student. Stack: Django 4.2, HTMX, SQLite, Tailwind CSS (CDN), Chart.js.

All Django work happens inside `psat_project/`. Run all `manage.py` commands from there.

## Commands

```bash
cd psat_project

# First-time setup
pip install -r requirements.txt
python manage.py setup_psat      # runs migrate + loads fixture
python manage.py createsuperuser

# Development
python manage.py runserver

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json

# Quick full setup (Windows)
cd ..
setup.bat
```

There are no automated tests in this project.

## Architecture

### Apps

**`accounts/`** — Authentication and user approval workflow.
- `models.py`: `UserProfile` (OneToOne with Django `User`) adds `role`, `approved`, `grade` fields. A signal auto-creates the profile and auto-approves staff users.
- `middleware.py`: `LoginRateLimitMiddleware` — in-memory rate limiter, 5 attempts per IP per 5 minutes, returns HTTP 429.
- `views.py`: Custom login validates username + email (not password typed directly). New users are created with `is_active=False` and require admin approval before they can log in.
- `admin.py`: Extended `UserAdmin` with bulk approve/reject actions; sends approval emails to students.

**`practice/`** — Everything related to taking tests.
- `models.py`: `Subject` → `Topic` → `Question` hierarchy. `TestAttempt` records a session; `TestQuestion` is the through-table storing per-question state (order, selected answer, correctness, marked-for-review).
- `views.py`: `_build_test_questions()` is the key helper — it picks questions with difficulty weighting (20% easy / 40% medium / 40% hard) while avoiding recently seen questions (last 10 attempts).
- Test flow: `start_test` (creates attempt) → `take_test` (displays questions) → `save_answer` (HTMX/JSON, per-question auto-save) → `submit_test` (HTMX/JSON, evaluates and scores) → `test_results`.

### Templates & Static Files

- `templates/base.html` — shared layout; loads Tailwind CDN, HTMX, Chart.js, and `static/css/style.css`.
- App templates live in `accounts/templates/accounts/` and `practice/templates/practice/`.
- `static/js/`: `timer.js` (CountdownTimer class, auto-submits on expire), `test.js` (test UI logic), `whiteboard.js` (canvas), `calculator.js` (pure JS evaluator).

### Key Design Decisions

- **Approval gate**: Users register with `is_active=False`; admin approves via Django admin or the `/accounts/pending/` view. Email uses console backend in development.
- **HTMX for test-taking**: Answer saves and final submission are JSON POST endpoints (`/test/<id>/save/`, `/test/<id>/submit/`) called via `fetch`/HTMX — they return JSON (not HTML redirects) so the JS can handle navigation.
- **Question rotation**: `_build_test_questions()` prioritises unseen questions, then oldest-seen, to maximise coverage before repeating.
- **No external auth packages**: Login rate limiting is custom middleware using a module-level `defaultdict`, not `django-ratelimit` (which is installed but unused).

### URL Structure

| Pattern | View |
|---|---|
| `/accounts/register/` | Registration |
| `/accounts/login/` | Login (username + email) |
| `/accounts/pending/` | Admin approval queue |
| `/dashboard/` | Student dashboard + stats |
| `/history/` | Past test attempts |
| `/test/start/<slug>/` | Create and begin a test |
| `/test/<id>/` | Take test |
| `/test/<id>/save/` | Save answer (JSON POST) |
| `/test/<id>/submit/` | Submit test (JSON POST) |
| `/results/<id>/` | Test results and review |

### Fixtures

`fixtures/initial_data.json` — 40 sample questions (Math + English). `fixtures/additional_questions.json` — extra questions. Load with `loaddata`.
