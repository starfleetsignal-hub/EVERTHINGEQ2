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
  revision: 2032073
  revised: '2026-10-12T20:19:11Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21-40/41+).

## Abilities

- **Raywing Buffet**
- Applies a knockback to targets in front of Lord Shomp. He turns to face a random player before he casts this spell.
- **Overrun**
- An incurable elemental that decreases in-combat movement speed by 5.0% per increment. Each nullite foot soldier that is not charmed, feared, mesmerized, or stunned adds an increment. At 20 increments, the player is instantly killed.
- **Zon Zobbonk!**
- An incurable elemental that deals heat damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Despotic Decree**
- A curable curse that kills the player when it expires. At stage 41+, the curse requires the target to be in one of several positions or perform one of several actions before being cured. If the requirement is not met, curing the curse kills the target. These requirements include (a) standing behind Shomp, (b) crouching, (c) standing in front of Shomp, (d) sitting, (e) standing within 2 meters of Shomp. Lord Shomp tells the target player (and only the targeted player) which action should be performed.
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
- **Make it Reign [41+]**
- A buff that increases fervor, ability doublecast avoidance, flurry avoidance, and combat mitigation for each increment. Increments can be removed by arcane dispels or by damaging Shomp for 1% of his health.

## Strategy

Lord Shomp summons [[A nullite foot soldier]] in groups of (2/2/3).

At 76%, 51%, and 26% [Stage 1-40], or at 80%, 60%, 40%, and 20% [Stage 41+], Lord Shomp summons several storm clouds, which can be destroyed by dispelling them. He runs from cloud to cloud uncontrollably until the last cloud is dispelled.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)begins to ride the voidstreams&quot; SD=&quot;dispell clouds&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "dispell clouds" when Lord Shomp summons his storm clouds.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)Shomp faces (?&amp;lt;Player&amp;gt;\w+)!&quot; SD=&quot;knock back ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "knock back <player>" when Lord Shomp begins casting Raywing Buffet.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)I declare you dead&quot; SD=&quot;cure curse&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "cure curse" when Lord Shomp casts Despotic Decree.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)TIMMMBERRR!&quot; SD=&quot;cure fallen&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "group cure" when Lord Shomp casts Timmmberrr!
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Shomp)must be cured WHILE (?&amp;lt;Position&amp;gt;[A-Z ]+)!&quot; SD=&quot;${Position} then cure&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "<Position> then cure" when Lord Shomp casts Despotic Decree at stages 41+.
