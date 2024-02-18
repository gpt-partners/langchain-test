from unittest.mock import patch


def test_simple_bot():
    with patch("src.simple_bot.ChatOpenAI.invoke") as mock_invoke:
        from src.simple_bot import answer

        mock_invoke.return_value = "This is the answer"
        prospct = "Apple"
        company = "Microsoft"

        res = answer(company, prospct)
        assert res == ["This is the answer"]
