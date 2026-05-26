# Plain Weave

The simplest weave. The fundamental binary.

## Construction

- Warp goes over one weft, under the next, alternating every pick
- Weft goes over one warp, under the next, alternating every thread
- Repeat unit: 2×2
- Binary matrix: `[[1,0],[0,1]]` (or `[[0,1],[1,0]]` — equivalent)

## Visual Characteristics

- Flat, even surface
- No diagonal lines, no floats over 1
- Matte appearance (unless high-thread-count silk)
- Crisp, grid-like texture at close range
- Strongest weave structure per thread

## Variations

### Balanced Plain Weave
Warp and weft counts are equal. Threads are equally visible.

### Unbalanced Plain Weave
Warp count ≠ weft count. One direction dominates visually.

### Basket Weave (Derivation)
Plain weave with grouped threads: 2/2, 3/3, 4/4. Creates checkerboard texture.

## Shader Parameters

```glsl
float plain_weave(vec2 uv, float warp_count, float weft_count) {
    float x = fract(uv.x * warp_count);
    float y = fract(uv.y * weft_count);
    float warp_bit = step(0.5, x);
    float weft_bit = step(0.5, y);
    // XOR: warp visible when bits differ
    return abs(warp_bit - weft_bit);
}
```

| Parameter | Value Range | Notes |
|-----------|-------------|-------|
| `warp_count` | 20–200 | Threads per unit |
| `weft_count` | 20–200 | Usually equal to warp |
| `thread_thickness` | 0.3–0.7 | In cell space (0–1) |
| `tension_variance` | 0.0–0.05 | Slight waviness |

## Material Examples

- **Muslin**: Fine cotton plain weave, semi-sheer
- **Calico**: Medium-weight cotton, often printed
- **Percale**: High-thread-count cotton, crisp hand
- **Taffeta**: Silk plain weave, slight rib from filament
- **Canvas**: Heavy cotton/linen, coarse threads

## Prompt Notes

Plain weave is the default. To make it interesting, specify:
- Fiber type (raw silk, hand-spun cotton, wild flax)
- Thread irregularity (slub, neps, variation)
- Dye method (solid, space-dyed, ikat)
- Scale (gauze-sheer vs canvas-heavy)

## Common Confusions

- **Plain weave vs muslin**: Muslin is a fabric weight; plain weave is a structure. Muslin is usually plain weave, but not all plain weave is muslin.
- **Plain weave vs percale**: Percale is plain weave with thread count ≥ 180.

## Drift Repair

If plain weave looks flat/boring:
- Add fiber fuzz or slub texture
- Add slight tension variance for organic waviness
- Add raking light to show thread roundness
- Add dye variation or ikat blur
