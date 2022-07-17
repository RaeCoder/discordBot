import discord
import asyncio

#auto generate a bot controller role
#take variable inputs
#music bot

#https://discordpy.readthedocs.io/en/latest/index.html

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {}".format(client.user.id))

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
        await msg.channel.send("Exiting")
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
        await msg.channel.send("The name of the user's top role is: {}".format(msg.author.top_role.name))
        await asyncio.sleep(0.5)
        await msg.channel.send("User is administrator: {}".format(msg.author.top_role.permissions.administrator))

    if msg.content.startswith("$makerole"):
        await msg.guild.create_role(name="yo", permissions=msg.author.top_role.permissions.all())
        await msg.channel.send("Successfully made role \"yo\"")

    if msg.content.startswith("$giverole"):
        rawMessageRoleData = msg.raw_role_mentions
        rawMessageMemberData = msg.raw_mentions
        try:
            lolkappa = rawMessageRoleData[0]
            targetRole = msg.guild.get_role(rawMessageRoleData[0])
        except:
            targetRole = None
        try:
            lolkappa = rawMessageMemberData[0]
            targetMember = msg.guild.get_member(rawMessageMemberData[0])
        except:
            targetMember = None
        if targetRole == None:
            await msg.channel.send("Failed to find Role")
        if targetMember == None:
            await msg.channel.send("Failed to find User")
        elif targetRole != None and targetMember != None:
            await msg.channel.send("Name: {} || Role: {}".format(targetMember.name, targetRole.name))
            await targetMember.add_roles(targetRole, atomic=True)
        


        

#@client.event
#async def on_typing(chnl, usr, tme):
#
#    if usr.name != client.user.display_name:
#        async with chnl.typing():
#            await asyncio.sleep(2)
#        await chnl.send("I see you typing there {}".format(usr.name))


client.run("")

