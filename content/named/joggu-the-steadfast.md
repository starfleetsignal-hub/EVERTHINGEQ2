---
title: Joggu the Steadfast
type: named
expansion: Scars of Destruction
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: '{{waypoint 88.98, 7.19, 392.05}}'
health: 209 Quadrillion
primary_damage: Crushing
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Monsters that award SP
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Joggu the Steadfast
  url: https://eq2.fandom.com/wiki/Joggu_the_Steadfast
  history: https://eq2.fandom.com/wiki/Joggu_the_Steadfast?action=history
  revision: 1863929
  revised: '2025-03-10T03:29:17Z'
  license: CC BY-SA 3.0
---

Joggu the Steadfast is a Tier 1 raid boss.

## Statistics

- Max Health: 209,906,348,472,185,344
- Strength: 4,903
- Resolve: 10,795
- Bleedthrough: 50
- Combat Mitigation: 1,553,045
- Potency: 44,500.0
- Casting Speed: 100.0
- Reuse Speed: 100.0
- Damage Per Second: 13,000.0
- Attack Speed: 4,000.0
- Multi-Attack Chance: 0.0
- Strikethrough: 65.0
- Accuracy: 150.0
- AE Auto-Attack Chance: 10.0
- Weapon Damage Bonus: 175.0
- Flurry Avoidance: 410.0
- Ability Doublecast Avoidance: 490.0

## Abilities

- **Chip and Shatter**
- A curable trauma that deals increasing damage over time to all players within 20 meters.
- **Bombarded Force**
- A curable arcane that knocks down the target and deals crushing damage.
- **Swampquake**
- A curable curse that lands on all players within 2 meters of Joggu or any of his Chips. This curse cannot be cured while the afflicted player is targeting Joggu. If it expires naturally, the entire raid is instantly killed.
- **Steadfast Reaction**
- A curable arcane that deals fast-growing noxious damage over time.
- **Erosion of Will**
- A curable arcane that deals fast-growing magic damage over time. It also recasts **Protection of Joggu** on all nearby Chips.
- **Mountainous Protection**
- A buff on Joggu that starts with six increments, reducing incoming damage for each increment. Increments decrease as Chips of Joggu join the fight.
- **Protection of Joggu**
- A buff present on all Chips of Joggu when they initially spawn. This buff reduces all incoming damage while Joggu has any increments of Mountains Protection.
- **Mountain Stance**
- A buff on Joggu that increases outgoing damage and decreases incoming damage. This effect can be dispelled.
- **Barrage**
- A nameless spell that can only be blocked by casting [[Bulwark of Order]].

## ACT Triggers

- &lt;Trigger R=&quot;(?&amp;lt;Joggu&amp;gt;chips some of his rock hard skin)&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Says "add up" when a Chip of Joggu joins the fight.
- &lt;Trigger R=&quot;(?&amp;lt;Joggu&amp;gt;begins to channel a powerful Swampquake)&quot; SD=&quot;curse soon&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Sodden Archipelago: Thawed Marshes [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Says "curse soon" when Joggu and his Chips are about to cast Swampquake.
- &amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Joggu&amp;amp;gt;barrels for other targets)&amp;quot; SD=&amp;quot;memwipe&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes [Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;
  - Says "memwipe" when Joggu shuffles his hate list.
