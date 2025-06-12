import pytest
from project import ask_to_continue
import builtins


def test_continue_yes(monkeypatch):
    # simulate user input: "yes"
    monkeypatch.setattr(builtins, "input", lambda _: "yes")
    result = ask_to_continue("Alice")
    assert result is True


def test_continue_no(monkeypatch):
    # simulate user input: "n"
    monkeypatch.setattr(builtins, "input", lambda _: "n")
    with pytest.raises(SystemExit) as exc_info:
        ask_to_continue("Bob")
    assert exc_info.value.code == 0


def test_invalid_then_valid(monkeypatch, mocker):
    # simulate user inputs: "maybe", then "yes"
    responses = iter(["maybe", "yes"])
    monkeypatch.setattr(builtins, "input", lambda _: next(responses))

    # optionally mock `show_box` to avoid printing during test
    mock_show_box = mocker.patch("project.show_box")
    result = ask_to_continue("Carol")
    assert result is True

    # confirm that an invalid warning was shown
    mock_show_box.assert_any_call("Invalid input!", "Please enter 'Yes' or 'No'.")
