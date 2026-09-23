---
title: The Unseen
type: named
expansion: Rage of Cthurath
in_game_name: the Unseen
race: Evil Eye
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Unseen Horrors (Raid)]]'
location: Unseen Observatory {{waypoint -657.51, 284.04, -370.45}}
primary_damage: Crushing, Poison
drops:
- '[[Fetid Bracelet of Unseen Horror]]'
- '[[Fetid Coif of Unseen Horror]]'
- '[[Fetid Helm of Unseen Horror]]'
- '[[Fetid Hood of Unseen Horror]]'
- '[[Fetid Barbute of Unseen Horror]]'
- '[[Remnant of the Unseen Horror]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Evil Eye
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Oogothl Sprawl: Unseen Horrors (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: The Unseen
  url: https://eq2.fandom.com/wiki/The_Unseen
  history: https://eq2.fandom.com/wiki/The_Unseen?action=history
  revision: 2028796
  revised: '2026-09-11T01:45:37Z'
  license: CC BY-SA 3.0
---

the Unseen is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Void-Cloaked**
- A buff that gives a chance to trigger Negative Static on an attacker.
- **Unseen Surges**
- An incurable arcane that deals increasing magic, poison, and heat damage to health and power over time.
- **Mindwracking Influence II**
- An incurable arcane that causes all abilities to cost additional power.
- **Negative Static**
- A curable arcane that interrupts the target, deals magic damage, decreases fervor, and decreases accuracy.
- **Unseen Arcanum**
- A curable arcane that deals increasing arcane damage and increases elemental and noxious damage from all sources.
- **Unseen Poisons**
- A curable noxious that deals fast ticking poison damage and increases elemental and arcane damage from all sources.
- **Unseen Travels**
- A curable  that deals increasing heat, magic, and poison damage, and reduces in-combat movement speed. This spell can be blocked by area effect blockers.
- **Monumental Misstep**
- A curable noxious that deals diesease damage which grows based on how low the Unseen's health is. While applied, the target cannot use beneficial abilities. If any player runs out of power, every player in raid is hit with Monumental Misstep.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

the Unseen summons two types of minions into the fight. A [[Summoned presence]] casts a curable arcane called Snap Attention that forces the player to target the presence. If a third summoned presence spawns (while two are already active), the Unseen heals 25%. A [[Void-borne Emergence]] begins healing the Unseen 30 seconds after it joins the fight. If a second Void-borne joins the fight, the entire raid is killed.

the Unseen emits a frontal cone of Unseen energy, displayed as a yellow-orange fire effect. Any [[Summoned presence]] that gets caught in the energy is killed and heals the Unseen. The cone targets a random player, which could be behind him at the time.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Unseen)I see YOU!&quot; SD=&quot;Move Cone&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;T&quot; TN=&quot;Next move&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "move cone" when the Unseen emits a cone of energy.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Unseen)is summoned into the fight&quot; SD=&quot;kill add&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill add" when a [[Summoned presence]] or a [[Void-borne Emergence]] joins the fight.
