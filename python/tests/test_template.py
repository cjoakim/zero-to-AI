from src.os.system import System
from src.util.template import Template

# pytest -v tests/test_template.py
# Chris Joakim, 3Cloud/Cognizant, 2026


def test_template_lookup_and_rendering():
    if System.is_linux():
        pass  # TODO - diagnose the issue in Github Actions
    else:
        values = dict()
        values["group"] = "Dire Straits"
        values["artist"] = "Mark Knopfler"
        t = Template.get_template(System.pwd(), "unit_tested.txt")
        code = Template.render(t, values)
        lines = code.split("\n")
        assert len(lines) == 4
        assert lines[0] == "Header line"
        assert lines[1] == "Group: Dire Straits"
        assert lines[2] == "Artist: Mark Knopfler"
        assert lines[3] == "Last line"
