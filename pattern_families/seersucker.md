# Seersucker

Puckered summer magic.

## What It Is

Seersucker is a **thin fabric with alternating smooth and puckered stripes**, created by weaving some warp threads under higher tension than others. The tension difference causes the fabric to pucker into permanent ridges.

## Construction

- **Tension differential**: Some warp threads are held tighter during weaving
- **Automatic puckering**: When tension releases, some threads relax and pucker
- **No pressing needed**: The texture is woven in, not pressed
- **Cotton tradition**: Almost always cotton or cotton blend

## Visual DNA

- **Striped puckers**: Alternating smooth and bumpy vertical bands
- **Permanent texture**: Doesn't iron flat
- **Breathable**: Puckers hold fabric away from skin
- **Summer classic**: Light colors (blue/white, pink/white)
- **Common uses**: Summer suits, shirts, dresses, children's clothing

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `pucker_amplitude` | 0.0–0.1 | Normal displacement for ridges |
| `stripe_width` | 0.02–0.1 | Width of smooth/puckered bands |
| `tension_ratio` | 0.5–2.0 | Relative tension between warp groups |
| `color_alternation` | 0–1 | Color stripe or texture stripe |

## GLSL Snippet

```glsl
float seersucker(vec2 uv, float stripe_width) {
    float stripe = floor(uv.x / stripe_width);
    float is_pucker = mod(stripe, 2.0);
    float pucker = is_pucker * sin(uv.y * 50.0) * amplitude;
    return pucker;
}
```

## Prompt Template

> "Classic blue and white seersucker cotton fabric, alternating smooth and puckered vertical stripes, permanent woven-in texture, summer suit material, light and airy, flat lay"

## Anti-Drift

- **Not crinkle fabric**: Crinkle is pressed or chemically treated; seersucker is woven
- **Not pleated**: Pleats are folded; seersucker is tension-woven
- **Usually striped**: The puckers often align with color stripes
- **Summer only**: Heavy seersucker is a contradiction

---

*Tension differential. The pucker is woven in.*
