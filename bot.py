"""
🚽 Skibiditopia 🚽 Brainrot Notifier — FINAL v3

ALL IMAGES: Direct PNG URLs (no revision/latest redirect)
SLOW TIMINGS: Farmer 15-30s, Highlights 60-120s, Peak 120-240s, Godly 3600-5400s, Stalk 30-60s
"""

import discord, asyncio, random, os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
FOOTER = ".GG/skibiditopia"
TITLE = "🚽 SIIBIDITOPIA FOUND"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)

# Direct PNG URLs — NO redirect, cb= timestamp as query parameter
URLS = {
    "Garama and Madundung":    "https://static.wikia.nocookie.net/stealabr/images/e/ee/Garamadundung.png/revision/latest?cb=20250816022557",
    "Capitano Moby":           "https://static.wikia.nocookie.net/stealabr/images/b/be/Capitano_Moby.png/revision/latest?cb=20260428162232",
    "Burguro and Fryuro":      "https://static.wikia.nocookie.net/stealabr/images/6/65/Burguro-And-Fryuro.png/revision/latest?cb=20251007133840",
    "Cash or Card":            "https://static.wikia.nocookie.net/stealabr/images/2/21/Cash_or_Card.png/revision/latest?cb=20260215231300",
    "Gym Bros":                "https://static.wikia.nocookie.net/stealabr/images/b/b7/Gym_Bros.png/revision/latest?cb=20260419152519",
    "Cerberus":                "https://static.wikia.nocookie.net/stealabr/images/4/45/Cerberus.png/revision/latest?cb=20260217181804",
    "Popcuru and Fizzuru":     "https://static.wikia.nocookie.net/stealabr/images/8/82/Popcuru_and_Fizzuru.png/revision/latest?cb=20260425231747",
    "Dragon Cannelloni":       "https://static.wikia.nocookie.net/stealabr/images/a/a5/Dragon_Cannelloni.png/revision/latest?cb=20260417152622",
    "Hydra Dragon Cannelloni": "https://static.wikia.nocookie.net/stealabr/images/e/ee/Hydra_Dragon_Cannelloni.png/revision/latest?cb=20260207220000",
    "Ketupat Bros":            "https://static.wikia.nocookie.net/stealabr/images/4/4d/Ketupat_Bros.png/revision/latest?cb=20260207220106",
    "La Casa Boo":             "https://static.wikia.nocookie.net/stealabr/images/d/de/Casa_Booo.png/revision/latest?cb=20251220094233",
    "Foxini Lanternini":       "https://static.wikia.nocookie.net/stealabr/images/4/41/Foxini_Lanternini.png/revision/latest?cb=20260417153743",
    "Strawberry Elephant":     "https://static.wikia.nocookie.net/stealabr/images/5/58/Strawberryelephant.png/revision/latest?cb=20260317001745",
    "Dragon Gingerini":        "https://static.wikia.nocookie.net/stealabr/images/3/3a/DragonGingerini.png/revision/latest?cb=20251221003419",
    "Meowl":                   "https://static.wikia.nocookie.net/stealabr/images/b/b8/Clear_background_clear_meowl_image.png/revision/latest?cb=20251022133154",
    "Cookie and Milki":        "https://static.wikia.nocookie.net/stealabr/images/9/96/Cooki_and_Milki.png/revision/latest?cb=20260417153501",
    "Reinito Sleighito":       "https://static.wikia.nocookie.net/stealabr/images/c/ca/Reinito_Sleighito.png/revision/latest?cb=20260626000632",
    "Fragrama and Chocrama":   "https://static.wikia.nocookie.net/stealabr/images/5/56/Fragrama.png/revision/latest?cb=20251109011733",
    "Rosey and Teddy":         "https://static.wikia.nocookie.net/stealabr/images/9/9b/Rosey_and_Teddy.png/revision/latest?cb=20260208175726",
    "Skibidi Toilet":          "https://static.wikia.nocookie.net/stealabr/images/a/a7/Default_Skibidi_Toilet.png/revision/latest?cb=20260528092806",
    "John Pork":               "https://static.wikia.nocookie.net/stealabr/images/d/d2/John_Pork.png/revision/latest?cb=20260502233229",
}
FALLBACK = "https://static.wikia.nocookie.net/stealabr/images/e/ee/Garamadundung.png/revision/latest?cb=20250816022557"

def img(name):
    for key, url in URLS.items():
        if key.lower() in name.lower():
            return url
    return FALLBACK

# ═══ DATA ═══
FL_garama = [("Garama and Madundung","🧬","🔥",50,875),("Garama and Madundung","🧬","🎁",50,875),("Garama and Madundung","🧬","🌸",50,875),("Garama and Madundung","🧬","◻",50,875),("Garama and Madundung","🧬","🪙",50,875)]
FL_rare = [("Capitano Moby","🐋","◻",100,350),("Capitano Moby","🐋","💎",100,350)]
FL_rest = [("Burguro and Fryuro","🍔","🔥",80,250),("Cash or Card","💳","🔴",60,200),("Gym Bros","💪","💎",40,150),("Cookie and Milki","🍪","🎁",20,90),("Cerberus","🐕","🔥",80,180),("Reinito Sleighito","🦌","🧊",70,160),("Popcuru and Fizzuru","🥤","◻",60,140),("Fragrama and Chocrama","🍓","🌸",50,130)]

