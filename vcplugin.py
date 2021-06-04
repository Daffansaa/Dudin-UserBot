# Adudin
# Copyright (C) 2021 Geez Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio

@register(outgoing=True, pattern="^.vcjoin(?: |$)(.*)")
async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@register(outgoing=True, pattern="^.vcstop(?: |$)(.*)")
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await eor(e, "`Voice Chat Stopped...`")
        vcdyno("off")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@register(outgoing=True, pattern="^.vcplay(?: |$)(.*)")
async def _(e):
    zz = await eor(e, "`VC bot started...`")
    er, out = await bash("npm start")
    LOGS.info(er)
    LOGS.info(out)
    vcdyno("on")
    if er:
        await zz.edit(f"Failed {er}\n\n{out}")


@register(outgoing=True, pattern="^.vcinvite(?: |$)(.*)")
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

@register(outgoing=True, pattern="^.vcstart(?: |$)(.*)")
    pattern="startvc$",
    admins_only=True,
    groups_only=True,
)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await eor(e, "`Voice Chat Started...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@register(outgoing=True, pattern="^.listvcaccess(?: |$)(.*)")
async def _(e):
    xx = await eor(e, "`Getting Voice Chat Bot Users List...`")
    mm = get_vcsudos()
    pp = f"**{len(mm)} Voice Chat Bot Approved Users**\n"
    if len(mm) > 0:
        for m in mm:
            try:
                name = (await e.client.get_entity(int(m))).first_name
                pp += f"• [{name}](tg://user?id={int(m)})\n"
            except ValueError:
                pp += f"• `{int(m)} » No Info`\n"
    await xx.edit(pp)


@register(outgoing=True, pattern="^.rmaccess(?: |$)(.*)")
async def _(e):
    xx = await eor(e, "`Disapproving to access Voice Chat features...`")
    input = e.pattern_match.group(1)
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        name = (await e.client.get_entity(userid)).first_name
    elif input:
        try:
            userid = await get_user_id(input)
            name = (await e.client.get_entity(userid)).first_name
        except ValueError as ex:
            return await eod(xx, f"`{str(ex)}`", time=5)
    else:
        return await eod(xx, "`Reply to user's msg or add it's id/username...`", time=3)
    if not is_vcsudo(userid):
        return await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is not approved to use my Voice Chat Bot.`",
            time=5,
        )
    try:
        del_vcsudo(userid)
        await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is removed from Voice Chat Bot Users.`",
            time=5,
        )
    except Exception as ex:
        return await eod(xx, f"`{str(ex)}`", time=5)

@register(outgoing=True, pattern="^.vcaccess(?: |$)(.*)")
async def _(e):
    xx = await eor(e, "`Approving to access Voice Chat features...`")
    input = e.pattern_match.group(1)
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        name = (await e.client.get_entity(userid)).first_name
    elif input:
        try:
            userid = await get_user_id(input)
            name = (await e.client.get_entity(userid)).first_name
        except ValueError as ex:
            return await eod(xx, f"`{str(ex)}`", time=5)
    else:
        return await eod(xx, "`Reply to user's msg or add it's id/username...`", time=3)
    if is_vcsudo(userid):
        return await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is already approved to use my Voice Chat Bot.`",
            time=5,
        )
    try:
        add_vcsudo(userid)
        await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is added to Voice Chat Bot Users.`",
            time=5,
        )
    except Exception as ex:
        return await eod(xx, f"`{str(ex)}`", time=5)


@register(outgoing=True, pattern="^.exitvc(?: |$)(.*)")
async def evc(e):
    if e.sender.id == ultroid_bot.uid:
        vcdyno("off")
    elif is_sudo(e.sender.id):
        vcdyno("off")
    elif is_vcsudo(e.sender.id):
        vcdyno("off")
        
        
        CMD_HELP.update(
    {
        "fakeaction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcjoin : .vcstop : .vcplay : .vcinvite .fgame <jumlah text>`"
        "\n• : Fake typing ini Berfungsi dalam group"
    }
)
        
        
        
        
