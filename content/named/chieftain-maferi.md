---
title: Chieftain Maferi
type: named
expansion: Scars of Destruction
race: Mandoko
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: Mandoko Jungle {{waypoint -149.28, 121.14, 184.13}}
health: 279 Quadrillion
primary_damage: Zap, Crush
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Mandoko
- Monsters that award AA
- Monsters that award SP
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Chieftain Maferi
  url: https://eq2.fandom.com/wiki/Chieftain_Maferi
  history: https://eq2.fandom.com/wiki/Chieftain_Maferi?action=history
  revision: 1874518
  revised: '2025-05-05T03:14:05Z'
  license: CC BY-SA 3.0
---

Chieftain Maferi is a Tier 1 raid boss. To spawn him, defeat all [[Mandoko Chanter|Mandoko Chanters]] within the Mandoko Jungle.

## Statistics

- Max Health: 279,488,539,080,232,160
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
- AE Auto-Attack Chance: 10.0
- Weapon Damage Bonus: 175.0
- Flurry Avoidance: 410.0
- Ability Doublecast Avoidance: 490.0

## Abilities

- **Mandoko Surge**
- Deals increasing elemental damage to health and power over time.
- **Chanting Reverberation**
- An incurable arcane that debuffs the target for each Mandoko Chanter in the fight.
- **Blurred Sight**
- A curable arcane that blurs vision and deals fast ticking increasing arcane damage over time.
- **Chanting Support**
- A buff that decreases damage taken from all sources for each Mandoko Chanter in the fight.
- **Curse of the Totem**
- An incurable curse that can only be removed by moving within 5 meters of a ritual totem. The totem has four spawn locations around the lake and only exists in one location at a time. When this curse expires, it kills the entire raid instantly.
- **Monkey Around**
- A curable arcane that deals growing arcane damage. When removed, it triggers Finding Out on all allies within 10 meters, which deals much faster arcane damage and slows movement speed. This ability only lands on players within 3 meters of Maferi.
- **Barrage**
- An unnamed spell that can only be countered with [[Bulwark of Order]].

## ACT Triggers

- <code>&amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Chieftain&amp;amp;gt;&#91;A-F0-9]&#123;6}(?&amp;amp;lt;Player&amp;amp;gt;\w+) prepares to Monkey Around and Find Out!)&amp;quot; SD=&amp;quot;Get away $&#123;Player}&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&amp;quot; T=&amp;quot;T&amp;quot; TN=&amp;quot;Monkey&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;</code>
  - Says "Get away <player>" when the player is hit with Monkey Around.
- <code>&amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Chieftain&amp;amp;gt;begins to chant)&amp;quot; SD=&amp;quot;add up&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;</code>
  - Says "add up" when a Mandoko Chanter spawns.
- <code>&amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Chieftain&amp;amp;gt;targets (?&amp;amp;lt;PLAYER&amp;amp;gt;\w+) with Curse of the Totem!)&amp;quot; SD=&amp;quot;$&#123;PLAYER} Totem&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes &#91;Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;</code>
  - Says "<player> totem" when the player is hit with Curse of the Totem.
