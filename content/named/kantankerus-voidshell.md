---
title: Kantankerus Voidshell
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Yon Gorroth: Voidshell Caverns (Raid)]]'
primary_damage: Piercing
drops:
- '[[Kantankerus Voidshell Pauldrons of Tenacity]]'
- '[[Kantankerus Voidshell Shawl of Tenacity]]'
- '[[Kantankerus Voidshell Shoulderpads of Tenacity]]'
- '[[Kantankerus Voidshell Shoulderguards of Tenacity]]'
- '[[Kantankerus Ring of Snip-Snaps]]'
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Yon Gorroth: Voidshell Caverns (Raid) Named Monsters'
source:
  title: Kantankerus Voidshell
  url: https://eq2.fandom.com/wiki/Kantankerus_Voidshell
  history: https://eq2.fandom.com/wiki/Kantankerus_Voidshell?action=history
  revision: 1998260
  revised: '2026-04-27T00:55:08Z'
  license: CC BY-SA 3.0
---

Kantankerus Voidshell is a Tier 1 raid boss. He gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Conscription of the Depths**
- A buff that gives a chance to interrupt and deal cold and disease damage when hit.
- **Divine Representation**
- A buff that applies an increment for each priest in the raid. Above 9 increments, it grants additional hit points and resolve per increment.
- **Stealthy Representation**
- A buff that applies an increment for each scout in the raid. Above 4 increments, it grants AE Auto Attack Chance, Attack Speed, DPS, and Melee Damage multiplier per increment.
- **Spellcaster Representation**
- A buff that applies an increment for each mage in the raid. Above 4 increments, it grants fervor, strikethrough, and potency per increment.
- **Stalwart Representation**
- A buff that applies an increment for each fighter in the raid. Above 4 increments, it grants maximum hit points and defensive skills per increment.
- **Ciguaic Support**
- A buff that increases Melee Multiplier, Haste, and DPS per increment. It also increases Resolve per increment, if at least 5 increments. It decreases damage from all sources per increment. Increments are applied for each [[Ciguaic Conger]] in the fight. This buff also heals the Voidshell when a Conger spawns.
- **Overbearing Influence I**
- An incurable detriment that causes power usage to also cost health based on the amount of power used.
- **Surging Snip-Snaps**
- An incurable trauma that deals increasing physical and elemental damage to health and power over time.
- **Darkwater Freeze**
- A curable elemental that deals fast-growing cold damage over time.
- **Storm of Poison**
- A curable elemental that deals fast ticking increasing elemental and poison damage and increases physical damage from all sources.
- **Poisonous Push**
- A curable noxious that deals fast ticking poison damage and increases physical damage from all sources.
- **Crustacean Mutation Curse**
- A curable curse that changes the target into a Void Crustacean and must be cured before it expires or the target dies. The first failure kills the target. The second failure kills the target. The third failure kills the target and their group. The fourth failure kills the entire raid. After a few seconds, the curse spreads to another player. As the Voidshell loses health, the curse is cast more frequently.
- **Spotted Weakness**
- An incurable noxious that marks the target. If a second Spotted Weakness lands on the same target, the target and their group dies.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]]

## Strategy

The Voidshell calls [[Ciguaic Conger]] into the fight, increasing in speed as his health decreases. This eel has a green bubble around it that does nothing. When the eel dies, a black pool is left behind. Standing in the black pool causes an incurable curse. If two black pools overlap, they merge into a much larger pool. If enough pools merge together, the new pool covers the entire zone.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;leaves something foul behind&quot; SD=&quot;move out of circle&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: Voidshell Caverns [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "move out of circle" when a Ciguaic Conger dies.
- **<code>&lt;Trigger R=&quot;potential weakness in (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;tank swap ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: Voidshell Caverns [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap <player>" when the Voidshell casts Spotted Weakness.
- **<code>&lt;Trigger R=&quot;slithers into the area&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Yon Gorroth**: Voidshell Caverns [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a Ciguaic Conger arrives.
