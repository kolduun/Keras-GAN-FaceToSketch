from backend.cliobot import run_clio_telegram_bot

if __name__ == "__main__":
    bot1 = run_clio_telegram_bot()
    bot2 = run_clio_telegram_bot()
    bot3 = run_clio_telegram_bot()
    print(bot1==bot2==bot3)