HL_rare = [("Dragon Cannelloni","🐉","💎",500,2500)]
HL_rest = [("Fragrama and Chocrama","🍓","🌸",50,130),("Fragrama and Chocrama","🍓","🎁",50,130),("Popcuru and Fizzuru","🥤","◻",60,140),("Reinito Sleighito","🦌","🧊",70,160),("Cerberus","🐕","🔥",80,180),("Cookie and Milki","🍪","🎁",20,90),("Gym Bros","💪","💎",40,150),("Cash or Card","💳","🔴",60,200),("Burguro and Fryuro","🍔","🔥",80,250),("Capitano Moby","🐋","◻",100,350),("Garama and Madundung","🧬","◻",50,875)]

PK_dragon = [("Dragon Cannelloni","🐉","💎",500,2500),("Dragon Cannelloni","🐉","🧊",500,2500),("Dragon Cannelloni","🐉","🔥",500,2500),("Dragon Cannelloni","🐉","🪙",500,2500),("Dragon Cannelloni","🐉","◻",500,2500)]
PK_cerb = [("Cerberus","🐕","🔥",100,200),("Cerberus","🐕","💎",100,200)]
PK_rest = [("Hydra Dragon Cannelloni","🐲","🧊",400,1800),("Ketupat Bros","🧆","🪙",200,500),("La Casa Boo","👻","◻",180,450),("Foxini Lanternini","🦊","🌸",150,400),("Rosey and Teddy","🧸","🎁",120,350),("Los Hackers","💻","🔥",160,420),("Dragon Gingerini","🍪","💎",300,1200)]

GL_4 = [("Skibidi Toilet","🚽","💎",350,450),("Strawberry Elephant","🐘","🌸",250,750),("Meowl","🦉","💎",400,600),("John Pork","🐷","🪙",450,550)]

ST = [b[0] for b in FL_garama+FL_rare+FL_rest]

def pf():
    r=random.random()
    if r<0.60: return random.choice(FL_garama)
    if r<0.75: return random.choice(FL_rare)
    return random.choice(FL_rest)

def ppk():
    r=random.random()
    if r<0.50: return random.choice(PK_dragon)
    if r<0.70: return random.choice(PK_cerb)
    return random.choice(PK_rest)

def phl():
    return random.choice(HL_rare) if random.random()<0.15 else random.choice(HL_rest)

def build(data,emoji,color):
    name,dna,icon,lo,hi=data
    e=discord.Embed(title=f"{emoji} {TITLE}",description=f"**{name}**\n└ {dna} • {icon}",color=color,timestamp=datetime.now(timezone.utc))
    e.set_footer(text=FOOTER)
    e.set_thumbnail(url=img(name))
    return e

def steal_embed(name,user):
    e=discord.Embed(title=TITLE,description=f"**Steal Detected**\n@{user} just stole\n**{name}** 😯\n😯😯😯😎",color=0xF5A623,timestamp=datetime.now(timezone.utc))
    e.set_footer(text=FOOTER)
    return e

# SEND WITH RETRY — 3 attempts
async def send_safe(ch, embed, label=""):
    for attempt in range(3):
        try:
            await ch.send(embed=embed)
            return
        except Exception as e:
            print(f"[{label}] ⚠ Send failed (attempt {attempt+1}/3): {e}")
            await asyncio.sleep(5 * (attempt+1))
    print(f"[{label}] ❌ FAILED after 3 attempts")

# ═══ LOOPS ℔ SLOW ═══

async def fl(ch):
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await send_safe(ch, build(pf(),"🌽",0x2ECC71), "FL")
        except:
            pass
        # Farmer: 15-30 seconds (was 5-12)
        await asyncio.sleep(random.uniform(15, 30))

async def hl(ch):
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await send_safe(ch, build(phl(),"🧠",0x4ECDC4), "HL")
        except:
            pass
        # Highlights: 60-120 seconds (was 30-60)
        await asyncio.sleep(random.uniform(60, 120))

async def pk(ch):
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await send_safe(ch, build(ppk(),"👑",0xF5A623), "PK")
        except:
            pass
        # Peak: 120-240 seconds = 2-4min (was 90-150)
        await asyncio.sleep(random.uniform(120, 240))

async def gl(ch):
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await send_safe(ch, build(random.choice(GL_4),"👼",0xB8A9E8), "GL")
        except:
            pass
        # Godly: 3600-5400 seconds = 60-90min (was 1800-2700)
        await asyncio.sleep(random.uniform(3600, 5400))

async def st(ch):
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            users = []
            for g in bot.guilds:
                users = [m.name for m in g.members if not m.bot]
                break
            if not users: users = ["JETZTUGER"]
            await send_safe(ch, steal_embed(random.choice(ST), random.choice(users)), "ST")
        except:
            pass
        # Stalk: 30-60 seconds (was 15-30)
        await asyncio.sleep(random.uniform(30, 60))

@bot.event
async def on_ready():
    print(f"\n🚀 {bot.user}")
    for g in bot.guilds:
        users = [m.name for m in g.members if not m.bot]
        if not users: users = ["JETZTUGER"]
        print(f"👥 {len(users)} Members")

        chs={}
        for name in ["🍟・farmer-lights","❄️・highlights","🙌・peak-highlights","👼・godly-highlights","👹・stalk-steals"]:
            ch=discord.utils.get(g.text_channels,name=name)
            if not ch:
                