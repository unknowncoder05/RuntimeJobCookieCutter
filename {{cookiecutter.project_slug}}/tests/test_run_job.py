import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import run_job


class RuntimeJobTests(unittest.TestCase):
    def test_build_record_includes_payload(self):
        record = run_job.build_record({"message": "success"})

        self.assertEqual(record["payload"]["message"], "success")
        self.assertIn("checked_at", record)

    def test_append_jsonl_writes_one_line(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "data" / "events.jsonl"
            run_job.append_jsonl({"ok": True}, str(output))

            lines = output.read_text(encoding="utf-8").splitlines()

        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0]), {"ok": True})

    def test_main_fetches_and_appends(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "events.jsonl"
            with patch.object(run_job, "fetch_json", return_value={"latitude": "1", "longitude": "2"}):
                with patch.dict("os.environ", {"JOB_OUTPUT_PATH": str(output)}):
                    run_job.main()

            record = json.loads(output.read_text(encoding="utf-8").splitlines()[0])

        self.assertEqual(record["payload"]["latitude"], "1")
        self.assertEqual(record["payload"]["longitude"], "2")


if __name__ == "__main__":
    unittest.main()
