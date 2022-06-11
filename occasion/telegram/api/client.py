import contextlib
from typing import BinaryIO
from datetime import datetime
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import exceptions

from pyrogram import Client


class TelegramClient:
    def __init__(self, session_name: str, api_id: str, api_hash: str):
        self.app = Client(
            name=session_name,
            api_id=api_id,
            api_hash=api_hash,
            device_model='Occasion'
        )

    def __enter__(self):
        self.app.start()
        return self

    def __exit__(self, *args):
        with contextlib.suppress(ConnectionError):
            self.app.stop()

    def create_channel(self, title: str, description: str = ""):
        return self.app.create_channel(title=title, description=description)

    def create_channel_invite_link(
            self,
            chat_id: int | str,
            name: str,
            member_limit: int | None = 1
    ):
        return self.app.create_chat_invite_link(
            chat_id=chat_id,
            name=name,
            member_limit=member_limit
        )

    def revoke_chat_invite_link(self, chat_id: int | str, invite_link: str) -> None:
        with contextlib.suppress(exceptions.EditBotInviteForbidden, exceptions.InviteHashExpired):
            self.app.revoke_chat_invite_link(chat_id, invite_link)

    def send_message(
            self,
            chat_id: int | str,
            text: str,
            photo: BinaryIO | str | None = None,
            schedule_dt: datetime | None = None,
    ):
        if photo:
            return self.app.send_photo(
                chat_id=chat_id,
                caption=text,
                photo=photo,
                schedule_date=schedule_dt,
            )
        return self.app.send_message(
            chat_id=chat_id,
            text=text,
            schedule_date=schedule_dt)

    def edit_message(
            self,
            chat_id: int | str,
            message_id: int,
            text: str | None = None,
    ):
        try:
            return self.app.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text
            )
        except exceptions.BadRequest:
            return self.app.edit_message_caption(
                chat_id=chat_id,
                message_id=message_id,
                caption=text
            )

    def edit_message_photo(
            self,
            chat_id: int | str,
            message_id: int,
            photo: BinaryIO | str,
    ):
        return self.app.edit_message_media(
            chat_id=chat_id,
            message_id=message_id,
            media=InputMediaPhoto(media=photo)
        )
