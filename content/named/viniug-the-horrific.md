---
title: Viniug the Horrific
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Zon Zobboz: Gaze of the Oglth (Raid)]]'
location: Abominable Bluff {{waypoint 602.96, 106.22, 615.27}}
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
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: Gaze of the Oglth (Raid) Named Monsters'
source:
  title: Viniug the Horrific
  url: https://eq2.fandom.com/wiki/Viniug_the_Horrific
  history: https://eq2.fandom.com/wiki/Viniug_the_Horrific?action=history
  revision: 1993521
  revised: '2026-04-03T20:01:54Z'
  license: CC BY-SA 3.0
---

Viniug the Horrific is a Tier 1 raid boss. He gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Vaporproof I**
- A buff that protects Viniug from any targets that have the Rift Vapors effect.
- **Conscription of Blight**
- A buff that has a chance at interrupting the attacker, deal disease damage, and debuff the attacker's offensive ability.
- **Surging Consumption**
- An incurable trauma that deals physical and heat damage to health and power over time.
- **Mindwracking Influence I**
- An incurable arcane that causes all abilities to cost additional power.
- **Situational Awareness**
- A buff that increases outgoing damage to Viniug's main target for each increment..
- **Raining Cinders I**
- A curable elemental that deals fast-growing damage over time.
- **Burning Gaze**
- An incurable detriment that lands on Viniug's main target. If the detriment lands on the same player twice, the player is killed, and Viniug heals for 25% of his maximum health.

## Strategy

Throughout the fight, Viniug summons [[A Horrific Bonder]], which is permanently rooted. If it dies within 15 meters of Viniug, then Viniug heals slightly.

Separately, Viniug summons a Void Rift, which is non-attackable. Viniug heals significantly while standing near a Void Rift. The Rift immediately begins energizing with a timer of 1 minute and 15 seconds (visible beneath its name). If it reaches zero, the entire raid is killed. If even a single player is standing near the Rift, it instead begins collapsing with a similar timer. If the collapsing timer reaches zero, the Void Rift disappears. If two Void Rifts are up simultaneously, the entire raid is killed.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Viniug)A Void Rift has appeared&quot; SD=&quot;void rift&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "void rift" when a Void Rift appears on the island.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Viniug)commits (?&amp;lt;Player&amp;gt;\w+) to memory&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <player>" when a player is hit with Burning Gaze.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Viniug)a Horrific Bonder&amp;#92;&amp;#92;/a forms from the shadows&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a Horrific Bonder appears on the island.
