import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  School, BarChart3, CalendarDays, GraduationCap, Star,
  Clock, BookOpen, Zap, CheckCircle2, Handshake, ArrowRight,
} from "lucide-react"

const bounce = { type: "spring" as const, stiffness: 300, damping: 15 }

function ClayIcon({ icon: Icon, bg, border, color, size = "w-14 h-14" }: { icon: React.ElementType; bg: string; border: string; color: string; size?: string }) {
  return (
    <motion.div
      className={`${size} rounded-2xl ${bg} border-2 ${border} flex items-center justify-center clay-sm shrink-0`}
      whileHover={{ scale: 1.1, rotate: [-2, 2, 0] }}
      transition={bounce}
    >
      <Icon className={`w-6 h-6 ${color}`} />
    </motion.div>
  )
}

function PageHero() {
  return (
    <section className="relative bg-[#FED7AA] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[12%] w-16 h-16 rounded-3xl bg-[#BFDBFE] border-2 border-[#93C5FD] clay rotate-6 opacity-50" />
      <div className="absolute bottom-14 left-[7%] w-12 h-12 rounded-2xl bg-[#DDD6FE] border-2 border-[#C4B5FD] clay -rotate-12 opacity-50" />
      <div className="absolute top-40 left-[20%] w-10 h-10 rounded-xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay rotate-12 opacity-40" />
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
          <span className="inline-flex items-center gap-2 bg-white border-2 border-[#FDBA74] rounded-2xl px-4 py-2 clay-sm mb-6">
            <School className="w-4 h-4 text-[#F97316]" />
            <span className="text-gray-800 font-bold text-sm">For schools</span>
          </span>
        </motion.div>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-gray-900 leading-tight"
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
    {
      icon: BarChart3,
      title: "Measurable improvement",
      desc: "Schools that partner with us see measurable improvements in student participation, presentation quality, and classroom engagement within one term.",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
      iconBg: "bg-[#BFDBFE]",
      iconBorder: "border-[#93C5FD]",
      iconColor: "text-[#2563EB]",
    },
    {
      icon: CalendarDays,
      title: "Fits your calendar",
      desc: "Programs integrate with your existing schedule — during assemblies, after school, or dedicated time slots. We work around you.",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
      iconBg: "bg-[#BBF7D0]",
      iconBorder: "border-[#86EFAC]",
      iconColor: "text-[#16A34A]",
    },
    {
      icon: GraduationCap,
      title: "Trained facilitators",
      desc: "Our facilitators are trained specifically for youth communication development. We handle everything — curriculum, materials, assessment, and reporting.",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
      iconBg: "bg-[#FDE68A]",
      iconBorder: "border-[#FCD34D]",
      iconColor: "text-[#D97706]",
    },
    {
      icon: Star,
      title: "Differentiate your school",
      desc: "Communication training is a tangible value-add that parents notice. Schools that offer structured speaking programs stand out.",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
      iconBg: "bg-[#DDD6FE]",
      iconBorder: "border-[#C4B5FD]",
      iconColor: "text-[#7C3AED]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-bold text-[#D97706] uppercase tracking-widest mb-4 text-center">Why partner</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-4">
            Because the curriculum <span className="marker-coral">doesn't teach this</span>.
          </h2>
          <p className="text-gray-500 text-center text-lg max-w-2xl mx-auto mb-14">
            Schools teach subjects. We teach the skill that makes every subject more accessible — the ability to think clearly and communicate effectively.
          </p>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {reasons.map((r, i) => (
            <FadeIn key={r.title} delay={i * 0.1}>
              <motion.div
                className={`${r.bg} p-8 rounded-3xl border-3 ${r.border} clay`}
                whileHover={{ scale: 1.02, y: -4 }}
                transition={bounce}
              >
                <ClayIcon icon={r.icon} bg={r.iconBg} border={r.iconBorder} color={r.iconColor} />
                <h3 className="font-bold text-xl text-gray-900 mt-4 mb-2">{r.title}</h3>
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
    {
      icon: Clock,
      title: "After-School Program",
      desc: "A weekly after-school club that runs for a full term. Students meet once or twice a week for structured speaking sessions. Our most popular format.",
      best: "Best for: Schools wanting a regular, low-disruption program",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
      iconBg: "bg-[#BBF7D0]",
      iconBorder: "border-[#86EFAC]",
      iconColor: "text-[#16A34A]",
    },
    {
      icon: BookOpen,
      title: "Curriculum Integration",
      desc: "Communication training embedded into existing class time — English, Life Skills, or dedicated periods. We provide lesson plans, materials, and facilitator support.",
      best: "Best for: Schools wanting skills across the student body",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
      iconBg: "bg-[#FDE68A]",
      iconBorder: "border-[#FCD34D]",
      iconColor: "text-[#D97706]",
    },
    {
      icon: Zap,
      title: "Workshop Series",
      desc: "Intensive multi-day workshops during specific school events — career weeks, leadership days, or term openings. Focused, high-impact sessions.",
      best: "Best for: Schools wanting to start with a pilot first",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
      iconBg: "bg-[#DDD6FE]",
      iconBorder: "border-[#C4B5FD]",
      iconColor: "text-[#7C3AED]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-bold text-[#059669] uppercase tracking-widest mb-4 text-center">Partnership formats</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-14">
            Flexible options for <span className="marker-green">every school</span>.
          </h2>
        </FadeIn>
        <div className="space-y-6">
          {formats.map((f, i) => (
            <FadeIn key={f.title} delay={i * 0.12}>
              <motion.div
                className={`${f.bg} border-3 ${f.border} rounded-3xl p-8 flex flex-col md:flex-row items-start gap-6 clay`}
                whileHover={{ scale: 1.01, x: 4 }}
                transition={bounce}
              >
                <ClayIcon icon={f.icon} bg={f.iconBg} border={f.iconBorder} color={f.iconColor} size="w-16 h-16" />
                <div>
                  <h3 className="font-bold text-xl text-gray-900 mb-2">{f.title}</h3>
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
          <p className="text-sm font-bold text-[#0EA5E9] uppercase tracking-widest mb-4 text-center">What's included</p>
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 text-center mb-14">
            Everything you need. <span className="marker-blue">Nothing you don't</span>.
          </h2>
        </FadeIn>
        <div className="space-y-4">
          {items.map((item, i) => (
            <FadeIn key={item} delay={i * 0.08}>
              <motion.div
                className="flex items-center gap-4 bg-white p-5 rounded-2xl border-2 border-[#93C5FD] clay-sm"
                whileHover={{ scale: 1.01, x: 4 }}
                transition={bounce}
              >
                <div className="w-10 h-10 rounded-xl bg-[#BBF7D0] border-2 border-[#86EFAC] flex items-center justify-center clay-sm shrink-0">
                  <CheckCircle2 className="w-5 h-5 text-[#16A34A]" />
                </div>
                <p className="text-gray-700 font-medium">{item}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function CTA() {
  return (
    <section className="py-20 px-6 bg-[#FED7AA] relative overflow-hidden">
      <div className="absolute top-8 right-[10%] w-16 h-16 rounded-2xl bg-[#BFDBFE] border-2 border-[#93C5FD] clay rotate-12 opacity-40" />
      <div className="absolute bottom-12 left-[8%] w-12 h-12 rounded-2xl bg-[#BBF7D0] border-2 border-[#86EFAC] clay -rotate-6 opacity-40" />
      <div className="absolute top-[50%] left-[4%] w-10 h-10 rounded-xl bg-[#DDD6FE] border-2 border-[#C4B5FD] clay rotate-6 opacity-30" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <ClayIcon icon={Handshake} bg="bg-[#FDE68A]" border="border-[#FCD34D]" color="text-[#D97706]" size="w-16 h-16" />
          <h2 className="text-3xl md:text-5xl font-bold text-gray-900 leading-tight mt-6">
            Let's discuss what this <span className="marker-coral">looks like</span> for your school.
          </h2>
          <p className="mt-5 text-lg text-gray-600">
            Every partnership starts with a conversation. Tell us about your school, your students, and your goals — we'll design a program that fits.
          </p>
          <Link to="/contact">
            <motion.button
              className="mt-8 bg-[#F97316] text-white font-bold px-8 py-4 rounded-2xl text-lg inline-flex items-center gap-2 border-2 border-[#EA580C] clay-sm transition-all"
              whileHover={{ scale: 1.05, rotate: 1 }}
              whileTap={{ scale: 0.95 }}
              transition={bounce}
            >
              Start a Conversation <ArrowRight className="w-5 h-5" />
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
