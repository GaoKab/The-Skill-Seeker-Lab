# Motion (Framer Motion) React animation library. Use for drag-and-drop, scroll animations, gestures, SVG morphing, or encountering bundle size, complex transitions, spring physics errors.

license: MIT

# Motion Animation Library

## Overview

Motion (package: `motion`, formerly `framer-motion`) is the industry-standard React animation library used in production by thousands of applications. With 30,200+ GitHub stars and 300+ official examples, it provides a declarative API for creating sophisticated animations with minimal code.

**Key Capabilities:**
- **Gestures**: drag, hover, tap, pan, focus with cross-device support
- **Scroll Animations**: viewport-triggered, scroll-linked, parallax effects
- **Layout Animations**: FLIP technique for smooth layout changes, shared element transitions
- **Spring Physics**: Natural, customizable motion with physics-based easing
- **SVG**: Path morphing, line drawing, attribute animation
- **Exit Animations**: AnimatePresence for unmounting transitions
- **Performance**: Hardware-accelerated, ScrollTimeline API, bundle optimization (2.3 KB - 34 KB)

**Production Tested**: React 19, Next.js 15, Vite 6, Tailwind v4

---

## When to Use This Skill

### ✅ Use Motion When:

**Complex Interactions**:
- Drag-and-drop interfaces (sortable lists, kanban boards, sliders)
- Hover states with scale/rotation/color changes
- Tap feedback with bounce/squeeze effects
- Pan gestures for mobile-friendly controls

**Scroll-Based Animations**:
- Hero sections with parallax layers
- Scroll-triggered reveals (fade in as elements enter viewport)
- Progress bars linked to scroll position
- Sticky headers with scroll-dependent transforms

**Layout Transitions**:
- Shared element transitions between routes (card → detail page)
- Expand/collapse with automatic height animation
- Grid/list view switching with smooth repositioning
- Tab navigation with animated underline

**Advanced Features**:
- SVG line drawing animations
- Path morphing between shapes
- Spring physics for natural bounce
- Orchestrated sequences (staggered reveals)
- Modal dialogs with backdrop blur

**Bundle Optimization**:
- Need 2.3 KB animation library (useAnimate mini)
- Want to reduce Motion from 34 KB to 4.6 KB (LazyMotion)

### ❌ Don't Use Motion When:

- **Simple list animations** (use `auto-animate` instead: 3.28 KB vs 34 KB)
- **Static content** without interactions
- **Cloudflare Workers** (use `framer-motion` v12.23.24 workaround - see Known Issues)
- **3D animations** (use Three.js or React Three Fiber instead)

---

## Installation

### Latest Stable Version

```bash
bun add motion  # preferred
# or: npm install motion
# or: yarn add motion
```

**Current Version**: 12.23.24 (verified 2025-11-07)

**Alternative for Cloudflare Workers**:
```bash
# Use framer-motion if deploying to Cloudflare Workers
bun add framer-motion
# or: npm install framer-motion
```

### Package Information

- **Bundle Size**:
  - Full `motion` component: ~34 KB minified+gzipped
  - `LazyMotion` + `m` component: ~4.6 KB
  - `useAnimate` mini: 2.3 KB (smallest React animation library)
  - `useAnimate` hybrid: 17 KB
- **Dependencies**: React 18+ or React 19+
- **TypeScript**: Native support included (no @types package needed)

---

## Core Concepts

### 1. The `motion` Component

Transform any HTML/SVG element into an animatable component:

```tsx
import { motion } from "motion/react"

// Basic animation
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5 }}
>
  Content fades in and slides up
</motion.div>

// Gesture controls
<motion.button
  whileHover={{ scale: 1.1 }}
  whileTap={{ scale: 0.95 }}
>
  Click me
</motion.button>
```

**Props:**
- `initial`: Starting state (object or variant name)
- `animate`: Target state (object or variant name)
- `exit`: Unmounting state (requires AnimatePresence)
- `transition`: Timing/easing configuration
- `whileHover`, `whileTap`, `whileFocus`: Gesture states
- `whileInView`: Viewport-triggered animation
- `drag`: Enable dragging ("x", "y", or true for both)
- `layout`: Enable FLIP layout animations

### 2. Variants (Animation Orchestration)

Named animation states that propagate through component tree:

```tsx
const variants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
}

<motion.div variants={variants} initial="hidden" animate="visible">
  Content
</motion.div>
```

### 3. AnimatePresence (Exit Animations)

Enables animations when components unmount:

```tsx
import { AnimatePresence } from "motion/react"

<AnimatePresence>
  {isVisible && (
    <motion.div
      key="modal"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      Modal content
    </motion.div>
  )}
</AnimatePresence>
```

