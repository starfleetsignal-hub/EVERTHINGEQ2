---
title: The Exhumed Executioner (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: The Exhumed Executioner
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Dominion of Pain (Untold Heroic)]]'
location: Gallows of Damnation {{waypoint 343.79, 0.52, 330.07}}
primary_damage: Disease, Slashing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- 'Gerion: Dominion of Pain (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: The Exhumed Executioner (Untold Heroic)
  url: https://eq2.fandom.com/wiki/The_Exhumed_Executioner_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/The_Exhumed_Executioner_(Untold_Heroic)?action=history
  revision: 1990709
  revised: '2026-03-14T21:18:29Z'
  license: CC BY-SA 3.0
---

## Abilities

- **Stay of Execution**
- A buff that starts at 55 increments and decrements by 1 per second. An additional increment is removed if a player and a member of the Gerion Deathsquad occupy the same gallows space. When it reaches 0 increments, it kills the entire party.
- **Up Ward**
- A buff that reduces all damage from targets not within the upper gallows. Performing a heroic opportunity replaces this with Down Ward.
- **Down Ward**
- A buff that reduces all damage from targets not within the lower gallows. Performing a heroic opportunity replaces this with Up Ward.
- **Upward Offensive Posture**
- A buff that increases fervor, flurry, and flurry multiplier every second. If dispelled while Down Ward is active, it adds 10 increments to Stay of Execution. If dispelled while Up Ward is active, it fully recharges Stay of Execution.
- **Downward Defensive Posture**
- A buff that increases ability doublecast avoidance and flurry multiplier mitigation every second. If dispelled while Up Ward is active, it adds 10 increments to Stay of Execution. If dispelled while Down Ward is active, it fully recharges Stay of Execution.
- **Verdict**: Guilty
- A curable elemental that kills the target when it expires.
- **Verdict**: Innocent
- A curable elemental that kills the target when it is cured.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Executioner)Guilty, or innocent&quot; SD=&quot;Check Verdict&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Check Verdict" when Verdict: Guilty and Verdict: Innocent are cast.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Executioner)'s posture changes&quot; SD=&quot;check posture&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "check posture" when Upward Offensive Posture and Downward Defensive Posture are cast.
