# Runtime Job Workflows

## Local Check

```bash
python -m py_compile scripts/run_job.py
python -m unittest discover -s tests
```

## Run Once

```bash
python scripts/run_job.py
```

The script appends one JSON object per line to the configured output file.

## CodeSwarm Runtime

1. Attach the generated repository to a CodeSwarm project.
2. Sync runtime units from `projectmaker.yml`.
3. Enable the generated schedule.
4. Inspect `RuntimeRun` records and output logs from the Runtime page or API.
