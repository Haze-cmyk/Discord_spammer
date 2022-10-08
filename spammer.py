print("""
                                                        
        ('-. .-.              .-') _           
        ( OO )  /             (  OO) )
        ,--. ,--.    .---.  ,(_)----.  .-----.
        |  | |  |   / .  |  |       | /  -.   \ 
        |   .|  |  / /|  |  '--.   /  '-' _'  |
        |       | / / |  |_ (_/   /      |_  <
        |  .-.  |/  '-'    | /   /___ .-.  |  | 
        |  | |  |`----|  |-'|        |\ `-'   /
        `--' `--'     `--'  `--------' `----''
        Made BY = H4Z3(HAZE)
        Github = https://github.com/Haze-cmyk
        Owner = H4Z3
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Done :)) ")
