# Tartan / Plaid

The color-grid weave. The clan barcode.

## Construction

Tartan is a **colored plain weave** where warp and weft threads follow a repeating color sequence (the "sett"). Where colors intersect, they blend.

- **Sett**: The complete color sequence before repeat
- **Thread count**: Number of threads of each color in sequence
- **Balanced tartan**: Warp sett = weft sett
- **Asymmetric tartan**: Warp and weft have different setts

## Visual Characteristics

- Grid of colored blocks
- Intersections create blended colors (warp + weft)
- Overcheck lines: thin contrasting threads crossing the field
- Usually 2–6 colors in sett
- Repeat can be simple (4 colors) or complex (20+ threads)

## The Sett Math

A sett is described as a thread count sequence:
> "K4 B24 G24 K24 Y4" = Black 4, Blue 24, Green 24, Black 24, Yellow 4

This sequence repeats in both warp and weft. The intersection grid creates the pattern.

## Major Tartan Families

### Scottish Clan Tartans
- Each clan has registered sett patterns
- Ancient (vegetable dyes, muted), modern (synthetic dyes, bright), hunting (muted for field), dress (white background)

### District Tartans
- Regional patterns not clan-specific

### Universal / Fashion Tartans
- Non-clan, designed for aesthetic

### Non-Scottish Plaids
- **Madras**: Indian cotton plaid, bright colors, often bleed
- **Black Watch**: Dark military tartan
- **Royal Stewart**: Bright red-based tartan, most recognized
- **Burberry check**: Beige-based fashion plaid

## Shader Parameters

```glsl
vec3 tartan(vec2 uv, float sett_size, int num_colors, vec3 palette[], int sett_counts[]) {
    float warp_pos = fract(uv.x / sett_size);
    float weft_pos = fract(uv.y / sett_size);
    
    int warp_idx = 0;
    float accum = 0.0;
    for (int i = 0; i < num_colors; i++) {
        accum += float(sett_counts[i]) / float(total_threads);
        if (warp_pos < accum) { warp_idx = i; break; }
    }
    
    // Same for weft
    int weft_idx = get_sett_index(weft_pos, sett_counts);
    
    vec3 warp_color = palette[warp_idx];
    vec3 weft_color = palette[weft_idx];
    
    // Intersection: blend or add depending on fiber
    vec3 intersection = mix(warp_color, weft_color, 0.5);
    
    return intersection;
}
```

| Parameter | Value Range | Notes |
|-----------|-------------|-------|
| `sett_size` | 0.05–0.5 | Size of full color repeat in UV |
| `num_colors` | 2–8 | Palette size |
| `thread_ratio` | 0.3–0.7 | Visible thread width in cell |
| `overcheck_width` | 1–4 threads | Thin contrast lines |
| `blend_mode` | mix/add/overlay | How colors combine at intersections |

## Material Examples

- **Wool tartan**: Heavy, traditional, crisp hand
- **Silk tartan**: Lighter, shinier, drapier
- **Cotton plaid**: Madras, flannel, shirting
- **Polyester plaid**: Uniform, bright, less texture

## Prompt Notes

Tartan prompts must specify:
- The sett colors and approximate thread counts
- Material (wool, silk, cotton)
- Scale (shirting-weight vs blanket-weight)
- Tradition (clan name or "fashion plaid")

## Common Confusions

- **Tartan vs plaid**: In Scotland, "tartan" = registered pattern; "plaid" = any check. In America, "plaid" = tartan.
- **Tartan vs gingham**: Gingham is dyed-yarn check with usually 2 colors; tartan has more colors and complex sett
- **Woven vs printed plaid**: Printed plaid lacks thread intersections and has uniform color blocks

## Drift Repair

If tartan looks like printed check:
- Add thread-level detail — individual threads visible
- Add intersection blending at color crossings
- Add slight thread waviness (no cloth is perfectly flat)

If tartan colors are too uniform:
- Add slight variation per thread (dye lot variation)
- Add raking light to show thread roundness
