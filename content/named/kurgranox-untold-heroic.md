---
title: Kur'Granox (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Kur'Granox
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Chimeric Chain (Untold Heroic)]]'
location: The Wretched Wombs {{waypoint -785.01, 48.89, 215.37}}
primary_damage: Disease, Cold
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
  title: Kur'Granox (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Kur'Granox_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Kur'Granox_(Untold_Heroic)?action=history
  revision: 2011530
  revised: '2026-06-10T01:11:01Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21+).

## Abilities

- **Zon Zobbonk!**
- An incurable trauma that deals slashing damage over time and decreases power over time. It also procs Defensive Breach, which inflicts magic damage over time.
- **Writhing Whiplash**
- An interruptible attack that knocks all players away from Kur'Granox. If it is interrupted while Aegis of Bloodshed is active, the casting player dies.
- **Aegis of Bloodshed**
- A buff that adds a damage proc to Kur'Granox's attacks and reduces all damage by 50%. It can be removed with [[Bulwark of Order]], which also causes Kur'Granox to lock onto the target with the most increments of Crimson Cuts for 12 seconds.
- **Null Form**
- A curable curse that reduces the target's Crit Bonus and Fervor. It also prevents the target from interfering with Eternal Thirst.
- **Eternal Thirst**
- A buff that begins gaining increments at 45%. It increases Fervor, Flurry, Flurry Multiplier, and Combat Mitigation per increment. It gains 1 increment per second for each active vat that Kur'Granox has line of sight to. It loses 1 increment per second for each active vat with a player between the vat at Kur'Granox. Line of sight is marked with a colored beam that ends at Kur'Granox (active) or a player (blocked).
- **Sanguine Surge [21+]**
- A buff that applies around 20% and increases strikethrough by 100.0% and causes Kur'Granox to select a new target every 5 seconds.

## Strategy

It is intended to fight Kur'Granox where he stands as he has a short leash range. This positioning also makes it easier to block the beams that originate from the experiment vats.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Granox)Blood (once again )?coagulates against&quot; SD=&quot;bulwark&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "bulwark" when Kur'Granox casts Aegis of Bloodshed.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Granox)tentacles uncoil violently&quot; SD=&quot;interrupt now&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Chimeric Chain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "interrupt now" when Kur'Granox casts Writhing Whiplash.
