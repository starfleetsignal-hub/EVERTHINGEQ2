---
title: Slash Commands
type: page
aliases:
- Macro Command Language
- Pet Commands
- Slash commands
categories:
- EverQuest II
- Slash Commands
source:
  title: Slash Commands
  url: https://eq2.fandom.com/wiki/Slash_Commands
  history: https://eq2.fandom.com/wiki/Slash_Commands?action=history
  revision: 2028878
  revised: '2026-09-12T17:29:20Z'
  license: CC BY-SA 3.0
---

This page holds a full list of the slash commands available. See more at Slash Commands.

- For ease of use with many of these commands, press **O** while in game to open the Macros window. You can save any of these commands as a macro, then drag the icon to hotbar for one-click use.

## Ability commands

| Command | Example | Notes |
|---|---|---|
| /useability {ability} | /useability Minor Aid | Will execute the spell or ability *Minor Aid* on your current or implied target. |
| /useabilityonplayer {player} {ability} | /useabilityonplayer Exultavit Minor Aid | Will execute the spell or ability *Minor Aid* on player Exultavit. |
| /useabilityonmerc {player} {ability} | /useabilityonmerc Exultavit Minor Aid | Will execute the spell or ability *Minor Aid* on the merc of player Exultavit. |
| /useabilityonmerc {merc} {ability} | /useabilityonmerc Krivok Minor Aid | Will execute the spell or ability *Minor Aid* on merc Krivok. |
| /useabilityonrt {ability} | /useabilityonrt Cure | Will execute Cure on the last person who send you a /tell without changing target |
| /cancel_spellcast | /cancel_spellcast | Cancels the spell currently being cast (both commands perform the same function) |
| /clearabilityqueue<br>/clearallqueuedabilities<br>/cl | /clearabilityqueue<br>/clearallqueuedabilities<br>/cl | Clears your current spell/ability queue |
| /cancel_maintained {maintained ability} | /cancel_maintained [[Aegolism]] | Cancels a maintained spell, if more than one of the same name is active, they are cancelled in the order they were cast. |

## Fight commands

| Command | Example | Notes |
|---|---|---|
| /autoattack | /autoattack | Toggles autoattacking on or off. |
| /autoattack 0 | Stops all autoattacks (only stops autoattack momentarily) |  |
| /autoattack 1 | Turns melee autoattacking on |  |
| /autoattack 2 | Turns ranged autoattacking on |  |
| /setauto | /setauto | Toggles your autoattack style (same as in Characters options) |
| /setauto 0 | Turns autoattack style to "Automatic" |  |
| /setauto 1 | Turns autoattack style to "Forced Melee" |  |
| /setauto 2 | Turns autoattack style to "Forced Ranged/Spell" |  |
| /setauto 3 | Turns autoattack style to "off". |  |
| /toggleautoattack | /toggleautoattack | Another alias for /autoattack. |
| /togglerangedattack | /togglerangedattack | Toggles ranged autoattacking on or off. |

## Pet commands

| Command | Example | Notes |
|---|---|---|
| /pet | /pet backoff | Pet will (try to) back off from its current target and run to you. It will stop protecting itself or you. |
| /pet autoassist | Toggles the pet assisting you |  |
| /pet preserve_self | Toggles whether or not pet will protect itself from new attackers when not otherwise engaged. |  |
| /pet preserve_master | Toggles whether or not pet will protect you from new attackers when not otherwise engaged. |  |
| /pet attack | Sends pet to attack your current or implied target. |  |
| /pet stayhere | Pet will stop following you and remain where it is. |  |
| /pet followme | Pet will follow you |  |
| /pet getlost | Pet will disappear |  |
| /pet hide | Hide or Unhide your various pets or familiars in the current zone. If you want to hide your pet permanently do the following:<br>#right click the pet<br>#click on Pet Options<br>#click on the hood |  |
| /pet melee | Your pet will use melee attacks |  |
| /pet ranged | Your pet will use ranged attacks and casts spells more freqently as in melee stance |  |
| /petname {name} | /petname Lapsisusi | Your next summoned pet will be named Lapsisusi. |
| /petoptions | /petoptions | Brings up the Pet Options window. Works only if you have just one pet up, this includes the deity pet. |
| /togglepet | /togglepet | Toggles the display of the pet information and command UI window. |

## Overseer command

| Command | Example | Notes |
|---|---|---|
| /toggleoverseer | /toggleoverseer | Opens the Overseer UI window. |

## Mercenary commands

| Command | Example | Notes |
|---|---|---|
| /merc | /merc ranged | Your mercenary  will use ranged attacks and casts spells more freqently as in melee stance |
| /merc melee | Your mercenary will use melee attacks |  |
| /merc resume | Your mercenary will return after being suspended |  |
| /merc suspend | Will suspend your active mercenary after you acknowledge a dialog warning the mercenary cannot be recalled for one minute |  |
| /merc attack | Sends mercenary to attack your current or implied target |  |
| /merc backoff | Mercenary will (try to) back off from its current target and run to you. It will stop protecting itself or you. |  |
| /merc preserve_self | Toggles whether or not the merc will protect itself from new attackers when not otherwise engaged. |  |
| /merc preserve_master | Toggles whether or not the merc will protect you from new attackers when not otherwise engaged. |  |
| /mercname {name} | /mercname Soandso | Your mercenary's name will be changed to Soandso |
| /togglemerc | /togglemerc | Toggles the display of the Mercenary information and command UI window. |
| /cl_ignore_merc_chatter {true/false} | /cl_ignore_merc_chatter true | Enables or disables Mercenary group chat |

