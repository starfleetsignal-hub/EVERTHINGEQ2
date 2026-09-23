---
title: Do'Guen (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Do'Guen
level: '143'
difficulty: Heroic ^^^
zone: '[[The Unknown: Edge of Oblivion (Untold Heroic)]]'
location: wanders {{waypoint -270.33, 96.91, 173.26}}
primary_damage: Slashing, Cold
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Unknown: Edge of Oblivion (Untold Heroic) Named Monsters'
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: Do'Guen (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Do'Guen_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Do'Guen_(Untold_Heroic)?action=history
  revision: 2002259
  revised: '2026-05-12T22:16:45Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Sledge of Oblivion**
- An incurable arcane that deals divine damage over time, decreases power over time, and procs Defensive Breach, which deals magic damage.
- **Hail Bent**
- A incurable elemental that deals increasing cold damage over time, decreases power over time, stuns the target, and reduces fervor. It also knocks back players that are not fighters. This effect lands on players in front of Do'Guen.
- **Void-Bound**
- An incurable elemental that deals cold damage and decreases power multiplied by increments. Leaving the Void-Bound Aura removes all increments. It also increases melee weapon range and hostile ability range.
- **Snatch Prey**
- An attack that pulls the closest player into the center of the Void-Bound Aura.
- **Unyielding Pain**
- An incurable elemental that deals high damage. It can be removed with a fighter's [[Intercept]].
- **Void-Cursed Bleeding**
- A curable curse that inflicts increasing slashing damage over time.

## Strategy

When the fight begins, Do'Guen summons all remaining [[A void-bound companion|void-bound companions]] throughout the zone.

At 75% and 25%, Do'Guen places a Void-Bound Aura (purple/blue bubble) around herself. While it is up, she is rooted to the center of the aura. Players within the aura are slowed and receive increasing damage. Purple pillars around the outside of the aura pull players back into the center. While the aura is up, Do'Guen continuously summons [[A void-bound slasher]].

At 50%, Do'Guen releases her Void-Bound Aura and summons four [[A darkened slasher|darkened slashers]]. She is immune to all damage until these four companions are killed.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;DoGuen)gathers ice to blast forward&quot; SD=&quot;frontal&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Edge of Oblivion [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "frontal" when Hail Bent begins casting.
