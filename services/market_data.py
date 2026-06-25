import yfinance as yf


def get_stock_metrics(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "ticker": ticker,
        "name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe": info.get("trailingPE"),
        "revenue_growth": info.get("revenueGrowth", 0),
        "earnings_growth": info.get("earningsGrowth", 0),
        "profit_margin": info.get("profitMargins", 0),
        "target_price": info.get("targetMeanPrice"),
        "currency": info.get("currency")
    }
