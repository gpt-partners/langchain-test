def test_tools_bot():
    from src.tools_bot import tool_bot

    t = tool_bot()
    assert t == 1
