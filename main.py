import discord
from bot_logic import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$saluda'):
        await message.channel.send("Hola")
    elif message.content.startswith('$bot_hacme_un_pastel'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$que es este server'):
        await message.channel.send('es para estar juntos (:')
    elif message.content.startswith('$quien_creo_este_server'):
        await message.channel.send("el_rey_potato.")
    elif message.content.startswith('$me estan asiendo buling'):
        await message.channel.send("gracias por informarnos te ayudaremos cuando posible (:")
    elif message.content.startswith('$puedo jugar minecraft?'):
        await message.channel.send("si!,si puedes jugarlo") 
    elif message.content.startswith('$hola podemos hablar'):
        await message.channel.send("si!(:")
    elif message.content.startswith('$manda un emoji'):
        await message.channel.send("\U0001f642")              
        

                
    else:
        await message.channel.send("que dijiste?")

client.run("")