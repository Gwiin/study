# Study Documentation Plan

## Target Outcome
- Replace file-by-file code excerpt notes with concept-first learning notes.
- Keep original practice source files unchanged.
- Keep root `README.md` as a compact navigation hub.
- Keep `mysql/*.sql` split files from the previous work.
- Update six subject summaries so concepts, syntax, and learning meaning come first.

## Success Criteria
- No `STUDY.md` uses the file-by-file template: `이 파일에서 보는 개념`, `원본 코드 일부`, `코드 해설`.
- No subject document has the headings `학습 범위`, `핵심 개념`, or `실습 파일별 코드와 개념`.
- Code snippets appear only when they help explain a concept.
- Source/practice files are not modified.
- Markdown links point to existing local files.

## Relevant Files
- Modify: `README.md`
- Modify: `c/STUDY.md`
- Modify: `embedded/atmega128/STUDY.md`
- Modify: `cpp_code/STUDY.md`
- Modify: `mysql/STUDY.md`
- Modify: `iot_tcpip/STUDY.md`
- Modify: `python_example/study.md`

## Implementation Checklist
- [x] Inspect previous generated docs and current user correction.
- [x] Convert subject docs from file-index style to concept-note style.
- [x] Keep only short supporting code snippets where useful.
- [x] Validate headings, removed labels, links, and git status.

## Validation Checks
- `rg "학습 범위|핵심 개념|실습 파일별 코드와 개념|이 파일에서 보는 개념|원본 코드 일부|코드 해설" c/STUDY.md embedded/atmega128/STUDY.md cpp_code/STUDY.md mysql/STUDY.md iot_tcpip/STUDY.md python_example/study.md`
- `python3` link check for Markdown links.
- `git status --short`

## Blockers / Open Questions
- None.