## Log/combat Filters

| Command | Example | Notes |
|---|---|---|
| /combat_filter <filter#> | /combat_filter 0 | none *does not persist through zoning so you will have to set it each time you zone* |
| /combat_filter 1 | Self (you will only get combat messages for yourself/your pet)<br><br>*If you are seeing huge lag please try "/combat_filter 1" and see if that helps*<br><br>*does not persist through zoning so you will have to set it each time you zone* |  |
| /combat_filter 2 | group *does not persist through zoning so you will have to set it each time you zone* |  |
| /combat_filter 3 | raid *does not persist through zoning so you will have to set it each time you zone* |  |
| /log | /log | turns logging either on or off *for example Logging to logs/[server]/eq2log_[char].txt is now *ON** |
| /log {name of log file}<br>/log doesitwork<br>/log on<br>/log off | turns logging either on or off, but it changes the name of the logfile to the {name of log file} ("doesitwork", "on", "off").<br>Example for "/log on" *Logging to 'logs/[server]/on.txt' is now *OFF** <-> *Logging to 'logs/[server]/on.txt' is now *ON**<br><br>*that means "/log on" or "/log off" doesn't turn logging on or off as such .. it changes the name of the logfile + if it was deactivated it gets activated and vice-versa*<br><br>Best use is just "/log" |  |

## Character Appearance

| Command | Example | Notes |
|---|---|---|
| /showhood | /showhood | Displays or hides cape hood. |
| /showhelm | /showhelm | Displays or hides helmet. |
| /showranged | /showranged | Displays your bow. |
| /hide_illusions<br>/hi | /hide_illusions<br>/hi | Hides your illusion forms |
| /showcloak | /showcloak | Hides or shows your cloak |
| /suspend_mount_mode N | /suspend_mount_mode 0 | Always show mount |
| /suspend_mount_mode 1 | Hide mount during combat |  |
| /suspend_mount_mode 2 | Always hide mount |  |
| /togglepersonaltorch | /togglepersonaltorch | Turns on/off your personal torch. |

## Gear Macros

| Command | Example | Notes |
|---|---|---|
| /unequip_appearance | /unequip_appearance cloak | Empties the cloak appearance slot. |
| /unequip_appearance primary | Empties primary weapon appearance slot. |  |
| /unequip_appearance head | Empties helm appearance slot. |  |
| /equip_equipment_set | /equip_equipment_set 0 "MaxHitpoint" | Swaps Equipment sets, 0 for Adventure gear 1 for Appearance, The Set name in quotes. |

## Inventory commands

| Command | Example | Notes |
|---|---|---|
| /empty overflow | /empty overflow | Empties the overflow stack into inventory. |
| /togglebags | /togglebags | If your bags are all open, closes them; if they are closed, opens them. |
| /togglehouseinventory | /togglehouseinventory | Opens your House Inventory if you are in a House or Guild Hall.  You must own a house before your House Inventory is usable. |
| /finditem<br>/finditem <item> | /finditem<br>/finditem sword | Opens a search window where you can search your entire inventory, including bank and house vault, for items by their name.  If an item name is supplied, it will search for all items that match. |
| /get_coins | /get_coins | Shows the amounts of platinum, gold, silver and copper you currently possess on your person. |
| /inventory unequip all | /inventory unequip all | All your gear is unequipped and dropped in your backpack. Everything including food and drink on the Equipment tab. |
| /sort_bags | /sort_bags level d | sorts the items in your bags by level, descending |

## Use Commands

| Command | Example | Notes |
|---|---|---|
| /use_equipped_item | /use_equipped_item 0 | primary |
| /use_equipped_item 1 | secondary |  |
| /use_equipped_item 2 | head |  |
| /use_equipped_item 3 | chest |  |
| /use_equipped_item 4 | shoulders |  |
| /use_equipped_item 5 | forearms |  |
| /use_equipped_item 6 | hands |  |
| /use_equipped_item 7 | legs |  |
| /use_equipped_item 8 | feet |  |
| /use_equipped_item 9 | left ring |  |
| /use_equipped_item 10 | right ring |  |
| /use_equipped_item 11 | ear slot 1 |  |
| /use_equipped_item 12 | ear slot 2 |  |
| /use_equipped_item 13 | neck |  |
| /use_equipped_item 14 | left wrist |  |
| /use_equipped_item 15 | right wrist |  |
| /use_equipped_item 16 | ranged |  |
| /use_equipped_item 17 | ammo |  |
| /use_equipped_item 18 | waist |  |
| /use_equipped_item 19 | cloak |  |
| /use_equipped_item 20 | charm slot 1 |  |
| /use_equipped_item 21 | charm slot 2 |  |
| /use_equipped_item 22 | food |  |
| /use_equipped_item 23 | drink |  |
| /use_itemvdl | /use_itemvdl 136666185 | Uses Robust Elemental Potion |

