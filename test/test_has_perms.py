import dpylint
import pylint.testutils
import astroid


class TestHasPermissionsChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = dpylint.HasPermissionsChecker

    def test_invalid_permission_value(self):
        deco_node, func_node = astroid.extract_node("""
        @commands.command()
        @commands.has_permissions(manage_messages="a") #@
        async def test(ctx): #@
            await ctx.send("hi")
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='W9002',
                node=deco_node,
                args='a'
            )
        ):
            pass

    def test_invalid_permission_name(self):
        deco_node, func_node = astroid.extract_node("""
        @commands.command()
        @commands.has_permissions(manage_server=True) #@
        async def test(ctx): #@
            await ctx.send("hi")
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='E9001',
                node=deco_node,
                args=('manage_server', 'manage_guild')
            )
        ):
            pass

    def test_no_permission_passed(self):
        deco_node, func_node = astroid.extract_node("""
        @commands.command()
        @commands.has_permissions() #@
        async def test(ctx): #@
            await ctx.send("hi")
        """)

        self.checker.visit_asyncfunctiondef(func_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='W9003',
                node=deco_node,
            )
        ):
            pass
