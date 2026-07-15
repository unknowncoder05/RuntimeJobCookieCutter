# {{ cookiecutter.project_name }}

{{ cookiecutter.job_description }}

This is a CodeSwarm runtime job project. It is intentionally not a web app. The
job runs as a scheduled runtime unit and appends one JSON line per invocation to
`{{ cookiecutter.output_path }}`.

## Run Locally

```bash
python scripts/run_job.py
```

## Test

```bash
python -m py_compile scripts/run_job.py
python -m unittest discover -s tests
```

## Runtime Unit

The runtime unit is declared in `projectmaker.yml` as `{{ cookiecutter.job_key }}`.
CodeSwarm can sync it and run its `run` command on a schedule every
`{{ cookiecutter.schedule_interval_seconds }}` seconds.
