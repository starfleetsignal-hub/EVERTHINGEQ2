---
title: Temper
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[The Oogothl Sprawl: Unseen Horrors (Raid)]]'
location: Eerie Ridges {{waypoint -585.47, 127.63, -114.87}}
primary_damage: Crushing, Heat
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Oogothl Sprawl: Unseen Horrors (Raid) Named Monsters'
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
source:
  title: Temper
  url: https://eq2.fandom.com/wiki/Temper
  history: https://eq2.fandom.com/wiki/Temper?action=history
  revision: 2019196
  revised: '2026-07-24T01:11:18Z'
  license: CC BY-SA 3.0
---

Temper is a Tier 2 raid boss. He gains an additive advantage for each player below 18 and has a soft time limit of 45 minutes.

## Statistics

- Flurry Avoidance 400.0
- Ability Doublecast Avoidance 800.0
- Resolve 13,430.0

## Abilities

- **Conscription of Consequence**
- A buff that gives a chance to trigger Bolt of Consequence on an attacker, which deals cold damage and interrupts the target, and Forced Consequence, a self-buff that increases offensive ability.
- **Increments of RAGE!**
- A buff that increases outgoing damage to Temper's main target for each increment. Increments can stack up to 48 times and cannot be removed until his next triggered RAGE.
- **Surging Temper**
- An incurable trauma that deals increasing crushing and noxious damage to health and magic damage to power over time.
- **Mindwracking Influence II**
- An incurable arcane that causes all abilities to cost additional power.
- **Arcane Storm**
- A curable arcane that deals increasing arcane damage and increases physical damage from all sources.
- **Cold Blooded**
- A curable elemental that deals fast-growing cold damage over time.
- **Brain Burst I**
- A curable arcane that deals increasing mental damage. This ability can be blocked by Area Effect blockers, and the reuse time is 60 seconds.
- **Spellweaved Admonishment**
- A curable elemental that only lands on mages.
- **Raging Curse**
- A curse that deals increasing physical damage. It can only be cured if the target is more than 30 meters away from Temper.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Temper)curse targeting (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;${Player} joust 30&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "<Player> joust 30" when Temper casts Raging Curse.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Temper)joins the fight&quot; SD=&quot;kill add&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Oogothl Sprawl**: Unseen Horrors [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "kill add" when a [[Manifestation of Temper]] joins the fight.
