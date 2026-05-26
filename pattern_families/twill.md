# Twill

The diagonal weave. The workhorse of durability and drape.

## Construction

Each weft pick shifts the interlacing point by a fixed step, creating a diagonal line across the fabric.

- Step size = 1: Basic twill (45° diagonal)
- Step size = 2: Steep twill (>45°)
- Step size = 3+: Very steep, can look like satin

## Visual Characteristics

- Diagonal ribs ("wale") visible on surface
- Floats of 2–4 threads create ridges
- Drapes well due to thread mobility in floats
- Strong and durable — used for denim, gabardine, chino
- Direction matters: Z-twill (left) vs S-twill (right)

## The Twill Family

### 2/1 Twill
Float of 2, under 1. Basic diagonal.

### 3/1 Twill
Float of 3, under 1. Steeper, more pronounced ribs.

### 2/2 Twill (Balanced)
Also called "equilibrium twill." Common in wool suiting.

### Broken Twill
Reverses direction at intervals — creates zigzag or diamond.

### Herringbone
Broken twill with sharp reversal. Zigzag pattern.

### Chevron
Broken twill with smooth reversal. V-shaped pattern.

## Shader Parameters

```glsl
float twill(vec2 uv, float count, float step_size, float float_length) {
    float x = fract(uv.x * count);
    float y = fract(uv.y * count);
    float diagonal = fract(x + y * step_size);
    float visibility = step(1.0 - float_length / count, diagonal);
    return visibility;
}
```

| Parameter | Value Range | Notes |
|-----------|-------------|-------|
| `count` | 30–300 | Threads per unit |
| `step_size` | 1–3 | Diagonal angle control |
| `float_length` | 2–5 | Consecutive overs |
| `rib_depth` | 0.0–0.1 | Normal displacement for wale |

## Material Examples

- **Denim**: 3/1 cotton twill, indigo-dyed warp, white weft
- **Gabardine**: Steep twill, fine wool, smooth surface
- **Chino**: 2/1 twill, cotton, khaki-dyed
- **Cavalry twill**: Heavy wool, steep twill, riding breeches
- **Surah**: Silk twill, soft drape

## Prompt Notes

The twill diagonal is the signature. Specify:
- Direction (Z-left or S-right)
- Steepness (shallow vs steep)
- Material weight (heavy denim vs light surah)
- Wash/wear (raw denim fade lines along twill ribs)

## Denim-Specific Details

Denim is 3/1 twill with indigo-dyed warp and undyed weft.
- Right side = indigo diagonal ribs (warp-dominant)
- Wrong side = lighter, weft-dominant
- Fades along twill ribs, creating vertical streaks
- Whiskers and honeycombs form at stress points

## Common Confusions

- **Twill vs satin**: Both use floats, but satin distributes floats evenly; twill creates diagonal lines
- **Herringbone vs chevron**: Herringbone has sharp, broken reversal; chevron has smooth, continuous V
- **Denim vs chambray**: Chambray is plain weave; denim is twill

## Drift Repair

If twill looks like plain weave:
- Increase `step_size` to make diagonal visible
- Increase `rib_depth` for stronger normal displacement
- Add raking light from diagonal direction to catch wale

If twill looks like satin:
- Reduce float length
- Ensure diagonal is continuous, not scattered
