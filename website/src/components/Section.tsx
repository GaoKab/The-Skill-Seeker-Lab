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
      initial={{ opacity: 0, y: 28 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.55, delay, ease: [0.22, 1, 0.36, 1] }}
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
    <FadeIn className="text-center max-w-3xl mx-auto mb-14">
      {label && (
        <span className="inline-block bg-[#e0f2fe] text-[#0284c7] font-black text-xs tracking-widest uppercase px-4 py-1.5 rounded-full mb-4">
          {label}
        </span>
      )}
      <h2
        className={`text-3xl md:text-4xl lg:text-5xl font-black leading-tight ${
          light ? "text-white" : "text-gray-900"
        }`}
        style={{ fontFamily: "Nunito, sans-serif" }}
      >
        {title}
      </h2>
      {subtitle && (
        <p
          className={`mt-5 text-lg leading-relaxed ${
            light ? "text-sky-100" : "text-gray-500"
          }`}
        >
          {subtitle}
        </p>
      )}
    </FadeIn>
  )
}
