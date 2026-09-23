---
title: Foulgore the Rotten
type: named
expansion: Scars of Destruction
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Blackhook Spiral: Frenzied Breach (Raid)]]'
location: Corrupted Caldera
achievement_xp: true
added_in: Scars of Destruction
categories:
- 'Blackhook Spiral: Frenzied Breach (Raid) Named Monsters'
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Foulgore the Rotten
  url: https://eq2.fandom.com/wiki/Foulgore_the_Rotten
  history: https://eq2.fandom.com/wiki/Foulgore_the_Rotten?action=history
  revision: 1880230
  revised: '2025-08-18T00:55:53Z'
  license: CC BY-SA 3.0
---

Foulgore the Rotten is a Tier 2 raid boss.

## Statistics

- Flurry Avoidance: 470.0
- Ability Doublecast Avoidance: 540.0
- Resolve 11,015.0

## Abilities

- **Void Burn**
- An incurable arcane that deals fast ticking magical damage. This effect is from standing near an active void essence fissure.
- **Foul Touch**
- An incurable noxious that deals fast ticking poison damage.
- **Gore Burn**
- A curable elemental that deals fast ticking elemental damage and increases arcane damage from all sources.
- **Curse of Foulgore**
- An incurable curse that heals Foulgore for 25% of his health when it expires. The curse is cured by walking into any active void essence fissure, other than the one Foulgore is standing in. If Foulgore is not standing in any fissure, then curing the curse heals Foulgore for 2.5% of his health. After absorbing two fissures, this curse also causes the target to remain at the bottom of the hate list until cured.
- **Blackhook Heartspike**
- An incurable trauma that inflicts piercing damage over time.
- **Crazed Throws**
- A curable trauma that deals fast ticking physical damage and increases noxious damage from all sources.
- **Intrusive Thoughts**
- A curable arcane that deals fast ticking arcane damage and increases physical damage from all sources.
- **Stealthy Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on scouts.
- **Foul Amplification**
- A buff that decreases damage taken by 20% for each increment. At 3 increments, Foulgore immediately kills the entire raid. Increments are added for each Curse of Foulgore that expires naturally. Increments cannot be removed.
- **Void Shielded**
- A buff that prevents all damage when Foulgore is not standing in an active void fissure.

## Strategy

Near the beginning of the fight, 5 void essence fissures appear on the island. At 75%, 50%, and 25%, Foulgore consumes one of the fissures, closing it and increasing his strength.

Foulgore casts an AoE attack that instantly kills all players within 10 meters. Each time he casts this spell, he concentrates on either fighters, mages, priests, or scouts. The selected class is teleported close to him right before the attack lands. The attack kills all nearby players, regardless of which class he is concentrating on.

## ACT Triggers

- <code>&lt;Trigger R=&quot;(?&amp;lt;Foulgore&amp;gt;begins concentrating)&quot; SD=&quot;joust 15&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Blackhook Spiral: Frenzied Breach [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "joust 15" when Foulgore begins concentrating on his AoE attack.
- <code>&lt;Trigger R=&quot;(?&amp;lt;Foulgore&amp;gt;fissure has closed)&quot; SD=&quot;move next fissure&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Blackhook Spiral: Frenzied Breach [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "move next fissure" when Foulgore consumes one of the void essence fissures.
