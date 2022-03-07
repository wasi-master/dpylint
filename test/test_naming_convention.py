import dpylint
import pylint.testutils
import pylint.interfaces
import astroid


class TestNamingConventionChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = dpylint.NamingConventionChecker

    def test_misleading_client_name(self):
        assign_node= astroid.extract_node("""
        client = commands.Bot("!")
        """)

        self.checker.visit_assign(assign_node)
        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id='C9006',
                node=assign_node,
                args=()
            )
        ):
            pass

    def test_misleading_client_name_with_custom_class(self):
        assign_node= astroid.extract_node("""
        class MyBot(commands.Bot): pass
        client = MyBot("!")
        """)

        self.checker.visit_assign(assign_node)
        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id='C9006',
                node=assign_node,
                confidence=pylint.interfaces.INFERENCE,
                args=()
            )
        ):
            pass

