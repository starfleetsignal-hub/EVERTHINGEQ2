---
title: Xigothid (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Xigothid
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Chimeric Chain (Untold Heroic)]]'
location: The Skyvarium {{waypoint -793.40, 103.10, 598.44}}
primary_damage: Magic, Disease
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
  title: Xigothid (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Xigothid_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Xigothid_(Untold_Heroic)?action=history
  revision: 1990732
  revised: '2026-03-15T00:29:04Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Tentacle Lash**
- A curable arcane that . Cures from players other than a mage instantly kill the target. This attack can be avoided by facing away from Xigothid.
- **Grav Flux**
- An incurable trauma that launches players straight up into the air and causes them to descend slowly.
- **Barrage**: Unfathomable Foray
- An attack that can only be blocked with [[Bulwark of Order]].

## Strategy

Xigothid summons [[Gazer gestation goo]] from the southern experiment orb, which begins wandering towards one of the remaining two experiment orbs. If it reaches its destination, it transforms into an Epic creature with its own Barrage attack.

At 45%, black holes begin appearing on the platform. Players have a very short time to get out of the circle before falling through to the Gore Dump below. These holes remain for the duration of the fight.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Xigothid)begins to tamper with gravity&quot; SD=&quot;knock up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "knock up" when Xigothid begins casting Grav Flux.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Xigothid)gazer gestation goo (before|flows)&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a gazer gestation goo spawns.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Xigothid)lashes out at everyone&quot; SD=&quot;face away&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "face away" when Xigothid begins casting Tentacle Lash.
