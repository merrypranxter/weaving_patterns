# Kente

Proverbs in cloth.

## What It Is

Kente is a **Ghanaian woven cloth** made of narrow strips sewn together, featuring bold geometric patterns with symbolic meaning. Each color and pattern combination represents a proverb, historical event, or social value.

## Construction

- **Strip weaving**: Narrow bands woven on horizontal treadle looms
- **Strip assembly**: Multiple strips sewn edge-to-edge for wider cloth
- **Supplementary weft**: Pattern created by extra weft threads floated over ground
- **Color symbolism**: Each color has specific meaning (gold = wealth, green = growth, etc.)

## Visual DNA

- **Bold geometry**: Triangles, squares, diamonds, zigzags in strong colors
- **Strip boundaries**: Visible seams where strips join
- **Asymmetric blocks**: Pattern blocks shift and change across the cloth
- **High contrast**: Bright colors against dark or contrasting grounds
- **Common uses**: Ceremonial wear, graduation stoles, cultural celebration

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `strip_width` | 0.05–0.2 | Width of woven strip |
| `block_size` | 0.02–0.1 | Pattern unit within strip |
| `color_symbolism` | — | Map colors to meanings |
| `weft_float_ratio` | 0.3–0.8 | How much pattern weft shows |

## GLSL Snippet

```glsl
float kente(vec2 uv, float strip_w, float block_s) {
    float strip = floor(uv.x / strip_w);
    vec2 block = fract(uv / block_s);
    float motif = geometric_pattern(block, strip);
    return motif;
}
```

## Prompt Template

> "Traditional Ghanaian kente cloth in [COLOR SET], bold geometric supplementary weft patterns with symbolic blocks of triangles and zigzags, narrow woven strips assembled into wider cloth, ceremonial Ashanti textile"

## Anti-Drift

- **Not just "African print"**: Kente is specifically Ghanaian, woven, and strip-based
- **Not printed**: The pattern is woven, not surface-printed
- **Color meaning matters**: Each color carries specific symbolism
- **Strip construction is visible**: You can see where strips join

---

*Proverbs in woven strips. The pattern is the message.*