## Soga (Alternative Models)

| Command | Example | Notes |
|---|---|---|
| /soga_models | /soga_models on | Turns all Soga (Alternative Models) on |
| /soga_models off | Turns all Soga (Alternative Models) off |  |

## General Chat

| Command | Example | Notes |
|---|---|---|
| /set_language | /set_language Language_Name | You change the language that shows up in /say and /shout |
| /emote<br>/em<br>:<br>/e | /emote starts to cry!<br>/em starts to cry<br>: starts to cry!<br> /e starts to cry! | *Player* starts to cry! |
| /say<br>/s<br>' | /say Hello<br>/s Hello<br>' Hello | You say Hello in Spatial say with your determined Language and a chatbubble |
| /shout<br>! | /shout Hello<br>! Hello | You shout *Hello* with your determined Language and a chatbubble |
| /ooc | /ooc Hello | You say Hello zonewide without a chatbubble |
| /auction<br>$ | /auction WTS a gold cluster<br>$ WTS a gold cluster | You say *WTS a gold cluster* zonewide as auction |
| /ventsay | /ventsay He was it! | Your target says (through ventriloquism) *He was it!* |
| /filter | /filter | Toggles the obscenity filter between on and off |

## Search for Player

| Command | Example | Notes |
|---|---|---|
| /who {parameters} | /who | If parameters are not given, a list of all characters in the current zone is returned. Note that players using the anonymous or roleplaying tags may not be returned by a search. |
| /who {name} | Limits the search to character names and guild names matching the pattern. For example, **/who legend** could return a player named "Legendee", or a guild such as "Legends of the Tundra". |  |
| /who {class} | Limits the search to characters with the listed class, subclass, or archetype; spaces are not allowed. For example, use **/who all priest** to list all the healers in your current zone; **/who all bard** to locate dirges and troubadours in your zone; **/who illusionist** to find all the illusionists in your zone.  This includes both adventure and crafting classes: */who all provisioner 95* will list all the level 95 provisioners currently online. |  |
| /who {race} | Limits the search to characters with the listed race; spaces are not allowed. For example, **/who human** will list all the human players in your zone. |  |
| /who {level} | Limits the search to characters of the specified level. For example, **/who warrior 95** will list all the level 95 guardians and berserkers in your zone. |  |
| /who {low level} {high level} | Limits the search to characters of the specified level range (inclusive). For example, **/who coercer 50 59** will list all the coercers from level 50 to level 59 in your current zone. |  |
| /who {alignment} | Limits the search to characters of the specified alignment (good, evil, or neutral). |  |
| /who {player tag} | Limits the search to players showing the specified tag (LFG, LFW). For example, **/who all scout 95 LFG**, or **/who all sage 90 95 LFW** |  |
| /who friend | Limits the search to characters on your friends list. |  |
| /who guild | Limits the search to characters within your guild. |  |
| /who GM | Limits the search to characters who are showing the GM flag. |  |
| /who Guide (or Guides) | Limits the search to characters who members of the EverQuestII Guide Program. |  |
| /who all | Expands the search to all zones rather than the current zone. |  |
|  | Additional usage examples:<br>***/who evil friends all** - Search all zones for characters who are both evil and on your friends list.<br>***/who fighter 16 10 LFG** - Search the current zone for any fighter between the levels of 10 and 16 who are looking for group.<br>***/who all crusader 25 guild** - Search all zones for Paladins and Shadowknights who are level 25 and in your guild.<br>***/who bubba halfling shadowknight** - Search the current zone for a player whose name or guild begins with the word "bubba". |  |

## Community commands

| Command | Example | Notes |
|---|---|---|
| /friends {name} | /friends Exultavit | If Exultavit is not on your friends list, adds him; if he is, removes him from the list. |
| /friend_add {name} | /friend_add Exultavit | Adds Exultavit to your friends list. |
| /friend_remove {name} | /friend_remove Exultavit | Removes Exultavit from your friends list. |
| /ignores {name} | /ignores Exultavit | If Exultavit is not on your ignore list, adds him; if he is, removes him from the list. |
| /ignore_add {name} | /ignore_add Exultavit | Adds Exultavit to your ignore list. |
| /ignore_remove {name} | /ignore_remove Exultavit | Removes Exultavit from your ignore list. |
| /save_friends | /save_friends | Saves a list of a characters friends to a .txt file. |
| /load_friends | /load_friends | Loads a list of friends from the selected file. |

## Guild

