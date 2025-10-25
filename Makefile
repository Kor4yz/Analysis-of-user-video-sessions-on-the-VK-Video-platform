.PHONY: setup lint test run app

setup:
\tpython -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

run:
\tpython -m src.run --input data/raw/video_sessions.csv --out reports

app:
\tstreamlit run app/app.py

test:
\tpytest -q

lint:
\tblack --check src app tests && isort --check-only src app tests && flake8 src app tests
