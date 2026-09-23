---
title: The Stalking Doombringer
type: named
expansion: Scars of Destruction
race: Void Beast
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Blackhook Spiral: Spiritual Terror (Raid)]]'
location: '{{waypoint -569.98, 167.82, 205.32}}'
achievement_xp: true
added_in: Scars of Destruction
categories:
- 'Blackhook Spiral: Spiritual Terror (Raid) Named Monsters'
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
- Void Beast
source:
  title: The Stalking Doombringer
  url: https://eq2.fandom.com/wiki/The_Stalking_Doombringer
  history: https://eq2.fandom.com/wiki/The_Stalking_Doombringer?action=history
  revision: 1878287
  revised: '2025-06-26T02:18:39Z'
  license: CC BY-SA 3.0
---

The Stalking Doombringer is a Tier 2 raid boss.

## Statistics

- Flurry Avoidance: 470.0
- Ability Doublecast Avoidance: 540.0
- Resolve 11,015.0

## Abilities

- **Distorted Thoughts I**
- A curable arcane that deals fast-growing damage over time.
- **Doomstorm**
- A curable arcane that deals fast ticking increasing arcane damage and increases physical damage from all sources.
- **Ragestorm**
- A curable elemental that deals fast ticking increasing elemental damage and increases physical damage from all sources.
- **Pesterstorm**
- A curable noxious that deals fast ticking poison damage and increases physical damage from all sources.
- **Feignstorm**
- A curable trauma that deals growing physical damage. When removed, it triggers a knockback on all allies within 12 meters.
- **Stealthy Admonishment**
- A curable elemental that only lands on scouts. It deals elemental damage and increases all other damage types. This effect cannot be blocked.
- **Doomling Support**
- A buff that decreases damage taken from all sources for each active [[Summoned doomling]].
- **Reverberating Doom**
- A debuff that applies "more of a debuff" for each active [[Summoned doomling]].
- **Stalking Strike**
- An incurable trauma that deals physical damage and heals the Doombringer. It applies to players who stand in void energies for too long. When it expires, it is replaced with Voidsoaked.
- **Impending Doom**
- "Impending Doom" [this is all the in-game debuff says]. If dispelled by any class other than a mage, the player who cast the dispell is killed.
- **Barrage**
- An attack that can only be countered with [[Bulwark of Order]].

## Strategy

The Doombringer continuously places circles of void energies on the ground. Players who stand in the energies for too long are hit with Stalking Strike. If the Doombringer itself remains in a circle of void energies, it heals significantly. The void energies remain throughout the entire fight.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;lt;Doombringer&amp;gt;[0-9A-F]{6}(?&amp;lt;Player&amp;gt;\w+) feels the need to blurt out obscenities)&quot; SD=&quot;get away ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Blackhook Spiral: Spiritual Terror [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "get away <player>" when Doombringer casts Feignstorm on <player>.
