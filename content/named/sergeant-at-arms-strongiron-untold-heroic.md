---
title: Sergeant-at-Arms Strongiron (Untold Heroic)
type: named
in_game_name: Sergeant-at-Arms Strongiron
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Realm of Conquest (Untold Heroic)]]'
location: '{{waypoint -367.87, 2.03, 352.17}}'
primary_damage: Slashing, Cold
achievement_xp: true
added_in: LU131
categories:
- 'Gerion: Realm of Conquest (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- LU131 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: Sergeant-at-Arms Strongiron (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Sergeant-at-Arms_Strongiron_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Sergeant-at-Arms_Strongiron_(Untold_Heroic)?action=history
  revision: 2022971
  revised: '2026-08-19T20:32:51Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes between stages (1-20/21+).

## Abilities

- **Master-at-Arms-Length**
- A buff that casts Leveraged Strike on any combat or spell hit.
- **Bone-Bound Armor**
- A buff that increases combat mitigation, ability doublecast avoidance, and flurry avoidance multiplied by increments. Increments can be removed through [[Bulwark of Order|Overpowering Barrage]]. Each successful dispell spawns a piece of animated armor.
- **Balanced Bulwark**
- A buff that has a 50% chance to trigger Shield Surge when damaged. The chance may be delayed by turning Strongiron 180 degrees.
- **Shield Surge**
- A buff that increases block chance. It increments each time Balanced Bulwark triggers, to a maximum of 20. When it expires, Strongiron casts Shield Barrage which inflicts immitable crushing damage multiplied by increments, unless targets are protected by [[Bulwark of Order]].
- **War Torn**
- An incurable arcane that inflicts magic damage over time, decreases power over time, and casts Defensive Breach, which inflicts crushing damage.
- **Leveraged Strike**
- An incurable trauma that deals slashing damage multiplied by increments and increases all damage done to target by 20% multiplied by increments. The spell terminates if the target remains beyond 3 meters of Strongiron for at least 6 seconds.
- **Grave Error**
- A curable curse that lands on (2/3) players simultaneously. The flavor text of the spell includes the epitaph "Here Lies <Name>, <Race> <Class>, killed in Gerion...". If the name, race, and class listed match that of the target, curing the curse cures all curses. If the race and class listed do not match the target, curing the curse kills the target. The target is also killed if the curse expires.
- **Shield Press [21+]**
- A curable elemental that inflicts heat damage over time, decrease power over time, decreases the speed of the target, and teleports Strongiron to the target.

## Strategy

Strongiron summons [[A Risen Royal Antonican Guard]] throughout the fight, which cast Oathbound, which forces the player to target the Guard. Each Guard has a 50% chance to absorb all damage from the target of Oathbound.

Fighter-initiated heroic opportunities reset the reuse time of [[Bulwark of Order]].

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Strongiron)SHIELD BARRAGE&quot; SD=&quot;Bulwark&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Realm of Conquest [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Bulwark" when Strongiron casts Shield Barrage.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Strongiron)Someone's soon-to-be grave's in error&quot; SD=&quot;Check curse, cure correct&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Realm of Conquest [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Check curse, cure correct" when Strongiron casts Grave Error.
