---
title: Nazkun (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Nazkun
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Ark of Ascension (Untold Heroic)]]'
location: Triforium of Servitude {{waypoint -150.93, 23.68, -469.29}}
primary_damage: Cold, Slashing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- 'Gerion: Ark of Ascension (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: Nazkun (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Nazkun_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Nazkun_(Untold_Heroic)?action=history
  revision: 1991333
  revised: '2026-03-20T04:39:14Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21+).

## Abilities

- **Sufferance**: Mind
- An incurable detriment that wounds the caster's power pool by 10% per increment. Increments are gained by clicking on the eastern altar on the main floor. Across the group, a combined (6/12) increments are required to see Nazkun. This spell persists through death and can be canceled.
- **Overlord's Tithe**
- An incurable noxious that deals poison damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Tenets of Servitude**
- An incurable elemental that procs when the target surpasses (80%/70%) power, which casts Power Struggle.
- **Power Struggle**
- A curable curse that decreases fervor for each increment. The duration increases each time a spell is cast.
- **Unyielding Pain**
- An incurable detriment that deals significant damage to its target. It can be removed through a fighter's [[Intercept]].
- **Withering Way (Green)**
- A buff that increases flurry every 4 seconds, dispels physical and noxious hostile effects every 4 seconds, and reduces physical and noxious damage by 90%. The buff is removed when a player lights a number of torches equal to the number of increments, all within a single alcove.
- **Withering Way (Blue)**
- A buff that increases fervor every 4 seconds, dispels elemental and arcane hostile effects every 4 seconds, and reduces elemental and arcane damage by 90%. The buff is removed when a player lights a number of torches equal to the number of increments, all within a single alcove.
- **Withering Way (Red)**
- **Mind Wipe (21+)**
- A curable curse that kills the target if also a victim of Slave Mind, or when it expires.
- **Slave Mind (21+)**
- A curable elemental that kills the target if cured by any class other than a mage.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;Intercepting (?&amp;lt;Player&amp;gt;\w+)'s damage would be beneficial&quot; SD=&quot;intercept ${Player}&quot; ST=&quot;3&quot; CR=&quot;F&quot; C=&quot; General&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>**
- Calls "intercept <player>" when Unyielding Pain is cast.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Nazkun)slowly enslaves your mind&quot; SD=&quot;mage cure&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Ark of Ascension [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "mage cure" when Slave Mind is cast.
