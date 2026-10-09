---
title: 'The Fabled Ssraeshza Temple: Inner Sanctum (Solo)'
type: instance
release: '[[Revelations of Malice]]'
levels: 135+
access: Solo-Group
entered_from: '[[Gerion, Hold of D''Lere]]'
players: 90 minutes-3 days
success_lockout: 90 minutes
failure_lockout: 90 minutes
categories:
- Gerion, Hold of D'Lere Instances
- IZone pages that need EQ2MAP uid
- Instances
- Persistent Instances
- Revelations of Malice
- Revelations of Malice Instances
- Solo-Group Zones
- Zones
source:
  title: 'The Fabled Ssraeshza Temple: Inner Sanctum (Solo)'
  url: https://eq2.fandom.com/wiki/The_Fabled_Ssraeshza_Temple:_Inner_Sanctum_(Solo)
  history: https://eq2.fandom.com/wiki/The_Fabled_Ssraeshza_Temple:_Inner_Sanctum_(Solo)?action=history
  revision: 2030960
  revised: '2026-10-05T09:53:38Z'
  license: CC BY-SA 3.0
---

## Names

**These descriptions will cover both the [Solo] AND the [Heroic] versions of these fights (they're *very* similar) due to mutli-player mechanics activating/deactivating based on the number of players present in the party during the fights. (Solo can be run with 1 OR 2 players (or 1 player + 1 mercenary) resulting in some mechanics being skipped if only 1 actual player is present. Mercs do not generally count towards player-count when determining if mechanics are skipped)**<br>

- **Pox Xin'Kaas** {{waypoint 379, -88, 67}} on top of the plateau in the middle of the first room
  - [Tank & Spank] Boss is stationary but has a frontal cone attack, tanks/party should position acordingly.
    - At 75% and 50%, starts a slow cast and ports the group to a sealed/dark area underneath the zone (representing a 'dream state' that players must be 'woken' from).
      - While the active party is down in the 'dream' area, an unconscious 'copy' of each player's body will be left behind at the boss's feet during this phase.  While in the dream realm adds will spawn (1 for each member of the group). As each add is defeated, each remaining add will grow in strength.
      - Eventually, a member of the team will 'snap out of it' and be returned to the platform up top.  This person must then begin clicking on each remaining 'unconsious' team member above to 'awaken' them and return them to the fight also.  Awoken/returned players may assist with remaining unconscious teammates as they themselves are brought back.  Any party member that remains in the 'dream realm' for too long is automatically defeated *(death prevents do not block this)*.
      - *NOTE: This 'wake your teammates' mechanic is skipped if only 1 player is in the party, the single player is simply returned to the boss after a period of time in he dream realm - mercs do **not** count towards party totals for this phase*
    - At 25% Boss starts a long-cast knockback that launches players radially out from the direction of the boss - the party may avoid this by several means:
      - Burning the boss to 0% before it completes
      - Avoid via line-of-sight down the ramp before it completes
      - All players may stack up in the same place so that everyone get launched in the same general direction off the platform. *(Wait until the cast actually starts, otherwise non-tanks risk getting hit by the frontal beforehand)*  If the boss completes the knockback effect, it will no longer be stationary and will freely pursue the hate list to wherever they land, and finish the fight there (tank still needs to position frontal away from party).
- **Stonefang** {{waypoint 227, -101, 55}} through the crack in the wall after killing Pox Xin'Kaas
  - At increments, there will be a yellow warning that "Stonefang starts shedding his stony scales! The Sanctum's walls should provide refuge!"
    - Players MUST avoid this effect by moving out of line-of-sight of the boss or be instantly defeated *(death prevents to do trigger as this is not a death, rather a standard 'fail' condition on the part of the player, which bypasses all death-prevent mechanics)*.  The only way to avoid this is by leaving the central chamber and hiding behind the outside wall or moving quickly into one of the two side chambers and hiding behind a wall there.
    - Note that while players are *not* in the main chamber with the boss, additional adds will continuously spawn.  This forces the players to spend as little time 'hiding' as possible, otherwise they risk getting overrun by continuous adds if they try to hide too soon or for too long.
    - ACT Trigger: *<Trigger R="starts shedding his stoney scales!" SD="hide line of sight" ST="3" CR="F" C="The Fabled Ssraeshza Temple: Inner Sanctum [Heroic]" T="F" TN="" Ta="F" />*
  - Has a permanent stoneskin (-50% damage) versus Physical damage.  Use 'damage changers' (consumables, Ascension stances, etc) to move your damage type away from physical, or depend on your non-physcial damage teammates to DPS the fight in your stead.
- **Kessatras Sonssiu** {{waypoint 224, -83, 44}} above Stonefang through the left archway and up the ramp
  - Tank/Burn phase.
    - Periodically long-casts fear - use Fear adornment if available - it can be cured, however.
  - "Illusion" Phase (***NOTE:** This phase 'starts' but then is immediately skipped if only 1 person is in the party*)
    - Boss will then long-cast 30 **Non-Aggro** illusions across the two middle chambers where it is being fought.
      - 3 rows of 5 illusions in each room (3x5x2 = 30) The 'true' boss is hiding amongst the illusions (so, technically 29 illusions + 1 boss)
      - Player(s) must click the illusions to attempt to 'find' the real boss.  If a player clicks a 'wrong' illusion, the clicked illusion becomes **Aggro** and attacks the party.  So don't just click randomly, otherwise adds will get out of control.  Try to only click on the 'real' boss once by following visual clues
      - Successfully clicking on the 'real' boss will immediately dispel any remaining non-aggro illusions (Aggro'd illusions will remain)
    - If not 'skipped', this will be a vision interrupt.
      - All players' screens turn white.
      - After that clears, 1 player's screen will remain purple instead. This player is being 'mind-invaded' by the boss and cannot act, but the mental invasion is two-way, allowing the controlled player to 'share' vision with the boss; as such, their own 'camera' is then centered on the 'true' boss, allowing them to 'direct' any remaining players (via voice or chat) to that real boss.
      - Other visual clues also exist for non-controlled players.  The 'real' boss will occasionally 'twitch' and also occasionally 'shimmer' with a purple aura, allowing vigilant players to spot this.  Alternatively, while regular pets are 'fooled' by the illusion just like players, 'dumbfire' pets (from Brigands, Necros, Conjurors, etc) are NOT fooled by it.  Any dumbfire pets that are cast before the long-cast illusion completes will move directly to the correct illusion during (and after) the white screen and are generally easy to follow. Players can simply follow those dumbfires and click on the resulting correct illusion.
- **Kesa'Tra Xon'Xiu** {{waypoint 243, -65, 56}}
  - To spawn the named, you have to destroy all the Xin'Kass Portals on this level.  Whilst the portals are alive, they will spawn "a Telaris Va'Shen" when you are near to a portal. Burn each portal and clear the add before moving on to the next portal. Each Telaris Va'Shen get a incremental stacking Flurry buff "Rise of Vin'Shyan" the longer they are up, so burn through each one separately before moving onto the next portal.
    - *Note: (Possible bug?) Buff doesn't seem to have an upper limit (I let it count up to 240 - and it was doing 400+ billion damage), it just continues incrementing every c.5 seconds, so if you die whilst these Va'Shen are alive, your encounter might be broken and beyond salvage. [needs clarification]*
  - Once all the portals are destroyed, the named will appear in the centre of the room.
  - Named periodically becomes immune to damage and starts zapping himself all over the room, leaving behind 'echoes' in each spot they were standing.  Eventually these echoes become targetable and begin moving slowly towards the boss.  Any echoes that reach the boss will heal it by 5%-10%.  These are quite fragile once they start moving and may be destroyed via normal damage abilities or by simply running (NOT walking) through them, causing them to shatter. *Note: Players near them when they shatter will take some damage, so 'shatter' with care.*
  - Periodically, Luclin-era shades will surround the central circle and begin slowly moving inward. The closer they get, the more damage the party takes.  They are relatively weak and 1 or 2 AOEs from most any class will clear them quickly.  *(Allegedly, if they reach the center, the party dies, but they are so weak and die so easily there do not appear to be any reports of this actually happening in this Fabled version [Solo] or [Heroic]... yet)*
- **Arch Lich Rhag'Zadune** {{waypoint 110, -49, 54}}
  - There are basically 2 stages of this encounter.
    1. Warrior and two Summoners:
       - The order of summoners is 1: Vhen 2: Des 3: Toz (partial names) - get close enough to the Epic mob to activate the summoners. He emotes, and then they are active.
       - Stay out of the center of the room. If you enter the circle in the center, you'll get tossed away and either rooted or stunned for a bit.
       - When you're attacking the summoners, they summon portal defenders. Just stay on the summoners and AE the portal guys down. If your dps is low, you might want to focus on the portal guys just to prevent yourselves from being overrun.
    1. Rhag'Vozgath and Rhag'Yalzzen pop after all three summoners are down.
       - They spawn with very little health. It's probably wise to focus on Rhag'Yalzzen first since he gets this incremental reflecting buff.
  - (Note: In the **[Heroic]** version of this encounter, the boss opens with a **Non-standard** barrage effect.  (ACT users will need to watch for the red text non-standard barrage message in chat, as the 'standard' barrage trigger will *not* notifiy of this)  This must be countered like any other barrage - by a Fighter's [[Bulwark of Order]]
    - **[Heroic]-only:** There is a curse that is also cast at this time.  If that curse is cured (or other fight mechanics interfere), it will immediately jump to a new target, triggering an additional Barrage, whether the Fighter's bulwark cooldown has completed or not.  Do not cure until the fighter's Bulwark has reset.
    - *The [Solo] version does not appear to have any penalties for curing detriments during this fight.*
    - ACT TRIGGER (optional): *<Trigger R="The Arch Lich breaks from the portal" SD="Bulwark - wait for cure" ST="3" CR="F" C="The Fabled Ssraeshza Temple: Inner Sanctum [Heroic]" T="F" TN="" Ta="F" />*
