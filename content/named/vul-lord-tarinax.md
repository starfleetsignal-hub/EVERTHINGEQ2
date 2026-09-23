---
title: Vul Lord Tarinax
type: named
expansion: Scars of Destruction
race: Dragon
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Blackhook Spiral: Spiritual Terror (Raid)]]'
achievement_xp: true
added_in: Scars of Destruction
categories:
- 'Blackhook Spiral: Spiritual Terror (Raid) Named Monsters'
- Dragon
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Vul Lord Tarinax
  url: https://eq2.fandom.com/wiki/Vul_Lord_Tarinax
  history: https://eq2.fandom.com/wiki/Vul_Lord_Tarinax?action=history
  revision: 1880455
  revised: '2025-08-24T22:12:55Z'
  license: CC BY-SA 3.0
---

Vul Lord Tarinax is a Tier 2 raid boss.

## Statistics

- 470.0 Flurry Avoidance
- 540.0 Ability Doublecast Avoidance
- 11,015.0 Resolve

## Abilities

- **Stalwart Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on fighters.
- **Stealthy Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on scouts.
- **Soul Evisceration**
- A curable noxious that cancels up to 75% of the target's speed buffs and inflicts 50% of max health in poison damage.
- **Reduce to Bones**
- An incurable curse. If the target dies before it expires, then all players afflicted with Reduce to Bones die at the same time.
- **Spirituality Enhancement**
- A buff that decreases damage taken from all sources for each [[Uncontrolled Spirit]] in the fight.
- **Endless Suffering**
- An incurable curse that deals growing mental damage. When it expires, it triggers an explosion on all allies within 10 meters.
- **Deteriorate Armor**
- An incurable curse that increases the damage received from all sources. If the target is afflicted by this curse a second time, then the target dies, and Tarinax heals significantly. Non-fighters struck by this effect receive major gear damage.
- **Unfathomable Scourge**
- A buff that casts Unfathomable Corruption on the attacker when Tarinax takes damage. Unfathomable Scourge gains increments each time it lands on a player. Periodically, Tarinax consumes all increments, dealing increased damage for each increment.
- **Osteoblast**
- A buff that increases Tarinax's power whenever a Bone Shard melds with him.

## Strategy

Throughout the fight, additional [[Soulless Vengeance]] creatures join the fight. When they die, an [[Uncontrolled Spirit]] appears in its place.

Whenever a player dies, an [[Uncontrolled Spirit]] joins the fight.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;lt;Tarinax&amp;gt;[0-9A-F]{6}(?&amp;lt;Player&amp;gt;\w+) begins to suffer)&quot; SD=&quot;Get away ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Blackhook Spiral: Spiritual Terror [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "Get away <player>" when a player is struck by Endless Suffering.
