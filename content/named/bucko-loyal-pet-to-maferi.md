---
title: Bucko, Loyal Pet to Maferi
type: named
expansion: Scars of Destruction
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Sodden Archipelago: Thawed Marshes (Raid)]]'
location: Sultry Dunes Gate {{waypoint 111.74, 131.52, 133.22}}
health: 279 Quadrillion
primary_damage: Pierce, Slash
achievement_xp: true
added_in: Scars of Destruction
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Scars of Destruction Named Monsters
- 'Sodden Archipelago: Thawed Marshes (Raid) Named Monsters'
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Bucko, Loyal Pet to Maferi
  url: https://eq2.fandom.com/wiki/Bucko,_Loyal_Pet_to_Maferi
  history: https://eq2.fandom.com/wiki/Bucko,_Loyal_Pet_to_Maferi?action=history
  revision: 1871750
  revised: '2025-04-14T02:39:51Z'
  license: CC BY-SA 3.0
---

Bucko, Loyal Pet to Maferi is a Tier 1 raid boss.

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

- **Surging Gashes**
- An incurable arcane that deals increasing arcane damage to health and power over time.
- **Noxious Storm**
- A curable noxious that deals fast ticking poison damage to targets within 45 meters and increases incoming physical damage from all sources.
- **Stalwart Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types within 45 meters. This effect cannot be blocked.
- **Venomous Slice**
- A curable noxious that deals fast ticking poison damage to targets within 45 meters.
- **Blurred Sight**
- A curable arcane that blurs vision and deals fast ticking increasing arcane damage over time.
- **Remembrance**
- The target of Remembrance will be remembered by the caster. If checked again, and the caster's target is already the target of Remembrance, they will be slain.
- **Aftershock Release**
- A curable trauma that deals growing arcane damage. When removed, it triggers Aftershock Reverberation on all allies within 10 meters of the target player, which deals much faster physical damage and slows movement speed for 20 seconds.

## Strategy

Bucko summons pets called Shelled Repairer, Loyal Pet to Bucko, which periodically heal Bucko. These smaller pets do not move.

Bucko casts an AoE that appears as a large pink bubble. Players within the bubble are killed (unless they are Bucko's current target).

## ACT Triggers

- &amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Bucko&amp;amp;gt;places a favored mark on (?&amp;amp;lt;Player&amp;amp;gt;\w+))&amp;quot; SD=&amp;quot;tank swap ${Player}&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes [Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;
  - Calls "tank swap <player>" when <player> has just been hit with Remembrance.
- &amp;lt;Trigger R=&amp;quot;(?&amp;amp;lt;Bucko&amp;amp;gt;[A-F0-9]{6}(?&amp;amp;lt;Player&amp;amp;gt;\w+) prepares to purge physical damage)&amp;quot; SD=&amp;quot;Get away ${Player}&amp;quot; ST=&amp;quot;3&amp;quot; CR=&amp;quot;T&amp;quot; C=&amp;quot;Sodden Archipelago: Thawed Marshes [Raid]&amp;quot; T=&amp;quot;F&amp;quot; TN=&amp;quot;&amp;quot; Ta=&amp;quot;F&amp;quot; /&amp;gt;
  - Calls "get away <player>" when <player> has just been hit with Aftershock Release.
