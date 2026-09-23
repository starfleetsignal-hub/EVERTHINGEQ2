---
title: Tha'Bael the Invader
type: named
expansion: Rage of Cthurath
race: Grathok
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Yon Gorroth: The Infinite Abyss (Raid)]]'
location: Darou Village {{waypoint 395.78, 72.67, -490.69}}
primary_damage: Slashing
drops:
- '[[Tha''Bael''s Buckle of the Void Invader]]'
- '[[Tha''Bael''s Plate Bracers of the Invader]]'
- '[[Tha''Bael''s Chain Bracers of the Invader]]'
- '[[Tha''Bael''s Leather Bracers of the Invader]]'
- '[[Tha''Bael''s Cuffs of the Invader]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Grathok
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Yon Gorroth: The Infinite Abyss (Raid) Named Monsters'
source:
  title: Tha'Bael the Invader
  url: https://eq2.fandom.com/wiki/Tha'Bael_the_Invader
  history: https://eq2.fandom.com/wiki/Tha'Bael_the_Invader?action=history
  revision: 2019581
  revised: '2026-07-27T01:44:36Z'
  license: CC BY-SA 3.0
---

Tha'Bael the Invader is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Conscription of Disease**
- A buff that gives a chance of triggering Splash of Putrescence on the attacker, which deals disease damage.
- **Surging Void-Strike**
- An incurable trauma that deals increasing physical, cold, and disease damage to health and power over time.
- **Mindwracking Influence II**
- An incurable arcane that causes all abilities to cost additional power.
- **Arcane Burst I**
- A curable arcane that deals increasing magic damage. This ability can be blocked with area of effect blockers.
- **Noxious Burst I**
- A curable noxious that deals increasing disease damage. This ability can be blocked with area of effect blockers.
- **Infectious Burst I**
- A curable noxious that deals increasing disease and poison damage. This ability can be blocked with area of effect blockers.
- **Ferocious Snarl**
- A curable elemental that deals cold damage and increases arcane and noxious damage from all sources.
- **Corrosive Wounding**
- A curable noxious with three increments. It wounds the target's maximum health by 25% (regardless of increments). It also deals growing poison damage and decreases spell casting and damage potential for each increment.
- **Invader's Dissection**
- A curable trauma that knocks down the target, dealing more crushing damage if the target is farther from Tha'Bael.
- **Infectious Pulse**
- A curable noxious that deals increasing disease damage and increases cold and physical damage from all sources. This ability can be blocked with area of effect blockers.
- **Void Shackled II**
- A curse that is incurable for 5 seconds before automatically becoming curable. It prevents the target from moving or casting spells and deals increasing crushing damage. When cured, it propagates to all other players within 10 meters.
- **Touch of Tha'Bael**
- A curable curse that deals disease damage, dazes, and prevents hostile spells. It lands on all players within 15 meters of Tha'Bael.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

Tha'Bael summons an [[Infectious Crawler]] into the fight. The crawler is rooted in a fixed position.

Tha'Bael goes into a frenzy and selects a new target, during which time Tha'Bael's previous target is forced to the bottom of the hate list.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Tha'Bael)Crawler&amp;#92;&amp;#92;/a is summoned&quot; SD=&quot;add up go kill it&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up go kill it" when an [[Infectious Crawler]] is summoned.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Tha'Bael)prepares to apply an ancient curse to those nearby&quot; SD=&quot;joust 16 from named&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;T&quot; TN=&quot;tank joust&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "joust 16 from named" when Touch of Tha'Bael is cast.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Tha'Bael)the Invader goes into a frenzy,&quot; SD=&quot;tank swap&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: The Infinite Abyss [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap" when Tha'Bael goes into a frenzy.
