---
title: The Summoned Swarmguard
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Zon Zobboz: The Outer Swarmyard (Raid)]]'
location: The Wretched Wombs {{waypoint -777.84, 48.97, 209.04}}
primary_damage: Crushing, Poison
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: The Outer Swarmyard (Raid) Named Monsters'
source:
  title: The Summoned Swarmguard
  url: https://eq2.fandom.com/wiki/The_Summoned_Swarmguard
  history: https://eq2.fandom.com/wiki/The_Summoned_Swarmguard?action=history
  revision: 2018059
  revised: '2026-07-16T21:25:47Z'
  license: CC BY-SA 3.0
---

The Summoned Swarmguard is a Tier 1 raid boss. It gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Conscription of Blight**
- A buff that has a chance to trigger Ocular Blight on an attacker, which interrupts and deals disease damage and debuffs offensive ability.
- **Monstrous Ambition**
- A buff that decreases damage taken from all sources for each active [[A Swarming Monstrous Elemental|Swarming Monstrous Elemental]]. Each additional Elemental beyond 2 heals the Swarmguard slightly.
- **Deliquescent Ambition**
- A buff that decreases damage taken from all sources for each active [[A Swarming Deliquescent|Swarming Deliquescent]]. Each additional Deliquescent beyond 2 heals the Swarmguard slightly.
- **Swarmed Ambition**
- A buff that decreases damage taken from all sources for each active [[A Swarming Goo|Swarming Goo]]. Each additional goo beyond 2 heals the Swarmguard slightly.
- **Surging Swarm**
- An incurable elemental that deals increasing elemental and poison damage to health and power over time.
- **Overbearing Influence I**
- An incurable trauma that makes power usage also cost health.
- **Swarmguard's Affliction**
- A curable trauma that deals crushing damage and increases elemental and noxious damage from all sources.
- **Poisonous Burst I**
- A curable noxious that
- **Flame Burst I**
- A curable elemental that
- **Mark of Resistance**
- An incurable trauma that deals slashing damage and increases noxious, elemental, and arcane damage from all sources. It can be blocked with area effect blockers.
- **Noxious Mists**
- **Corrosive Lash**
- A curable noxious with three increments that deals growing poison damage and decreases spell casting and damage potential for each increment applied.
- **Overloading Destruction**
- A curable curse that transfers to another player when it is cured. If the target dies, or the curse expires, an additional Swarming monster is summoned into the fight. A second failure additionally kills the target. A third failure additionally kills the target's group. A fourth failure additionally kills the entire raid.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

The Summoned Swarmguard summons his own pets throughout the fight: [[A Swarming Monstrous Elemental]], [[A Swarming Deliquescent]], and [[A Swarming Goo]]. These pets are identical other than name and appearance. Each attempts to heal the Swarmguard if they are close enough to it, and each locks onto the Swarmguard's current target when they arrive. The heal decreases as the monsters are pulled farther from the Swarmguard, failing to heal at all at a sufficient distance. The Swarmguard can also direct the pet to attack the Swarmguard's current target, locking it to that player.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Swarmguard)is summoned into the fight&quot; SD=&quot;add up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Outer Swarmyard [Raid]&quot; T=&quot;T&quot; TN=&quot;Obsidian Mind&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "add up" when a Swarming monster is summoned.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Swarmguard)Swarmguard.*focusing his allies' attention&quot; SD=&quot;tank swap&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: The Outer Swarmyard [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "tank swap" when the Swarmguard snaps a monster to its current target.
