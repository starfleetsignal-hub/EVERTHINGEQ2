---
title: Bludge the Bludgeoner (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Bludge the Bludgeoner
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Graftwerk (Untold Heroic)]]'
location: Blighted Shoal {{waypoint 421.07, 9.43, 740.69}}
primary_damage: Poison, Piercing
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
- 'Zon Zobboz: The Graftwerk (Untold Heroic) Named Monsters'
source:
  title: Bludge the Bludgeoner (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Bludge_the_Bludgeoner_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Bludge_the_Bludgeoner_(Untold_Heroic)?action=history
  revision: 2012266
  revised: '2026-06-17T00:57:10Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Zon Zobbonk!**
- An incurable arcane that deals magic damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Mincemeat**
- A buff that increases flurry and melee multiplier every 2 seconds. It also adds a damage proc. If Bludge has both Mincemeat and Meatshield, then neither spell can be dispelled. Mincemeat also cannot be dispelled if any player is cursed with Rancid Retort.
- **Meatshield**
- A buff that increases potency and ability doublecast avoidance every 2 seconds. It also adds a damage proc. If Bludge has both Mincemeat and Meatshield, then neither can be dispelled. Meatshield also cannot be dispelled if any player is cursed with Rancid Retort.
- **Rancid Retort**
- A curable curse that deals increasing disease damage over time, drains 60% of wards, and disables threat transfers to and from the target. The priest's Cure Curse spell resets if there are no dumped prototypes in the fight.

## Strategy

The portal behind Bludge pushes out [[A dumped prototype]]. Initially, these creatures are very weak and can be killed in one hit. If left to recover, they join the fight as regular encounters. As the fight progresses, the portal begins pushing them out two or three at a time.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Bludge)&amp;quot;Make mincemeat!&amp;quot;&quot; SD=&quot;dispell&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Graftwerk [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "dispell" when Mincemeat is cast.
