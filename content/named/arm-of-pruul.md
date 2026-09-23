---
title: Arm of Pruul
type: named
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Flooded Scar: Abyssal Assault (Raid)]]'
achievement_xp: true
added_in: LU123
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- 'Flooded Scar: Abyssal Assault (Raid) Named Monsters'
- LU123 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
source:
  title: Arm of Pruul
  url: https://eq2.fandom.com/wiki/Arm_of_Pruul
  history: https://eq2.fandom.com/wiki/Arm_of_Pruul?action=history
  revision: 1877253
  revised: '2025-06-09T02:07:05Z'
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
- **Ravenous Hunger**
- An attack that instantly kills a random member of the raid, heals the Arm significantly, and dispells the Arm's current Mercurial Mitigation. It can be interrupted by scouts. If any other class interrupts this attack, it instantly kills the player who interrupted and performs all other effects as if the spell cast successfully.
- **Wisdom of Pruul**
- A buff that absorbs all damage if no priests have Wisdom of Pruul. The detriment of the same name sets the recast time of Cure Curse to 10 seconds and prevents the priest from being interrupted due to movement. This "detrimental" effect remains active after the Arm of Pruul is defeated.
- **Perils of Pruul**
- A curable curse that drains 50% of all wards every 2 seconds. It kills the target on expiration. If a second player in the same group also has a curse (any curse, not just Perils), then the entire group is slain instantly.

## ACT Triggers

- <code>&lt;Trigger R=&quot;Pruul &amp;#92;&amp;#92;&amp;#35;[A-F0-9]{6}attempts to sate&quot; SD=&quot;priest interrupt Pruul&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Flooded Scar: Abyssal Assault [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
  - Calls "priest interrupt Pruul" when the Arm begins casting Ravenous Hunger.
