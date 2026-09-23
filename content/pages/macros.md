---
title: Macros
type: page
categories:
- Macros
source:
  title: Macros
  url: https://eq2.fandom.com/wiki/Macros
  history: https://eq2.fandom.com/wiki/Macros?action=history
  revision: 1846674
  revised: '2024-12-19T07:01:13Z'
  license: CC BY-SA 3.0
---

EverQuest II has an in game Macro system which allows you combine several commands.<br>

## possible with macro

- Use Commands from [[Slash Commands]]
- Equip Gear
- cast spells and define 1 spell that shall be cast first
- Display the reuse of 1 spell, by dragging the spell into the icon slot
- say something in a channel (say, gsay, guild, tellchannel)
  - When you macro something to a channel, it's better to use the "tellchannel mychannel" than just the channelnumber.
  - *You may or may have not seen misstells of raid parses in normal channels ;), most likly they used a channelnumber and not the channelname*

## Not possible with macro

- it is NOT possible to run another macro from within a macro.
- it is NOT possible to add a pause into a macro
- it is NOT possible to make a macro repeat itself automatically

## Useful Macros

### [[Alcohol Tolerance]]

- Raise your [[Alcohol Tolerance]] quickly by drinking lot of [[Dwarven Ale (Alcoholic)]]
  - Buy 300 [[Dwarven Ale (Alcoholic)]]
  - Make 10 lines with "use item" and drag the [[Dwarven Ale (Alcoholic)]] into each line
  - Use the macro 30 times you drink the 300 [[Dwarven Ale (Alcoholic)]]
  - In case you ain't hit the cap buy more and use the macro.
  - *Note: Losing a duel gets you sober right away*

### Chain cast 2 Spells/Abilties

- make 2 lines with use "Spell/Ability"
  - Place a Spell or Combat Art into each line and flag one as "Primary"
  - The "Primary" Spell/Ability" will start casting and the other one will be "queued"

### [[Advanced Combat Tracker]]

- The [[Advanced Combat Tracker]] (shot ACT) its basically setup to parse fights and export the results to "act-export.txt"
- The advantage of the macro is that you can show the whole parse and not only the first 255chars when you paste it.
- make a macro with the command "/do_file_commands act-export.txt"
- You change the name of the file "act-export.txt" in ACT, for example to "actdps.txt".
- You can export various kinds of export at once, for example
  - a heal parse as "act-hps.txt"
  - a dps parse as "act-dps.txt"
  - a power feed parse as "act-powerfeed.txt"
    - Sugguestion make 1 marco for each parse

### assist

- make a macro with the command "/assist <name of toon>"

### Balanced Synergy

- make a macro with
  - the command "/gsay Casting Synergy"
  - the "use Spell/Ability" [[Balanced Synergy]]

## external Macro guides

- [eq2 Forum : Creating Macro's - a basic guide](https://forums.daybreakgames.com/eq2/index.php?threads/creating-macros-a-basic-guide.461740/)
