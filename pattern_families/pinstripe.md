# Pinstripe

The line of power.

## What It Is

Pinstripe is a **very narrow vertical stripe** woven into fabric, traditionally in dark wool suiting with thin light-colored lines. It's associated with business, banking, and formal menswear.

## Construction

- **Warp stripes**: Thin colored warp threads on dark ground
- **Even spacing**: Usually widely spaced, 1/2" to 1" apart
- **Suiting base**: Almost always worsted wool
- **Color logic**: Ground = dark (navy, charcoal, black); stripe = light (white, grey)

## Visual DNA

- **Vertical emphasis**: Elongating, formal, structured
- **Minimal contrast**: Subtle, not bold
- **Business association**: Banker, lawyer, formal uniform
- **Chalk vs. pin**: Chalk stripe is wider and softer; pinstripe is thin and sharp
- **Common uses**: Business suits, formal trousers, occasional womenswear

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stripe_width` | 0.001–0.01 | Very thin lines |
| `stripe_spacing` | 0.05–0.5 | Distance between stripes |
| `ground_color` | RGB | Dark base |
| `stripe_color` | RGB | Light line |

## GLSL Snippet

```glsl
float pinstripe(vec2 uv, float width, float spacing) {
    float stripe = smoothstep(width, 0.0, abs(fract(uv.x / spacing) - 0.5) * spacing);
    return stripe;
}
```

## Prompt Template

> "Navy worsted wool pinstripe suiting fabric, thin white vertical warp stripes spaced evenly on dark ground, formal business textile, sharp tailored appearance, flat lay"

## Anti-Drift

- **Not chalk stripe**: Chalk is wider, softer, more casual; pin is thin and sharp
- **Not banker stripe**: Banker stripe is wider and more pronounced
- **Vertical only**: Pinstripe is always vertical; horizontal pinstripe is not a thing
- **Not printed**: Woven pinstripe has depth; printed lacks dimensionality

---

*Thin vertical line. The stripe is authority.*
