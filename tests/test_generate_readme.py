import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import generate_readme

GROUPS = [
    "AI / Agents",
    "Security",
    "DevX",
    "OpenCode Plugins",
    "Embedded",
]


class ProjectsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        profile = yaml.safe_load((ROOT / "profile.yaml").read_text())
        cls.projects = profile["projects"]
        cls.readme = generate_readme.render(profile)

    def test_profile_has_thirteen_projects(self):
        self.assertEqual(13, len(self.projects))

    def test_projects_section_is_grouped(self):
        self.assertIn("## PROJECTS", self.readme)
        self.assertNotIn("## EXAMPLES", self.readme)
        for group in GROUPS:
            self.assertIn(f"### {group}", self.readme)

    def test_each_project_has_language_and_tech(self):
        self.assertEqual(13, self.readme.count("**Language:**"))
        self.assertEqual(13, self.readme.count("**Tech:**"))
        for project in self.projects:
            self.assertIn(f'**[{project["name"]}]({project["url"]})**', self.readme)
            self.assertIn(f'**Language:** {project["language"]}', self.readme)

    def test_private_calvin_is_absent(self):
        self.assertNotIn("calvin", self.readme.lower())


if __name__ == "__main__":
    unittest.main()