| Command | Example | Notes |
|---|---|---|
| /guild | /guild create GuildName | temporary method of guild creation |
| /guild invite playername | invites playername to join your guild |  |
| /guild invite %rt | sends a guild invitation to the last player who sent you a tell |  |
| /guild kick playername | removes playername from a guild |  |
| /guild promote | promote player |  |
| /guild motd [your msg here] | Sets a new Guild Motd msg |  |
| /who all guild | /who all guild | lists whoever is on in guild at the moment |
| /guildsay<br>/gu<br>@ | /guildsay message<br>/gu message<br>@ message | You say *message* in Guild chat |
| /officersay text<br>/os text<br>/of text | /officersay message<br>/os message<br>/of message | You say *message* in Officer chat of your guild |
| /guild points {add/subtract} {point value} {*who*} {comment} | /guild points add 100 raid PR Raid for fun 4/10/2010 | *point value* - you can "add" a negative number if you like.<br> *who* - can be a specific toon's name, "all" for the whole guild, "online" for players currently logged in, "group" for guild members in group with you, or "raid" for members on a raid with you.<br> *comment* - you can add a text comment to explain the addition or subtraction of points.<br> /guild points *view player name* - will bring up a verbose list containing any comments included with points changes. |

## Channels

*# = channelname/channelnumber*

| Command | Example | Notes |
|---|---|---|
| /tellchannel<br>/csay | /tellchannel Channelname msg<br>/csay Channelname msg | send message to Channelname with msg |
| /# | /# msg | send message to Channel# with msg |
| /joinchannel | /joinchannel channelname | Join or create the channelname |
| /leavechannel<br>/chatleave | /leavechannel #<br>/chatleave # | leave channel #<br> |
| /leaveall | /leaveall | leave all your channels |
| /channellist | /channellist | lists all channels you are currently in |
| /chat_allowduplicatechannels | /chat_allowduplicatechannels 0 <br>/chat_allowduplicatechannels 1 | Allows chat channels to show up on multiple tabs <br>0 = off <br>1 = on |
| /whochannel #<br>/wc #<br>/chatwho # | /whochannel #<br>/wc #<br>/chatwho # | lists all players that are in channel # |
| /setchannelnumber X Y | /setchannelnumber 1 3 | moves channel 1 to 3, if channelnumber 3 is not in use |
| /chat_show_category true | /chat_show_category true | lists the chat option tag (so that you know what chat option channel each type of dialogue goes in) of all of the chat shown |
| /chat_show_category false | /chat_show_category false | hides the chat option tag of all of the chat shown |
| /chat_show_time true | /chat_show_time true | lists the timestamp of all chat shown |
| /chat_show_time false | /chat_show_time true | hides the timestamp of all chat shown |

## Group and Raid

| Command | Example | Notes |
|---|---|---|
| /gsay<br>/g<br># | /gsay Hi<br>/g Hi<br># Hi | You say *Hi* in groupchat with a chatbubble. |
| /raidsay<br>/rsay<br>/r<br>^ | /raidsay Hi<br>/rsay Hi<br>/r Hi<br>^ Hi | You say *Hi* in raidchat without a chatbubble. |
| /whogroup | /whogroup<br>/whog | Lists everyone that is a member of your group. |
| /whoraid | /whoraid<br>/whor | Lists everyone that is a member of your raid. |
| /invite<br>/i | /invite Player<br>/i Player | Sends an invite to your group to Player |
| /AC | /ACceptinvite | Accepts an invite to the group or raid |
| /raidinvite | /raidinvite Player | Sends an invite to your raid to Player or his group leader. |
| /raid_looter | /raid_looter add Player | adds Player as a raid looter |
| /raid_looter remove Player | removes Player from being a raid looter |  |
| /makeleader<br>/make | /makeleader Player<br>/make Player | Make Player the leader of the group/raid instead of yourself (even you are in different zones). |
| /disband<br>/di | /disband | Leave the current group. |
| /kickfromgroup {player name} | /kickfromgroup Ninjalooter | Removes the target or named player from group. |
| /kickfromraid |  | Removes the targeted group from raid. |
| /split {p g s c} | /split 12 40 20 10 | splits 12p 40g 20s 10c between all group/raid members that are in the same zone. |
| /cl_ignore_merc_chatter {true/false} | /cl_ignore_merc_chatter true | Enables or disables Mercenary group chat. |
| /countdown {seconds} | /countdown | opens the countdown ui to set a counddown timer that is visible for everyone in the raid *(that pings every 5 seconds, only the group/raid leader can use it)* |
| /countdown 10 | skips the ui and starts a 10 second countdown visible for everyone in the raid  *(that pings every 5 seconds, only the group/raid leader can use it)* |  |

## Private tells

| Command | Example | Notes |
|---|---|---|
| /tell<br>/t | /tell Sanji Hi<br>/t Sanji Hi | You send a tell to Sanji with *Hi* |
| /tell *Server.Character*<br>/t *Server.Character* | /tell Butcherblock.Sanji Hi<br>/t Butcherblock.Sanji Hi | You send a tell to Sanji on the Butcherblock server with *Hi* |
| /telltarget<br>/tt<br>/t %T | /telltarget Hi<br>/tt Hi<br>/t %T Hi | You send a tell to your current target with *Hi* |
| /reply | /reply *Hi* | You send a tell to the last person that sent you a tell with *Hi&#x27;* |

## Mailbox

| Command | Example | Notes |
|---|---|---|
| /clear_mailbox | /clear_mailbox | To clear your mailbox before a character move or if a full notice is given and your box is empty so as to get rid of the mail you can not see..<br>**Note this command will delete all your mail so use it wisely!** |

