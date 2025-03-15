# 📊 Crypto Terminal Dashboard  

Monitor de criptomoedas em tempo real diretamente no seu terminal! Desenvolvido com Python + Textual.  

---

## ✨ Funcionalidades  

- **Preços em tempo real** de Bitcoin, Ethereum, Dogecoin e Binance Coin  
- Atualização automática a cada 10 segundos (via CoinGecko API)  
- Interface estilizada com CSS integrado  
- Grid layout responsivo  
- Tratamento robusto de erros e reconexão automática  
- Timestamp de última atualização  
- Arquitetura extensível para novas moedas  

---

## ⚙️ Pré-requisitos  

- Python 3.10+  
- Terminal moderno (Windows Terminal, iTerm2, GNOME Terminal)  

---

## 🚀 Instalação  

```bash  
# Clone o repositório  
git clone https://github.com/seu-usuario/crypto-terminal-dashboard.git  
cd crypto-terminal-dashboard  

# Crie e ative o ambiente virtual (recomendado)  
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  

# Instale as dependências  
pip install -r requirements.txt  
