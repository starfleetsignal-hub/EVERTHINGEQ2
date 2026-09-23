---
title: Frostking Jund'Erin (Abdicated Throne)
type: named
expansion: Scars of Destruction
in_game_name: Frostking Jund'Erin
race: Giant
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Kael Drakkel: Abdicated Throne (Raid)]]'
location: '{{waypoint -107.70, -129.18, 1797.21}}'
health: 250 Quadrillion
primary_damage: Crushing
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Giant
- 'Kael Drakkel: Abdicated Throne (Raid) Named Monsters'
- Monsters that award AA
- Named Monster needing location
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Frostking Jund'Erin (Abdicated Throne)
  url: https://eq2.fandom.com/wiki/Frostking_Jund'Erin_(Abdicated_Throne)
  history: https://eq2.fandom.com/wiki/Frostking_Jund'Erin_(Abdicated_Throne)?action=history
  revision: 1908292
  revised: '2025-10-22T03:59:46Z'
  license: CC BY-SA 3.0
---

Frostking Jund'Erin is a Tier 4 raid boss. The fight is nearly identical to [[Jund'Erin (Exploration Determination)]], except with higher stats.

## Statistics

- Flurry Avoidance: 575.0
- Ability Doublecast Avoidance: 645.0
- Resolve: 11,365.0

## Abilities

- **Stalwart Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on fighters.
- **Spellweaved Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on mages.
- **Frozen Giantspike**
- An incurable trauma that deals piercing damage over time.
- **Piercing Thoughts II**
- A curable trauma that deals fast-growing damage over time.
- **Usurp Power II**
- A curable arcane that drains power over time until cured. Targets closer to Jund'Erin will lose more power.
- **Usurp Life II**
- A curable arcane that drains health over time until cured. Targets closer to Jund'Erin will lose more health.
- **Frostgiant Slice II**
- A curable trauma that deals fast-growing physical damage over time.
- **Static Blast II**
- A curable arcane that deals magic damage over time. It inflicts more damage to targets in front of Jund'Erin, and less to targets behind him. It also roots the target.
- **King's Fury II**
- A curable trauma that deals crushing damage over time. It inflicts more damage to targets in front of Jund'Erin, and less to targets behind him. It also prevents targets from casting hostile spells.
- **Teamwork**: Leader
- A buff that casts Tag Team Strike on the current target, if that target already has the effect from Teamwork: Member.
- **Glacial Reflection**
- A buff that reflects all damage taken by Jund'Erin back onto the caster.
- **Frostking's Crystallizing Compression**
- An incurable curse that can only be removed by clicking one of several purple crystals nearby. If the curse expires, the entire raid is killed instantly.
- **Barrage**
- An attack that can only be countered with [[Bulwark of Order]].

## Strategy

Jund'Erin continuously summons a [[Warring Frostgiant Blitzstomper]] which has the Teamwork: Member buff.

If a player clicks on a purple crystal without Frostking's Crystallizing Compression, then they die instantly.

## ACT Triggers

- &lt;Trigger R=&quot;prepares to protect himself.&quot; SD=&quot;Reflect up, stop attacking&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Kael Drakkel: Abdicated Throne [Raid]&quot; T=&quot;T&quot; TN=&quot;reflect down&quot; Ta=&quot;F&quot; /&gt;
  - Calls "Reflect up, stop attacking" when Jund'Erin casts Glacial Reflection.
- &lt;Spell N=&quot;reflect down&quot; T=&quot;15&quot; OM=&quot;F&quot; R=&quot;F&quot; A=&quot;F&quot; WV=&quot;1&quot; RD=&quot;F&quot; M=&quot;F&quot; Tt=&quot;&quot; FC=&quot;-16777056&quot; RV=&quot;-5&quot; C=&quot; General&quot; RC=&quot;F&quot; SS=&quot;none&quot; WS=&quot;tts [reflect down]&quot; /&gt;
  - A timer (complementary to the above trigger) that counts 15 seconds and calls "reflect down".
