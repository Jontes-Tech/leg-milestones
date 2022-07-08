# Sorry for the ugly code.
import discord
import requests
with open('../discord_token.secret', 'r') as f:
    token = str(f.readline())
intents = discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print("logged in")
    for guild in client.guilds:
        print(guild)
        mem = guild.members
        for user in mem:
            if user.bot == False:
                uid = user.id
                av = user.avatar_url
                av = str(av)
                if av == 'None':
                    pass
                else:
                    av = av.replace("?size=1024","?size=64")
                    fname = str(uid) + '.png'
                    print(av)
                    r = requests.get(av)
                    if av.startswith("https://cdn.discordapp.com/avatars/"):
                        open("custom/"+fname,'wb').write(r.content)
                    elif av.startswith("https://cdn.discordapp.com/embed/avatars/"):
                        open("defaults/"+fname,'wb').write(r.content)
                    else:
                        print("Error")
    print('finished downloading - you might wanna run mogrify -resize 64x64 *.png in the defaults directory')
client.run(token)