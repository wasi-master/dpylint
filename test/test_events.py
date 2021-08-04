import dpylint
import pylint.testutils
import astroid

class TestEvents(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = dpylint.EventsChecker

    def test_invalid_event_name_in_func_with_listener(self):
        func_node = astroid.extract_node("""
        @commands.Cog.listener()
        async def on_guld_jon(ctx): #@
            return ctx
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='E9004',
                node=func_node,
                args=('on_guld_jon', 'on_guild_join')
            )
        ):
            pass

    def test_invalid_event_name_in_listener_with_listener(self):
        deco_node, func_node = astroid.extract_node("""
        @commands.Cog.listener("on_tpying") #@
        async def test(ctx): #@
            return ctx
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='E9004',
                node=deco_node.nodes[0],
                args=('on_tpying', 'on_typing')
            )
        ):
            pass

    def test_invalid_event_params_with_listener_with_event_name_in_func(self):
        func_node = astroid.extract_node("""
        @commands.Cog.listener()
        async def on_message(message, user): #@
            return message, user
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='E9005',
                node=func_node,
                args=('on_message', '(message, user)', '(message)')
            )
        ):
            pass

    def test_invalid_event_params_with_listener_with_event_name_in_listener(self):
        func_node = astroid.extract_node("""
        @commands.Cog.listener("on_ready")
        async def test(ctx):
            return ctx
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='E9005',
                node=func_node,
                args=('on_ready', '(ctx)', '()')
            )
        ):
            pass
