---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Epsilon Emerald
layout: default
---

# Changelog

This document serves to record changes made between releases, newest version first.

## v1.0.4

- Added even more trainer class OW gfx, thanks to shikashipx
- Allow resetting the clock in-game + time and day-of-week display
- Updated Pokemon Center layout slightly
- Allow flying to your Secret Base, if it is on a Route that can be flown to
- Added some of ORAS' Eon Ticket text / interactions
- Support shortened Wonder Codes
- Reworked trainers up to Slateport
- Added Day-Care Man to the PokeNav
- Added short notification when picking up an item fills the last slot in the Bag

- Fixed the Claw and Root Fossils being missable, if the Bag was full
- Added a test/workaround for rare GBA SP hardware issue
- Fixed level cap overflow issue for scaled trainer parties
- Fixed hatched eggs not correctly inheriting Ability and Poke Ball
- Fixed Battle Factory sometimes generating empty slots
- Fixed Pokedex game freeze when button mode L=A
- Fixed script error in Pacifidlog Town
- Fixed graphical bug with the PokeNav's region map
- Fixed trainer card badge rendering in Union Room
- Fixed transparency in Golbat icon
- Fixed Groudon Primal Reverting into Castform Sunny (lol)
- Fixed a missing failsafe when getting the Red and Blue Orbs
- Fixed some collision errors in Sky Pillar

## v1.0.3

- Reworked trainer teams up to Rustboro Gym (102, 104, Petalburg Woods)
- Fix substitute gfx when player has no pokemon
- Halve NPC IVs on Easy difficulty
- Cancelling a DexNav search now decreases the current chain by 1
- Fixed trainer position in Victory Road
- Fixed flag ordering for Mt. Pyre summit's old man
- Fixed some wrong warps/oopses in Space Center cutscenes
- Fixed tile/elevation oopses in Aqua Hideout, Sky Pillar, Granite Cave
- Fixed Secret Base trainer class rendering the wrong gender
- Make PP of held mon in the PC appear full
- Fixed Alolan Raichu & Raichu not having Surf in their learnset
- Fixed post-contest cutscene trigger for Lisia & Wallace
- Improved availability of Razor Fang and Dragon Scale
- Expanded Lavaridge Mart item selection slightly
- Fixed inaccessible item inside Abandoned Ship
- Match Call can now be accessed with 1 badge as intended
- Fixed Sap Sipper not blocking Bullet Seed

## v1.0.2

- Fixed bug with Revives in double battles
- Allowed DexNav to work inside dark caves
- Gave Obstagoon its correct cry
- Prevent Mega Stones from being (temporarily) lost to Knock Off, Thief, etc
- reworked dexnav shiny odds; they should almost exactly mirror ORAS, now
- allow 'un'bookmarking mons in DexNav
- When DexNav generates a shiny, make the icon appear shiny before encountering it
- Items used in battle are now counted correctly; blue flute, etc, no longer consumable
- fixed bug where Best Friends ribbon wouldn't count for the PokeNav's Ribbons function
- actually remove sheen limits to Pokeblock application
- fixed Route 123 boundary error
- fixed Custap Berry not activating
- fixed post-contest cutscenes being out of order (oops)
- re-added Draco Meteor to tutorable learnsets
- added one-time choice between an Ability Capsule and Ability Patch (see the old man at Ritzy Retail Remedies in Mauville)
- added a mint clerk to Mauville 1F
- fixed tile error for littleroot's light posts

## v1.0.1

- fixed bug where post-battle evolutions couldn't occur while nuzlocking
- fixed bug where pokemon in the pokedex could appear as shiny
- fixed sorting error messages when sorting empty pockets
- tried to make the save type visible to emulators like Delta and open_agb_firm; let me know if it works
- a few small tile errors
- fixed missing terminator on a string when you can't cut a tree

## v1.0.0

- Initial Release
