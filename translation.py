class Translation(object):
    START_TEXT = """Hi {},
You can upload File|Video To Telegram with direct link, Using this bot!
Support Site <a href="https://ytdl-org.github.io/youtube-dl/supportedsites.html">HERE</a>
/help for more details!"""
    FORMAT_SELECTION = "Choose the desired format: <a href='{}'>file size may be approximate</a> \nIf you want to set a custom thumbnail, send the photo before or quickly after tapping one of the buttons below.\nYou can use /deletethumbnail to delete auto-generated thumbnails."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, please provide them in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "📥download..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded at {} second.\nFile size Detected: {}\nSorry. But, I can't upload files larger than 2GB due to limitations of Telegram API."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thank you for using me \n\n<b>Join @ansakubotchannel For More Useful Bots Like Me </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded at {} second.\nUploaded in {} second.\n\n@ansakubotchannel"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video/thumbnail files saved. This image will be used in the video/file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail deleted successfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
    
   ☞My Name  : All Media Downloader

   ☞Updates  : @ansakubotchannel    

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Please Follow these steps!
    
1. Send url (example.domain/File.mp4 | New FileName.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select button.
   SVideo - Give File as video with Screenshot
   DFile  - Give File (video) as file with Screenshot
   Video  - Give File as video without Screenshot
   File   - Give File without Screenshot

If the bot doesn't respond, Ask Here @AnkiSatya"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply to /generatecustomthumbnail to media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media albums can only contain two photos. Please resend the media album, then try again, or send only two photos in one album."
You can use the /rename command after receiving the file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Aborted"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} second"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
