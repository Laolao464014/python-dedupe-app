from collections import defaultdict
from typing import List


def dedupe_header(columns: List[str]) -> List[str]:
    """
    Make header column names unique by appending numeric suffixes to duplicates.
    Rules:
    - The first occurrence of a name is kept as-is.
    - The 2nd, 3rd, ... occurrences of the same name get ".1", ".2", ... appended.
      (This mirrors how tools like pandas disambiguate duplicate column labels.)
    - Order is preserved exactly as given.
    - Input is a list of strings (column names); output is a same-length list.
    Example:
        ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1
    return result


def additional_functionality_example():
    """
    示例附加功能：提供统计信息
    """
    return "This is additional functionality for demonstration"


def get_duplicate_stats(columns: List[str]) -> dict:
    """
    统计重复列名信息
    """
    from collections import defaultdict
    stats = defaultdict(int)
    for col in columns:
        stats[col] += 1

    duplicate_stats = {k: v for k, v in stats.items() if v > 1}
    return {
        "total_columns": len(columns),
        "unique_columns": len(stats),
        "duplicate_columns": duplicate_stats,
        "duplicate_count": len(duplicate_stats)
    }


if __name__ == "__main__":
    # 示例用法
    test_columns = ["id", "name", "id", "name", "name", "age"]
    result = dedupe_header(test_columns)
    stats = get_duplicate_stats(test_columns)

    print("原始列名:", test_columns)
    print("去重后列名:", result)
    print("统计信息:", stats)
    print("附加功能:", additional_functionality_example())