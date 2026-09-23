---
title: Barlsbit the Scavenger
type: named
expansion: Scars of Destruction
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: '{{waypoint 523, 5, 606}}'
health: 279 Quadrillion
primary_damage: Crush, Disease
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Barlsbit the Scavenger
  url: https://eq2.fandom.com/wiki/Barlsbit_the_Scavenger
  history: https://eq2.fandom.com/wiki/Barlsbit_the_Scavenger?action=history
  revision: 1874517
  revised: '2025-05-05T00:52:23Z'
  license: CC BY-SA 3.0
---

Barlsbit the Scavenger is a Tier 1 raid boss.

## Statistics

- Max Health: 279,488,558,080,816,160
- Intelligence: 4,106
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
- AE Auto-Attack Chance: 20.0
- Weapon Damage Bonus: 175.0
- Flurry Avoidance: 410.0
- Ability Doublecast Avoidance: 490.0

## Abilities

- **Missive Weighting**
- A curable trauma that deals high health and power damage to those closer to Barlsbit. This ability also shuffles the hate list.
- **Noxious Storm**
- A curable noxious that deals fast ticking poison damage to players within 45 meters and increases incoming physical damage from all sources.
- **Noxious Spit**
- A curable noxious that stuns and knocks back the target, dealing more noxious damage to the target the farther from the caster the target is.
- **Strategic Stab I**
- A curable trauma that deals fast-growing damage over time.
- **Slashing Reprisal I**
- A curable trauma that deals fast-growing damage over time.
- **Transformation Incantation**
- A curable curse that shapeshifts the players and deals increasing damage over time. The last 3-4 players [range is exact, as seen in-game] to be cured are hit with Weakened Chant. If not cured, the effect will slay all members of the player's group.
- **Weakened Chant**
- An incurable curse that makes the player more likely to become Barlsbit's main target and increases damage from non-divine sources.
- **Revoke Protection**
- An incurable noxious that prevents the player from being Barlsbit's main target. Barlsbit memwipes shortly before and after casting this spell. Shortly after casting this spell, Barlsbit instantly slays his current target, if that target is not a fighter.
- **Concussive Release**
- A curable elemental that deals growing elemental damage to the player. When removed, it triggers a knockback to all allies within 12 meters, which "will lead to their demise".

## Strategy

Barlsbit summons additional small scavengers throughout the fight.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;amp;lt;Barlsbit&amp;amp;gt;presents itself in the area)&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "add up" when a small scavenger joins the fight.
- <code>&lt;Trigger R=&quot;(?&amp;amp;lt;Barlsbit&amp;amp;gt;goes after a weaker target)&quot; SD=&quot;memwipe&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "memwipe" when Barlsbit changes targets.
- <code>&lt;Trigger R=&quot;(?&amp;amp;lt;Barlsbit&amp;amp;gt;&#91;A-F0-9]&#123;6}(?&amp;amp;lt;Player&amp;amp;gt;\w+) begins to mindlessly play)&quot; SD=&quot;Get away $&#123;Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "get away <player>" when <player> is hit with Concussive Release.
