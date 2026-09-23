---
title: Lazirah Darkmoore (Untold Heroic)
type: named
in_game_name: Lazirah Darkmoore
level: '143'
difficulty: Epic x2 ^^^
zone: '[[Gerion: Realm of Conquest (Untold Heroic)]]'
location: '{{waypoint -496.03, 9.56, 286.35}}'
primary_damage: Heat, Slashing
achievement_xp: true
added_in: LU131
categories:
- Epic Named Monsters
- Epic x2 Named Monsters
- 'Gerion: Realm of Conquest (Untold Heroic) Named Monsters'
- LU131 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- Tier 15 Epic x2 Named Monsters
- Tier 15 Named Monsters
source:
  title: Lazirah Darkmoore (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Lazirah_Darkmoore_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Lazirah_Darkmoore_(Untold_Heroic)?action=history
  revision: 2022974
  revised: '2026-08-19T20:34:12Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes between stages (1-20/21+).

## Abilities

- **Conscripts of Qeynos**
- A buff that increases combat mitigation and melee multiplier for each active Conscript of Qeynos.
- **Gerion Royal Legion**
- A buff that increases ability doublecast avoidance, flurry avoidance, dodge, fervor, flurry, and flurry multiplier for each active Lucanic soldier.
- **Ealaynya's Reckoning**
- An incurable arcane that inflicts divine damage and reduces healing received.
- **Defensive Pressure**
- An elemental that inflicts increasing heat damage over time, decreases power over time, and increases all damage taken by 100%. It can only be cured while the target and Lazirah are on opposite sides of the platform.
- **Scorched Earth**: Lucanic
- An incurable elemental that kills the target when it expires, if the target is not standing on the Qeynos side.
- **Scorched Earth**: Qeynos
- An incurable elemental that kills the target when it expires, if the target is not standing on the Lucanic side.
- **Tap Strength [21+]**
- An incurable trauma that decreases strength multiplied by increments. It gains one increment every two seconds while the target and Lazirah are in opposite sections. It does not increment if the target also has Scorched Earth. Increments are reset to zero when Lazirah is hit with [[Bulwark of Order|Overpowering Barrage]]. If the target's strength is reduced to zero, the target dies.
- **Order of Execution [21+]**
- A curable curse that kills the target on expiration, or if the target is cured while any soldiers are empowered with Order of Execution.

## Strategy

The platform Lazirah is standing on is split into two sections. The west side (closer to the Claymore statue) is the Qeynos side. The east side (closer to the Soulfire statue) is the Lucanic side.

Lazirah summons loyal Lucanic soldiers or resurrected Qeynos soldiers to fight for her, depending on which section she is standing in. If 10 soldiers of any combination are active, the entire group is killed. Each soldier has its own damage protection. When Lazirah crosses from the Lucanic side to the Qeynos side (or vice versa), she summons an additional soldier.

- [[Resurrected Celestial Watch]] - cannot be damaged unless a priest is on the Qeynos side.
- [[Risen Circle of Ten]] - cannot be damaged unless a scout is on the Qeynos side.
- [[Corpus Concordium]] - cannot be damaged unless a mage is on the Qeynos side.
- [[Steel Warrior Spirit]] - cannot be damaged unless a fighter is on the Qeynos side.

Heroic Opportunities initiated by a fighter reset the reuse time of [[Bulwark of Order]].

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Lazirah)You must be on the Lucanic side of Lazirah's command post to avoid incoming death&quot; SD=&quot;change to Lucanic side&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Realm of Conquest [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "change to Lucanic side" when Lazirah casts Scorched Earth: Qeynos.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Lazirah)You must be on the Qeynos side of Lazirah's command post to avoid incoming death&quot; SD=&quot;change to Qeynos side&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Realm of Conquest [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "change to Qeynos side" when Lazirah casts Scorched Earth: Lucanic.
