import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import {
  ArrowRight,
  CheckCircle2,
  School,
  BookOpen,
  Calendar,
  Users,
  Award,
  BarChart3,
} from "lucide-react"

function PageHero() {
  return (
    <section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900 pt-32 pb-20 px-6">
      <div className="max-w-7xl mx-auto">
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-teal-400 font-semibold text-sm uppercase tracking-wide"
        >
          For Schools
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-white mt-4 max-w-3xl tracking-tight"
        >
          Bring Find Your Voice into your school.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-slate-300 max-w-2xl leading-relaxed"
        >
          We partner with schools across Botswana to deliver structured
          communication training — integrated into your calendar, aligned
          with your goals, and designed for measurable student outcomes.
        </motion.p>
      </div>
    </section>
  )
}

function WhyPartner() {
  const reasons = [
    {
      icon: BarChart3,
      title: "Measurable improvement",
      desc: "Schools that partner with us see measurable improvements in student participation, presentation quality, and classroom engagement within one term.",
    },
    {
      icon: Calendar,
      title: "Fits your calendar",
      desc: "Programs are designed to integrate with your existing schedule — during assemblies, after school, or as part of dedicated time slots. We work around you.",
    },
    {
      icon: Users,
      title: "Trained facilitators",
      desc: "Our facilitators are trained specifically for youth communication development. We handle everything — curriculum, materials, assessment, and reporting.",
    },
    {
      icon: Award,
      title: "Differentiate your school",
      desc: "Communication training is a tangible value-add that parents notice. Schools that offer structured speaking programs stand out in a competitive market.",
    },
  ]

  return (
    <Section>
      <SectionHeader
        label="Why partner"
        title="Because the curriculum doesn't teach this."
        subtitle="Schools teach subjects. We teach the skill that makes every subject more accessible — the ability to think clearly and communicate effectively."
      />
      <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        {reasons.map((r, i) => (
          <FadeIn key={r.title} delay={i * 0.1}>
            <div className="flex items-start gap-5">
              <div className="w-12 h-12 rounded-xl bg-teal-100 flex items-center justify-center shrink-0">
                <r.icon size={22} className="text-teal-600" />
              </div>
              <div>
                <h3 className="font-bold text-lg text-slate-900 mb-2">
                  {r.title}
                </h3>
                <p className="text-slate-500 leading-relaxed">{r.desc}</p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Formats() {
  const formats = [
    {
      icon: School,
      title: "After-School Program",
      desc: "A weekly after-school club that runs for a full term. Students meet once or twice a week for structured speaking sessions. This is our most popular school format.",
      best: "Best for: Schools wanting a regular, low-disruption program",
    },
    {
      icon: BookOpen,
      title: "Curriculum Integration",
      desc: "Communication training embedded into existing class time — English, Life Skills, or dedicated periods. We provide lesson plans, materials, and facilitator support.",
      best: "Best for: Schools wanting communication skills across the student body",
    },
    {
      icon: Calendar,
      title: "Workshop Series",
      desc: "Intensive multi-day workshops during specific school events — career weeks, leadership days, or term openings. Focused, high-impact sessions.",
      best: "Best for: Schools wanting to start with a pilot before committing long-term",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="Partnership formats"
        title="Flexible options for every school."
        subtitle="We don't believe in one-size-fits-all. Here are three ways to bring Find Your Voice into your school."
      />
      <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {formats.map((f, i) => (
          <FadeIn key={f.title} delay={i * 0.12}>
            <motion.div
              className="bg-white rounded-2xl border border-slate-200 p-8 h-full flex flex-col"
              whileHover={{ y: -4 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <div className="w-12 h-12 rounded-xl bg-teal-100 flex items-center justify-center mb-5">
                <f.icon size={22} className="text-teal-600" />
              </div>
              <h3 className="font-bold text-xl text-slate-900 mb-3">
                {f.title}
              </h3>
              <p className="text-slate-500 leading-relaxed flex-1">
                {f.desc}
              </p>
              <p className="text-sm text-teal-600 font-medium mt-4">
                {f.best}
              </p>
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
    <Section>
      <SectionHeader
        label="What's included"
        title="Everything you need. Nothing you don't."
        subtitle="We handle the program end to end. Your role is to give us the students and the time."
      />
      <div className="max-w-2xl mx-auto space-y-4">
        {items.map((item, i) => (
          <FadeIn key={item} delay={i * 0.08}>
            <div className="flex items-start gap-3 bg-slate-50 p-5 rounded-xl">
              <CheckCircle2
                size={20}
                className="text-teal-500 shrink-0 mt-0.5"
              />
              <p className="text-slate-700">{item}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function CTA() {
  return (
    <Section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900">
      <div className="text-center max-w-3xl mx-auto">
        <FadeIn>
          <School className="text-teal-400 mx-auto mb-4" size={32} />
          <h2 className="text-3xl md:text-4xl font-bold text-white">
            Let's discuss what this looks like for your school.
          </h2>
          <p className="mt-5 text-lg text-slate-300">
            Every partnership starts with a conversation. Tell us about your
            school, your students, and your goals — we'll design a program
            that fits.
          </p>
          <Link to="/contact">
            <motion.button
              className="mt-8 bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg inline-flex items-center gap-2 transition-colors"
              whileHover={{ scale: 1.03 }}
              whileTap={{ scale: 0.97 }}
            >
              Start a Partnership Conversation
              <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
      </div>
    </Section>
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
