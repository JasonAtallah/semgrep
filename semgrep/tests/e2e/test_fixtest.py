import pytest

from semgrep.constants import OutputFormat
from tests.conftest import _clean_stdout


@pytest.mark.kinda_slow
def test_fixtest_test1_no_json(run_semgrep_in_tmp, snapshot):
    results, _ = run_semgrep_in_tmp(
        "rules/fixtest/test1.yaml",
        target_name="fixtest/test1.py",
        options=["--test"],
        output_format=OutputFormat.TEXT,
    )

    snapshot.assert_match(
        results,
        "output.txt",
    )


@pytest.mark.kinda_slow
def test_fixtest_test1_json(run_semgrep_in_tmp, snapshot):
    stdout, _ = run_semgrep_in_tmp(
        "rules/fixtest/test1.yaml",
        target_name="fixtest/test1.py",
        options=["--test"],
        output_format=OutputFormat.JSON,
    )
    snapshot.assert_match(stdout, "test-results.json")


@pytest.mark.kinda_slow
def test_fixtest_test2_no_json(run_semgrep_in_tmp, snapshot):
    results, _ = run_semgrep_in_tmp(
        "rules/fixtest/test2.yaml",
        target_name="fixtest/test2.py",
        options=["--test"],
        output_format=OutputFormat.TEXT,
    )

    snapshot.assert_match(
        results,
        "output.txt",
    )


@pytest.mark.kinda_slow
def test_fixtest_test2_json(run_semgrep_in_tmp, snapshot):
    stdout, _ = run_semgrep_in_tmp(
        "rules/fixtest/test2.yaml",
        target_name="fixtest/test2.py",
        options=["--test"],
        output_format=OutputFormat.JSON,
    )
    snapshot.assert_match(stdout, "test-results.json")


@pytest.mark.kinda_slow
def test_fixtest_test3_no_json(run_semgrep_in_tmp, snapshot):
    results, _ = run_semgrep_in_tmp(
        "rules/fixtest/test3.yaml",
        target_name="fixtest/test3.py",
        options=["--test"],
        output_format=OutputFormat.TEXT,
    )

    snapshot.assert_match(
        results,
        "output.txt",
    )


@pytest.mark.kinda_slow
def test_fixtest_test3_json(run_semgrep_in_tmp, snapshot):
    stdout, _ = run_semgrep_in_tmp(
        "rules/fixtest/test3.yaml",
        target_name="fixtest/test3.py",
        options=["--test"],
        output_format=OutputFormat.JSON,
    )
    snapshot.assert_match(stdout, "test-results.json")


@pytest.mark.kinda_slow
@pytest.mark.xfail(reason="depends on absolute path in output")
def test_fixtest_test4_no_json(run_semgrep_in_tmp, snapshot):
    stdout, _ = run_semgrep_in_tmp(
        "rules/fixtest/test4.yaml",
        target_name="fixtest/test4.py",
        options=["--test"],
        output_format=OutputFormat.TEXT,
        assert_exit_code=1,
    )
    snapshot.assert_match(stdout, "error.txt")


@pytest.mark.kinda_slow
@pytest.mark.xfail(reason="depends on absolute path in output")
def test_fixtest_test4_json(run_semgrep_in_tmp, snapshot):
    stdout, stderr = run_semgrep_in_tmp(
        "rules/fixtest/test4.yaml",
        target_name="fixtest/test4.py",
        options=["--test"],
        output_format=OutputFormat.JSON,
        assert_exit_code=1,
    )
    snapshot.assert_match(stderr, "error.txt")
    snapshot.assert_match(_clean_stdout(stdout), "error.json")


@pytest.mark.kinda_slow
def test_fixtest_test5_no_json(run_semgrep_in_tmp, snapshot):
    results, _ = run_semgrep_in_tmp(
        "rules/fixtest/test5.yaml",
        target_name="fixtest/test5.py",
        options=["--test"],
        output_format=OutputFormat.TEXT,
    )

    snapshot.assert_match(
        results,
        "output.txt",
    )


@pytest.mark.kinda_slow
def test_fixtest_test5_json(run_semgrep_in_tmp, snapshot):
    stdout, _ = run_semgrep_in_tmp(
        "rules/fixtest/test5.yaml",
        target_name="fixtest/test5.py",
        options=["--test"],
        output_format=OutputFormat.JSON,
    )
    snapshot.assert_match(stdout, "test-results.json")