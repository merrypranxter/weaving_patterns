# Brocade

Embroidered by the loom.

## What It Is

Brocade is a **rich, decorative fabric** where supplementary weft threads are woven into the base fabric to create raised, elaborate patterns. Unlike damask, brocade adds extra threads specifically for pattern.

## Construction

- **Supplementary weft**: Extra weft threads float over the ground weave
- **Ground fabric**: Usually plain or twill weave underneath
- **Float cutting**: Modern brocade often cuts long floats on the back
- **Gold/metal threads**: Traditional brocade uses metallic supplementary wefts

## Visual DNA

- **Raised pattern**: Supplementary threads sit on top of ground
- **Lustrous contrast**: Pattern threads often shinier than ground
- **Elaborate motifs**: Floral, scroll, animal, architectural
- **Heavy hand**: Dense, substantial fabric
- **Common uses**: Evening wear, ceremonial garments, upholstery, ecclesiastical

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `supplementary_weft_thickness` | 0.002–0.02 | Raised pattern thread diameter |
| `pattern_height` | 0.0–0.1 | Normal displacement for raised effect |
| `metallic_ratio` | 0.0–1.0 | How much of pattern is metallic thread |
| `ground_visibility` | 0.0–1.0 | How much ground shows between pattern |

## GLSL Snippet

```glsl
float brocade(vec2 uv, sampler2D pattern, float height) {
    float motif = texture(pattern, uv).r;
    float raised = motif * height;
    float metallic = motif * metallic_ratio;
    return raised + metallic;
}
```

## Prompt Template

> "Rich brocade fabric in [COLOR] with gold supplementary weft pattern showing [MOTIF], raised ornate design on twill ground, metallic thread highlights, heavy ceremonial textile, flat lay"

## Anti-Drift

- **Not damask**: Damask uses weave structure; brocade adds supplementary threads
- **Not jacquard**: Jacquard is the loom mechanism; brocade is the fabric result
- **Cut vs uncut**: Cut brocade has clipped floats; uncut has long floats on back
- **Often metallic**: Gold and silver threads are traditional

---

*Supplementary weft luxury. The pattern sits on top.*
