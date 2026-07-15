# RuntimeJobCookieCutter

A CodeSwarm cookiecutter template for non-web scheduled jobs, one-off scripts,
small automation tasks, CLIs, and API polling jobs.

The generated repository uses the runtime-units manifest shape in
`projectmaker.yml`. It does not define a public web service, Docker Compose
route, Traefik labels, DNS, or HTTP health check.

## Requirements

```bash
pip install cookiecutter
```

## Usage

```bash
cookiecutter /path/to/RuntimeJobCookieCutter
```

## Template Variables

| Variable | Default | Description |
|---|---|---|
| `project_name` | Runtime Job | Human-readable project name |
| `project_slug` | `runtime_job` | Generated directory/package slug |
| `project_slug_dashed` | `runtime-job` | Runtime unit key friendly slug |
| `job_name` | `project_name` | Runtime unit display name |
| `job_key` | `project_slug_dashed` | Runtime unit key |
| `job_description` | A scheduled Python runtime job. | README and metadata description |
| `api_url` | Open Notify ISS API | API URL called by the example job |
| `output_path` | data/runtime_events.jsonl | JSONL output path |
| `schedule_interval_seconds` | 60 | Runtime schedule interval |

## Generated Structure

```text
<project_slug>/
├── projectmaker.yml
├── README.md
├── pyproject.toml
├── scripts/
│   └── run_job.py
├── tests/
│   └── test_run_job.py
└── data/
    └── .gitkeep
```

## CodeSwarm Runtime

After this repo is attached to a CodeSwarm project, sync runtime units from the
manifest. The runtime scheduler can then run the `run` command every configured
interval and persist stdout/stderr on `RuntimeRun`.
