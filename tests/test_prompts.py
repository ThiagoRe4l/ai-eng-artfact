import re
from datetime import datetime

from src.prompts import FUSO_CAMPO_GRANDE, WEEKDAY, build_system_prompt

# 04/11/2026 é uma quarta-feira.
FIXED_NOW = datetime(2026, 11, 4, 14, 30, tzinfo=FUSO_CAMPO_GRANDE)


def test_date_and_time_are_injected():
    prompt = build_system_prompt(FIXED_NOW)
    assert "04/11/2026 14:30" in prompt


def test_weekday_is_in_portuguese():
    prompt = build_system_prompt(FIXED_NOW)
    assert "quarta-feira, 04/11/2026 14:30" in prompt


def test_weekday_table_covers_all_days():
    # 02/11/2026 é segunda-feira; percorre a semana inteira.
    for offset, expected in enumerate(WEEKDAY):
        now = datetime(2026, 11, 2 + offset, 10, 0, tzinfo=FUSO_CAMPO_GRANDE)
        assert f"{expected}, {now:%d/%m/%Y}" in build_system_prompt(now)


def test_placeholder_is_replaced_and_no_braces_left():
    prompt = build_system_prompt(FIXED_NOW)
    assert "{" not in prompt
    assert "}" not in prompt


def test_current_context_is_last_section():
    prompt = build_system_prompt(FIXED_NOW)
    headings = re.findall(r"^# (.+)$", prompt, flags=re.MULTILINE)
    assert headings[-1] == "Contexto atual"
    assert headings.count("Contexto atual") == 1


def test_default_now_works_without_argument():
    prompt = build_system_prompt()
    assert "{" not in prompt
    assert "Data e hora atuais em Campo Grande:" in prompt
