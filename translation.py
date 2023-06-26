from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi there {} 

To add or update your flashshortx shortner api see example 👇👇

𝙸 𝙰𝚖 𝙵𝚕𝚊𝚜𝚑𝚜𝚑𝚘𝚛𝚝𝚇.𝚒𝚗 , 𝙱𝚞𝚕𝚔 𝙻𝚒𝚗𝚔 𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚎𝚛. 𝙸 𝙲𝚊𝚗 𝙲𝚘𝚗𝚟𝚎𝚛𝚝 𝙻𝚒𝚗𝚔𝚜 𝙳𝚒𝚛𝚎𝚌𝚝𝚕𝚢 𝙵𝚛𝚘𝚖 𝚈𝚘𝚞𝚛 𝙵𝚕𝚊𝚜𝚑𝚜𝚑𝚘𝚛𝚝𝚇.𝚒𝚗 𝙰𝚌𝚌𝚘𝚞𝚗𝚝,

𝟷. 𝚂𝚎𝚝 𝙵𝚛𝚒𝚜𝚝 👉  /𝚋𝚊𝚜𝚎_𝚜𝚒𝚝𝚎 𝙵𝚕𝚊𝚜𝚑𝚜𝚑𝚘𝚛𝚝𝚇.𝚒𝚗
𝟸. 𝙶𝚘 𝚃𝚘 👉 𝚑𝚝𝚝𝚙𝚜://𝙵𝚕𝚊𝚜𝚑𝚜𝚑𝚘𝚛𝚝𝚇.𝚒𝚗/𝚖𝚎𝚖𝚋𝚎𝚛/𝚝𝚘𝚘𝚕𝚜/𝚊𝚙𝚒
𝟹. 𝚃𝚑𝚊𝚗 𝙲𝚘𝚙𝚢 𝙰𝙿𝙸 𝙺𝚎𝚢
𝟺. 𝚃𝚑𝚊𝚗 𝚃𝚢𝚙𝚎 /𝚊𝚙𝚒 𝚝𝚑𝚊𝚗 𝚐𝚒𝚟𝚎 𝚊 𝚜𝚒𝚗𝚐𝚕𝚎 𝚜𝚙𝚊𝚌𝚎 𝚊𝚗𝚍 𝚝𝚑𝚊𝚗 𝚙𝚊𝚜𝚝𝚎 𝚢𝚘𝚞𝚛 𝙰𝙿𝙸 𝙺𝚎𝚢 (𝚜𝚎𝚎 𝚎𝚡𝚊𝚖𝚙𝚕𝚎 𝚝𝚘 𝚞𝚗𝚍𝚎𝚛𝚜𝚝𝚊𝚗𝚍 𝚖𝚘𝚛𝚎...)
/𝚜𝚑𝚘𝚛𝚝𝚎𝚗𝚎𝚛_𝚊𝚙𝚒  𝙰𝙿𝙸 𝙺𝚎𝚢 

(𝚂𝚎𝚎 𝙴𝚡𝚊𝚖𝚙𝚕𝚎.👇)
𝙴𝚡𝚊𝚖𝚙𝚕𝚎:

/𝚜𝚑𝚘𝚛𝚝𝚎𝚗𝚎𝚛_𝚊𝚙𝚒 𝟶𝟺𝚎𝟾𝚎𝚎𝟷𝟶𝚋𝟻𝚏𝟷𝟸𝟹𝟺𝟻𝟼𝚊𝟼𝟺𝟶𝚌𝟾𝚏𝟹𝟹𝟷𝟿𝟻𝚊𝚋𝚌 

- 𝙼𝚊𝚍𝚎 𝚆𝚒𝚝𝚑 🤍 𝙱𝚢 @𝙵𝚘𝚞𝚗𝚍𝚎𝚛𝙾𝚏_𝚂𝚑𝚘𝚛𝚝𝚇 -

| தமிழ் | తెలుగు | हिंदी | മലയാളം | ಕನ್ |

For adding footer write your footer text and then reply your footer text with /footer

Method: {flashshortx.in}
Shortener website: {flashshortx.in}
"""

HELP_MESSAGE = """Hey there! My name is {firstname} and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.

I have a ton of handy features to help you out, such as:

- [flashshortx.in](https://t.me/{username}) support 🔗
- Button conversion support 🔘
- Domain inclusion and exclusion options 🌐
- Header and footer text support 📝
- Replace username function 📎
- Banner image support 🖼️
- Batch conversion for channel admins only 📊
- Channel support for admins only 📢

Useful commands:

- /start: Start me up! You probably already used this.
- /help: Send this message; I'll tell you more about myself!
- /batch -100xxx: To shorten or convert all posts in your channel
"""

ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
`👨‍💻 Developer:` [Dev](https://t.me/FounderOf_ShortX)
`📢 Support:` [Talk Bot](https://t.me/FlashshortX)
`🌐 Source Code:` [GitHub](https://t.me/FlashshortX)
"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `flashshortx` - Change all the links of the post to your Flash account first and then short to {shortener} link.

> `flashshortx` - Short all the links of the post to {shortener} link directly.

> `flashshortx` - Save all the links of the post to your flash account.
    
To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/FlashshortX | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Methods", callback_data="method_command"),
            InlineKeyboardButton("Batch", callback_data="cbatch_command"),
        ],
        [
            InlineKeyboardButton("Custom Alias", callback_data="alias_conf"),
            InlineKeyboardButton("Admins", callback_data="admins_list"),
        ],
        [
            InlineKeyboardButton("Channels", callback_data="channels_list"),
            InlineKeyboardButton("Home", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Method", callback_data="method_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "MDLINK", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
            InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Shortener website: {base_site}

- 🧰 Method: {method}

- 🔌 {base_site} API: {shortener_api}

- 💾 Mdisk API: {mdisk_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api 6LZq851sXoPHugiKQq`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

To change your Shortener Website: /base_site

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
