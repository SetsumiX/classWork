def create_card(stats, name):
    t = [f"* {key.ljust(8)}: {str(val).rjust(2)} *" for key, val in stats.items() if key not in {"level", "score", "spec"}]
    card_lines = [
        f"****--{name}--*****",
        "*              *",
        *t,
        "*              *",
        "****************",
    ]
    return card_lines