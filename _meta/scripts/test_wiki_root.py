from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from wiki_root import resolve_root


class WikiRootResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / "repo"
        self.script = self.repo / "_meta" / "scripts" / "tool.py"
        self.script.parent.mkdir(parents=True)
        self.script.write_text("# fixture\n", encoding="utf-8")
        self.explicit = self.base / "explicit"
        self.env_root = self.base / "env"
        self.explicit.mkdir()
        self.env_root.mkdir()

    def test_priority_and_cwd_independence(self) -> None:
        env = {"OBSIDIAN_VAULT_PATH": str(self.env_root)}
        with patch("pathlib.Path.cwd", return_value=self.base / "unrelated"):
            self.assertEqual(resolve_root(self.explicit, environ=env, script_file=self.script), self.explicit)
            self.assertEqual(resolve_root(None, environ=env, script_file=self.script), self.env_root)
            self.assertEqual(resolve_root(None, environ={}, script_file=self.script), self.repo)

    def test_link_check_uses_same_priority(self) -> None:
        script = self.script.with_name("wiki_link_check.sh")
        for name in (script.name, "wiki_raw_source_urls.py", "wiki_health_check.py", "wiki_root.py"):
            shutil.copy2(Path(__file__).with_name(name), script.with_name(name))
        (self.repo / "raw").mkdir()
        (self.repo / "raw" / "source.md").write_text(
            '---\nsource_url: "https://example.org/source"\n---\n\nhttps://example.org/incidental\n',
            encoding="utf-8",
        )
        (self.repo / "_meta" / "lychee.toml").write_text("# fixture\n", encoding="utf-8")
        (self.repo / "raw" / "duplicates.md").write_text(
            "---\nsource_url: 'https://example.org/source'\n---\n", encoding="utf-8",
        )
        (self.repo / "raw" / "non-http.md").write_text(
            "---\nsource_url: file:///example\n---\n", encoding="utf-8",
        )
        fake_home = self.base / "home"
        fake_bin = fake_home / ".local" / "bin"
        fake_bin.mkdir(parents=True)
        fake = fake_bin / "lychee"
        fake.write_text("#!/usr/bin/env bash\nprintf '%s\\n' \"$PWD\"\ncat\n", encoding="utf-8")
        fake.chmod(0o755)
        env = os.environ.copy()
        env["HOME"] = str(fake_home)
        env["OBSIDIAN_VAULT_PATH"] = str(self.env_root)

        default = subprocess.run([script], cwd=self.base, env={k: v for k, v in env.items() if k != "OBSIDIAN_VAULT_PATH"}, text=True, capture_output=True, check=True)
        from_env = subprocess.run([script], cwd=self.base, env=env, text=True, capture_output=True, check=True)
        explicit = subprocess.run([script, "--root", str(self.explicit)], cwd=self.base, env=env, text=True, capture_output=True, check=True)

        self.assertEqual(default.stdout.splitlines(), [str(self.repo), "https://example.org/source"])
        self.assertEqual(from_env.stdout.strip(), str(self.env_root))
        self.assertEqual(explicit.stdout.strip(), str(self.explicit))


if __name__ == "__main__":
    unittest.main()
