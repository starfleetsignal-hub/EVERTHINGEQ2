---
title: The Dogmadog (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: The Dogmadog
race: Cerberus
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Ark of Ascension (Untold Heroic)]]'
location: Temple of the Overlord {{waypoint 0.61, -1.17, -429.05}}
primary_damage: Disease, Piercing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Cerberus
- 'Gerion: Ark of Ascension (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: The Dogmadog (Untold Heroic)
  url: https://eq2.fandom.com/wiki/The_Dogmadog_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/The_Dogmadog_(Untold_Heroic)?action=history
  revision: 1990696
  revised: '2026-03-14T21:10:56Z'
  license: CC BY-SA 3.0
---

## Abilities

- **All Bark and No Bite**
- A frontal that disables threat transfers on the target.
- **Tenets of Terror**
- A buff that begins with 89 increments. It loses one increment every time a hostile ability hits The Dogmadog. When it reaches zero, the caster who removed the final increment is cursed with Terror-Stricken. This buff is reapplied throughout the fight.
- **Terror-Sticken**
- A curable curse that fears the target and kills the victim on expiration.
- **Heretical Infestation**
- A buff that can be dispelled through elemental means, which summons 3 [[A heretick|hereticks]]. The buff is immediately reapplied.
- **Ferocious Feast**
- An attack that hits all players for massive damage. Each living heretick reduces the amount of damage taken by 40%.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dogmadog)readies a(?**: nother)? boisterous bark&quot; SD=&quot;frontal&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion: Ark of Ascension [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "frontal" when The Dogmadog begins casting All Bark and No Bite.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dogmadog)The Dogmadog hungers&quot; SD=&quot;summon ticks&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Ark of Ascension [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "summon ticks" when The Dogmadog begins casting Ferocious Feast.
