import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight, CheckCircle2, Clock, CalendarDays } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-gradient-to-br from-[#0ea5e9] via-[#38bdf8] to-[#7dd3fc] pt-32 pb-24 px-6 overflow-hidden">
      <div className="absolute top-20 right-[8%] w-40 h-40 bg-white/10 rounded-[2rem] rotate-6" />
      <div className="max-w-7xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-2xl">🎓</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-white mt-4 max-w-3xl leading-tight"
          style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Structured programs that build real skills.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-white/90 max-w-2xl leading-relaxed"
        >
          Every program is designed around one principle: children learn
          communication by communicating. Not by watching, not by reading — by doing.
        </motion.p>
      </div>
      <div className="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 60" fill="none" className="w-full"><path d="M0,30 C360,60 720,0 1440,30 L1440,60 L0,60 Z" fill="#fffbf5" /></svg>
      </div>
    </section>
  )
}

interface ProgramCardProps {
  emoji: string
  age: string
  name: string
  tagline: string
  description: string
  includes: string[]
  duration: string
  format: string
  color: string
  border: string
  text: string
  index: number
}

function ProgramCard({ emoji, age, name, tagline, description, includes, duration, format, color, border, text, index }: ProgramCardProps) {
  return (
    <FadeIn delay={index * 0.12}>
      <div className={`rounded-3xl border-2 ${border} overflow-hidden h-full`}>
        <div className={`${color} px-8 pt-8 pb-6`}>
          <span className="text-4xl">{emoji}</span>
          <span className={`block text-xs font-black uppercase tracking-widest ${text} mt-3`}>{age}</span>
          <h3 className="text-2xl font-black text-gray-900 mt-1" style={{ fontFamily: "Nunito, sans-serif" }}>{name}</h3>
          <p className={`${text} font-bold mt-1`}>{tagline}</p>
        </div>
        <div className="px-8 py-8 bg-white">
          <p className="text-gray-500 leading-relaxed mb-6">{description}</p>
          <div className="flex gap-6 mb-6 text-sm">
            <div className="flex items-center gap-2 text-gray-400">
              <Clock size={15} /><span>{duration}</span>
            </div>
            <div className="flex items-center gap-2 text-gray-400">
              <CalendarDays size={15} /><span>{format}</span>
            </div>
          </div>
          <h4 className="font-black text-gray-900 text-sm mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>What's included:</h4>
          <ul className="space-y-2">
            {includes.map((item) => (
              <li key={item} className="flex items-start gap-2 text-sm">
                <CheckCircle2 size={16} className="text-[#34d399] shrink-0 mt-0.5" />
                <span className="text-gray-500">{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </FadeIn>
  )
}

function CorePrograms() {
  const programs: Omit<ProgramCardProps, "index">[] = [
    {
      emoji: "🌱", age: "Ages 6–10", name: "Young Speakers", tagline: "Where confidence begins",
      description: "Designed for children just starting to find their voice. Through storytelling, show-and-tell, role play, and guided group activities, young speakers learn to organize their thoughts and share them with a supportive audience.",
      includes: ["Weekly 60-minute group sessions", "Storytelling and show-and-tell exercises", "Basic speech structure training", "End-of-phase showcase for parents", "Progress reports after each phase"],
      duration: "6-month program", format: "Weekly sessions",
      color: "bg-[#d1fae5]", border: "border-[#34d399]", text: "text-[#059669]",
    },
    {
      emoji: "🔥", age: "Ages 11–14", name: "Rising Voices", tagline: "Building thinkers who speak",
      description: "The bridge between childhood communication and real-world expression. Students tackle debates, persuasive speaking, group discussions, and impromptu challenges. They learn to defend ideas under pressure.",
      includes: ["Weekly 90-minute group sessions", "Structured debate and discussion formats", "Persuasive speaking and argumentation", "Critical thinking exercises", "Feedback from peers and facilitators", "Mid-program and final assessments"],
      duration: "6-month program", format: "Weekly sessions",
      color: "bg-[#fef3c7]", border: "border-[#fbbf24]", text: "text-[#d97706]",
    },
    {
      emoji: "👑", age: "Ages 15–18", name: "Future Leaders", tagline: "Preparing the next generation to lead",
      description: "Advanced communication training for teens ready to operate at a higher level. Covers presentations, panel discussions, interview preparation, and public-facing speaking opportunities.",
      includes: ["Weekly 90-minute sessions", "Presentation design and delivery", "Panel discussion and interview practice", "Leadership communication frameworks", "Real speaking opportunities (events, schools)", "Personal speaking portfolio", "Certificate of completion"],
      duration: "6-month program", format: "Weekly sessions",
      color: "bg-[#ede9fe]", border: "border-[#a78bfa]", text: "text-[#7c3aed]",
    },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="Core programs" title="Three tracks. Every age covered. 🎯" subtitle="Each program runs in 6-month phases with clear milestones, so both you and your child can see the growth." />
      <div className="grid lg:grid-cols-3 gap-8">{programs.map((p, i) => <ProgramCard key={p.name} {...p} index={i} />)}</div>
    </Section>
  )
}

function ProgramStructure() {
  const phases = [
    { emoji: "🧱", phase: "Phase 1 — Foundation", months: "Months 1–2", desc: "Core skills. Build the basics — voice control, eye contact, basic speech structure, and the habit of speaking regularly." },
    { emoji: "🚀", phase: "Phase 2 — Development", months: "Months 3–4", desc: "Depth and complexity. Move into persuasion, debate, impromptu speaking, and group leadership. Start handling pressure." },
    { emoji: "🏆", phase: "Phase 3 — Mastery", months: "Months 5–6", desc: "Performance and portfolio. Deliver polished speeches, participate in showcases, and build real speaking experience." },
  ]

  return (
    <Section className="bg-white">
      <SectionHeader label="The structure" title="6 months. 3 phases. Real transformation." subtitle="Every program follows the same proven structure — progressive skill-building that compounds over time." />
      <div className="max-w-3xl mx-auto space-y-6">
        {phases.map((p, i) => (
          <FadeIn key={p.phase} delay={i * 0.12}>
            <div className="flex gap-6 items-start bg-[#fffbf5] p-6 rounded-3xl border border-gray-100">
              <div className="w-14 h-14 rounded-2xl bg-[#e0f2fe] flex items-center justify-center shrink-0 text-3xl">{p.emoji}</div>
              <div>
                <h3 className="font-black text-lg text-gray-900" style={{ fontFamily: "Nunito, sans-serif" }}>{p.phase}</h3>
                <span className="text-sm text-[#0ea5e9] font-bold">{p.months}</span>
                <p className="text-gray-500 leading-relaxed mt-2">{p.desc}</p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function AdditionalOfferings() {
  const offerings = [
    { emoji: "🏫", title: "School Partnerships", desc: "We bring Find Your Voice directly into schools. Customized programs integrated into your school calendar — assemblies, after-school clubs, or curriculum-aligned training.", cta: "Learn about school partnerships", link: "/for-schools" },
    { emoji: "🎯", title: "One-on-One Coaching", desc: "Premium, personalized coaching for children who need individual attention. Whether it's preparing for a specific event or accelerating growth — this is the intensive track.", cta: "Inquire about coaching", link: "/contact" },
    { emoji: "💻", title: "Online Sessions (Zoom)", desc: "Can't make it to Gaborone? Our online sessions bring the same structured training to your screen. Small groups, live facilitation, and real-time practice.", cta: "Ask about online availability", link: "/contact" },
  ]

  return (
    <Section className="bg-[#fffbf5]">
      <SectionHeader label="More options" title="Beyond the classroom." subtitle="Different children need different paths. We've built programs that meet families wherever they are." />
      <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        {offerings.map((o, i) => (
          <FadeIn key={o.title} delay={i * 0.12}>
            <motion.div className="bg-white rounded-3xl border border-gray-100 shadow-sm p-8 h-full flex flex-col" whileHover={{ y: -4 }}>
              <span className="text-4xl mb-4">{o.emoji}</span>
              <h3 className="font-black text-xl text-gray-900 mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>{o.title}</h3>
              <p className="text-gray-500 leading-relaxed flex-1">{o.desc}</p>
              <Link to={o.link} className="inline-flex items-center gap-2 text-[#0ea5e9] font-bold mt-6 hover:underline text-sm">{o.cta} <ArrowRight size={16} /></Link>
            </motion.div>
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
            <span className="text-5xl block mb-4">✨</span>
            <h2 className="text-3xl md:text-4xl font-black text-white" style={{ fontFamily: "Nunito, sans-serif" }}>Ready to give your child the skills that school doesn't teach?</h2>
            <p className="mt-5 text-lg text-white/90">Enrollment is open for the next cohort. Spots are limited to keep groups small and personal.</p>
            <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/contact">
                <motion.button className="bg-[#fbbf24] hover:bg-[#f59e0b] text-gray-900 font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-amber-300/30 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, y: -2 }} whileTap={{ scale: 0.95 }}>
                  Enroll Now ✨ <ArrowRight size={20} />
                </motion.button>
              </Link>
              <Link to="/contact">
                <motion.button className="bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-8 py-4 rounded-full text-lg border-2 border-white/40 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, y: -2 }} whileTap={{ scale: 0.95 }}>
                  Ask a Question First
                </motion.button>
              </Link>
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
  )
}

export default function Programs() {
  return (
    <>
      <PageHero />
      <CorePrograms />
      <ProgramStructure />
      <AdditionalOfferings />
      <CTA />
    </>
  )
}
