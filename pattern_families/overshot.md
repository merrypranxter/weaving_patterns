# Overshot

Floats become the pattern.

## What It Is

Overshot is a **supplementary weft pattern weave** on a plain weave ground. A thick pattern weft floats over groups of warp threads in regular sequences, creating geometric motifs on a simple ground.

## Construction

- **Ground weave**: Plain weave with fine warp and weft
- **Pattern weft**: Thicker supplementary weft that floats over groups
- **Tie-down points**: Pattern weft goes under occasionally to anchor it
- **Traditional motifs**: "Monks belt," "Star of Bethlehem," "Blooming leaf"

## Visual DNA

- **Geometric motifs**: Diamonds, stars, curves on rectangular grids
- **Float texture**: Thick pattern threads sit visibly on surface
- **Color contrast**: Pattern weft usually different color from ground
- **Reversible distinction**: Pattern side vs. plain reverse (often called "float side")
- **Common uses**: Colonial American coverlets, traditional weaving, table runners

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `pattern_weft_thickness` | 0.005–0.03 | Thick supplementary weft |
| `float_group_size` | 2–8 | Warp threads per float |
| `tie_down_frequency` | 0.1–0.5 | How often pattern weft anchors |
| `motif_library` | — | Traditional overshot patterns |

## GLSL Snippet

```glsl
float overshot(vec2 uv, float group_size, float pattern) {
    vec2 grid = floor(uv * group_size);
    float float_region = mod(grid.x + grid.y, 2.0);
    float tie_down = step(0.5, fract(uv.x * tie_freq));
    return float_region * (1.0 - tie_down);
}
```

## Prompt Template

> "Traditional overshot woven coverlet in [COLOR] pattern weft on natural cotton ground, thick supplementary floats creating geometric [MOTIF] design, American colonial textile, handwoven"

## Anti-Drift

- **Not brocade**: Brocade has more complex float patterns; overshot is simpler and geometric
- **Ground is always plain weave**: The pattern is purely from supplementary weft
- **Float side vs. back**: The reverse shows long floats; this is normal and expected

---

*Supplementary weft on plain ground. The float is the picture.*
