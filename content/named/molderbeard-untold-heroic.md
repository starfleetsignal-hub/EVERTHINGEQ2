---
title: Molderbeard (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Molderbeard
level: '143'
difficulty: Heroic ^^^
zone: '[[The Unknown: Sacrificial Pursuits (Untold Heroic)]]'
location: Spore Fields {{waypoint -1022.99, 26.71, 1049.50}}
primary_damage: Mental, Poison
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Unknown: Sacrificial Pursuits (Untold Heroic) Named Monsters'
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: Molderbeard (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Molderbeard_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Molderbeard_(Untold_Heroic)?action=history
  revision: 2028525
  revised: '2026-09-08T21:04:08Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Moldy Gills**
- A buff that has a 10% chance to cast Spiked Spores when damaged. Spiked Spores stifles the target, inflicts piercing damage over time, decreases power over time, and knocks the target back in a random direction when it expires.
- **Mycelial Network**
- A buff that increases combat mitigation, ability doublecast avoidance, and flurry avoidance for each active Bloom. At 6 increments, Molderbeard kills the entire party.
- **Moldy Breath**
- A curse that increases all damage done to targets by 100%. Target cannot survive multiple Moldy Breaths at once. It cannot be cured while afflicted with a Bloom effect.
- **Moldermez**
- A curable elemental that mesmerizes all targets and decreases power over time.

## Strategy

Throughout the fight, Molderbeard plants large mushroom caps. Each mushroom increments Mycelial Network, provides a buff to Molderbeard, and provides a detriment to the party. Each mushroom cap can only be targeted by a certain class. If 4 blooms are up simultaneously, Molderbeard kills the entire party.

- Sporecrux Cap (yellow), targetable by priests, casts Wilting Bloom
  - Applies a buff that reduces incoming arcane damage by 70% and increases mental damage every 3 seconds. It can be dispelled by arcane means.
  - Applies an incurable arcane that inflicts divine damage over time and reduces healing received.
- Sporepox Cap (green), targetable by scouts, casts Mephitic Bloom
  - Applies an incurable noxious that inflicts poison damage over time, decreases casting speed by 100%, and reduces the base trigger chance of abilities.
- Sporespawn Cap (blue), targetable by mages, casts Hallucinogenic Bloom
  - Applies a buff that reduces incoming elemental damage by 70% and increases cold damage every 3 seconds. It can be dispelled by elemental means.
  - Applies an incurable elemental that inflicts heat damage over time, decreases power over time, and prevents the target from seeing Molderbeard.
- Sporerage Cap (red), targetable by fighters, casts

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Molderbeard)sucks in air\. Everyone in front&quot; SD=&quot;frontal&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Sacrificial Pursuits [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "frontal" when Molderbeard casts Moldy Breath.
