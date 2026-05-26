# Leno Weave

Twisted windows.

## What It Is

Leno weave is an **open mesh fabric** where adjacent warp threads are twisted around each other, with the weft passing through the twists. This locks the threads in place while creating a stable open grid.

## Construction

- **Warp twist**: Two warp ends twist around each other
- **Weft lock**: Weft passes through the twist, holding it
- **Stable openwork**: The mesh doesn't shift or fray
- **Can be combined**: Often used as ground for brocade or embroidery

## Visual DNA

- **Open grid**: Visible holes between twisted warp pairs
- **Twisted pairs**: The warp threads spiral around each other
- **Stable edges**: Unlike simple gauze, leno doesn't unravel
- **Crisp hand**: Usually firm, structured fabric
- **Common uses**: Fruit bags, sheer curtains, ground for embroidery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `mesh_density` | 2–20 | Twisted pairs per unit |
| `twist_tightness` | 0.1–1.0 | How tightly warps spiral |
| `grid_openness` | 0.3–0.9 | Ratio of hole to thread |
| `weft_presence` | 0.0–1.0 | Visibility of locking weft |

## GLSL Snippet

```glsl
float leno_weave(vec2 uv, float density) {
    float twist = sin(uv.y * density * PI) * 0.5 + 0.5;
    float grid_x = abs(fract(uv.x * density) - 0.5) * 2.0;
    float open = smoothstep(twist * 0.5, twist, grid_x);
    return open;
}
```

## Prompt Template

> "Leno weave mesh fabric in natural linen, twisted warp pairs creating stable open grid with visible spiral texture, sheer but structured, textile ground for embroidery"

## Anti-Drift

- **Not plain weave gauze**: Gauze is simple open plain weave; leno actively twists warps
- **Not lace**: Leno is woven mesh; lace is built on a ground mesh with motifs
- **Stable openwork**: The twist prevents the mesh from shifting

---

*Twisted warp, open grid. The spiral is the lock.*
