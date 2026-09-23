---
title: Infernal Tyrant Dennigrah (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Infernal Tyrant Dennigrah
race: Lamia
level: '143'
difficulty: Epic x2 ^^^
zone: '[[The Unknown: Edge of Oblivion (Untold Heroic)]]'
location: Infernal Pinnacle {{waypoint 219.30, 156.89, 57.31}}
primary_damage: Heat, Piercing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x2 Named Monsters
- Lamia
- Monsters that award AA
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Unknown: Edge of Oblivion (Untold Heroic) Named Monsters'
- Tier 15 Epic x2 Named Monsters
- Tier 15 Named Monsters
source:
  title: Infernal Tyrant Dennigrah (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Infernal_Tyrant_Dennigrah_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Infernal_Tyrant_Dennigrah_(Untold_Heroic)?action=history
  revision: 2002267
  revised: '2026-05-12T23:24:13Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Sledge of Oblivion**
- An incurable arcane that inflicts mental damage over time, decreases power over time, and procs Defensive Breach, which deals magic damage.
- **Consumer's Caress**
- A buff that increases Combat Mitigation, Ability Doublecast Avoidance, Flurry Avoidance, Dodge, and the chance to reflect hostile abilities for each active Ebonlithe in the encounter. The entire party is killed at 10 increments.
- **Beguiling Bond**
- A curable arcane that roots, slows, and decreases in-combat movement speed of targets.
- **Dazzling Dance**
- A curable arcane that mesmerizes targets and decreases power over time.
- **Infernal Consummation**
- An incurable elemental that only lands on a fighter. On any combat or spell hit, it has a chance to cast Eternal Pain onto a player within 5 meters of the fighter.
- **Eternal Pain**
- An incurable elemental that inflicts increasing heat damage over time. It can be removed with a fighter's [[Intercept]].
- **Infernal Tyranny**
- A curable curse that inflicts disease damage over time and reduces fervor. When cured, it summons an Ebonlith, which clears the reuse of [[Cure Curse]] when killed. The curse lands on all players except fighters.
- **Cthurath's Will**
- An incurable detriment that initially has 5 increments. It increases by 1 when a curse is cured from the target. It decreases by 1 if the target dies or if the target is hit by Testament to the Consumer (which also summons an Ebonlithe). If any player reaches 0 increments, or if any player reaches 10 increments, the entire party is killed.

## Strategy

Dennigrah casts Testament to the Consumer with a medium-length cast time. This spell targets one particular player, hitting that player and all nearby players. For each player it hits, it summons an Ebonlithe and decreases the increments on Cthurath's Will.

Dennigrah summons a linked pair of [[A flight fiend]] and [[A fright fiend]].

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Tyrant)High Priestess targets (?&amp;lt;Player&amp;gt;\w+)&quot; SD=&quot;joust ${Player} joust&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Edge of Oblivion [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "joust <player> joust" when Dennigrah casts Testament to the Consumer.
