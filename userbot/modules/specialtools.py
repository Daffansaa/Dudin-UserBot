import os
from datetime import datetime as dt
from random import choice
from shutil import rmtree

import moviepy.editor as m
import pytz
import requests
from bs4 import BeautifulSoup as b

from . import *


@ultroid_cmd(
    pattern="getaudio$",
)
async def daudtoid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await eor(event, "`Reply To Audio Only..`")
        return
    xx = await eor(event, "`processing...`")
    d = os.path.join("resources/extras/", "ul.mp3")
    await xx.edit("`Downloading... Large Files Takes Time..`")
    await event.client.download_media(ureply, d)
    await xx.edit("`Done.. Now reply to video In which u want to add that Audio`")


@ultroid_cmd(
    pattern="addaudio$",
)
async def adaudroid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await eor(event, "`Reply To Gif/Video In which u want to add audio.`")
        return
    xx = await eor(event, "`processing...`")
    ultt = await ureply.download_media()
    ls = os.listdir("resources/extras")
    z = "ul.mp3"
    x = "resources/extras/ul.mp3"
    if z not in ls:
        await xx.edit("`First reply an audio with .aw`")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("ok.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="ok.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    os.remove("ok.mp4")
    os.remove(x)
    os.remove(ultt)
    await xx.delete()
