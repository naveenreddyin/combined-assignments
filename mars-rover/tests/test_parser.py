import pytest

from unittest.mock import patch, mock_open

from utils.parser import is_string, parse, parse_semicolon


def test_parse_without_file():
    with pytest.raises(TypeError) as _:
        parse()


def test_parse_without_non_file_param():
    with pytest.raises(SystemExit) as _:
        parse("sdfsdf")


def test_parse_with_mock_file_param():
    file_content_mock = """Plateau:5 5
                        Rover1 Landing:1 2 N
                        Rover1 Instructions:LMLMLMLMM
                        Rover2 Landing:3 3 E
                        Rover2 Instructions:MMRMMRMRRM"""
    fake_file_path = "file/path/mock"
    with patch(
        "builtins.open",
        new=mock_open(read_data=file_content_mock),
    ) as _file:
        parse(fake_file_path)
        _file.assert_called_once_with(fake_file_path, "r")


def test_if_string_with_wrong_input():
    assert is_string(1) == False


def test_if_string_with_right_input():
    assert is_string("hello") == True


def test_extract_through_semicolor():
    assert len(parse_semicolon("Plateau:5 5")) == 2
