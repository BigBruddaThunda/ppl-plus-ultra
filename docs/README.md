# Docs

## GitHub Pages setup for dashboard

1. Commit `docs/dashboard/` to the default branch.
2. In GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, set:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/docs/dashboard`
4. Save and wait for Pages to publish.

The dashboard reads `docs/dashboard/data/progress.json`, which is generated from repo state by:

```bash
python scripts/build-dashboard-data.py
```