## Keyring

| Command | Example | Notes |
|---|---|---|
| /keys | /keys | shows all your "keys" you have to access zones from the [[Planes of Prophecy]] expansion |

## Emotes

*See [[Emotes]].*

## Targeting commands

| Command | Example | Notes |
|---|---|---|
| /target {name} | /target mayong | Targets a mayong. |
| /target_self | /target_self | You target yourself |
| /target_previous | /target_previous | You target whatever you were targeting prior to this commmand. |
| /target_pet | target_pet | Targets your pet. |
| /target_group_member {#} | /target_group_member 0 | Targets a group member (member number starts at zero, order is as shown on the group window). |
| /target_group_pet {#} | /target_group_pet 1 | Targets the pet of your group member 1 (order is as shown on the group window). |
| /assist {name} | /assist Chalmo | Targets Chalmo's current target. |
| /target_merc | /target_merc | Targets your merc |
| /target_nearest_npc | /target_nearest_npc | Targets the nearest NPC or harvesting node. |
| /target_next_npc | /target_next_npc | Targets the next NPC. |
| /target_prev_npc | /target_prev_npc | Targets the last NPC. |
| /target_none | /target_none | Your target nothing |
| /targetpc {name} | /targetpc Sanji | You target a player called Sanji |
| /target_next_pc | /target_next_pc | Targets the next player character. |
| /whotarget | /whotarget {target a PC/NPC}<br>/whot {target} | Will return information on the character (level, race, guild, etc - unless /Anonymous).<br>If you target an NPC or monster, it will at least return that the target "is an NPC." |
| /tagtarget <br>/tag | /tagtarget skull<br>/tag skull | tag your target with a skull icon |
| /tagtarget sword<br>/tag sword | tag your target with a yellow sword icon |  |
| /tagtarget cross<br>/tag cross | tag your target with a red X icon |  |
| /tagtarget flame<br>/tag flame | tag your target with a green flame icon |  |
| /tagtarget star<br>/tag star | tag your target with a pink star icon |  |
| /tagtarget 1<br>/tag 1 | tag your target with a 1 *(works up for 1 to 6)* |  |
| /tagtarget clear<br>/tag clear | clear your target's tag |  |

## Map, waypoint and location commands

| Command | Example | Notes<br> |
|---|---|---|
| /loc | /loc | Displays your current location. |
| /loc clipboard | Displays your current location and copies it to the clipboard |  |
| /map2_show_zone_rect | /map2_show_zone_rect | Shows you the mapstyle name (internal DBG map name) and its ZoneRect, both needed for map mods. |
| /show_map_style_name | /show_map_style_name 1 | 1 Enables and 0 Disables showing the mapstyle name of every zone that is entered, also needed for map mods. |
| /waypoint<br>/way<br>/wa | /waypoint 100, 0, -100<br>/way 100, 0, -100<br>/wa 100, 0, -100<br>/way 100 0 -100 | Leads you to the location 100, 0, -100 in your current zone and a **•** will pop up on the map. <br> *the "," is optional for the coordinates.* |
| /waypoint_cancel | /waypoint_cancel | Cancels your current location. |

## User Interface

| Command | Example | Notes |
|---|---|---|
| /load_uisettings | /load_uisettings | Brings up a dialog with a list of characters. Select a character with the window (UI) laylout you want |
| /load_uisettings {name}.dat | Loads your user interface settings from the file if you had  saved with "/save_uisettings {name}.dat" command before. |  |
| /loadui | Loads your user interface skin. |  |
| /save_uisettings {name}.xml | /save_uisettings {name}.xml | Saves your user interface settings to a file *{name}.xml* under your eq2 directory with the named specified. Very useful in case you lose your hotbars look, etc. *Tip: If you can name your files combining with your toon name and date, it may be easier for you to switch back to your older profile.* |
| /savehotkeys <filename> | /savehotkeys nameofhotkeysetup | Saves your current hotkey setup to a text file so that you can load it again. |
| /loadhotkeys <filename> [0/1] | /loadhotkeys nameofhotkeysetup [clear hotkeys] | Loads the hot key setup file you specify. Optional parameter specifies if hotkeys should be cleared first. Default is to clear. |
| /load_heroic_ui <Class> | /load_heroic_ui Class | Loads the heroic hotbars to help returning players adjust to the number of combat arts/spells. |
| /open_next_hotbar | /open_next_hotbar | Opens up another Hotbar in your UI |
| /clearchattab | /clearchattab [window] [tab] | Clears chat text on the tab [tab] of window [window] (name of window) |
| /clearchat | /clearchat | Clears chat text on all tabs and windows |

## Windows

| Command | Example | Notes |
|---|---|---|
| /togglebeastlordwindow | /togglebeastlordwindow | Toggles the display of the Beastlord's Primal abilities button bar. |
| /togglesavagerywindow | /togglesavagerywindow | Toggles the display of the Beastlord's Savagery progress bar. |
| /togglechannelerwindow | /togglechannelerwindow | Toggles the display of the Channeler's abilities button bar. |
| /toggledissonancewindow | /toggledissonancewindow | Toggles the display of the Channeler's dissonance bar. |
| /togglebroker | /togglebroker | Toggles the broker window, optional way it is to open it from the eq2 button. |
| /togglethreatlistwindow | /togglethreatlistwindow | Enables the [[Threat List Window]] for all access members. |
| /toggleinfusion | /toggleinfusion | Opens the [[Equipment Infusing\|infusion]] window. |
| /research | /research | Brings up Knowledge window with [[Research]] tab in focus. |
| /welcome_info | /welcome_info<br>/wel<br>/we | Brings up the welcome screen which shows the DD and HZ among other things.<br>*Note: **/welcome** is an emote...* |

## Browser

| Command | Example | Notes |
|---|---|---|
| /browser | /browser | Opens ingame browser. |
| /browser eq2.wikia.com | Opens ingame browser on the website eq2.wikia.com |  |
| /browser eq2.wikia.com/wiki/%T | Open the article matching the name of what you have targeted. If an exact match exists, it will take you directly there! |  |
| /browser eq2.wikia.com/wiki/Special:Search?search=%T | Search for any and all articles matching the name of what you have targeted. If an exact match exists, it will take you directly there! |  |

## Exiting / Switch Character

| Command | Example | Notes |
|---|---|---|
| /camp | /camp | Sits, camps and logs out to character selection |
| /camp {character} | Sits, camps and automatically logs in named character. |  |
| /camp {server}**.**{character} | Sits, camps and automatically logs in named character on a *different* server. *(Only works for characters you see in the character selection)* |  |
| /camp desktop | Sits, camps and exits the game client. |  |
| /camp login | Sits, camps and returns to username/login screen. |  |
| /exit<br>/quit desktop | /exit<br>/quit desktop | Immediately exits and closes the game client.  *WARNING! Your character is still in-game on the server for a minute or so after doing this and CAN die if you are not in a safe area.* |
| /quit | /quit | Will quickly log off of your character and return you to the Character Select screen. *NOTE: Your character may still remain in-game for a few moments as **Linkdead** before it is fully removed from whichever zone you last were in.* |

## Account

| Command | Example | Notes |
|---|---|---|
| /show_account_features | /show_account_features | Shows all active features of the account (Expansions and Adventure packs) |

## File commands

| Command | Example | Notes |
|---|---|---|
| /do_file_commands {name} | /do_file_commands c:\show_all_windows.txt | Will execute commands from the file *c:\show_all_windows.txt*. Commands in this file **must not** have a preceding slash. |

## Sounds

Play many built-in EQ2 sounds on demand. See main article [[Playsound]].

## Screen control or visualization commands

| Command | Example | Notes |
|---|---|---|
| /cl_fullscreen {true} or {false} | /cl_fullscreen true | Will toggle the playing window to fullscreen. (Same as alt-enter.) Alt-tab on Windows will automatically toggle fullscreen off again. |
| /camera_recenter | /camera_recenter | Re-centers the camera. |

## Copy to Testserver / beta server

| Command | Example | Notes |
|---|---|---|
| /testcopy add | /testcopy add | You get added to the queue for copy to [[Test Copy (Server)]]. Your Char will get copied 1:1 to this server. |
| /beta | /beta | You get added to end of the queue for copy to [[Beta (Server)]]. Your char will get copied 1:1 to this server.<br><br>*Note: everytime you do /beta you get added to the end of the queue! => to get transfered quickly do it only once and give it "some time"* |
| /guildbetaapply | /guildbetaapply all | Needs to be done as Guildleader. Your guild get added to end of the queue for copy to [[Beta (Server)]]. Your char will get copied 1:1 to this server.<br><br>*Note: everytime you do /beta you get added to the end of the queue! => to get transfered quickly do it only once and give it "some time"*<br><br>*Use '/guildbetaapply all' to add your request to have the entire guild be copied to the Beta server.* |

## Dynamic Data information

| Command | Example | Notes |
|---|---|---|
| /weaponstats | /weaponstats | Shows the current damage of your weapons. |
| /dynamicdata | /dynamicdata stats.ability_mod | Shows your ability modifier amount |
| /show_window | /show_window mainHUD.ImpliedTarget | opens window showing who your target is targeting, good for healers and tanks |
| /show_window Custom.MyPersonalBox | opens a custom ui window called "MyPersonalBox".<br>#make a own ui Window called My_Personal_Box.xml<br>#at the <code>Page</code> section is the "name" definition of the window name that is called by the command <code>Name="MyPersonalBox"</code><br>#add "My_Personal_Box.xml" to the "eq2ui_custom.xml" |  |

## Dynamic Macro Elements

These variables cannot be used by themselves, but must be used in conjunction with a slash command. By combining these together you can create dynamic chat strings. While certain elements like "race" and "gender" are always capitalized, other variables are *case sensitive*. For example: %**S** = "He", "She", or "It" and %**s** = "he", "she", or "it".

| Command | Example | Notes |
|---|---|---|
| %a | /say Assist the tank in killing **%a** ! | Name of target's target. (ie: You say, "Assist the tank in killing {AssistTarget}!") |
| %t | /say An angry **%t** incoming!! | Name of target. (ie: You say, "An angry {targetName} incoming!!") |
| %m | /say Assist **%m**! | Name of *your* pet if you have one. (ie: You say, "Assist {petName}!") |
| %g | /say You are **%g**. | Gender of target. (ie: You say, "You are {targetGender)." |
| %r | /say You are **%r**. | Race of target. (ie: You say, "You are {targetRace}.") |
| %rt | /useabilityonplayer %rt Spellname | Will cast Spellname on the last person to send you a tell. |
| %o | /say Give **%o** hell! | Objective gender-specific pronoun for target. [him, her, it] (ie: You say, "Give {objectiveGender} hell!") |
| %p | /say What is **%p** weakness? | Possessive gender-specific pronoun for target. [his, her, its] (ie: You say, "What is {possessiveGender} weakness?") |
| %s | /say I think **%s** is AFK. | Subjective gender-specific pronoun for target. [he, she, it] (ie: You say, "I think {subjectiveGender} is AFK.") |

## Achievements

| Command | Example | Notes |
|---|---|---|
| /medals_show_all | /medals_show_all | Toggles displaying full achievement chains in the journal. The default is off displaying only the highest rank awarded for each achievement chain. |

## Mentoring

| Command | Example | Notes |
|---|---|---|
| /mentor | /mentor <playername><br>/men <playername> | You can either specify the name of a player that you are grouped with but not in the same zone with, target another player and use the command, or right-click the player (or their name in the group window) and select to mentor and mirror their character level.  When grouped with multiple players, each of a different level, this command will open a window asking you to whom you wish to mentor.<br>*Note: if you do not explicitly right-click and "mentor" another player, you will get the window for your choice of mentored level.* |
| /unmentor | /unmentor<br>/u | This cancels mentoring and chronomages' auto-mentor, returning you to your actual level. |

## Aliasing

| Command | Example | Notes |
|---|---|---|
| /alias {macro_name}:{string} | /alias Mac:assist Tankname<br>/Mac (automatically /assists Tankname) from then on | Creates a new macro/shortcut based on the {macro_name} chosen.  The text {string} is sent to the server as a command so an initial slash (/) is not required. |

## Looting

| Command | Example | Notes |
|---|---|---|
| /setautolootmode {#} | /setautolootmode 0 | Sets Auto-Loot mode for your character.<br>0 = None<br>1 = Greed or Accept<br>2 = Decline |
| /summon | /summon | Summons all nearby treasure chests that are yours to you. |

## Broker

| Command | Example | Notes |
|---|---|---|
| /start_broker_anywhere | /start_broker_anywhere | Opens Broker From Anywhere |
| /cl_mkt_price_confirmation <1-50000> | /cl_mkt_price_confirmation 250 | Set’s the Broker Purchase Confirmation to 2p 50g |

## Accessing House/Guild Hall

| Command | Example | Notes |
|---|---|---|
| /house | /house | The "effect" of this command depends on where you use it<br>#In your House or Guild Hall: Opens the House / Guild Hall management window (set Access, deposit and so on) same as you would click on the Exit Door or when you click the "House" icon<br>#In a Zone that is connected to any House or Guild Hall (no matter if yours is there or not): Opens the list of **your** houses / Guild Hall and allows you to pay upkeep or access it. *Example in Freeport /house => Access to Freeport Houses and the T3 Guild Hall in Antonica* You cannot access any House you are listed as Friend or Trustee that "feature" only works in the Guild Hall Amentiy to Player Houses |
| /summon_movingcrate | /summon_movingcrate | summons the house moving crate to your current position |

## Fast travel

| Command | Example | Notes |
|---|---|---|
| /smp pon pon_teleport | /smp pon pon_teleport | opens the fast travel map |

## Fluff Commands

| Command | Notes |
|---|---|
| /cutemode | Enlarges the head on most models. Reenter the command to return to normal. |
| /cutemode2 | Enlarges the head and feet on most models. Reenter the command to return to normal. |
| /cutemode3 | Enlarges the head, hands, and feet on most models and shrinks the overall model size. Reenter the command to return to normal. |
| /pizza | Opens the browser to delicious images of pizza. |

## Display

### Performance

| Option | Slash Command | Data |
|---|---|---|
| Performance Profile | /r_performance | [0-7] Quality<->Performance, Custom |
| Full Screen | /cl_fullscreen | [true, false] |
| Full Screen UI Resolution | /cl_screenwidth<br>/cl_screenheight<br>/cl_screenrefresh | [?-?] ie 1920 <br>[?-?] ie 1200 <br>[?-?] ie 60 |
| Multi Sample Anti Aliasing | /r_multisamples | [1, 2, 4, 8] |
| Reflections | /r_reflections | [true, false] |
| Block Windows(tm) Keys in Full Screen | /cl_disable_windows_keys | [true, false] |
| Multi-Core Support | /cl_multicore | [true, false] |
| Synchronize Refresh | /cl_refresh_sync | [true, false] |
| Triple Buffer | /cl_triple_buffer | [true, false] |
| Reuse Vertex Buffers | /r_reuse_vertex_buffers | [true, false] |
| Graphics Resolution | /r_frame_buffer_scale | [0.5-1] |
| Lighting Resolution | /r_light_buffer_scale | [0.5-1] |
| Rendering Distance | /o_max_farplane | [120-999] |
| Complex Shader Distance | /r_fast_layer_min_distance | [-1,0-500] |

### Widescreen Letterbox

| Option | Slash Command | Data |
|---|---|---|
| Letterbox Size | /cl_letter_box_amount<br><br>/cl_letter_box_frame_only_amount<br><br>/cl_letter_box_position<br><br> | {-1 <- 0 -> 1} <br> percentage of screen covered<br>{-1 <- 0 -> 1} <br> percentage of screen covered for frame position<br>{-1 <- 0 -> 1} <br> percentage of screen coverage between top and bottom |
| Letterbox Border | /letterbox_frame_visible | {0, 1} |

### Texture Resolution

| Option | Slash Command | Data |
|---|---|---|
| Texture Resolution | /cl_textureshrink | {0, 1, 2, 3, 4} Min, Low, Med, High, Max |
| Character Resolution | /cl_charactertextureshrink | {0, 1, 2, 3, 4} Min, Low, Med, High, Max |
| Character LOD Resolution | /r_texture_lodding_shrink | {0, 1, 2, 3, 4} Min, Low, Med, High, Max |

### Atmospheric Effects

| Option | Slash Command | Data |
|---|---|---|
| Enable Bloom Effect | /r_bloom | {true, false) |
| Atmospheric Bloom | /r_bloom_atmospheric | {true, false) |
| Heat Shimmer | /r_heatshimmer | {true, false) |

### Water

| Option | Slash Command | Data |
|---|---|---|
| Underwater Distortion | /r_underwaterdistortion | {true, false} |
| Water Interaction | /r_splashes | {0, 1} |
| Splash Particles | /splash_particles_enabled | {true, false} |
| Animate Procedural Textures | /r_update_procedural_textures | {true, false} |

### Particle Effects

| Option | Slash Command | Data |
|---|---|---|
| Particle Quality | /r_particle_priority | [-1,0,1,2,3] Off, Minimal, Average, High, Very High |
| Max Spell Results per Character | /num_active_spell_results | [0-8] |
| Show Particles in Reflections | /r_particlesinreflections | [true, false] |
| Show Particles in Reflections Inside Houses | /r_particlesinreflectionsinhouse | [true, false] |
| Particle Level of Detail (Far) | /r_particle_lod_scale 0.100000 | [3.0 - 0.1] |
| Particle Level of Detail (Near) | /r_point_particle_near_plane | [-3.0 - -0.0] |
| Maximum Particle Size | /r_point_particle_max_size 0.750000 | [0 - 0.75] |

### Lighting

| Option | Slash Command | Data |
|---|---|---|
| Light Quality |  |  |
| Personal Torch |  |  |
| Torch Intensity |  |  |
| Secondary Torch Light |  |  |
| Number of Lights |  |  |
| Specular Lighting |  |  |
| Additional Specular While Raining |  |  |
| Specular Lights |  |  |
| Ambient Light |  |  |

### Shadows

| Option | Slash Command | Data |
|---|---|---|
| Shadow Type |  |  |
| GPU Shadow Quality |  |  |
| GPU Shadow Darkness |  |  |
| CPU Shadows Indoors |  |  |
| Point Light Shadows (CPU) |  |  |
| Off-Screen GPU Shadows |  |  |
| Number of CPU Shadows |  |  |
| CPU Torch Shadows |  |  |
| CPU Character Shadows |  |  |
| CPU Environment Shadows |  |  |
| Off-Screen CPU Shadows |  |  |
| Specular Off in CPU Shadows |  |  |

### Model Detail

| Option | Slash Command | Data |
|---|---|---|
| Level of Detail Bias |  |  |
| Triangle Density |  |  |
| High Detail Characters |  |  |
| Low Detail Characters |  |  |

### Animation

| Option | Slash Command | Data |
|---|---|---|
| Animation Rate |  |  |
| Fast Animation Distance |  |  |
| Animation Quality |  |  |
| Cloth Simulation |  |  |
| Render Cloaks |  |  |
| Render Mounts |  |  |

### Flora

| Option | Slash Command | Data |
|---|---|---|
| Enable Flora |  |  |
| Flora Radius |  |  |
| Flora Density |  |  |

### Color Correction

| Option | Slash Command | Data |
|---|---|---|
| Overall Gamma |  |  |
| Contrast |  |  |
| Brightness |  |  |
| Red Gamma |  |  |
| Green Gamma |  |  |
| Blue Gamma |  |  |

### Camera

| Option | Slash Command | Data |
|---|---|---|
| Dynamic Field of View |  |  |

### Stereoscopic 3D

| Option | Slash Command | Data |
|---|---|---|
| Enable Stereo Driver |  |  |
| Convergence |  |  |
| Separation |  |  |
| Software Cursor |  |  |
| Software Cursor Size |  |  |
| World Depth User Interface |  |  |

### Special Effects

| Option | Slash Command | Data |
|---|---|---|
| Depth of Field |  |  |
| Ambient Occlusion |  |  |
| Sun Shafts |  |  |
