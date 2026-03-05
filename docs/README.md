# Docs

## GitHub Pages setup for dashboard

1. Commit `docs/dashboard/` to the default branch.
2. In GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, set:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/docs`
4. Save and wait for Pages to publish.

After publish, open `/dashboard/` under your site URL (for example,
`https://<org-or-user>.github.io/<repo>/dashboard/`).

The dashboard reads `docs/dashboard/data/progress.json`, which is generated from repo state by:

```bash
python scripts/build-dashboard-data.py
```
