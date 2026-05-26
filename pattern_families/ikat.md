# Ikat / Kasuri

Resist-dyed before weaving.

## What It Is

Ikat (kasuri in Japan) is a **resist-dye technique applied to threads before weaving**, creating patterns with characteristic feathered, blurred edges where dyed and undyed sections meet at the loom.

## Construction

- **Warp ikat**: Warp threads resist-dyed in pattern before weaving
- **Weft ikat**: Weft threads resist-dyed before weaving (more difficult)
- **Double ikat**: Both warp and weft resist-dyed (extremely rare, e.g. Patan, India)
- **Tie-resist**: Threads bound in pattern, then dyed; bindings removed before weaving

## Visual DNA

- **Feathered edges**: The resist boundaries blur slightly when woven
- **Color bleeding**: Small amounts of dye migrate past resist lines
- **Pattern alignment**: Requires careful loom setup to align dyed sections
- **Traditional motifs**: Geometric, floral, or abstract depending on region
- **Common uses**: Silk and cotton garments, upholstery, ceremonial textiles

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `dye_bleed` | 0.0–0.05 | UV space blur at resist boundary |
| `thread_alignment` | 0.0–1.0 | How perfectly dyed sections align |
| `ikat_type` | 0–2 | 0 = warp, 1 = weft, 2 = double |
| `motif_complexity` | 0–1 | Simple bands to elaborate patterns |

## GLSL Snippet

```glsl
float ikat(vec2 uv, float dye_bleed, sampler2D resist_pattern) {
    float resist = texture(resist_pattern, uv).r;
    float blur = gaussian_blur(resist, uv, dye_bleed);
    return blur;
}
```

## Prompt Template

> "Hand-woven [TYPE] ikat silk in [COLOR PALETTE], showing resist-dyed threads with characteristic feathered edges where color boundaries meet, traditional [REGION] textile, slight irregularity from hand binding"

## Anti-Drift

- **Not printed**: Ikat is dyed before weaving; the pattern is in the threads
- **Not tie-dye**: Tie-dye is resist-dye on finished cloth; ikat is on threads before weaving
- **Feathered edges are signature**: Sharp edges = not ikat
- **Double ikat is rare**: Most ikat is warp-only; double ikat is master-level craft

---

*Resist-dyed threads. The blur is the evidence.*
