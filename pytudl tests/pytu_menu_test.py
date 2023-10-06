import pytest
import pytu_menu


def test_dircreationexit(monkeypatch):
    inp = "q"
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": inp)
        with pytest.raises(SystemExit):
            pytu_menu.dir_input()


def test_linkcreationexit(monkeypatch):
    inp = "q"
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": inp)
        with pytest.raises(SystemExit):
            pytu_menu.link_input()


def test_menuexit(monkeypatch):
    inp = "q"
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": inp)
        with pytest.raises(SystemExit):
            pytu_menu.input_option(
                'https://www.youtube.com/watch?v=KXMJmKXo6Hc', '~/')
