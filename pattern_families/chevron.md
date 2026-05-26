# Chevron Weave

Point-to-point geometry.

## What It Is

Chevron weave creates continuous **V-shaped stripes** or **zigzag lines** running across the fabric. Unlike herringbone, the points connect rather than breaking.

## Construction

- **Point repeat**: Rows meet at sharp angles creating arrow shapes
- **Color logic**: Often uses color blocks within the V shapes
- **Can be twill-based or plain-based**: Structure varies by complexity
- **Scale range**: From subtle texture to bold graphic statement

## Visual DNA

- **Arrow/peak motifs**: Repeating upward or downward points
- **Striped V's**: Color bands following the point shape
- **Bold graphic quality**: Strong visual rhythm
- **60s/70s association**: Common in vintage upholstery and fashion
- **Common uses**: Blankets, upholstery, fashion, military insignia fabric

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `v_angle` | 30°–90° | Sharpness of the point |
| `stripe_width` | 0.02–0.2 | Width of each colored band |
| `point_spacing` | 0.05–0.5 | Distance between peaks |
| `color_count` | 2–6 | Number of colors in repeat |

## GLSL Snippet

```glsl
float chevron(vec2 uv, float spacing, float angle) {
    float x = uv.x;
    float sawtooth = abs(fract(x / spacing) - 0.5) * 2.0;
    float y_offset = sawtooth * spacing * tan(angle);
    float pattern = step(0.5, fract((uv.y + y_offset) / stripe_width));
    return pattern;
}
```

## Prompt Template

> "Bold chevron woven blanket in [COLOR PALETTE], continuous V-shaped stripes in alternating colors, sharp points meeting across the fabric, 1970s graphic textile aesthetic"

## Anti-Drift

- **Not herringbone**: Chevron is continuous; herringbone has a visible break
- **Not zigzag stitch**: This is woven, not embroidered
- **Military chevrons**: The insignia derives from this shape

---

*Point-to-point. The arrow is the rhythm.*
