# Basket Weave

Over-two, under-two. Plain weave on steroids.

## What It Is

Basket weave is a variation of plain weave where **two or more warp threads** are treated as one unit, and **two or more weft threads** cross them as a unit. The result looks like a woven basket — a checkerboard of larger squares.

## Construction

- **Warp grouping**: 2+ ends working as one
- **Weft grouping**: 2+ picks working as one
- **Balance**: Symmetric when warp group = weft group count
- **Common variants**: 2×2, 3×3, 4×4 basket weave

## Visual DNA

- **Macro checkerboard**: Large squares visible at arm's length
- **Squared texture**: Individual threads visible within each square
- **Soft drape**: More flexible than plain weave due to longer floats
- **Reversible**: Same appearance on both sides
- **Common uses**: Suitings, monk's cloth, oxford cloth shirts

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `group_size` | 2–8 | Threads per group unit |
| `thread_thickness` | 0.001–0.02 | Relative to group spacing |
| `gap_between_groups` | 0.0–0.05 | Visual separation |

## GLSL Snippet

```glsl
float basket_weave(vec2 uv, float group_size) {
    vec2 grid = floor(uv * group_size);
    float checker = mod(grid.x + grid.y, 2.0);
    return checker; // 0 or 1 for over/under
}
```

## Prompt Template

> "Basket weave fabric in [COLOR], showing 2×2 grouped thread checkerboard pattern, visible macro-squares with finer thread texture within each block, soft suiting fabric, flat lay"

## Anti-Drift

- **Not plain weave**: Plain weave has no grouping; basket has visible macro squares
- **Not leno**: Leno twists warp threads; basket groups them
- **Oxford cloth is basket**: The "oxford" in oxford cloth refers to 2×2 basket structure

---

*Grouped plain weave. The square is the unit.*
