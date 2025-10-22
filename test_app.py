import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe_header, additional_functionality_example, get_duplicate_stats


def test_unique_columns():
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]


def test_duplicate_columns():
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]


def test_mixed_columns():
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected


def test_empty_list():
    assert dedupe_header([]) == []


def test_special_characters():
    cols = ["col-1", "col-1", "col_2", "col_2"]
    expected = ["col-1", "col-1.1", "col_2", "col_2.1"]
    assert dedupe_header(cols) == expected


def test_additional_functionality():
    assert additional_functionality_example() == "This is additional functionality for demonstration"

    # 测试统计功能
    columns = ["id", "name", "id", "age", "name"]
    stats = get_duplicate_stats(columns)

    assert stats["total_columns"] == 5
    assert stats["unique_columns"] == 3
    assert stats["duplicate_count"] == 2
    assert stats["duplicate_columns"]["id"] == 2
    assert stats["duplicate_columns"]["name"] == 2