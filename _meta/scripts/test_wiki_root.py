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
        source = Path(__file__).with_name("wiki_link_check.sh")
        script = self.repo / "_meta" / "scripts" / "wiki_link_check.sh"
        shutil.copy2(source, script)
        (self.repo / "_meta" / "lychee.toml").write_text("# fixture\n", encoding="utf-8")
        fake_home = self.base / "home"
        fake_bin = fake_home / ".local" / "bin"
        fake_bin.mkdir(parents=True)
        fake = fake_bin / "lychee"
        fake.write_text("#!/usr/bin/env bash\nprintf '%s\\n' \"$PWD\"\n", encoding="utf-8")
        fake.chmod(0o755)
        env = os.environ.copy()
        env["HOME"] = str(fake_home)
        env["OBSIDIAN_VAULT_PATH"] = str(self.env_root)

        default = subprocess.run([script], cwd=self.base, env={k: v for k, v in env.items() if k != "OBSIDIAN_VAULT_PATH"}, text=True, capture_output=True, check=True)
        from_env = subprocess.run([script], cwd=self.base, env=env, text=True, capture_output=True, check=True)
        explicit = subprocess.run([script, "--root", str(self.explicit)], cwd=self.base, env=env, text=True, capture_output=True, check=True)

        self.assertEqual(default.stdout.strip(), str(self.repo))
        self.assertEqual(from_env.stdout.strip(), str(self.env_root))
        self.assertEqual(explicit.stdout.strip(), str(self.explicit))


if __name__ == "__main__":
    unittest.main()
