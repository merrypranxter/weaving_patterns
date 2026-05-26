# Damask

Reversible figured fabric.

## What It Is

Damask is a **reversible patterned fabric** woven on a jacquard loom, using a satin weave to create the pattern and a contrasting satin weave (or plain weave) for the ground. The pattern is visible on both sides in reversed colors.

## Construction

- **Satin weave basis**: Pattern area = satin floats; ground = different weave
- **Reversible**: Same pattern, opposite color relationship on reverse
- **Single color family**: Traditionally monochrome (white/ivory, red/crimson)
- **Monochrome depth**: Pattern visible through light play, not color contrast

## Visual DNA

- **Subtle sheen contrast**: Satin pattern catches light differently than ground
- **Reversible elegance**: Both sides are presentable
- **Classical motifs**: Floral scrolls, medallions, architectural elements
- **Monochrome luxury**: Depth created by weave, not color
- **Common uses**: Table linens, bedding, formalwear, upholstery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `pattern_satin_angle` | 0°–90° | Direction of pattern floats |
| `ground_satin_angle` | 0°–90° | Direction of ground floats (usually perpendicular) |
| `sheen_contrast` | 0.1–0.5 | Difference in specular between pattern/ground |
| `motif_complexity` | 0–1 | Simple geometric to elaborate scrollwork |

## GLSL Snippet

```glsl
float damask(vec2 uv, sampler2D motif, float shine) {
    float pattern = texture(motif, uv).r;
    float specular = mix(0.2, 0.8, pattern) * shine;
    return specular;
}
```

## Prompt Template

> "White silk damask tablecloth with [MOTIF] pattern, reversible figured fabric showing satin weave pattern against matte ground, light catching the raised satin areas, classical luxury textile"

## Anti-Drift

- **Not brocade**: Brocade uses supplementary weft; damask uses weave structure alone
- **Reversible**: Both sides are presentable; brocade has a messy back
- **Monochrome tradition**: Multi-colored damask exists but is less traditional
- **Named after Damascus**: Historical silk trading city

---

*Reversible figured satin. The light reveals the pattern.*
