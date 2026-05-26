# Satin Weave

Long floats, liquid light.

## What It Is

Satin weave is defined by **long floats** — threads that pass over many warp (or weft) threads before going under one. This creates a smooth, reflective surface with minimal thread intersection visibility.

## Construction

- **Float length**: 4–12+ threads (longer = more lustrous)
- **Point of interlacement**: Single thread goes under, creating "points" in the pattern
- **Regular spacing**: Points are distributed to avoid tracking lines
- **Common counts**: 5-harness, 8-harness satin

## Visual DNA

- **Mirror surface**: High reflectivity from long floats catching light
- **Soft hand**: Smooth, slick texture
- **Color depth**: Light penetrates surface and reflects from within
- **Reversible distinction**: Satin (warp-float face) vs. sateen (weft-float face)
- **Common uses**: Evening wear, linings, ribbons, bridal

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `float_length` | 4–12 | Threads per float |
| `harness_count` | 5, 8, 12 | Shafts controlling the point |
| `specular_power` | 32–128 | Shininess of float surface |
| `thread_angle` | 0°–45° | Direction of light reflection |

## GLSL Snippet

```glsl
float satin_weave(vec2 uv, float harness, float point_spacing) {
    float x = mod(uv.x * harness, 1.0);
    float point = step(point_spacing, x);
    float float_region = 1.0 - point; // Long float area
    return float_region;
}
```

## Prompt Template

> "[COLOR] satin fabric with [HARNNESS]-harness weave, long floating threads creating a mirror-like reflective surface, light sliding across the cloth in liquid highlights, luxury evening wear material"

## Anti-Drift

- **Not twill**: Twill has diagonal lines; satin has no visible diagonal
- **Long floats snag easily**: The surface is delicate
- **Satin vs sateen**: Satin = warp floats on face; sateen = weft floats on face
- **Shiny is not always satin**: Some fabrics are calendered (pressed) to shine

---

*Long floats, liquid surface. The thread is the mirror.*
