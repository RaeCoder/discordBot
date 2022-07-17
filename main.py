import discord
import asyncio

#auto generate a bot controller role
#take variable inputs
#music bot

#https://discordpy.readthedocs.io/en/latest/index.html

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {}".format(client.user))

@client.event
async def on_message(msg):

    def trueReturn(m):
        return True

    if msg.author == client.user:
        return
    
    if msg.content.startswith("$hello"):
        await msg.channel.send("Hello {}!".format(msg.author))

    if msg.content.startswith("$print"):
        await msg.channel.send(msg.content)

    if msg.content.startswith("$exit"):
        await client.close()

    if msg.content.startswith("$delete-some"):
        if msg.author.top_role.permissions.administrator or msg.author.top_role.permissions.manage_messages:
            try:
                count = int(msg.content[13:])
                await msg.channel.purge(limit=count+1, check=trueReturn)
            except:
                await msg.channel.send("\"$delete-some [number]\" is the correct format")
                await asyncio.sleep(0.5)
                await msg.channel.send(msg.content[13:])
        else:
            await msg.channel.send("manage-messages permission required")

    if msg.content.startswith("$roles"):
        await msg.channel.send("All roles are: {}".format(msg.author.roles))
        await asyncio.sleep(0.5)
        await msg.channel.send("The name of the top role is: {}".format(msg.author.top_role.name))
        await asyncio.sleep(0.5)
        await msg.channel.send("User is administrator: {}".format(msg.author.top_role.permissions.administrator))

    if msg.content.startswith("$makerole"):
        await msg.guild.create_role(name="yo", permissions=msg.author.top_role.permissions.all())

    if msg.content.startswith("$giverole"):
    
        targetID = msg.raw_mentions
        targetMember = msg.guild.get_member(targetID[0])
        if targetMember == None:
            await msg.channel.send("Failed to find user")
        else:
            await msg.channel.send(targetMember.name)


        

#@client.event
#async def on_typing(chnl, usr, tme):
#
#    if usr.name != client.user.display_name:
#        async with chnl.typing():
#            await asyncio.sleep(2)
#        await chnl.send("I see you typing there {}".format(usr.name))


client.run("")

