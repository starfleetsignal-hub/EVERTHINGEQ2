---
title: Veru the Combiner
type: named
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Unknown: Voidborn Emergence (Raid)]]'
location: '{{waypoint -1101.49, -40.33, 1059.64}}'
primary_damage: Crushing, Poison
achievement_xp: true
added_in: LU131
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- LU131 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- 'The Unknown: Voidborn Emergence (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Veru the Combiner
  url: https://eq2.fandom.com/wiki/Veru_the_Combiner
  history: https://eq2.fandom.com/wiki/Veru_the_Combiner?action=history
  revision: 2032074
  revised: '2026-10-12T20:36:23Z'
  license: CC BY-SA 3.0
---

Veru the Combiner is a Tier 3 raid boss. She gains an additive advantage for each player below 22 and has a hard time limit of 30 minutes.

## Statistics

- Flurry Avoidance 550.0
- Ability Doublecast Avoidance 900.0
- Resolve 13,670

## Abilities

- **Voracious Protection**
- A buff that enhances Veru's ability to dodge while any [[Voracious protector|voracious protectors]] are active.
- **Void-Cloaked II**
- A buff that gives Veru a chance to trigger Negative Static, which deals magic damage and reduces fervor.
- **Surging Combination**
- An incurable elemental deals increasing slashing, heat, and mental damage to health and power over time. High crushing damage is added if the target is also under the effects of Focused Combination.
- Mindwracking Influence III
- An incurable arcane that causes all abilities to cost additional power.
- **Whirling Magics III**
- A curable arcane that deals increasing arcane damage over time and increases physical and noxious damage from all sources.
- **Whirling Maelstrom III**
- **Whirling Mindstorm III**
- A curable noxious that deals increasing poison damage over time to health and power and increases physical and arcane damage from all sources.
- **Whirling Drain III**
- A curable arcane that drains health over time. The closer to Veru the target is, the more health that is drained.
- **Combined Elements III**
- A curable elemental that deals increasing cold and heat damage over time and increases physical damage from all sources.
- **Prepared Stare**
- An incurable trauma that marks Veru's current target. If the target already has Prepared Stare, the target is killed, and Veru heals for 25%.
- **Confounding Pain**
- A curable curse with 7 increments that prevents the target from casting hostile abilities and forces the target to the bottom of the hatelist. If it expires, the entire raid is killed.
- **Counfounded**
- An incurable curse that reduces the maximum power pool of the target, prevents casting hostile or beneficial spells, and prevents the target from moving. This effect is applied to targets within 18 meters of Veru while Confounding Punishment is active.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

When the raid engages Veru, a purple dome appears around him. Players may enter the dome, but are unable to leave the dome. Veru leashes if pulled outside this dome.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Veru)commits (?&amp;lt;Player&amp;gt;\w+) to memory&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Voidborn Emergence [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <player>" when Veru casts Prepared Stare.
