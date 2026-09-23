---
title: Evuntressa, Kryterion's Behest
type: named
race: Lamia
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Unknown: Abyssal Behest (Raid)]]'
location: Evuntressa's Charge {{waypoint -1311.80, 51.31, -1149.02}}
primary_damage: Crushing, Slashing
achievement_xp: true
added_in: LU131
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- LU131 Named Monsters
- Lamia
- Monsters that award AA
- Named Monsters
- 'The Unknown: Abyssal Behest (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Evuntressa, Kryterion's Behest
  url: https://eq2.fandom.com/wiki/Evuntressa,_Kryterion's_Behest
  history: https://eq2.fandom.com/wiki/Evuntressa,_Kryterion's_Behest?action=history
  revision: 2024397
  revised: '2026-08-26T16:40:10Z'
  license: CC BY-SA 3.0
---

Evuntressa, Kryterion's Behest is a Tier 3 raid boss. She gains an additive advantage for each player below 22 and has a hard time limit of 30 minutes.

## Statistics

- Flurry Avoidance 550.0
- Ability Doublecast Avoidance 900.0
- Resolve 13,640

## Abilities

- **Voracious Protection**
- A buff that protects Evuntressa from all harm while any [[Voracious protector|voracious protectors]] are active.
- **Conscription of Disease**
- A buff that has a chance of triggering Splash of Putresence on the attacker, which deals disease damage.
- **Vaporproof III**
- A buff that protects Evuntressa from any targets that have Rift Vapors applied to them.
- **Consumer Support**
- A buff that increases Evuntressa's offensive and defensive ability for each [[Tentacle of Oppression]] that is active. If there are 3 or more Tentacles active, Evuntressa heals significantly.
- **Seeping Rift Power**
- A buff that increases Evuntressa's outgoing damage and resolve for each Void Rift that successfully emerges.
- **Bolstered Behest**
- A buff that increases outgoing damage and decreases incoming damage while applied. It applies at 70%, 50%, 30%, and 15%, then lasts for 18 seconds. If damaged too much while this effect is active, Evuntressa gains the ability to deathtouch her current target.
- **Mindwracking Influence III**
- An incurable arcane that causes all abilities to cost additional power.
- **Surging Summons**
- An incurable trauma that deals increasing slashing, magic, heat, and disease damage to health and power over time.
- **Slashing Hopes**
- A curable trauma that deals fast ticking slashing damage and increases noxious, arcane, and elemental damage from all sources.
- **Faltering Courage**
- A curable arcane that drains power over time. The closer to the boss the target is, the more power that is drained.
- **Faltering Flameheist**
- A curable elemental that deals increasing heat damage. This ability can be blocked by Area Effect blockers.
- **Raining Cinders III**
- A curable elemental that deals increasing damage over time.
- **False Priorities**
- An incurable noxious that clears the target's target.
- **Rift Vapors**
- An incurable detriment that severely debuffs outgoing damage potential. This effect is applied to all players standing inside a Void Rift.
- **Earnest Behest**
- A curse that cannot be cured while the target is within 10 meters of any allies or any Void Rifts. The effect is incurable for the first 8 seconds. If it expires, the entire raid is killed.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

A [[Tentacle of Oppression]] has a frontal ability with a weak knockback effect.

Evuntressa summons Void Rifts throughout the battlefield. Each rift has a timer starts at 1 minute 30 seconds and counts up. If it is allowed to reach its maximum value, the rift "emerges" and provides a powerful buff to Evuntressa. While any number of players are standing inside the rift, the timer counts down to the rift's "collapse". More players causes the timer to count down faster. The countdown is further increased by each player with the ability Augmented Void Collapse (such as from [[Benelith's Heartsworn Hood]]). If a second rift is summoned while the first is still active, the first rift emerges, regardless of its countdown. Additionally, Evuntressa regains health and power while standing in or near a Void Rift.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Evuntressa)A Void Rift has appeared&quot; SD=&quot;void rift&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Abyssal Behest [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "void rift" when a Void Rift appears.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Evuntressa)seeks (?**: a target|\d targets) to bestow&quot; SD=&quot;joust curse soon&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown: Abyssal Behest [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "curse joust" shortly before Evuntressa casts Earnest Behest.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Evuntressa)strengthens herself for the next&quot; SD=&quot;stop dps&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Abyssal Behest [Raid]&quot; T=&quot;T&quot; TN=&quot;EvuntressaBolster&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "stop dps" when Evuntressa casts Bolstered Behest, and starts a timer.
- **<code>&lt;Spell N=&quot;EvuntressaBolster&quot; T=&quot;20&quot; OM=&quot;F&quot; R=&quot;F&quot; A=&quot;F&quot; WV=&quot;0&quot; RD=&quot;T&quot; M=&quot;T&quot; Tt=&quot;&quot; FC=&quot;-16776961&quot; RV=&quot;-15&quot; C=&quot;The Unknown**: Abyssal Behest [Raid]&quot; RC=&quot;F&quot; SS=&quot;&quot; WS=&quot;tts start dps&quot; /&gt;</code>
- Calls "start dps" when Bolstered Behest expires.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Evuntressa)Tentacle of Oppression&amp;#92;&amp;#92;/a is summoned from the strange fiery liquid&quot; SD=&quot;tentacle&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Abyssal Behest [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tentacle" when a [[Tentacle of Oppression]] is summoned.
