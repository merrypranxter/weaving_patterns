# Weaving Patterns

Warp. Weft. Shed. Pick. Float. Repeat.

This repository documents woven textile structures as **procedural binary systems** — interlaced thread grids where the visual pattern emerges from over-under logic.

## The Core Principle

Weaving is a 2D binary matrix. At every intersection:
- **Warp** (vertical/lengthwise thread) goes **over** → cell = 1
- **Warp** goes **under** → cell = 0

The pattern is entirely determined by this binary choice across the grid.

## Visual DNA of Woven Cloth

- **Orthogonal grid** — threads cross at 90°
- **Thread visibility** — floats (consecutive overs/unders) create ridges and shadows
- **Anisotropic highlights** — light catches differently on warp vs weft direction
- **Selvedge edge** — the finished side where weft turns around
- **Repeat unit** — the smallest block of interlacing that tiles seamlessly

## The Weave Families

### Basic Weaves
- [Plain weave](pattern_families/plain_weave.md) — 1/1 alternation, simplest binary
- [Basket weave](pattern_families/basket_weave.md) — grouped plain weave, checker texture
- [Twill family](pattern_families/twill.md) — diagonal ribs, float progression
- [Satin / sateen](pattern_families/satin.md) — long floats, smooth surface

### Complex Weaves
- [Herringbone](pattern_families/herringbone.md) — zigzag twill reversal
- [Chevron weave](pattern_families/chevron.md) — V-shaped twill
- [Waffle weave](pattern_families/waffle_weave.md) — recessed square grid
- [Leno weave](pattern_families/leno.md) — twisted warp pairs, open mesh
- [Double weave](pattern_families/double_weave.md) — two layers interchanged

### Figured / Programmable Weaves
- [Jacquard](pattern_families/jacquard.md) — programmable pattern, unlimited design
- [Damask](pattern_families/damask.md) — reversible figured weave, one color each side
- [Brocade](pattern_families/brocade.md) — supplementary weft floats for pattern
- [Tapestry weave](pattern_families/tapestry.md) — discontinuous weft, pictorial

### Patterned Ground Weaves
- [Overshot](pattern_families/overshot.md) — supplementary pattern weft on plain ground
- [Seersucker](pattern_families/seersucker.md) — puckered stripe, tension differential

### Check / Plaid / Stripe Systems
- [Tartan / plaid](pattern_families/tartan.md) — colored warp/weft sett repeats
- [Gingham](pattern_families/gingham.md) — dyed yarn checks, simple color grid
- [Houndstooth](pattern_families/houndstooth.md) — broken twill check
- [Pinstripe](pattern_families/pinstripe.md) — narrow warp stripe on solid ground

### Dye-Weave Hybrids
- [Ikat / kasuri](pattern_families/ikat.md) — resist-dyed threads before weaving
- [Kente-style strip](pattern_families/kente.md) — narrow woven strips joined
- [Moiré silk](pattern_families/moire.md) — watered fabric, optical interference

## Shader Translation: Weave-Specific Parameters

| Parameter | What It Controls | Range | Notes |
|-----------|---------------|-------|-------|
| `warp_count` | Threads per unit horizontally | 10–500 | Higher = finer cloth |
| `weft_count` | Threads per unit vertically | 10–500 | Often equals warp for balanced cloth |
| `warp_thickness` | Visible diameter of warp | 0.001–0.1 | In UV space |
| `weft_thickness` | Visible diameter of weft | 0.001–0.1 | Often slightly larger than warp |
| `float_length` | Consecutive overs/unders | 1–20 | Determines smoothness vs texture |
| `twill_step` | Diagonal shift per row | 1–5 | 1 = basic twill, 2 = steep twill |
| `satin_float` | Long float in satin | 4–12 | More = smoother, less durable |
| `thread_color` | Color per thread | RGB | Tartan uses multiple colors |
| `nap_direction` | Light reflection angle | 0°–180° | For velvet pile, corduroy |
| `tension_variance` | Tension irregularity | 0.0–1.0 | Creates organic waviness |

## Weave-to-Shader Logic

### Basic Interlacing
```glsl
float weave(float uv_x, float uv_y, float warp_count, float weft_count) {
    float warp_phase = fract(uv_x * warp_count);
    float weft_phase = fract(uv_y * weft_count);
    float over = step(0.5, warp_phase);
    float under = step(0.5, weft_phase);
    // Plain weave: alternate every intersection
    float interlace = abs(over - under);
    return interlace; // 1.0 = warp visible, 0.0 = weft visible
}
```

### Twill Logic
```glsl
float twill(float uv_x, float uv_y, float count, float step_size) {
    float x = fract(uv_x * count);
    float y = fract(uv_y * count);
    float diagonal = fract(x + y * step_size);
    return step(0.5, diagonal);
}
```

### Tartan / Plaid Logic
```glsl
vec3 tartan(float uv_x, float uv_y, float sett_size) {
    float warp_band = floor(fract(uv_x / sett_size) * num_colors);
    float weft_band = floor(fract(uv_y / sett_size) * num_colors);
    vec3 warp_color = palette[warp_band];
    vec3 weft_color = palette[weft_band];
    // Intersection = blend of warp + weft colors
    vec3 intersection = mix(warp_color, weft_color, 0.5);
    float is_intersection = step(0.0, warp_band - weft_band) * step(0.0, weft_band - warp_band);
    return mix(intersection, warp_color, is_intersection);
}
```

## Prompt Templates

### Close-up Woven Texture
> "Extreme macro of a [WEAVE TYPE] in [FIBER], showing individual warp and weft threads interlacing with [TEXTURE DETAIL], raking light revealing float shadows, thread-level detail, museum specimen"

### Tartan / Plaid
> "A traditional [REGION] tartan with [COLOR COUNT] colors — [COLOR LIST] — in a [SETT SIZE] sett repeat, woven in [FIBER], photographed flat with even light showing thread intersections"

### Damask / Brocade
> "Reversible [damask/brocade] weave in [COLOR] silk with [MOTIF] pattern, one side matte and one side shiny, supplementary [weft/warp] floats creating raised pattern, baroque textile detail"

### Ikat
> "Handwoven ikat fabric with blurred resist-dyed edges in [COLOR PALETTE], showing the characteristic feathered boundary where pre-dyed threads intersect, traditional [REGION] style"

## Anti-Drift: Weaving-Specific

- **Never call a printed check "woven plaid"** — woven plaids have thread-color intersections; printed checks sit on the surface
- **Never mix twill direction** unless specifying herringbone/chevron reversal
- **Satin is not sateen** — satin = warp floats dominant; sateen = weft floats dominant
- **Jacquard is not a weave structure** — it's a control system; the weave can be plain, twill, or satin underneath
- **Damask is reversible** — if it's not reversible, it's brocade or a figured plain weave, not damask

---

*This repo treats the loom as a binary computer. Every pattern is a program. Every thread is a bit.*
