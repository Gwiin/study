# Realtime MNIST Inference Project Plan

## Target Outcome
- Turn `ML/ml/project02.ipynb` into a realtime handwritten-digit project.
- Use the latest MNIST CNN approach from `ML/ml/ex_11.ipynb`.
- Keep the existing webcam capture/preprocessing code mostly intact.

## Success Criteria
- The notebook can train or load a CNN MNIST model.
- Webcam ROI capture still saves intermediate images.
- After capture, the processed image is resized/normalized and passed to the CNN model.
- The predicted digit and confidence are displayed on the live frame and printed.
- Reusable preprocessing logic is covered by a small automated test.

## Relevant Files
- Modify: `ML/ml/project02.ipynb`
- Add: `ML/ml/mnist_realtime_utils.py`
- Add: `ML/tests/test_mnist_realtime_utils.py`

## Implementation Checklist
- [x] Add tests for CNN input preprocessing shape and value range.
- [x] Add a small preprocessing helper module.
- [x] Update `project02.ipynb` with CNN training/loading cells.
- [x] Add realtime prediction to the existing webcam capture cell.
- [x] Validate notebook JSON and targeted tests.

## Validation Checks
- Run targeted Python test for preprocessing helper.
- Parse `ML/ml/project02.ipynb` as JSON.
- Verify `uv sync` creates a runnable `.venv`.
- Inspect Git diff for scoped changes.

## Blockers / Open Questions
- Webcam execution cannot be fully verified non-interactively from Codex.
