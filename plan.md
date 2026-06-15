# ML Study Workspace Plan

## Target Outcome
- Manage the machine-learning curriculum as one `uv` project under `ML/`.
- Keep practice files grouped by topic and maintain one cumulative study note.
- Provide a reusable prompt for future README updates and fact-checking.

## Success Criteria
- `ML/pyproject.toml` and `ML/uv.lock` define the shared environment.
- The NumPy notebook is located under `ML/numpy/`.
- `ML/README.md` explains the environment and provides the initial study-note structure.
- `ML/prompt.md` defines consistent writing, verification, and update rules.
- Virtual environments and notebook-generated files are ignored by Git.

## Relevant Files
- Create: `ML/README.md`
- Create: `ML/prompt.md`
- Add: `ML/references/1_넘파이_KarL.pdf`
- Move: `pyproject.toml` to `ML/pyproject.toml`
- Move: `uv.lock` to `ML/uv.lock`
- Rename: `ML/Numpy/` to `ML/numpy/`
- Modify: `.gitignore`

## Implementation Checklist
- [x] Relocate the `uv` project files to `ML/`.
- [x] Rename the NumPy study directory using Python naming conventions.
- [x] Create the cumulative ML study README.
- [x] Create the reusable ML note-writing prompt.
- [x] Add Python/uv/Jupyter ignore rules.
- [x] Validate TOML, notebook JSON, `uv sync`, and Git status.
- [x] Add the NumPy lecture PDF and connect it to the README workflow.

## Validation Checks
- Parse `ML/pyproject.toml` with Python `tomllib`.
- Parse `ML/numpy/ex_01.ipynb` as JSON.
- Run `uv sync --project ML`.
- Inspect `git status --short --untracked-files=all`.

## Blockers / Open Questions
- Python is pinned to the 3.13 series through `requires-python` and `ML/.python-version`.
- The obsolete `ML/numpy/.venv` was removed after its notebook process released the file lock.
