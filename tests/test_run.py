"""
This module contains example tests for a Kedro project.
Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py.
"""

import pytest
from pathlib import Path
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality


class TestKedroRun:
    @pytest.mark.skip(reason="Skip default Kedro test since no pipeline is defined yet.")
    def test_kedro_run_no_pipeline(self):
        # This example test expects a pipeline run failure, since
        # the default project template contains no pipelines.
        bootstrap_project(Path.cwd())

        with pytest.raises(Exception) as excinfo:
            with KedroSession.create(project_path=Path.cwd()) as session:
                session.run()

        assert "Pipeline contains no nodes" in str(excinfo.value)
