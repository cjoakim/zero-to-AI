from src.util.uv_parser import UVParser

# pytest -v tests/test_uvparser.py
# Chris Joakim, 3Cloud/Cognizant, 2026


def test_parse_pip_list():
    uvp = UVParser()
    data = uvp.parse_pip_list()
    assert isinstance(data, dict)
    names = sorted(data.keys())
    assert names[0] == "agent-framework"
    assert names[-1] == "zipp"
    assert data["m26"] == "0.3.2"
    assert len(data) > 280
    assert len(data) < 300

def test_parse_tree():
    uvp = UVParser()
    data = uvp.parse_tree()
    assert isinstance(data, list)

    assert len(data) > 630
    assert len(data) < 650
