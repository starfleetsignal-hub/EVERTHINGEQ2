---
title: The Abominable Dreadarou (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: The Abominable Dreadarou
race: Gruengach
level: '143'
difficulty: Heroic ^^^
zone: '[[Zon Zobboz: The Graftwerk (Untold Heroic)]]'
location: Abominable Bluff {{waypoint 626.56, 105.32, 630.27}}
primary_damage: Crushing, Disease
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Gruengach
- Heroic Named Monsters
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: The Graftwerk (Untold Heroic) Named Monsters'
source:
  title: The Abominable Dreadarou (Untold Heroic)
  url: https://eq2.fandom.com/wiki/The_Abominable_Dreadarou_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/The_Abominable_Dreadarou_(Untold_Heroic)?action=history
  revision: 2028534
  revised: '2026-09-08T21:28:45Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes with stages (1-20/21+).

## Abilities

- **Zon Zobbonk!**
- **Bloodcurdling Bleat**
- An incurable trauma that throws the target back and wounds the target's health by 10% multiplied by increments. All increments are removed when the Parasite reattaches to the Dreadarou. It also reduces incoming damage by a percentage proportional to wounds.
- **Healthiest of Hosts**
- A curable elemental that lands on the entire group when a Bulbous Parasite spawns. When cured from all players, the Parasite curses the player with the highest health. If that player has less health than the Dreadarou, nothing happens to the player, and the Parasite reattaches to the Dreadarou.
- **Gangrenous Glare**
- An incurable detriment that decreases the effectiveness of noxious mitigation, reduces healing, and forces the player to target only the Bulbous Parasite.
- **Hoof and Mouth Disease**
- A curable curse that slows the target by 100.0%. When cured, it resets the priest's Cure Curse. It kills the target on expiration. When the target casts a hostile ability, it casts Bulbous Blisters on the player. At 21+, it kills the target if cured while the target has Bulbous Blisters.
- **Bulbous Blisters**
- A curable noxious that inflicts disease damage multiplied by increment stacks. It also reduces fervor by 20%. At 10 increments, it kills the target.
- **Bloodgraft**
- A curable curse that inflicts increasing heat damage over time. When terminated, the Bulbous Parasite reattaches to the Dreadarou. At 21+, it also disarms the head slot and kills target on expiration.

## Strategy

Throughout the fight, the Dreadarou's head detaches, adding [[A Bulbous Parasite]] to the encounter. While its head is detached, the Dreadarou attacks randomly and cannot be controlled.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dreadarou)lets out a Bloodcurdling Bleat&quot; SD=&quot;knockback&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Graftwerk [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "knockback" when the Dreadarou begins casting Bloodcurdling Bleat.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Dreadarou)Your hostile abilities cause you to form blisters!&quot; SD=&quot;stop attack, cure curse&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Graftwerk [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "stop attack, cure curse" when the Dreadarou casts Hoof and Mouth Disease.
