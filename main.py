import json, requests, pystyle, os, time

def get_json(invite_code):
    return requests.get(f'https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true').text

def main():
    os.system('cls')
    print('\n'*3)
    print(pystyle.Center.XCenter(pystyle.Box.Lines("Invite-Tracker")), pystyle.Colors.red)
    print('\n'*3)
    code = pystyle.Write.Input("            Invite Code -> ", pystyle.Colors.red_to_purple, interval=0.0025)
    data_ = json.loads(get_json(str(code)))
    if data_['code'] == 10006:
        print(f"", pystyle.Colors.red)
        print('        [ERROR] Invalid Guild Invite', pystyle.Colors.red)
        print(f"", pystyle.Colors.white)
        time.sleep(3)
        main()
    print(f"", pystyle.Colors.cyan)
    for key, value in data_.items():
        if str(key).lower() != "guild":
            print(f"        [{str(key).upper().replace('_', '-')}] - {value}", pystyle.Colors.cyan)
    print(f"        [GUILD-NAME] - {data_['guild']['name']}", pystyle.Colors.cyan)
    print(f"        [GUILD-ID] - {data_['guild']['id']}", pystyle.Colors.cyan)
    print(f"        [GUILD-DESC] - {data_['guild']['description']}", pystyle.Colors.cyan)
    print(f"        [GUILD-VERIF-LEVEL] - {data_['guild']['verification_level']}", pystyle.Colors.cyan)
    print(f"        [GUILD-VANITY] - {data_['guild']['vanity_url_code']}", pystyle.Colors.cyan)
    print(f"        [GUILD-BOOST-COUNT] - {data_['guild']['premium_subscription_count']}", pystyle.Colors.cyan)
    print(f"        [GUILD-NSFW] - {data_['guild']['nsfw']}", pystyle.Colors.cyan)
    print(f"        [GUILD-NSFW-LEVEL] - {data_['guild']['nsfw_level']}", pystyle.Colors.cyan)
    print(f"", pystyle.Colors.white)
    input('')
    time.sleep(1)
    main()


if __name__ == "__main__":
    main()