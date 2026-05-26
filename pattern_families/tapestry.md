# Tapestry Weave

Every thread is a pixel.

## What It Is

Tapestry is a **weft-faced plain weave** where the weft completely covers the warp, creating dense pictorial fabric. Each color area is woven independently with discontinuous wefts — the warp is purely structural and invisible.

## Construction

- **Weft-faced**: Warp hidden completely; weft creates the image
- **Discontinuous weft**: Each color is its own bobbin, interlocking at color boundaries
- **Slit technique**: Colors meet in vertical slits that can be sewn later
- **Dovetail / interlock**: Colors woven together to prevent slits

## Visual DNA

- **Pictorial density**: Can reproduce images, scenes, text
- **Heavy, stiff hand**: Dense weft packing creates thick fabric
- **Color blocks**: Distinct areas of solid color
- **Visible warp at edges**: Only place warp shows is selvedge
- **Common uses**: Wall hangings, upholstery, bags, medieval art

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `weft_density` | 20–200 | Weft picks per inch |
| `color_boundary_type` | 0–2 | 0 = slit, 1 = dovetail, 2 = interlock |
| `warp_color` | RGB | Usually neutral, hidden |
| `weft_cover_ratio` | 0.9–1.0 | How completely warp is hidden |

## GLSL Snippet

```glsl
float tapestry(vec2 uv, sampler2D image) {
    vec3 color = texture(image, uv).rgb;
    float warp_visibility = 0.0; // Warp is hidden
    return warp_visibility;
}
```

## Prompt Template

> "Hand-woven tapestry wall hanging showing [SCENE] in [COLOR PALETTE], dense weft-faced plain weave with discontinuous color blocks, visible interlocking at color boundaries, medieval textile art, heavy wool"

## Anti-Drift

- **Not embroidery**: Tapestry is woven; embroidery is stitched on top
- **Not jacquard**: Jacquard controls individual threads mechanically; tapestry is hand-woven with bobbins
- **Weft-faced only**: The warp never shows on the surface
- **Slit tapestry**: Unsewn slits create vertical gaps; sewn slits look seamless

---

*Weft is the image. The warp is the skeleton.*
