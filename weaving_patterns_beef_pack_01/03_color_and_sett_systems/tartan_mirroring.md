# Tartan Mirroring

## What it controls

Tartan Mirroring defines how color and spacing behave before the cloth surface exists.

In woven systems, color is not simply painted onto a plane. Color is carried by individual threads.

## Structural rules

- warp colors run lengthwise
- weft colors run crosswise
- intersections mix optically
- sett controls scale and density
- repeating color orders can align with or fight the weave structure

## Generative use

Represent warp and weft as arrays:

```js
const warpColors = ['navy', 'cream', 'red', 'cream'];
const weftColors = ['navy', 'cream', 'red', 'cream'];
```

Then the visible cell chooses a color from whichever thread is on top.

## Prompt language

Use phrases like thread-dyed, sett repeat, warp stripe sequence, weft stripe sequence, optical color mixing at intersections.
