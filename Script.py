class script(object):
    START_TXT = """HELLO {}  🙋🏻🙋🏻‍♀️
I can provide movies in group as well as the personal chat, send me movie name / ADD me to group and enjoy
I delete all messgaes in groups for restrict group from coppyrights issues ( 5min default delete time)
"""
    START_grp_TXT = """
    Hai..,
I can provide movies in group as well as the personal. ADD me to your group as admin or just send movie name to me personally
    
    
    """
    START_gp_TXT = """𝙷𝙴𝙻𝙾 {}  🙋🏻🙋🏻‍♀️
I can provide movies/ series, just send movie name to me or you can add me to your group
I delete all messgaes in groups for restrict group from coppyrights issues ( 5min default delete time)
"""
    HELP_TXT = """𝙷𝙴𝚈  {}  🙋🏻🙋🏻‍♀️
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>♠️ MY NAME: {}</b>
<b>♣️ OWNED BY:</b> <a href=https://t.me/JiC54_SERIES_Bot>Click Here!</a>
<b>♣️ LANGUAGE:</b> 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
<b>♣️ DATABASE:</b> 𝙼𝙾𝙽𝙶𝙾
<b>♣️ BOT SERVER:</b> 𝙷𝙴𝚁𝙾𝙺𝚄
<b>♣️ 𝙱OT VERSION:</b> <code>12.2.1</code>"""
    SOURCE_TXT = """<b>JiC54 CHANNELS:</b> 
    
<a href=https://t.me/+H_6j47erCp44YjY0>Movies and Series 2022</a>
<a href=https://t.me/+uQBJ5JaaLpgyMWI0>House of Movies</a>
<a href=https://t.me/+EHBqUrMHnglmZWY8>Dax songs</a>
<a href=https://t.me/+8eC2YwzHZtUwZDg0>DC Series</a>
<a href=https://t.me/+GvVfP9p-YAsyMTY0>Marvel Movies</a>
<a href=https://t.me/+6QrMOpOVtKAxOGQ0>African Movies</a>
<a href=https://t.me/+LhZuWiqE21NiYzY0>WWE wrestling</a>

<b>JiC54 GROUPS:</b>
<a href=https://t.me/+dFGzJDTQWow2ZGY8>Request Movies</a>
<a href=https://t.me/+bCTNQn4-5TtkZmZk>Request Series</a>
<a href=https://t.me/+gTYFpj1ZBIIxZTQ0>Request Dax Songs</a>
<b>JiC54 BOTS:</b>
<a href=http://t.me/JiC54_MOVIES_Bot>Movies Bot</a>
<a href=http://t.me/JiC54SeriesBot>Series Bot</a>
<a href=http://t.me/filestolinks1_bot>File to Links Bot</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found the message
<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
 ❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    
    
    BATCHMODE1_TXT = """Help: <b>Batch mode</b>
  
  This feature user can generate special links to send files like movies. store files in a public channel and send me <code> /batch https://t.me/jns_bots/20 https://t.me/jns_bots/30 </code> . i will generate and send you special link.
<b>NOTE:</b>
1.Works in both Private and Public channel
 ✤ Make me in admin in private channel
 ✤ Admin Privilege not req for public channel 
<b>Commands and Usage:</b>
 • /batch - To start batch mode  
 
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    
    
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features 
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱 
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥
"""
    MAIL_ID_TXT = """
    <b>Currently you are using this mail for heroku account</b>\n
ID - <code>{}</code>
"""