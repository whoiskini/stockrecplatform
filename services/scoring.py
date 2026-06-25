def calculate_score(metrics):

    score = 0

    revenue_growth = metrics.get("revenue_growth", 0)
    earnings_growth = metrics.get("earnings_growth", 0)
    pe = metrics.get("pe", 999)

    # Growth

    if revenue_growth > 0.20:
        score += 20

    elif revenue_growth > 0.10:
        score += 10

    if earnings_growth > 0.20:
        score += 20

    elif earnings_growth > 0.10:
        score += 10

    # Valuation

    if pe < 15:
        score += 25

    elif pe < 25:
        score += 15

    # Quality

    if metrics.get("profit_margin", 0) > 0.15:
        score += 15

    # Momentum

    if metrics.get("price_change_52w", 0) > 0:
        score += 20

    return min(score, 100)


def recommendation(score):

    if score >= 80:
        return "STRONG BUY"

    if score >= 65:
        return "BUY"

    if score >= 50:
        return "HOLD"

    return "AVOID"
