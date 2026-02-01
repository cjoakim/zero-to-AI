import os
import pytest

from src.os.env import Env
from src.os.system import System

# pytest -v tests/test_system.py
# Chris Joakim, 3Cloud/Cognizant, 2026


# This method runs once at the beginning of this test module.
@pytest.fixture(scope="session", autouse=True)
def setup_before_all_tests():
    Env.set_unit_testing_environment()


def test_platform():
    platform = System.platform()
    print("platform is: {}".format(platform))

    if platform.startswith("win"):
        assert System.is_windows() is True
        assert System.is_mac() is False
        assert System.is_linux() is False
    elif "darwin" in platform:
        assert System.is_windows() is False
        assert System.is_mac() is True
        assert System.is_linux() is False
    elif "linux" in platform:
        assert System.is_windows() is False
        assert System.is_mac() is False
        assert System.is_linux() is True
    else:
        assert False, "Unknown platform: {}".format(platform)


def test_github_actions_env():
    if "GITHUB_ACTIONS_ENV" in os.environ:
        assert os.environ["GITHUB_ACTIONS_ENV"] == "x"
        assert System.is_linux() is True


def test_cpu_count():
    n = System.cpu_count()
    assert isinstance(n, int)
    assert (n > 0) and (n <= 32)


def test_cwd():
    s = System.cwd()
    assert isinstance(s, str)
    assert s.endswith("python")


def test_pwd():
    s = System.cwd()
    assert isinstance(s, str)
    assert s.endswith("python")


def test_hostname():
    host = System.hostname()  # 'Chriss-Mac-Studio.local'
    assert isinstance(host, str)
    assert len(host) > 10
    assert len(host) < 40


def test_pid():
    n = System.pid()
    assert isinstance(n, int)
    assert n > 1024


def test_process_name():
    n = System.process_name()
    assert isinstance(n, str)
    assert n.lower() in ["python", "python.exe", "pytest"]
