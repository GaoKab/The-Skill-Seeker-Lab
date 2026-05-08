import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { ArrowRight, CheckCircle2 } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-[#ffedd5] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[12%] w-14 h-14 rounded-full bg-[#fb923c]/20" />
      <div className="absolute bottom-14 left-[7%] w-10 h-10 rounded-xl bg-[#a78bfa]/15 -rotate-12" />
      <div className="absolute top-28 left-[20%] text-3xl text-[#fdba74]/40 font-black rotate-12 select-none">✦</div>
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="inline-block bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full -rotate-1 shadow-sm mb-6">🏫 For schools</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Bring Find Your Voice <span className="marker-coral">into your school</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          We partner with schools across Botswana to deliver structured communication training — integrated into your calendar, aligned with your goals, and designed for measurable student outcomes.
        </motion.p>
      </div>
    </section>
  )
}

function WhyPartner() {
  const reasons = [
    { emoji: "📊", title: "Measurable improvement", desc: "Schools that partner with us see measurable improvements in student participation, presentation quality, and classroom engagement within one term.", bg: "bg-[#dbeafe]", tilt: "rotate-1" },
    { emoji: "📅", title: "Fits your calendar", desc: "Programs integrate with your existing schedule — during assemblies, after school, or dedicated time slots. We work around you.", bg: "bg-[#dcfce7]", tilt: "-rotate-1" },
    { emoji: "👩‍🏫", title: "Trained facilitators", desc: "Our facilitators are trained specifically for youth communication development. We handle everything — curriculum, materials, assessment, and reporting.", bg: "bg-[#fef3c7]", tilt: "rotate-2" },
    { emoji: "⭐", title: "Differentiate your school", desc: "Communication training is a tangible value-add that parents notice. Schools that offer structured speaking programs stand out.", bg: "bg-[#ede9fe]", tilt: "-rotate-2" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4 text-center">Why partner</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>
            Because the curriculum <span className="marker-coral">doesn't teach this</span>. 📚
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">
            Schools teach subjects. We teach the skill that makes every subject more accessible — the ability to think clearly and communicate effectively.
          </p>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {reasons.map((r, i) => (
            <FadeIn key={r.title} delay={i * 0.1}>
              <motion.div
                className={`${r.bg} p-8 rounded-3xl ${r.tilt} border-[3px] border-dashed border-gray-200/60`}
                whileHover={{ rotate: 0, scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-4xl block mb-3">{r.emoji}</span>
                <h3 className="font-black text-xl text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{r.title}</h3>
                <p className="text-gray-600 leading-relaxed">{r.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function Formats() {
  const formats = [
    { emoji: "🕐", title: "After-School Program", desc: "A weekly after-school club that runs for a full term. Students meet once or twice a week for structured speaking sessions. Our most popular format.", best: "Best for: Schools wanting a regular, low-disruption program", bg: "bg-[#dcfce7]", border: "border-[#86efac]" },
    { emoji: "📖", title: "Curriculum Integration", desc: "Communication training embedded into existing class time — English, Life Skills, or dedicated periods. We provide lesson plans, materials, and facilitator support.", best: "Best for: Schools wanting skills across the student body", bg: "bg-[#fef3c7]", border: "border-[#fde68a]" },
    { emoji: "⚡", title: "Workshop Series", desc: "Intensive multi-day workshops during specific school events — career weeks, leadership days, or term openings. Focused, high-impact sessions.", best: "Best for: Schools wanting to start with a pilot first", bg: "bg-[#ede9fe]", border: "border-[#c4b5fd]" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#059669] uppercase tracking-widest mb-4 text-center">Partnership formats</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Flexible options for <span className="marker-green">every school</span>.
          </h2>
        </FadeIn>
        <div className="space-y-6">
          {formats.map((f, i) => (
            <FadeIn key={f.title} delay={i * 0.12}>
              <motion.div
                className={`${f.bg} border-2 ${f.border} rounded-3xl p-8 flex flex-col md:flex-row items-start gap-6`}
                whileHover={{ scale: 1.01, x: 4 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-5xl shrink-0">{f.emoji}</span>
                <div>
                  <h3 className="font-black text-xl text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{f.title}</h3>
                  <p className="text-gray-600 leading-relaxed mb-3">{f.desc}</p>
                  <p className="text-sm font-bold text-gray-400">{f.best}</p>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
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
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#0ea5e9] uppercase tracking-widest mb-4 text-center">What's included</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Everything you need. <span className="marker-blue">Nothing you don't</span>.
          </h2>
        </FadeIn>
        <div className="space-y-3">
          {items.map((item, i) => (
            <FadeIn key={item} delay={i * 0.08}>
              <div className="flex items-center gap-4 bg-white p-5 rounded-2xl border-2 border-dashed border-gray-200/60 shadow-sm">
                <CheckCircle2 size={20} className="text-[#34d399] shrink-0" />
                <p className="text-gray-700 font-medium">{item}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function CTA() {
  return (
    <section className="py-20 px-6 bg-[#ffedd5] relative overflow-hidden">
      <div className="absolute top-10 right-[12%] w-12 h-12 rounded-full bg-[#fb923c]/15" />
      <div className="absolute bottom-10 left-[10%] w-10 h-10 rounded-xl bg-[#34d399]/15 rotate-12" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <span className="text-5xl block mb-6">🤝</span>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            Let's discuss what this <span className="marker-coral">looks like</span> for your school.
          </h2>
          <p className="mt-5 text-lg text-gray-600">Every partnership starts with a conversation. Tell us about your school, your students, and your goals — we'll design a program that fits.</p>
          <Link to="/contact">
            <motion.button className="mt-8 bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, rotate: 1 }} whileTap={{ scale: 0.95 }}>
              Start a Conversation <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
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
