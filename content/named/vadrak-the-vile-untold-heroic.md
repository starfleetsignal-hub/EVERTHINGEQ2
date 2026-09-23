---
title: Vadrak the Vile (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Vadrak the Vile
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Chimeric Chain (Untold Heroic)]]'
location: Ichor Grounds {{waypoint -441.78, 9.52, 844.63}}
primary_damage: Heat, Slashing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: The Chimeric Chain (Untold Heroic) Named Monsters'
source:
  title: Vadrak the Vile (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Vadrak_the_Vile_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Vadrak_the_Vile_(Untold_Heroic)?action=history
  revision: 2011529
  revised: '2026-06-10T01:00:11Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21+).

## Abilities

- **Radioactive Decay**
- A curable curse that increases all damage done to target by 1%, multiplied by increments. It increments by 1 every second. Curing any player also cures all other players and reduces the priest's Cure Curse reuse by the amount of increments. After being cured, the curse is reapplied to all targets.
- **Zon Zobbonk!**
- An incurable elemental that deals heat damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Gamma Ray**
- An incurable elemental that hits all targets in front of Vadrak. He turns to face a random player before he casts this spell.
- **Gamma Blast**
- A slow-casting attack that wipes the entire group if a fighter is not in the correct relative position. Vadrak calls the required position (only visible to the tank) prior to casting the spell. For example, if the tank reads "A fighter positioned 4th from Vadrak can absorb the blast", then the tank needs to be the 4th closest person to Vadrak. Any position between 1st (closest) and 6th (furthest) can be called.
- **Fungal Fever**
- A buff that increments for each fungified nullite killed within 10 meters of Vadrak. The buff instantly heals him for 5.0% and dispels hostile abilities. For each increment, it increases fervor, ability doublecast avoidance, flurry avoidance, and combat mitigation. At 10 increments, all players are immediately killed. Increments can be removed by killing an [[Ichorbloom pollen]] within 10 meters of Vadrak.
- **Irradiated Hide**
- A buff that automatically applies at (51%/60%). It adds a damage shield that deals heat damage and drains power. It cannot be removed.
- **Fungal Fallout**
- A buff that automatically applies at 25%. It adds a damage proc to all of Vadrak's attacks that deals disease and heat damage and decreases power of targets.
- **Meltdown [21+]**

## Strategy

When pulled, Vadrak summons all remaining [[An ichor fiend|ichor fiends]] to his side.

Vadrak continuously summons [[A fungified nullite]] into the fight.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Vadrak)Vile&amp;#92;&amp;#92;/a faces (?&amp;lt;Player&amp;gt;\w+)!&quot; SD=&quot;frontal ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "frontal <player>" when Vadrak begins casting Gamma Ray.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Vadrak)A fighter positioned (?&amp;lt;Position&amp;gt;\w+) (?**: to|from) Vadrak&quot; SD=&quot;move ${Position}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "move <position>" when Vadrak begins casting Gamma Burst.
