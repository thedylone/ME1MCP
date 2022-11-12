from main import SessionRunner
from os.path import dirname, join
import pytest

FXT_DIR = join(dirname(__file__), "fixtures/test_root/")


class TestMain:
    session_runner = SessionRunner()

    def test_getSessions(self):
        """Test getSesssions method."""
        sessions = self.session_runner.getSessions(FXT_DIR)
        assert sessions == ["session1", "session2"]

    def test_validateSession(self):
        """Test validateSession method."""
        # test valid session
        assert SessionRunner.validateSession("session1", FXT_DIR) is True
        # test invalid session
        with pytest.raises(ValueError):
            self.session_runner.validateSession("session3", FXT_DIR)

    def test_validateSessionDecorator(self):
        """Test validateSessionDecorator method."""

        @SessionRunner.validateSessionDecorator
        def test(self, session, dir=None):
            return True

        # test valid session
        assert test(SessionRunner, "session1", FXT_DIR) is True
        # test invalid session
        with pytest.raises(ValueError):
            test(SessionRunner, "session3", FXT_DIR)

    def test_validateInput(self):
        """Test validateInput method."""
        # test valid input
        assert SessionRunner.validateInput(["1", "2"], FXT_DIR) is True
        # test invalid input
        with pytest.raises(ValueError):
            SessionRunner.validateInput(["3"], FXT_DIR)
        # test all input
        assert SessionRunner.validateInput(["all"], FXT_DIR) is True
        # test empty input
        with pytest.raises(ValueError):
            SessionRunner.validateInput([""], FXT_DIR)

    def test_validateInputDecorator(self):
        """Test validateInputDecorator method."""

        @SessionRunner.validateInputDecorator
        def test(self, inputs, dir=None):
            return True

        # test valid input
        assert test(SessionRunner, ["1", "2"], FXT_DIR) is True
        # test invalid input
        with pytest.raises(ValueError):
            test(SessionRunner, ["3"], FXT_DIR)
        # test all input
        assert test(SessionRunner, ["all"], FXT_DIR) is True
        # test empty input
        with pytest.raises(ValueError):
            test(SessionRunner, [""], FXT_DIR)

    def test_runSession(self, capsys):
        """Test _runSession method."""
        # test valid input
        self.session_runner._runSession("session_test", __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # # test invalid input
        with pytest.raises(ValueError):
            self.session_runner._runSession("session3", __file__)

    def test_runAllSessions(self, capsys):
        """Test runAllSessions method."""
        self.session_runner.runAllSessions(__file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"

    def test_runSessionInput(self, capsys):
        """Test runSessionInput method."""
        # test valid input
        self.session_runner.runSessionInput(["session_test"], __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid input
        with pytest.raises(ValueError):
            self.session_runner.runSessionInput(["3"], __file__)
        # test all input
        self.session_runner.runSessionInput(["all"], __file__)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test empty input
        with pytest.raises(ValueError):
            self.session_runner.runSessionInput([""], __file__)

    def test_userSelect(self, monkeypatch, capsys):
        """Test userSelect method."""
        # test valid integer input
        monkeypatch.setattr("builtins.input", lambda _: "1")
        self.session_runner.userSelect(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid integer input
        monkeypatch.setattr("builtins.input", lambda _: "3")
        with pytest.raises(ValueError):
            self.session_runner.userSelect(file=__file__, debug=True)
        # test valid string input
        monkeypatch.setattr("builtins.input", lambda _: "session_test")
        self.session_runner.userSelect(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test invalid string input
        monkeypatch.setattr("builtins.input", lambda _: "session3")
        with pytest.raises(ValueError):
            self.session_runner.userSelect(file=__file__, debug=True)
        # test all input
        monkeypatch.setattr("builtins.input", lambda _: "all")
        self.session_runner.userSelect(file=__file__, debug=True)
        capture = capsys.readouterr()
        assert capture.out == "test\n\n\n"
        # test empty input
        monkeypatch.setattr("builtins.input", lambda _: "")
        with pytest.raises(ValueError):
            self.session_runner.userSelect(file=__file__, debug=True)
