# Adudin
# Copyright (C) 2021 Geez Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.vcinvite(?: |$)(.*)")
async def _(event):
    ok = await event edit "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in event.client.iter_participants(event.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await event.client(invitetovc(call=await get_call(event), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


        
        
        CMD_HELP.update(
    {
        "fakeaction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcjoin : .vcstop : .vcplay : .vcinvite : .fgame <jumlah text>`"
        "\n• : Fake typing ini Berfungsi dalam group"
    }
)
