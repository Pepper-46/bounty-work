# Somnia dashboard data patch

Nine Somnia CoinGecko/CoinMarketCap analytics listing `actionButtons` cells have verified chain-specific dashboard URLs and retain provider pricing links. Prepared 2026-10-07; `patch --dry-run` and CSV/JSON structural checks passed locally. No upstream PR or reward claimed.

Source targets: `listings/specific-networks/somnia/analytics.csv` at upstream blob `b29a8e6fb031ed963b5802414ad24d842e9db099`.

CoinGecko: https://www.coingecko.com/en/coins/somnia
CoinMarketCap: https://coinmarketcap.com/currencies/somnia/

Integration policy blocked the write to `Pepper-46/chain-love:data/somnia-market-dashboards`; prepared patch remains local.
