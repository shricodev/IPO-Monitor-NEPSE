# Author: Shrijal Achärya (r3alix01)
# Date: 2022/04/22
# Usage: Read The Description ;)


import sys
import time
import requests
from bs4 import BeautifulSoup
from plyer import notification


def notifier(shareName, sharePrice, changeHolder):
    # Use the module to notify via desktop notification.
    notification.notify(
        title=f"SHARE: {shareName}",
        message=f"The price has started to decrease with {changeHolder[0].get_text()}. Current price: {sharePrice}",
        timeout=15,
    )

    # Create and utilize Discord WebHook
    try:
        from discord_webhook import DiscordEmbed, DiscordWebhook
        from decouple import config

        webHookUrl = config('WEB_HOOK_URL')
        userName = config('USERNAME')

        contents = f"The price of IPO of {shareName} has started to decrease with {changeHolder[0].get_text()}. Current price: {sharePrice}"
        webhook = DiscordWebhook(url=webHookUrl, username=userName, content=contents)
        # It embeds the data wit TITLE.
        embed = DiscordEmbed(title="**The Data is taken from merolagani.com**", color=242424)
        embed.set_author(name="Shrijal Acharya", url=f"https://github.com/r3alix01", icon_url="https://user-images.githubusercontent.com/76906722/164422105-3acc12ef-4014-406e-8ca1-2bd996974ddc.jpg")
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()

    except ImportError:
        print("Make sure to download all the dependencies from requirements.txt")

    except Exception as e:
        print("Unexpected Error Occured Could Not create a Discord Webhook.")


def main():
    print("\n" + "*"*30)
    print("IPO Price Checker NEPSE.")
    print("*"*30 + "\n")
    shareName = input("Enter the short name of the share to check: ").upper()

    if shareName == "":
        print("Invalid Input!!")
        # Exits with a status code of 1.
        sys.exit(1)

    try:
        shareUrl = "https://merolagani.com/CompanyDetail.aspx" + f"?symbol={shareName}"
        # Counter Variable
        counter = 1

        while True:
            getRequest = requests.get(shareUrl)
            # This holds all the HTML content of the site.
            contents = getRequest.content
            # It parses the HTML in a proper way.
            soup = BeautifulSoup(contents, "html.parser")
            # fINDS THE table with id accordion
            tableData = soup.find('table', id="accordion")
            # Finds the table with a tag with id of "ctl00_ContentPlaceHolder1_CompanyDetail1_lblChange"
            changeHolder = tableData.select('#ctl00_ContentPlaceHolder1_CompanyDetail1_lblChange')
            # Current Price Holder
            priceHolder = tableData.select('#ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice')
            # It holds the numeric value of the percentage change without %.
            percentChange = (changeHolder[0].get_text()).split(" ")
            price = priceHolder[0].get_text()

            if float(percentChange[0]) < 0:
                print(f"{counter}) The price of the IPO -> {shareName} has started to decrease with {changeHolder[0].get_text()}. Current price: {price}")
                notifier(shareName, price, changeHolder)
                # Sleep the program for 3 minutes. This will act as a delay to our program.
                time.sleep(3*60)
                counter += 1
            else:
                # If the price is not decreasing It does nothing.
                time.sleep(3*60)

    except KeyboardInterrupt:
        print("Bye Bye!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
