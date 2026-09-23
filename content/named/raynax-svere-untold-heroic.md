---
title: Raynax S'Vere (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Raynax S'Vere
level: '143'
difficulty: Epic x2 ^^^
zone: '[[Gerion: Dominion of Pain (Untold Heroic)]]'
location: Pier of Judgment {{waypoint 486.26, 11.34, 280.18}}
primary_damage: Divine, Slashing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x2 Named Monsters
- 'Gerion: Dominion of Pain (Untold Heroic) Named Monsters'
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x2 Named Monsters
- Tier 15 Named Monsters
source:
  title: Raynax S'Vere (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Raynax_S'Vere_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Raynax_S'Vere_(Untold_Heroic)?action=history
  revision: 2018071
  revised: '2026-07-16T23:25:42Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Lifeblood of The Overlord**
- A buff that reduces all damage done to the caster by 90% and heals the caster for 2.0% every 3 seconds. It can be dispelled through a heroic opportunity.
- **Crime and Punishment**
- A curable elemental detriment that wounds health and power. It begins with two increments, and each cure removes one increment. Cures from classes other than mages kills the target.
- **Undying Authority**
- A buff that increases combat mitigation, ability doublecast avoidance, flurry avoidance, flurry, and fervor multiplied by increments. Increments are removed by occupying grates releasing the souls of the forgiven (orange). Increments can also be dispelled. Player curse cast while Undying Authority has any increments kills the target.
- **Souls of the Forgiven**
- A curable elemental applied while standing on an orange grate. The detriment increases melee weapon range and the range and radius of most abilities.
- **Soul Lock**
- A curable curse that lands on priests. It kills the priest if they attempt to revive a fallen player.
- **Guillotine Slash**
- A curable trauma that lands on players within 5 meters of S'Vere. It disarms the head slot of the target, if wearing a plate helmet, and kills targets whose helmet is already disarmed or is not wearing a plate helmet.
- **Grave Shackles**
- An incurable detriment that applies to any revived player. It inflicts increasing immitigable cold damage every second unless the target remains still.
- **Outlawed Opportunities**
- A curable trauma that kills the target if they start or complete a heroic opportunity.
- **Blades of Captivity**
- An incurable arcane that kills the target if they move outside the Blades of Captivity enemy.
- **Caged Beneficials**
- A curable elemental that .

## Strategy

At the start of combat, a wall of fire appears on the eastern edge of the pier, killing any player who touches it. S'Vere also summons all remaining [[A Lucanic Dreadflyer|Lucanic Dreadflyers]].

[Stage 21+] Cages fly over the platform. The path they travel is shown as a pink/orange trail across the grates.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Raynax)Guillotine Slash!&quot; SD=&quot;Joust 6 from named&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Joust 6 from named" when S'Vere begins casting Guillotine Slash.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Raynax)My liege, lend me your aid&quot; SD=&quot;heroic opportunity&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "heroic opportunity" when S'Vere begins casting Lifeblood of The Overlord.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Raynax)targets (?&amp;lt;Player&amp;gt;\w+) for Crime and Punishment&quot; SD=&quot;mage cure ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "mage cure <player>" when a player is targeted with Crime and Punishment.
