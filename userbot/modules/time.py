# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# module created by @aragon12

""" Userbot module for getting the date and time of any country or the userbot server.  """

from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
from userbot.events import register

COUNTRY = ''

""" returns the timezone for a given country """
async def get_tz(con):
    """ Get time zone of the given country. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands","minor outlying islands")
    if "Nl" in con:
        con  = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    return 0

""" For .time command, return the time of
        1. The country passed as an argument,
        2. The default userbot country(set it by using .timec),
        3. The server where the userbot runs.
"""
@register(outgoing=True, pattern="^.time ?(.*)")
async def time_func(tdata):
    if not tdata.text[0].isalpha() and tdata.text[0] not in ("/", "#", "@", "!"):
        con = tdata.pattern_match.group(1).title()
        t_form = "%I:%M %p"

        if not con:
            if not COUNTRY:
                await tdata.edit(f"`it's` **{dt.now().strftime(t_form)}**  `here.`")
                return

            time_zone = await get_tz(COUNTRY)
            await tdata.edit(
                f"`It's`  **{dt.now(time_zone).strftime(t_form)}**  `here, in {COUNTRY}`"
            )
            return

        time_zone = await get_tz(con)
        if not time_zone:
            return

        await tdata.edit("`it's` **"+dt.now(time_zone).strftime(t_form)+"**  `here, in "+con+"`")

@register(outgoing=True, pattern="^.date$")
async def date_func(dat):
    if not dat.text[0].isalpha() and dat.text[0] not in ("/", "#", "@", "!"):
        d_form = "%d/%m/%y - %A"
        con = dat.pattern_match.group(1).title()

        if not con:
            if not COUNTRY:
                await dat.edit(f"`It's`  **{dt.now().strftime(d_form)}**  `here.`")
                return

            time_zone = await get_tz(COUNTRY)
            await dat.edit(
                f"`It's`  **{dt.now(time_zone).strftime(d_form)}**  `here, in {COUNTRY}.`"
            )
            return

        time_zone = await get_tz(con)
        if not time_zone:
            await dat.edit("``` Wrong country given! Try again! ```")
            return

        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con

        await dat.edit("`it's`  **"+dt.now().strftime(d_form)+"**")

@register(outgoing=True, pattern="^.ctime (.*)")
async def set_time_country(loc):
    """ For .ctime command, change the default userbot country for date and time commands. """
    if not loc.text[0].isalpha() and loc.text[0] not in ("/", "#", "@", "!"):
        global COUNTRY
        temp_country = loc.pattern_match.group(1).title()

        time_zone = await get_tz(temp_country.title())
        if not time_zone:
            await loc.edit("``` Wrong country given! Try again! ```")
            return

        COUNTRY = temp_country.title()

        await loc.edit(f"``` Default country for date and time set to {COUNTRY} successfully! ```")
