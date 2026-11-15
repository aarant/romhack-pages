---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Epsilon Emerald
layout: patcher
---

# How to Play

Epsilon Emerald is distributed only in *patch* form---that is, in order to play the actual GBA ROM,
you'll first need to apply the patch to a clean, vanilla copy of an English Pokémon Emerald ROM.

Thanks to **byuu** for creating the BPS patch format <3

## Requirements

You will need a **clean** copy of an English base Pokémon Emerald ROM.

I can't provide or tell you where to get this; sharing ROMs is **forbidden** and legally dubious.

If you Google around though, you can easily find one, or dump your own Emerald cartridge if you have one.

## Instructions

- Load your base Emerald ROM into the patcher and make sure it shows green.
    The SHA-1 hash must be **exactly** `f3ae088181bf583e55daf962a92bb46f4f1d07b7`. The patcher will tell you if it's correct or not.
- Select your version of Epsilon Emerald, if applicable, and click **Apply patch**.
- You'll download a file named `pokeepsilon.gba`; this is your ROM!

> Note: Do not use an already existing `pokeepsilon.gba` here; each time, it must be a base Emerald ROM.

To upgrade, just replace your old `pokeepsilon.gba` with the new one; your save data will carry over!

## Recommendations

Once you have your ROM, there are a few ways to play:

- **For PC**: I reccommend mGBA: [https://mgba.io/](https://mgba.io/)
- **For Android**: I've heard good things about PizzaBoy and GBA.emu
- **For iOS**: Delta seems to be the go-to: [https://deltaemulator.com/](https://deltaemulator.com/)

> Note: !! Do not use **any** VBA emulator or its derivatives! VBA is quite inaccurate and you may run into various issues, which are beyond my scope to fix because of how outdated it is.

You can also play on a **Nintendo 3DS**, either by injecting the ROM as a `.cia` with the [New Super Ultimate Injector](https://www.gamebrew.org/wiki/New_Super_Ultimate_Injector_3DS) or baremetal with [open_agb_firm](https://github.com/profi200/open_agb_firm).

And of course, you can play on original GBA hardware, if you can get the ROM onto a suitable cartridge: GBA, GBA SP, GB Micro, GameBoy Player, etc.

> Note: If, when flashing to a flashcart, you receive an error to the effect of "The ROM file you have selected will not boot on actual hardware due to invalid boot logo data",
> click "Continue without fixing"; the flasher may be unaware that the GBA ROM header is allowed to differ in 1 byte to enable debugging behavior (which I use to show a crash screen).

## For Nerds

You can download the latest patch file [here](assets/patches/pokeepsilon.bps) and patch your base Emerald ROM locally using tools such as [Flips](https://www.smwcentral.net/?p=section&a=details&id=42149).

I sign all binaries of Epsilon Emerald with my public [PGP](https://www.gnupg.org/) key, which you can import from my GitHub:

```bash
curl -s https://github.com/aarant.gpg | gpg --import
```

You can then verify the ROM was built by yours truly, either with [this signature](./assets/patches/pokeepsilon.gba.sig) or extract the one embedded in the BPS patch manifest:

```bash
gpg --verify pokeepsilon.gba.sig
```

## Patcher