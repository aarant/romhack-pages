---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Epsilon Emerald
layout: default
---

# FAQ

### So when can I play it?

**You can play it now!** But this is not the end: I'll be supporting and providing updates well into 2027.

---

### So how can I play it?

You'll need an [emulator](https://mgba.io/) (or other equivalent hardware) and a copy of the base Pokémon Emerald ROM.
You can either use the patcher on this site or download a `.bps` file and patch it locally.

---

### Which Pokémon are included?

All 386 species from Generations 1-3, any regional forms, evolutions, and Mega Evolutions of those 386, Riolu & Lucario, and... something secret.

This means, for example, that Roserade, Alolan Ninetales, Sirfetch'd, Annihilape, etc are present, but not convergent species like Wugtrio.

This is partly philosophical (I don't believe 1000+ Pokémon fit nicely into Hoenn) and partly practical (every species, except Riolu & Lucario, appears to vanilla as its base species as it would exist in Generation 3).

> Note: At this time, the Hisuian forms are in the game code, but not distributed anywhere (yet).

---

### Can I use save-editing or other tools?

Yes! Epsilon Emerald saves should be fully compatible with save-editing tools like PKHeX.
You can even load a vanilla Emerald save in Epsilon or vice versa, or trade with vanilla.

Generally, if a tool works with vanilla Emerald, it should work with Epsilon as well.

---

### Can I transfer to Pokémon Bank/Home?

Yes... mostly! I've done my best to make sure that Pokémon caught in Epsilon are legitimate: any encounters that are not legitimate in vanilla are generated as if they were hatched from vanilla's POV, and there are other such tricks for things like Deoxys' met level and Faraway Island Mew's language.

Before atttempting to transfer to Home, though, definitely check your Pokémon in PKHeX, and do whatever cleanup might be needed there (especially with new moves/items).

---

## What are the shiny odds?

### They start at full odds: 1/8192. There are a few ways to get +1/8192, or an extra 'roll' for an encounter to be shiny:

- The Shiny Charm, rewarded for completing the Hoenn Dex, gives +2/8192
- Donating daily to the Ninetales statue postgame gives +1/8192
- The Masuda method for breeding gives +5/8192

Note that DevNav calculates its shiny odds differently, more inline with [ORAS](https://bulbapedia.bulbagarden.net/wiki/DexNav#Shiny_probability).

---

### How does Epsilon differ from vanilla Emerald and Omega Ruby / Alpha Sapphire?

Being built on `pokeemerald-expansion` means I have the luxury of picking and choosing which modern battle mechanics I want:
- The physical/special split is present
- The Fairy type exists
- Abilities and base stats generally are as they would be in Generation 9
- Learnsets are composite: mostly they follow Gen 6, but with modern moves added
- Hail replaces Snow, but still gives a +1 Defense boost to Ice-types

Additionally, there are a few small changes gifting certain Pokémon a new ability or type--it's very minor and meant to make certain underused Pokémon more interesting.

---

### Will you provide documentation?

Yes, though don't expect it to be pretty! I will export encounter tables, item locations, and boss information in a readable format. Evolution and learnset information can already be found in the in-game Pokédex.

---

### Will you add X/Y/Z?

**Maybe.** There is a roadmap after this release, broadly consisting of:

- Fixing bugs and feedback stemming from the release
- Finishing the import of Gen 9 forms and Mega Evolutions
- Upgrading the underlying version of pokemon-expansion
- Adding Acessories from Gen 4 into the 1st stage of Contests
- Adding a shopping channel to BuzzNav / TV
- PSS (Player Search System) functionality: GTS, Wonder Trade, Record Mixing, via the Mobile Adapter
- Preparation for Kanto and Johto
- Adding skin tone customization for the player
- Adding Regigigas, Regidrago, and Regieleki encounters
- Integrating Poké Transporter GB
- Balance adjustments, especially for Easy difficulty
- Adding an IV judge
- Uploading the soundtrack to YouTube
- Adding Sylveon

I **may** add the following:

- A randomizer, for those who want to do roguelike runs

I won't be adding these:

- Significant battle/overworld speedup
- Multiple save slots

---

### Can I transfer to Pal Park?

Yes, with a few caveats: we're still ironing out a few wrinkles with legitimacy.

For certain pokemon, the met game could appear as any of the other Generation 3 games, like Ruby (Zangoose), Sapphire (Lunatone), FireRed (Unown caught in Altering Cave, postgame), Colosseum (Legendary Beasts caught in Trackless Forest), etc.

Other pokemon appearing in locations they don't in vanilla may appear as if they were hatched from Eggs, instead.

As for items/moves unrecognized by Gen 4, they'd either be dropped, or you'd need to remove the item/move(s) before transferring.

---

### How do I enable auto-run?

Just Double-tap B!

---

### I just encountered a trainer with a Shiny Pokémon! Is that intended?

Yes: the rich boy/lady trainers have Shiny Pokémon. Perks of being wealthy, I guess.

---

### How do I obtain Mythical Pokémon?

Periodically until Bank's closure, I'll be releasing distributions for these Pokémon in the form of Wonder Cards / Codes.
These can be redeemed at any time.

There are also plans for a free DLC of sorts for Jirachi, though that will likely not land until after Bank closes.

---

### How do I unlock Mystery Gift?

Three ways! You can:

- Enter "LINK TOGETHER WITH ALL" in the questionnaire at any Mart
- Import a Mystery Gift Wonder Code via mGBA savestate
- Enter the following sequence on the Continue screen (must have reached Petalburg): `Select Up Up Down Down Left Right Left Right`

---

### How do I import Wonder Codes?

You can either:

- (mGBA only): Download the .ss1 file associated with the card, load your game in mGBA, then go to File -> Load state file. Locate the file you downloaded and press A!
- Type in the Wonder Code, by going to Mystery Gift -> Wonder Cards -> Wonder Code

---

### How do I view my Pokémon's EVs?

You can view them in the PokéNav's Condition screen after obtaining the Effort Ribbon.

---

### How do I change my Pokémon's nature/IVs?

For natures, you can use nature mints! (see [Items](../items))

For IVs, you can use Hyper Train your level 100 Pokémon with an NPC at the Battle Frontier.

---

### What glitches are kept from the base game?

Just the fun ones! (ones that can't be triggered accidentally and don't cause inconvenience)

Some examples are pomeg corruption, mail glitch, battle pike poison knockout glitch, dive gltich, etc.

---

### Is HM02 (Fly) fully replaced by Lati@s Soaring?

No, you can still Fly normally, and even issue a Fly command from the PokéNav and fly to routes.

---

### Which trainer teams have been overhauled? In what ways?

Every single trainer in the game was overhauled. Often I based the teams around what I thought would be fun, or funny, based on how GameFreak sometimes did.

For bosses, team and set selection often came out of the manga, aspects of their personality, etc.

---

### Can you rematch Brendan/May?

Yes, on Route 103 in the postgame.

---

### Is Steven or Wallace the champion?

Wallace is the champion at first, but don't worry! You'll still battle Steven at some point.

---

### Where can I find the shiny leaves?

The location of each of the five shiny leaves (A-E) depends on your Pokémon's nature. See the below chart:

| Natures                                                                          	| Leaf Locations                                                                                       	|
|----------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------	|
|    Hardy<br>Lonely<br>Brave<br>Adamant<br>Naughty<br>Bold<br>Docile<br>Relaxed   	| A: Routes 101 and 102<br>B: Route 110<br>C: Route 113<br>D: Route 116<br>E: Routes 119, 122, and 123 	|
|      Impish<br>Lax<br>Timid<br>Hasty<br>Serious<br>Jolly<br>Naive<br>Modest      	| A: Routes 101 and 102<br>B: Route 111<br>C: Route 114<br>D: Route 117<br>E: Routes 120, 122, and 123 	|
| Mild<br>Quiet<br>Bashful<br>Rash<br>Calm<br>Gentle<br>Sassy<br>Careful<br>Quirky 	| A: Routes 101 and 104<br>B: Route 112<br>C: Route 115<br>D: Route 118<br>E: Routes 121, 122, and 123 	|

---