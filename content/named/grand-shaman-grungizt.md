---
title: Grand Shaman Grungizt
type: named
expansion: Scars of Destruction
race: Kappa
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: Dankmar Swamp {{waypoint 328.25, 21.34, 487.98}}
health: 279 Quadrillion
primary_damage: Crushing, Disease
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Kappa
- Monsters that award AA
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Grand Shaman Grungizt
  url: https://eq2.fandom.com/wiki/Grand_Shaman_Grungizt
  history: https://eq2.fandom.com/wiki/Grand_Shaman_Grungizt?action=history
  revision: 1864297
  revised: '2025-03-14T02:57:18Z'
  license: CC BY-SA 3.0
---

Grand Shaman Grungizt is a Tier 1 raid boss.

## Statistics

- Max Health: 279,488,539,080,232,160
- Wisdom: 4,106
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
- AE Auto-Attack Chance: 10.0
- Weapon Damage Bonus: 175.0
- Flurry Avoidance: 410.0
- Ability Doublecast Avoidance: 490.0

## Abilities

- **Shamanistic Surge**
- An incurable noxious that deals increasing noxious damage to health and power over time.
- **Far Proximity Warning**
- An incurable curse that causes the target to take more damage from Shamanistic Surge if the target is more than 35 meters away.
- **Near Proximity Warning**
- An incurable curse that causes the target to take more damage from Shamanistic Surge if the target is less than 40 meters away.
- **Elemental Conjure Mastery**
- A buff that decreases damage taken from all sources for each active Minimonuseru Titan.
- **Aftershock Release**
- A curable arcane that deals growing arcane damage to the target. When removed, it triggers Aftershock Reverberation to all allies within 10 meters, which deals much faster arcane damage and slows movement speed.
- **Strategic Stab I**
- A curable trauma that deals fast-growing damage over time.
- **Noxious Storm**
- A curable noxious that deals fast ticking poison damage to targets within 45 meters and increases incoming physical damage from all sources.
- **Slashing Reprisal I**
- A curable trauma that deals fast-growing damage over time.
- **Barrage**
- A nameless spell that can only be countered with [[Bulwark of Order]].

## Strategy

Grungizt drops a black circle on the ground with a larger red circle surrounding it and a pillar of water in the center. Players standing in the circle are killed shortly after it appears.

## ACT Triggers

- <code>&amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Shaman&amp;amp;gt;&#91;A-F0-9]&#123;6}(?&amp;amp;lt;Player&amp;amp;gt;\w+) prepares to purge arcane damage)&amp;quot; SD=&amp;quot;Get away $&#123;Player}&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;</code>
  - Says "Get away <Player>" when Aftershock Release lands on that player.
- <code>&amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Shaman&amp;amp;gt;forms from the Shaman)&amp;quot; SD=&amp;quot;add up&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;</code>
  - Says "add up" when a Minimonuseru Titan joins the fight.