**Critical Rules:**
- AnimatePresence **must stay mounted** (don't wrap in conditional)
- All children **must have unique `key` props**
- AnimatePresence **wraps the conditional**, not the other way around

**Common Mistake** (exit animation won't play):
```tsx
// ❌ Wrong - AnimatePresence unmounts with condition
{isVisible && (
  <AnimatePresence>
    <motion.div>Content</motion.div>
  </AnimatePresence>
)}

// ✅ Correct - AnimatePresence stays mounted
<AnimatePresence>
  {isVisible && <motion.div key="unique">Content</motion.div>}
</AnimatePresence>
```

### 4. Layout Animations (FLIP)

Automatically animate layout changes:

```tsx
<motion.div layout>
  {isExpanded ? <FullContent /> : <Summary />}
</motion.div>
```

### 5. Scroll Animations

```tsx
// Viewport-triggered
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
>
  Fades in when entering viewport
</motion.div>

// Scroll-linked (parallax)
import { useScroll, useTransform } from "motion/react"
const { scrollYProgress } = useScroll()
const y = useTransform(scrollYProgress, [0, 1], [0, -300])
<motion.div style={{ y }}>Parallax effect</motion.div>
```

### 6. Gestures

```tsx
<motion.div drag="x" dragConstraints={{ left: -200, right: 200 }}>
  Drag me
</motion.div>
```

### 7. Spring Physics

```tsx
<motion.div
  animate={{ x: 100 }}
  transition={{ type: "spring", stiffness: 100, damping: 10 }}
/>
```

**Common presets**: Bouncy `{ stiffness: 300, damping: 10 }`, Smooth `{ stiffness: 100, damping: 20 }`.

---

## Integration Guides

**Vite**: `bun add motion` → `import { motion } from "motion/react"` (works out of the box)

**Next.js App Router**: Requires `"use client"` directive or client component wrapper
```tsx
"use client"
import { motion } from "motion/react"
```

**Tailwind**: ⚠️ Remove `transition-*` classes (causes conflicts with Motion animations)

**Cloudflare Workers**: Use `framer-motion` v12.23.24 instead (Motion has Wrangler build issues)

---

## Performance Optimization

**Bundle Size**: Use LazyMotion (34 KB → 4.6 KB):
```tsx
import { LazyMotion, domAnimation, m } from "motion/react"
<LazyMotion features={domAnimation}>
  <m.div>Only 4.6 KB!</m.div>
</LazyMotion>
```

**Large Lists**: Use virtualization (`react-window`, `react-virtuoso`) for 50+ animated items.

---

## Accessibility

**Respect `prefers-reduced-motion`**:
```tsx
import { MotionConfig } from "motion/react"
<MotionConfig reducedMotion="user">
  <App />
</MotionConfig>
```

**Keyboard Support**: Use `whileFocus` for keyboard-triggered animations.

---

## Common Patterns

**Modal Dialog** (AnimatePresence + backdrop):
```tsx
<AnimatePresence>
  {isOpen && (
    <motion.dialog exit={{ opacity: 0 }}>Content</motion.dialog>
  )}
</AnimatePresence>
```

**Accordion** (height animation):
```tsx
<motion.div animate={{ height: isOpen ? "auto" : 0 }}>
  Content
</motion.div>
```

---

## Known Issues & Solutions

### Issue 1: AnimatePresence Exit Not Working (MOST COMMON)

**Solution**: AnimatePresence must stay mounted, wrap the conditional:
```tsx
// ✅ Correct
<AnimatePresence>
  {isVisible && <motion.div key="unique">Content</motion.div>}
</AnimatePresence>
```

### Issue 2: Next.js "use client" Missing
**Solution**: Add `"use client"` directive.

### Issue 3: Tailwind Transitions Conflict
**Solution**: Remove `transition-*` classes.

### Issue 4: Cloudflare Workers Build Errors
**Solution**: Use `framer-motion` v12.23.24 instead.

### Issue 5: Large List Performance
**Solution**: Use virtualization (`react-window`, `react-virtuoso`).

---

## Official Documentation

- **Official Site**: https://motion.dev
- **GitHub**: https://github.com/motiondivision/motion (30,200+ stars)
- **Examples**: https://motion.dev/examples (300+ examples)

---

## Package Versions (Verified 2025-11-07)

| Package | Version | Status |
|---------|---------|--------|
| motion | 12.23.24 | ✅ Latest stable |
| framer-motion | 12.23.24 | ✅ Alternative for Cloudflare |
| react | 19.2.0 | ✅ Latest stable |
| vite | 6.0.0 | ✅ Latest stable |

---

**Production Tested**: ✅ React 19 + Next.js 15 + Vite 6 + Tailwind v4
**Bundle Size**: 2.3 KB (mini) - 34 KB (full), optimizable to 4.6 KB with LazyMotion
**Accessibility**: MotionConfig reducedMotion support
