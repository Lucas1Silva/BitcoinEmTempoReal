from textual.app import App, ComposeResult
from textual.widgets import Static, Label
from textual.containers import Container
from textual import work
import requests
import asyncio  # Importando o módulo asyncio

class CryptoDashboard(App):
    CSS = """
    Container {
        layout: grid;
        grid-size: 2;
        padding: 1;
    }
    Label {
        width: 20;
        height: 5;
        content-align: center middle;
        background: #1a1a1a;
        color: #00ff9d;
        border: round #333;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the layout of the dashboard."""
        yield Container(
            Label("Bitcoin (BTC)\nCarregando...", id="btc"),
            Label("Ethereum (ETH)\nCarregando...", id="eth"),
            Label("Dogecoin (DOGE)\nCarregando...", id="doge"),
            Label("Binance Coin (BNB)\nCarregando...", id="bnb"),
        )

    @work(exclusive=True)
    async def update_prices(self) -> None:
        """Update the cryptocurrency prices periodically."""
        coins = {
            "btc": "bitcoin",
            "eth": "ethereum",
            "doge": "dogecoin",
            "bnb": "binancecoin"
        }
        
        while True:
            for widget_id, coin in coins.items():
                try:
                    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd")
                    response.raise_for_status()
                    price = response.json()[coin]["usd"]
                    self.query_one(f"#{widget_id}", Label).update(f"{coin.upper()}\n$ {price:,.2f} 💲")
                except requests.RequestException as e:
                    self.query_one(f"#{widget_id}", Label).update(f"{coin.upper()}\nErro API ❌")
                    self.log.error(f"Failed to fetch price for {coin}: {e}")
            
            await asyncio.sleep(10)  # Atualiza a cada 10 segundos

    def on_mount(self) -> None:
        """Called when the application is mounted."""
        self.update_prices()

if __name__ == "__main__":
    CryptoDashboard().run()