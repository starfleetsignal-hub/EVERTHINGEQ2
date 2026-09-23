---
title: Court Sorcerer Viranor
type: named
expansion: Scars of Destruction
race: Giant
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Western Wastes: Exploration Determination (Raid)]]'
location: Rimeclaw Caves {{waypoint -665.24, 244.90, -329.67}}
primary_damage: Crushing, Magic
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
  title: Court Sorcerer Viranor
  url: https://eq2.fandom.com/wiki/Court_Sorcerer_Viranor
  history: https://eq2.fandom.com/wiki/Court_Sorcerer_Viranor?action=history
  revision: 1906138
  revised: '2025-09-21T21:35:54Z'
  license: CC BY-SA 3.0
---

Court Sorcerer Viranor is a Tier 3 raid boss.

## Statistics

- Flurry Avoidance: 525.0
- Ability Doublecast Avoidance: 590.0
- Resolve: 11,195.0

## Abilities

- **Giant's Stab**
- A curable trauma that deals fast-growing damage over time.
- **Court Pressure**
- A curable trauma that deals fast-growing damage over time.
- **Sword Rain**
- An incurable curse that lands on all players within 15 meters. The curse lands in three waves. First, it hits for normal damage. Second, it hits for damage plus stifle. Third, it hits for damage plus inability to cast hostile spells.
- **Spellweaved Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on mages.
- **Teamwork**: Leader
- A buff that casts Tag Team Strike on the current target, if that target already has the effect from Teamwork: Member.
- **Brain Fog**
- An incurable curse that lands on all players within 15 meters. Each increment decreases the player's maximum power pool by 5%. Increments cannot be removed and persist through death.
- **Frozen Giantspike**
- An incurable trauma that deals piercing damage over time.

## Strategy

Viranor summons a [[Riftcaster Wyvern]] continuously. If two wyverns are active simultaneously, the entire raid is instantly killed. The wyverns also have the Teamwork: Member buff.

Viranor has both a memwipe and a tank swap mechanic. The memwipe is a basic target swap with no additional effects. During the tank swap, the active tank loses all aggro and Viranor becomes invisible to that player (and only that player).

## ACT Triggers

- &lt;Trigger R=&quot;(?&amp;#35;Viranor)Bring on the swords&quot; SD=&quot;joust 16&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Western Wastes: Exploration Determination [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "joust 16" when Viranor begins casting Sword Rain.
- &lt;Trigger R=&quot;(?&amp;#35;Viranor)looks for a new target&quot; SD=&quot;tank swap&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Western Wastes: Exploration Determination [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "tank swap" when Viranor turns invisible to the active tank.
- &lt;Trigger R=&quot;(?&amp;#35;Viranor)swaps his strategy&quot; SD=&quot;memwipe&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Western Wastes: Exploration Determination [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "memwipe" when Viranor chooses a new random target.
