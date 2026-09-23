---
title: UI Modification
type: page
categories:
- UI Modification
source:
  title: UI Modification
  url: https://eq2.fandom.com/wiki/UI_Modification
  history: https://eq2.fandom.com/wiki/UI_Modification?action=history
  revision: 481354
  revised: '2010-05-31T01:18:45Z'
  license: CC BY-SA 3.0
---

## About the UI

The Everquest II UI follows a file structure and naming convention allowing one to locate and modify only the file or files they wish to have changed without the need to have an entire duplicate of the UI directory containing the same files as the default UI.
All custom skins should be located in *%EQ2%/UI/Skinname/*. If the only modified file is the map, then that is the only file that needs to be placed into the Skinname directory.

The XML structure itself is made up to allow a mine file for each UI group, such as inventory, to include several child files that comprise the tabs that are seen in UI Builder. This is the same method that allows opening eq2ui.xml to open up all of the UI files into the editor. eq2ui.xml includes all of the main files, then those files include the smaller drilled down UI elements.

### The XML Filelist

The following are all of the .xml files included with the default UI and what pieces they contain.

- eq2ui_inventory - parent container for:
  - eq2ui_inventory_bag - The Bag display
  - eq2ui_inventory_bank
  - eq2ui_inventory_commissioned_work
  - eq2ui_inventory_container
  - eq2ui_inventory_dressingroom
  - eq2ui_inventory_examine
  - eq2ui_inventory_exchange
  - eq2ui_inventory_guildbank
  - eq2ui_inventory_guildbanksettings
  - eq2ui_inventory_highlight
  - eq2ui_inventory_inventory
  - eq2ui_inventory_loot
  - eq2ui_inventory_market
  - eq2ui_inventory_marketplace
  - eq2ui_inventory_merchant
  - eq2ui_inventory_trade
- eq2ui_journals - Contains the achievement unlocked popup window. Parent container for:
  - eq2ui_journals_active
  - eq2ui_journals_quest

### Images

All of the images that are used in the UI can be modified or replace completely to give you true control over what your skins look like.

#### Formats

Any of these image formats can be used for GUI elements:

- BMP
- DDS
- PNG
- TGA

### Sounds

Many of the in game sounds can be replaced. This can be done on a per skin or a per client basis depending on which folder you add your new sounds to:

- *%EQ2%/UI/Default/Sounds* – to replace the sounds for the client, regardless of which skin is used
- *%EQ2%/UI/<skinname>/Sounds* – to replace the sounds only for a particular skin

#### Replaceable Sounds

<table style="font-size: 90%;">

<tr align="center" bgcolor="#a0c0de">
<th style="font-size: 110%;" width="40%">Name<br></th>
<th style="font-size: 110%;">Description<br></th>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>Broadcast</td>
<td>Used for SOE broadcast messages</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>Buy_failed</td>
<td>Unable to purchase item</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>Click</td>
<td>UI click 2</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>coin_cha_ching</td>
<td>Purchased item</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ding</td>
<td>DING!!!</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>encounter_broken</td>
<td>Broken encounter</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>frontend_pressed</td>
<td>UI click 1</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>inventory_attune</td>
<td>Attune item</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>inventory_cant_equip</td>
<td>Unable to equip item</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>inventory_destroy_item</td>
<td>Destroy item</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>inventory_equip</td>
<td>Equip item</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>inventory_un_equip</td>
<td>Unequip item</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>loot_failed</td>
<td>Unable to loot item</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>moveable_object_place_failed</td>
<td>Unable to place item (ie, house items)</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>place_item</td>
<td>Successful item placement (ie, house items)</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>quest_item</td>
<td>Quest item found</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>skill_up</td>
<td>Skill increase</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>spell_gained</td>
<td>New spell learned</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>too_far</td>
<td>Too far away from target</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>trade_accept</td>
<td>Trade accept</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>trade_propose</td>
<td>Trade offer</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_chestdrop</td>
<td>Chest drop from NPC on death</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ui_friend_logoff</td>
<td>Friend logoff alert</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_friend_logon</td>
<td>Friend logon alert</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ui_guild_lvl_up</td>
<td>Guild DING</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_invite</td>
<td>Invite to group alert</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ui_joined</td>
<td>Joined group alert</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_pressed</td>
<td>UI click 1</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ui_spirit_lvl_up</td>
<td>Tradeskill pristine item creation</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_tell_receive</td>
<td>Incoming tell</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>ui_tell_send</td>
<td>Outgoing tell</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>ui_tradeskills_lvl_up</td>
<td>Tradeskill DING</td>
</tr>
<tr align="left" bgcolor="#cef2e0">
<td>war_drum</td>
<td>Slayer update</td>
</tr>
<tr align="left" bgcolor="#c0e0fe">
<td>waypoint_activated</td>
<td>Waypoint alert</td>
</tr>
</table>

## Modifying the UI Using UIBuilder

### Starting Up

After having installed [UIBuilder] you need to locate and open UIBuilder.exe from the installed directory, typically *%EQ2%/UIBuilder/*. Once opened, load *%EQ2%/UI/eq2ui.xml*
