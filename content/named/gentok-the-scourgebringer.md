---
title: Gentok the Scourgebringer
type: named
race: Orc
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Spiral of Vul (Contested)]]'
location: Verge of Oblivion
primary_damage: Crushing, Mental
drops:
- '[[Gentok''s Phantasmal Conduit]]'
achievement_xp: true
added_in: LU128
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- LU128 Named Monsters
- Monsters that award AA
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Orc
- Spiral of Vul (Contested) Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Gentok the Scourgebringer
  url: https://eq2.fandom.com/wiki/Gentok_the_Scourgebringer
  history: https://eq2.fandom.com/wiki/Gentok_the_Scourgebringer?action=history
  revision: 2020797
  revised: '2026-08-02T12:33:45Z'
  license: CC BY-SA 3.0
---

Gentok the Scourgebringer is a Tier 3 contested raid boss. To summon Gentok, a raid force of at least 12 players must be present, and the following items must be added to the pillar in the center of the room.

- [[Figurine of the Scourgebringer]]
- [[Gentok's Contained Rage]]
- [[Gentok's Void-Touched Blade]]

The portal into the Verge of Oblivion is located at {{waypoint 16.41, 91.64, -14.76}} within the Spires of Deth Vuldor. The portal can only be seen by players who have completed the achievement [[Triumph: Life and Limbo]]. Using the portal pulls the entire raid into Verge of Oblivion, regardless of how many have completed the triumph. The portal is inactive while [[Gynethra]] (a heroic boss) is alive.

## Statistics

- Flurry Avoidance: 525.0
- Ability Doublecast Avoidance: 590.0
- Resolve: 11,195.0

## Abilities

- **Fist of Scourge**
- An incurable noxious that deals fast ticking poison damage and increases incoming elemental damage from all sources.
- **Scourgebringer's Touch**
- A curable curse that deals slashing damage and dazes non-fighters.
- **Vicious Slam**
- A curable trauma that deals light damage over time.
- **Vicious Followup**
- A curable arcane that heals Gentok for each player still afflicted with Vicious Slam.
- **Skinned and Prepped**
- An incurable curse that lowers maximum health to 50%. If the target dies before the curse expires, then all players afflicted with Skinned and Prepped die simultaneously. This attack is marked on the ground with a yellow frontal cone.
- **Dragonbone Strike**
- An incurable arcane that lands on targets in front of Gentok. The attack deals "extreme damage to anything it hits in front of Churaggus [SIC]..."

## Strategy

Gentok occasionally becomes "bored" of his current target, dropping them to the bottom of the hate list. For a short period of time, that player cannot generate any hate.

## ACT Triggers

- &lt;Trigger R=&quot;(?&amp;#35;Gentok)a mighty forward strike&quot; SD=&quot;get behind&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Spiral of Vul [Contested]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "get behind" when Gentok begins casting Dragonbone Strike.
- &lt;Trigger R=&quot;(?&amp;#35;Gentok)looks for another target&quot; SD=&quot;tank swap&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Spiral of Vul [Contested]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;
  - Calls "tank swap" when Gentok becomes bored with his current target.
