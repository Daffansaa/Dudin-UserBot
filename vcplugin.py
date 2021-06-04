# Adudin
# Copyright (C) 2021 Geez Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.vcinvit(?: |$)(.*)")
async def _(e):
    ok = await eor(e, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


        
        
        CMD_HELP.update(
    {
        "fakeaction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcjoin : .vcstop : .vcplay : .vcinvite .fgame <jumlah text>`"
        "\n• : Fake typing ini Berfungsi dalam group"
    }
)
        
        
        
        
