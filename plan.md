# VS Code C# Dev Kit Pico SDK Warning Plan

## Target Outcome
- Stop C# tooling from scanning vendor Pico SDK / lwIP legacy `.csproj` files in this study workspace.
- Keep source code and SDK files unchanged.

## Success Criteria
- Workspace settings exclude Pico SDK dependency paths from VS Code file search/watch and C# project discovery.
- Existing C/C++ and CMake settings remain intact.
- JSON settings validate.

## Relevant Files
- Modify: `.vscode/settings.json`
- Modify: `plan.md`

## Implementation Checklist
- [x] Inspect current VS Code settings and C# extension settings.
- [x] Confirm the logged `.csproj` files are vendor legacy .NET Framework projects, not study source.
- [x] Add narrow workspace excludes for `pico/deps` and `embedded/pico/deps`.
- [x] Validate JSON and summarize restart/reload step.

## Validation Checks
- `python3 -m json.tool .vscode/settings.json`
- `git diff -- .vscode/settings.json plan.md`

## Blockers / Open Questions
- The exact logged path `pico/deps/...` is not present in the current workspace. Current repo has `embedded/pico/deps/pico-sdk`; both path shapes will be excluded.
