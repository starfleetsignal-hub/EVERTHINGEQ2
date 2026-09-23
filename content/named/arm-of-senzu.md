---
title: Arm of Senzu
type: named
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Flooded Scar: Abyssal Assault (Raid)]]'
primary_damage: Poison
achievement_xp: true
added_in: LU128
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- 'Flooded Scar: Abyssal Assault (Raid) Named Monsters'
- LU128 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Arm of Senzu
  url: https://eq2.fandom.com/wiki/Arm_of_Senzu
  history: https://eq2.fandom.com/wiki/Arm_of_Senzu?action=history
  revision: 1877049
  revised: '2025-05-30T03:30:22Z'
  license: CC BY-SA 3.0
---

## Statistics

- Resolve: matches Zeraloth
- Ability Doublecast Avoidance: matches Zeraloth
- Flurry Avoidance: matches Zeraloth

## Abilities

- **Mercurial Mitigation vs. Casting**
- A buff that increases Ability Doublecast Avoidance by 300.0, decreases Flurry Avoidance by 300.0, decreases auto-attack mitigations, and increases ability mitigations. When dispelled, it is immediately replaced with Mercurial Mitigation vs. Melee.
- **Mercurial Mitigation vs. Melee**
- A buff that decreases Ability Doublecast Avoidance by 300.0, increases Flurry by 300.0, decreases ability mitigations, and increases auto-attack mitigations. When dispelled, it is immediately replaced with Mercurial Mitigation vs. Casting.
- **Agility of Senzu**
- A buff that absorbs all incoming damage if no scouts have Agility of Senzu. The detriment of the same name causes Escape to teleport the group the the scout's targeted Unfathomable Tentacle, sets the recast time of Escape to 10 seconds, and prevents the scout from being interrupted due to movement. This "detrimental" effect remains active after the Arm of Senzu is defeated.
- **Ravenous Hunger**
- An attack that instantly kills a random member of the raid, heals the Arm significantly, and dispells the Arm's current Mercurial Mitigation. It can be interrupted by scouts. If any other class interrupts this attack, it instantly kills the player who interrupted and performs all other effects as if the spell cast successfully.
- **Senzu's Encore**
- An attack that kills all scouts unless interrupted by the correct class. The class that needs to interrupt depends on whether Senzu's Ballad or Senzu's Lament is active.
- **Senzu's Ballad**
- An incurable noxious that allows rangers, swashbucklers, troubadours, and beastlords to interrupt Senzu's Encore. Kills the target if the target is also afflicted with Senzu's Lament.
- **Senzu's Lament**
- An incurable noxious that allows assassins, brigands, and dirges to interrupt Senzu's Encore. Kills the target if the target is also afflicted with Senzu's Ballad.

## ACT Triggers

- <code>&lt;Trigger R=&quot;Senzu &amp;#92;&amp;#92;&amp;#35;[A-F0-9]{6}attempts to sate&quot; SD=&quot;scout interrupt Senzu&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Flooded Scar: Abyssal Assault [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "scout interrupt Senzu" when the Arm begins casting Ravenous Hunger.
