import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight, CheckCircle2 } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] pt-32 pb-24 px-6 overflow-hidden">
      <div className="absolute top-16 right-[10%] w-36 h-36 bg-white/10 rounded-[2rem] -rotate-6" />
      <div className="max-w-7xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-2xl">🏫</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-white mt-4 max-w-3xl leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Bring Find Your Voice into your school.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-white/90 max-w-2xl leading-relaxed"
        >
          We partner with schools across Botswana to deliver structured communication training — integrated into your calendar, aligned with your goals, and designed for measurable student outcomes.
        </motion.p>
      </div>
      <div className="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,30 C360,60 720,0 1440,30 L1440,60 L0,60 Z" fill="#fffbf5" /></svg></div>
    </section>
  )
}

function WhyPartner() {
  const reasons = [
    { emoji: "📊", title: "Measurable improvement", desc: "Schools that partner with us see measurable improvements in student participation, presentation quality, and classroom engagement within one term." },
    { emoji: "📅", title: "Fits your calendar", desc: "Programs integrate with your existing schedule — during assemblies, after school, or dedicated time slots. We work around you." },
    { emoji: "👩‍🏫", title: "Trained facilitators", desc: "Our facilitators are trained specifically for youth communication development. We handle everything — curriculum, materials, assessment, and reporting." },
    { emoji: "⭐", title: "Differentiate your school", desc: "Communication training is a tangible value-add that parents notice. Schools that offer structured speaking programs stand out." },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="Why partner" title="Because the curriculum doesn't teach this. 📚" subtitle="Schools teach subjects. We teach the skill that makes every subject more accessible — the ability to think clearly and communicate effectively." />
      <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {reasons.map((r, i) => (
          <FadeIn key={r.title} delay={i * 0.1}>
            <motion.div className="flex items-start gap-5 bg-white p-7 rounded-3xl border border-gray-100 shadow-sm" whileHover={{ y: -3 }}>
              <span className="text-3xl">{r.emoji}</span>
              <div>
                <h3 className="font-black text-lg text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{r.title}</h3>
                <p className="text-gray-500 leading-relaxed">{r.desc}</p>
              </div>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Formats() {
  const formats = [
    { emoji: "🕐", title: "After-School Program", desc: "A weekly after-school club that runs for a full term. Students meet once or twice a week for structured speaking sessions. Our most popular format.", best: "Best for: Schools wanting a regular, low-disruption program", color: "bg-[#d1fae5]", border: "border-[#34d399]" },
    { emoji: "📖", title: "Curriculum Integration", desc: "Communication training embedded into existing class time — English, Life Skills, or dedicated periods. We provide lesson plans, materials, and facilitator support.", best: "Best for: Schools wanting skills across the student body", color: "bg-[#fef3c7]", border: "border-[#fbbf24]" },
    { emoji: "⚡", title: "Workshop Series", desc: "Intensive multi-day workshops during specific school events — career weeks, leadership days, or term openings. Focused, high-impact sessions.", best: "Best for: Schools wanting to start with a pilot first", color: "bg-[#ede9fe]", border: "border-[#a78bfa]" },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader label="Partnership formats" title="Flexible options for every school." subtitle="We don't believe in one-size-fits-all. Here are three ways to bring Find Your Voice into your school." />
      <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        {formats.map((f, i) => (
          <FadeIn key={f.title} delay={i * 0.12}>
            <motion.div className={`${f.color} rounded-3xl border-2 ${f.border} p-8 h-full flex flex-col`} whileHover={{ y: -4 }}>
              <span className="text-4xl mb-4">{f.emoji}</span>
              <h3 className="font-black text-xl text-gray-900 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>{f.title}</h3>
              <p className="text-gray-600 leading-relaxed flex-1">{f.desc}</p>
              <p className="text-sm font-bold text-gray-500 mt-4">{f.best}</p>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function WhatYouGet() {
  const items = [
    "Customized program design for your school's needs and schedule",
    "All training materials, exercises, and assessment frameworks",
    "Trained facilitators who specialize in youth communication",
    "Term-end reports showing individual and group progress",
    "Student showcase event for parents and school leadership",
    "Ongoing support and curriculum refinement each term",
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="What's included" title="Everything you need. Nothing you don't." subtitle="We handle the program end to end. Your role is to give us the students and the time." />
      <div className="max-w-2xl mx-auto space-y-4">
        {items.map((item, i) => (
          <FadeIn key={item} delay={i * 0.08}>
            <div className="flex items-start gap-3 bg-white p-5 rounded-2xl border border-gray-100 shadow-sm">
              <CheckCircle2 size={20} className="text-[#34d399] shrink-0 mt-0.5" />
              <p className="text-gray-700 font-medium">{item}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function CTA() {
  return (
    <section className="relative overflow-hidden">
      <div className="bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] py-20 md:py-28 px-6">
        <div className="absolute top-0 left-0 right-0"><svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,0 L1440,0 L1440,30 C1080,60 360,0 0,30 Z" fill="#fffbf5" /></svg></div>
        <div className="text-center max-w-3xl mx-auto relative z-10">
          <FadeIn>
            <span className="text-5xl block mb-4">🤝</span>
            <h2 className="text-3xl md:text-4xl font-black text-white" style={{ fontFamily: "Nunito, sans-serif" }}>Let's discuss what this looks like for your school.</h2>
            <p className="mt-5 text-lg text-white/90">Every partnership starts with a conversation. Tell us about your school, your students, and your goals — we'll design a program that fits.</p>
            <Link to="/contact">
              <motion.button className="mt-8 bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-amber-300/30 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, y: -2 }} whileTap={{ scale: 0.95 }}>
                Start a Conversation ✨ <ArrowRight size={20} />
              </motion.button>
            </Link>
          </FadeIn>
        </div>
      </div>
    </section>
  )
}

export default function ForSchools() {
  return (
    <>
      <PageHero />
      <WhyPartner />
      <Formats />
      <WhatYouGet />
      <CTA />
    </>
  )
}
