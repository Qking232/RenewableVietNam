# HTML Preview, Rendering & Versioning Rules

- **Internal HTML Rendering**: Always render and preview HTML documents and web interfaces directly inside Antigravity.
- **Generative UI & Embeds**: 
  - Save interactive or visual HTML pages as user-facing artifacts in the artifact directory (`UserFacing: true`).
  - Use `<agent-embed src="file:///<path>"></agent-embed>` or internal artifact side-panel previews so that the user can view and interact with the content inside the app.
- **Interactive Artifact Viewer Preference**: Always show output, previews, deliverables, visual interfaces, and interactive pages in the **Interactive Artifact Viewer** instead of opening or relying on the code editor. Whenever presenting visual results, UI, or documents, render them as user-facing artifacts (`UserFacing: true`) and embed or open them in the artifact viewer.
- **No External Browsers**: Never use OS shell commands (such as `start <file.html>`, `explorer.exe`, or external browser binaries) to open HTML files in third-party browsers unless the user explicitly asks for an external browser.
- **Version Numbering & No Deletion**:
  - Always save updates or revisions as a new file with the next incremented version number (e.g., `filename_v2`, `filename_rev1.1`) instead of overwriting or replacing the existing file.
  - Never delete any files or prior versions. All past versions must be kept and preserved intact.
