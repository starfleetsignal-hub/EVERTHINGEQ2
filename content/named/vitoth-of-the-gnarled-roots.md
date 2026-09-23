---
title: Vitoth of the Gnarled Roots
type: named
expansion: Scars of Destruction
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: Sultry Dunes {{waypoint 255, 0, -188}}
health: 279 Quadrillion
primary_damage: Crushing
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Vitoth of the Gnarled Roots
  url: https://eq2.fandom.com/wiki/Vitoth_of_the_Gnarled_Roots
  history: https://eq2.fandom.com/wiki/Vitoth_of_the_Gnarled_Roots?action=history
  revision: 1867713
  revised: '2025-04-04T01:42:54Z'
  license: CC BY-SA 3.0
---

Vitoth of the Gnarled Roots is a T1 raid boss. He spawns after each of the eight Fireant Mounds through the zone have been destroyed. The mounds only take damage when their companion fireant guards have been killed.

- Mandoko Jungle at {{waypoint -77.96, 126.30, 41.27}}
- Sultry Dunes Gate at {{waypoint 123.37, 132.12, 121.27}}
- Sodden Uplands at {{waypoint 311.90, 91.50, 393.33}}
- Sodden Uplands at {{waypoint 557.78, 69.74, 364.16}}
- Dankmar Swamp at {{waypoint 587.98, 5.74, 707.99}}
- Dankmar Swamp at {{waypoint 154.85, 5.01, 554.83}}
- Dankmar Swamp at {{waypoint -12.51, 14.71, 571.30}}
- Port Woe at {{waypoint -17.04, 6.09, 388.60}}

## Statistics

- Max Health: 279,488,558,080,816,160
- Wisdom: 4,106
- Resolve: 10,795
- Bleedthrough: 50
- Combat Mitigation: 1,553,045
- Potency: 44,500.0
- Casting Speed: 100.0
- Reuse Speed: 100.0
- Damage Per Second: 11,500.0
- Attack Speed: 2,500.0
- Multi-Attack Chance: 0.0
- Strikethrough: 65.0
- Accuracy: 150.0
- AE Auto-Attack Chance: 10.0
- Weapon Damage Bonus: 175.0
- Flurry Avoidance: 410.0
- Ability Doublecast Avoidance: 490.0

## Abilities

- **Noxious Storm**
- A curable noxious that deals fast ticking poison damage to targets within 35 meters and increases physical damage from all sources.
- **Elemental Storm**
- A curable elemental that deals fast ticking elemental damage and increases physical damage from all sources to targets within 25 meters.
- **Surging Elements**
- An incurable elemental that deals increasing elemental damage to health and power over time.
- **Primal Purge**
- A curable trauma that deals physical damage and increases elemental and mental damage from all sources to targets within 35 meters.
- **Flamewrithe**
- An incurable curse that kills the entire raid when it expires. It can be removed by standing in the elemental circle.
- **Mindwrithe**
- An incurable curse that kills the entire raid when it expires. It can be removed by standing in the arcane circle.
- **Infected Earth**
- A buff that decreases damage taken from all sources for each Fireant Mound in the area.
- **Disturbed Elements**
- A buff that increases damage potential for each "Earthen Ant Digger(s)" in the area.
- **Bolstered Elements**
- A buff that increases outgoing damage and decreases incoming damage. If Vitoth is damaged too much while this is active, he gains the ability to deathtouch his current target.
- **Barrage**
- An unnamed spell that can only be countered with [[Bulwark of Order]].

## Strategy

Fireant Mounds pop up continuously throughout the Sultry Dunes. Each Mound has three fireant hillguards that must be defeated before the Mound can take any damage. If there are more than 3 Fireant Mounds at the same time, then each additional Mound heals Vitoth for 10% of his max health.

Between the arrival of each Fireant Mound, a devoted earthen ant joins the fight. At 50%, this ant gains Vitoth's Decree, a dispellable buff, as it prepares to sacrifice itself to Vitoth. If the ant dies before this buff is dispelled, then Vitoth heals.

Vitoth continuously places circles on a random raid member, alternating between an elemental circle and an arcane circle. The elemental circle has a red-orange tone and rocks erupting from the center. The arcane circle has a darker purple tone with black clouds in the center. Players standing within these circles without the appropriate curse (Flamewrithe and Mindwrithe, respectively) are killed.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;lt;Vitoth&amp;gt;bolsters himself)&quot; SD=&quot;Stop DPS&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Says "stop DPS" when Vitoth casts Bolstered Elements on himself.
