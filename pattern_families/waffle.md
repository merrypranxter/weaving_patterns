# Waffle Weave

Grid of tiny pockets.

## What It Is

Waffle weave creates a **three-dimensional grid** of recessed squares by combining plain weave sections with warp and weft floats. The result looks like a breakfast waffle — raised edges around sunken cells.

## Construction

- **Recessed cells**: Plain weave centers sink below the surface
- **Raised ribs**: Float threads create the grid walls
- **Reversible texture**: Same 3D effect on both sides
- **Absorbency**: The pockets hold moisture (towels, thermal blankets)

## Visual DNA

- **Pocket grid**: Small square indentations across the surface
- **Ribbed borders**: Raised lines between pockets
- **Thermal quality**: Trapped air in pockets provides insulation
- **Textured hand**: Tactile, dimensional surface
- **Common uses**: Thermal blankets, dish towels, spa robes

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `cell_size` | 0.02–0.1 | Size of each pocket |
| `rib_width` | 0.005–0.02 | Width of raised border |
| `depth` | 0.0–0.15 | Normal displacement for pocket recess |
| `grid_spacing` | 0.03–0.15 | Distance between cell centers |

## GLSL Snippet

```glsl
float waffle_weave(vec2 uv, float cell_size) {
    vec2 cell = fract(uv / cell_size);
    vec2 border = smoothstep(0.0, 0.15, cell) * smoothstep(1.0, 0.85, cell);
    float pocket = border.x * border.y;
    return pocket; // 1.0 = recessed, 0.0 = raised rib
}
```

## Prompt Template

> "White cotton waffle weave thermal blanket, 3D grid of small square pockets with raised rib borders between them, absorbent texture, spa towel material, soft even lighting"

## Anti-Drift

- **Not honeycomb**: Honeycomb is a different weave with hexagonal cells
- **Pockets are structural**: The indentations are woven in, not pressed
- **Reversible**: Both sides show the same texture

---

*Pocket grid. The cell is the feature.*
