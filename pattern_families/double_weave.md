# Double Weave

Two fabrics, one loom.

## What It Is

Double weave produces **two layers of fabric simultaneously**, interwoven at the edges or at selected points. The layers can be the same or different colors/patterns, and can be connected or separate.

## Construction

- **Two warp sets**: One for top layer, one for bottom
- **Two weft sets**: Interlacing independently
- **Interchange points**: Where layers swap position or connect
- **Tube possibility**: If only connected at edges, forms a tube

## Visual DNA

- **Reversible contrast**: Top and bottom may be different colors
- **Pocket structures**: Layers connected at points create puff areas
- **Thickness**: Visibly thicker than single-layer fabric
- **Weight**: Heavy, substantial hand
- **Common uses**: Blankets, upholstery, bags, technical textiles

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `layer_separation` | 0.0–0.2 | Visual gap between layers |
| `interchange_freq` | 0–10 | Points where layers swap per unit |
| `top_color` | RGB | Upper layer color |
| `bottom_color` | RGB | Lower layer color |
| `pocket_size` | 0.05–0.5 | Size of connected areas |

## GLSL Snippet

```glsl
vec3 double_weave(vec2 uv, vec3 top, vec3 bottom, float interchange) {
    float swap = step(0.5, sin(uv.x * interchange) * sin(uv.y * interchange));
    return mix(top, bottom, swap);
}
```

## Prompt Template

> "Double weave blanket in [COLOR 1] and [COLOR 2], two layers visible at cut edges, interchanging at woven points to create pocket structures, thick heavy hand, warm winter textile"

## Anti-Drift

- **Not quilting**: Quilting sews layers together; double weave interweaves them
- **Two layers simultaneously**: Not one layer sewn to another
- **Tube potential**: Unconnected edges create fabric tubes

---

*Two layers, one construction. The interchange is the architecture.*
