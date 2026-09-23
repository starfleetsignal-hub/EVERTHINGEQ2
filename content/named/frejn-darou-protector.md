---
title: Frejn, Darou Protector
type: named
expansion: Rage of Cthurath
race: Gruengach
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Yon Gorroth: The Infinite Abyss (Raid)]]'
location: Managauth Fields {{waypoint 213.91, 65.00, -236.65}}
primary_damage: Mental
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Gruengach
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Yon Gorroth: The Infinite Abyss (Raid) Named Monsters'
source:
  title: Frejn, Darou Protector
  url: https://eq2.fandom.com/wiki/Frejn,_Darou_Protector
  history: https://eq2.fandom.com/wiki/Frejn,_Darou_Protector?action=history
  revision: 2000644
  revised: '2026-05-04T03:44:09Z'
  license: CC BY-SA 3.0
---

Frejn, Darou Protector is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Conscription of Consequence II**
- A buff that gives a chance of triggering Bolt of Consequence, which deals cold damage and interrupts the attacker, and Forced Consequence, which increases offensive ability.
- **Surging Horns**
- An incurable trauma that deals increasing physical, poison, and magic damage to health and power over time.
- **Overbearing Influence II**
- An incurable trauma that makes power usage also cost health based on the amount of power used.
- **Arcane Whirlwind**
- A curable arcane that deals fast ticking arcane damage and increases physical and noxious damage from all sources.
- **Loyal Warpwolves**
- A buff that decreases damage taken from all sources for each [[Trained Attack Warpwolf]] in the encounter. For each additional wolf beyond 2, each new wolf heals Frejn slightly.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].
- **Siphon Fortitude**
- A curable arcane that drains health over time until cured. The closer to Frejn the target is, the more health that is drained. For each target hit by this spell, Frejn gains an increment of Bolstered Fortitude which increases outgoing damage potential. If cured quickly enough, players hit by the spell are not counted for Bolstered Fortitude.
- **Ramming Headbutt**
- A curable trauma that deals growing physical damage. When removed, it triggers Traveling Migraine to all allies within 25 meters, which deals much faster physical damage and slows movement speed. If Traveling Migraine lands on the same player twice, that player dies.
- **Flame Burst II**
- A curable elemental that deals increasing heat damage. This ability can be blocked by Area Effect blockers.
- **Eye Gouge**
- A curable noxious that deals growing noxious damage. When cured, all allies within 8 meters are hit with Blinding Gouge, which interrupts the target, inflicts increasing poison damage over time, decreases power over time, decreases haste, and blinds the target. If Blinding Gouge lands on the same player twice, that player dies. Curing this spell causes a yellow warning text, even if no players are caught by Blinding Gouge.
- **Snap Jaws**
- A curable arcane that forces all players within 10 meters to target the [[Trained Attack Warpwolf]].
- **Noxious Whirlwind**
- A curable noxious that deals fast ticking poison damage and increases physical and arcane damage from all sources.
- **Strategic Misdirection**
- A curse that is incurable while the player is standing too close to Frejn or his Doomclock.
- **Prepared Stare**
- An incurable trauma that marks Frejn's current target. If the player receives a second Prepared Stare, they are killed, and Frejn heals for 25% of his maximum health.

## Strategy

Frejn summons [[Trained Attack Warpwolf|Trained Attack Warpwolves]] periodically. Each wolf decreases Frejn's incoming damage. Each wolf beyond 2 slightly heals Frejn.

Frejn attempts to activate an ancient device periodically. This "device" is a floating eyeball creature named Frejn's Doomclock, which begins counting down. The countdown is paused while the Doomclock is mesmerized. When the countdown hits zero, the entire raid is killed. If mesmerized long enough, the Doomclock despawns without killing the raid.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Frejn)&amp;#35;[A-F0-9]{6}(?&amp;lt;Player&amp;gt;\w+) (prepares|begins) to purge&quot; SD=&quot;get away ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "get away <player>" when a player is hit with Ramming Headbutt or Eye Gouge.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Frejn)begins to activate an ancient device&quot; SD=&quot;mesmerize eyes&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "mesmerize eyes" when Frejn's Doomclock joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Frejn)called into the fight with a whistle&quot; SD=&quot;kill wolf&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill wolf" when a [[Trained Attack Warpwolf]] joins the fight.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Frejn)commits (?&amp;lt;Player&amp;gt;\w+) to memory&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <player>" when Prepared Stare is cast.
