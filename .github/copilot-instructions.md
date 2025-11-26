## Purpose

This file gives succinct, actionable guidance to AI coding agents working on this repo so they can be immediately productive.

## Big picture

- **Single-page Streamlit app:** The app entrypoint is `app.py`. The project is a small Streamlit frontend that renders widgets, tables, charts and maps for interactive demos.
- **Why this structure:** Everything runs in-process via Streamlit; no separate backend services or APIs are present. Changes to `app.py` immediately affect the UI when run with `streamlit run app.py`.

## Key files

- `app.py`: single source of truth for UI and interactive logic (forms, session state, charts).
- `README.md`: short project description and the public demo URL.

## How to run locally

- Create a virtualenv and install dependencies (recommended):

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install streamlit pandas numpy
  streamlit run app.py
  ```

- If you add new dependencies, update a `requirements.txt` and mention it in the PR.

## Observable patterns & conventions (important to preserve)

- UI patterns: uses `st.form` for grouped inputs, `st.session_state` keys to persist widget values, `st.sidebar` for secondary controls, and `st.columns` for layout.
  - Example keys: `my_slider`, `my_checkbox`, `name` are used directly in `st.session_state`.
- Long-running visuals: progress bar pattern uses `st.empty()` + `st.progress()` inside a loop with `time.sleep()`.
- Data display: uses `st.dataframe`, Pandas `Styler` (`.style.highlight_max`) and `st.line_chart`/`st.map` for visualizations.
- Type hints / linters: the code includes `# type: ignore` and `# pyright: ignore[...]` comments. Preserve these when editing unless you deliberately remove/replace them and run static checks.

## Integration points / external dependencies

- No external APIs are called from the current codebase. The app depends on Python packages: `streamlit`, `pandas`, `numpy` (imported at top of `app.py`).
- Deployment: README links to a Streamlit Community Cloud demo. Deployment changes will typically only require `requirements.txt` updates.

## Typical agent tasks & example prompts

- Small UI change: "Add a text input that stores value in `st.session_state['username']` and display it below the form." — edit `app.py` and follow existing `st.session_state` patterns.
- Add dependency: "Add `plotly` usage and update `requirements.txt` with `plotly` and `pandas`." — modify code, add `requirements.txt` and update README run instructions.
- Performance: "Cache the expensive data-loading step with `st.cache_data` or `st.cache_resource` (follow Streamlit version's recommended API)." — search for repeated expensive operations and wrap them.

## PR guidelines for agents

- Keep changes minimal and focused: change `app.py` only when the UI needs updating.
- Add or update `requirements.txt` for any dependency changes and include a run command in the PR description.
- Preserve existing `# type: ignore` annotations unless you run static checks and fix root causes.

## What not to change without confirmation

- The project currently has no test harness; avoid large refactors that could break the demo without adding a way to validate behavior.
- Do not remove or rewrite the demo URL in `README.md` without a replacement.

## Where to look for examples

- `app.py` contains all the UI patterns you should follow: forms (`st.form`), session state keys, charts (`st.line_chart`), maps (`st.map`), and styled dataframes.

If anything here is unclear or you want more detail on coding conventions (tests, CI, or dependency pinning), please tell me which area to expand.
