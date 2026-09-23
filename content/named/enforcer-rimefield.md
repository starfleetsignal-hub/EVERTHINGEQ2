---
title: Enforcer Rimefield
type: named
expansion: Scars of Destruction
race: Giant
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Western Wastes: Exploration Determination (Raid)]]'
location: Rimeclaw Caves {{waypoint -789.07, 286.99, -298.87}}
primary_damage: Crushing
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Giant
- Monsters that award AA
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
- 'Western Wastes: Exploration Determination (Raid) Named Monsters'
source:
  title: Enforcer Rimefield
  url: https://eq2.fandom.com/wiki/Enforcer_Rimefield
  history: https://eq2.fandom.com/wiki/Enforcer_Rimefield?action=history
  revision: 1907019
  revised: '2025-10-02T02:22:16Z'
  license: CC BY-SA 3.0
---

Enforcer Rimefield is a Tier 3 raid boss.

## Statistics

- Flurry Avoidance: 525.0
- Ability Doublecast Avoidance: 590.0
- Resolve: 11,195.0

## Abilities

- **Heated Debating I**
- A curable elemental that deals fast-growing damage over time.
- **Stealthy Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on scouts.
- **Rimefrost**
- **Enforcement**
- A curable elemental that deals elemental damage and increases noxious damage from all sources.
- **Fiststorm**
- A curable trauma that deals fast ticking physical damage and increases incoming noxious damage from all sources..
- **Limited Power I/II/III**
- An incurable curse that reduces the target's maximum power pool by 25%/50%/75%.
- **Enforced Submission I/II/III**
- An incurable curse that reduces the target's maximum health pool by 25%/50%/75%.
- **Cached Power**
- A buff that decreases damage from all sources for each active summoned power cache.
- **Rime's Enforcement**
- A buff on [[A summoned power cache]] that lands at 50%. If not dispelled by the time the cache dies, then Rimefield heals.
- **Frozen Giantspike**
- An incurable trauma that deals piercing damage over time.
- **Barrage**
- An attack that can only be countered with [[Bulwark of Order]].

## ACT Triggers

- &lt;Trigger R=&quot;(?&amp;#35;Rimefield)(?&amp;lt;PLAYER&amp;gt;\w+) prepares to purge arcane damage.&quot; SD=&quot;${PLAYER} Joust and Cure&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Western Wastes: Exploration Determination [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "<Player> Joust and Cure" when Rimefield casts .
