---
title: Sinferzall (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Sinferzall
level: '143'
difficulty: Heroic ^^^
zone: '[[The Unknown: Edge of Oblivion (Untold Heroic)]]'
location: Infernal Heights {{waypoint -304.43, 87.18, -39.16}}
primary_damage: Piercing, Magic
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
  title: Sinferzall (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Sinferzall_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Sinferzall_(Untold_Heroic)?action=history
  revision: 2002256
  revised: '2026-05-12T21:50:25Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Protruding Fangs**
- A buff that grants a chance to cast Stake on a melee hit, which inflicts slashing damage and increases all damage done to the target, multiplied by increment stacks.
- **Sledge of Oblivion**
- An incurable noxious that inflicts disease damage over time, decreases power over time, and procs Defensive Breach, a spell that inflicts magic damage over time.
- **Anticoagulant**
- A curable arcane that lands on the furthest player from Sinferzall, reduces healing received, and drains wards. This spell can only be cured by mages.
- **Sap Claret**
- A curable noxious that lands on the furthest player from Sinferzall, teleporting that player to Sinferzall. It slows the target, decreases in-combat movement speed, and kills the target on expiration. It also kills the target if it is cured within 10 meters of Sinferzall.
- **Rampant Aggression**
- A buff that increments every 4 seconds if Sinferzall's target is not a fighter and decrements every 4 seconds otherwise.

## Strategy

Sinferzall summons [[A bloating heartstopper]], which kills the nearest player when it dies. The heartstoppers randomly shuffle their hate every few seconds.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Sinferzall)hinders healing&quot; SD=&quot;mage cure arcane&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Edge of Oblivion [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "mage cure arcane" when Anticoagulant is cast.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Sinferzall)pulls the furthest of you&quot; SD=&quot;joust noxious&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Edge of Oblivion [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "joust noxious" when Sap Claret is cast.
