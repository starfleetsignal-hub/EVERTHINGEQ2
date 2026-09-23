---
title: Darathar, Void Bound Ancient
type: named
expansion: Rage of Cthurath
race: Dragon
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Proclamation of Rage (Raid)]]'
location: Shadowed Precipice {{waypoint 547.22, 274.98, -651.43}}
primary_damage: Crushing
drops:
- '[[Banished One''s Void-bound Remnant]]'
- '[[Herald''s Cuirass of the Void]]'
- '[[Herald''s Hauberk of the Void]]'
- '[[Herald''s Robes of the Void]]'
- '[[Herald''s Tunic of the Void]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Dragon
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Oogothl Sprawl: Proclamation of Rage (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Darathar, Void Bound Ancient
  url: https://eq2.fandom.com/wiki/Darathar,_Void_Bound_Ancient
  history: https://eq2.fandom.com/wiki/Darathar,_Void_Bound_Ancient?action=history
  revision: 2018630
  revised: '2026-07-20T02:38:30Z'
  license: CC BY-SA 3.0
---

Darathar, Void Bound Ancient is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Conscription of Extortion**
- A buff that has a chance of triggering Extortion on an attacker.
- **Teamwork**: Leader
- A buff that applies a Tag Team Strike to Darathar's current target, if that target has also been hit by a mob with Teamwork: Member.
- **Void Bound Protection**
- A buff that redcues all damage by 300%, increases melee multiplier, haste, and DPS. This buff is active while there are any [[Void Bound Projection|Void Bound Projections]] in combat.
- **Draconic Surge**
- An incurable elemental that deals increasing slashing, heat, and mental damage to health and power over time. High crushing damage is added if the target also has Draconic Misdirection.
- **Mindwracking Influence II**
- An incurable arcane that causes all abilities to cost additional power.
- **Extortion**
- An incurable trauma that interrupts the target and deals crushing damage over time.
- **Fateful Mindstorm**
- A curable arcane that deals increasing mental damage and increases physical and elemental damage from all sources.
- **Forced Worship**
- An incurable detriment that deals disease damage inversely proportional to Darathar's health. It also roots the target and prevents beneficial spells. This detriment lands on players who fall below 5% power.
- **Draconic Misdirection**
- A curse that deals increasing slashing damage for each other player within 10 meters. It can only be cured if there are no other players within 10 meters.
- **Overwhelming Destruction**
- A curable curse that immediately propagates to a new target when removed.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

Darathar goes into a frenzy, selecting a new target for a short time. His previous target is forced to the bottom of the hate list.

Allowing either curse (Draconic Misdirection and Overwhelming Destruction) to expire counts as a failure. The first failure summons a [[Void Bound Projection]], which has Teamwork: Member. Darathar takes no damage while this Projection is alive. The second failure additionally kills the target. The third failure additionally kills the target's group. The fourth failure additionally kills the entire raid.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;casts his &amp;quot;Draconic Misdirection&amp;quot; curse targeting (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;${Player} Joust out 10&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Proclamation of Rage [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "<Player> joust out 10" when Darathar casts Draconic Misdirection.
- **<code>&lt;Trigger R=&quot;Darathar, Void Bound Ancient goes into a FRENZY&quot; SD=&quot;Tank swap&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Proclamation of Rage [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap" when Darathar selects a new target.
