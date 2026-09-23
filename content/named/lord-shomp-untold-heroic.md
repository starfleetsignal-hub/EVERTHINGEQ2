---
title: Lord Shomp (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Lord Shomp
race: Brownie
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Chimeric Chain (Untold Heroic)]]'
location: Nulltown {{waypoint -252.32, 15.39, 910.90}}
primary_damage: Divine, Slashing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Brownie
- Heroic Named Monsters
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: The Chimeric Chain (Untold Heroic) Named Monsters'
source:
  title: Lord Shomp (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Lord_Shomp_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Lord_Shomp_(Untold_Heroic)?action=history
  revision: 2011528
  revised: '2026-06-10T00:46:53Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21+).

## Abilities

- **Raywing Buffet**
- Applies a knockback to targets in front of Lord Shomp. He turns to face a random player before he casts this spell.
- **Overrun**
- An incurable elemental that decreases in-combat movement speed by 5.0% per increment. Each nullite foot soldier that is not charmed, feared, mesmerized, or stunned adds an increment. At 20 increments, the player is instantly killed.
- **Zon Zobbonk!**
- An incurable elemental that deals heat damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Despotic Decree**
- A curable curse that kills the player when it expires.
- **Foothold**
- A curable trauma cast by nullite foot soldiers. It inflicts crushing damage and roots the target. If two Footholds are on the same target, the root cannot be resisted.
- **Timmmberrr!**
- A curable noxious that lands on all players and causes feign death on one player. If it expires, the feigned player dies. At stage 21+, curing a player that does NOT have the feign death kills them.
- **Flight of the Nullite [detriment]**
- An incurable noxious that activates when Lord Shomp summons his storm clouds and clears when all storm clouds are dispelled. If it expires, all players die.
- **Flight of the Nullite [buff]**
- A buff that prevents all damage as long as any storm clouds are active.
- **Cloud Burst**
- An incurable arcane that inflicts divine damage and throws the target back. This spell is only cast while Flight of the Nullite is active.

## Strategy

Lord Shomp summons [[A nullite foot soldier]] in groups of two.

At 76%, 51%, and 26%, Lord Shomp summons several storm clouds, which can be destroyed by dispelling them. He runs from cloud to cloud uncontrollably until the last cloud is dispelled.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)begins to ride the voidstreams&quot; SD=&quot;dispell clouds&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "dispell clouds" when Lord Shomp summons his storm clouds.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)Shomp faces (?&amp;lt;Player&amp;gt;\w+)!&quot; SD=&quot;knock back ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "knock back <player>" when Lord Shomp begins casting Raywing Buffet.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)I declare you dead&quot; SD=&quot;cure curse&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "cure curse" when Lord Shomp casts Despotic Decree.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)TIMMMBERRR!&quot; SD=&quot;cure fallen&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "group cure" when Lord Shomp casts Timmmberrr!
