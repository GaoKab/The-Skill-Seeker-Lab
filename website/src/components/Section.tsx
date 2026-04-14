import { motion } from "motion/react"
import type { ReactNode } from "react"

interface SectionProps {
  children: ReactNode
  className?: string
  id?: string
}

export function Section({ children, className = "", id }: SectionProps) {
  return (
    <section id={id} className={`py-20 md:py-28 px-6 ${className}`}>
      <div className="max-w-7xl mx-auto">{children}</div>
    </section>
  )
}

export function FadeIn({
  children,
  className = "",
  delay = 0,
}: {
  children: ReactNode
  className?: string
  delay?: number
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-60px" }}
      transition={{ duration: 0.6, delay }}
      className={className}
    >
      {children}
    </motion.div>
  )
}

export function SectionHeader({
  label,
  title,
  subtitle,
  light = false,
}: {
  label?: string
  title: string
  subtitle?: string
  light?: boolean
}) {
  return (
    <FadeIn className="text-center max-w-3xl mx-auto mb-16">
      {label && (
        <span className="inline-block text-teal-600 font-semibold text-sm tracking-wide uppercase mb-3">
          {label}
        </span>
      )}
      <h2
        className={`text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight ${
          light ? "text-white" : "text-slate-900"
        }`}
      >
        {title}
      </h2>
      {subtitle && (
        <p
          className={`mt-5 text-lg leading-relaxed ${
            light ? "text-slate-300" : "text-slate-600"
          }`}
        >
          {subtitle}
        </p>
      )}
    </FadeIn>
  )
}
