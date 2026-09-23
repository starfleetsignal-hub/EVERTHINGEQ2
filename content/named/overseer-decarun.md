---
title: Overseer Decarun
type: named
expansion: Scars of Destruction
race: Orc
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Blackhook Spiral: Frenzied Breach (Raid)]]'
location: The Floating Steps {{waypoint -231.91, 204.32, -350.98}}
achievement_xp: true
added_in: Scars of Destruction
categories:
- 'Blackhook Spiral: Frenzied Breach (Raid) Named Monsters'
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monsters
- Orc
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Overseer Decarun
  url: https://eq2.fandom.com/wiki/Overseer_Decarun
  history: https://eq2.fandom.com/wiki/Overseer_Decarun?action=history
  revision: 1879638
  revised: '2025-08-08T01:53:07Z'
  license: CC BY-SA 3.0
---

Overseer Decarun is a Tier 2 raid boss.

When pulled, all remaining (living) orcs join the fight.

## Statistics

- Flurry Avoidance: 470.0
- Ability Doublecast Avoidance: 540.0
- Resolve 11,015.0

## Abilities

- **Blackhook Heartspike**
- An incurable trauma that inflicts piercing damage over time.
- **Stalwart Admonishment**
- A curable elemental that deals elemental damage over time and increases all other damage types. This spell only lands on fighters.
- **Growing Influence**
- A buff that increases all outgoing damage for each increment. Increments are gained over time and can be dispelled. If the spell reaches 20 increments, Decarun immediately defeats the entire raid.
- **Formidable**
- A buff that decreases all incoming damage for each [[Blackhook Lackey]] engaged in the fight.
- **Wound Ego**
- A curable arcane that deals high increasing arcane damage and increases physical damage from all sources.
- **Decarun's Decree**
- A curable elemental that deals growing elemental damage to the target. When removed, all allies within 12 meters are knocked back. If a player is hit by this knockback more than once during the fight, the second and subsequent knockbacks immediately kill the player.
- **Fated Overwatch**
- An incurable curse that reduces the target's max hp by 50%. If the target already has Fated Overwatch, they are slain, and Decarun receives a heal.
- **Convoked**
- A curable trauma that deals high increasing crushing damage and increases elemental damage from all sources.
- **Gale Force**
- A curable elemental that deals high increasing elemental damage and increases arcane damage from all sources.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;lt;Overseer&amp;gt;[0-9A-F]{6}(?&amp;lt;Player&amp;gt;\w+) gives into Decarun's Decree)&quot; SD=&quot;Get away ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Blackhook Spiral: Frenzied Breach [Raid]&quot; T=&quot;T&quot; TN=&quot;Decarun Decree&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "get away <player>" when Decarun casts Decarun's Decree on <player>.
