import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { ArrowRight, CheckCircle2 } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-[#dcfce7] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-24 right-[12%] w-12 h-12 rounded-full bg-[#34d399]/20" />
      <div className="absolute bottom-12 left-[8%] w-16 h-16 rounded-xl bg-[#fbbf24]/15 rotate-6" />
      <div className="absolute top-32 left-[20%] text-3xl text-[#86efac]/40 font-black -rotate-12 select-none">✦</div>
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="inline-block bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full rotate-1 shadow-sm mb-6">🎓 Our programs</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          Structured programs that build <span className="marker-green">real skills</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          Every program is designed around one principle: children learn communication by communicating. Not by watching, not by reading — by doing.
        </motion.p>
      </div>
    </section>
  )
}

function CorePrograms() {
  const programs = [
    {
      emoji: "🌱", age: "Ages 6–10", name: "Young Speakers", tagline: "Where confidence begins",
      description: "Designed for children just starting to find their voice. Through storytelling, show-and-tell, role play, and guided group activities, young speakers learn to organize their thoughts and share them with a supportive audience.",
      includes: ["Weekly 60-minute group sessions", "Storytelling and show-and-tell exercises", "Basic speech structure training", "End-of-phase showcase for parents", "Progress reports after each phase"],
      duration: "6-month program", format: "Weekly sessions",
      bg: "bg-[#dcfce7]", border: "border-[#86efac]", accent: "text-[#059669]",
    },
    {
      emoji: "🔥", age: "Ages 11–14", name: "Rising Voices", tagline: "Building thinkers who speak",
      description: "The bridge between childhood communication and real-world expression. Students tackle debates, persuasive speaking, group discussions, and impromptu challenges. They learn to defend ideas under pressure.",
      includes: ["Weekly 90-minute group sessions", "Structured debate and discussion formats", "Persuasive speaking and argumentation", "Critical thinking exercises", "Feedback from peers and facilitators", "Mid-program and final assessments"],
      duration: "6-month program", format: "Weekly sessions",
      bg: "bg-[#fef3c7]", border: "border-[#fde68a]", accent: "text-[#d97706]",
    },
    {
      emoji: "👑", age: "Ages 15–18", name: "Future Leaders", tagline: "Preparing the next generation to lead",
      description: "Advanced communication training for teens ready to operate at a higher level. Covers presentations, panel discussions, interview preparation, and public-facing speaking opportunities.",
      includes: ["Weekly 90-minute sessions", "Presentation design and delivery", "Panel discussion and interview practice", "Leadership communication frameworks", "Real speaking opportunities (events, schools)", "Personal speaking portfolio", "Certificate of completion"],
      duration: "6-month program", format: "Weekly sessions",
      bg: "bg-[#ede9fe]", border: "border-[#c4b5fd]", accent: "text-[#7c3aed]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#059669] uppercase tracking-widest mb-4 text-center">Core programs</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Three tracks. Every age <span className="marker-green">covered</span>. 🎯
          </h2>
        </FadeIn>

        <div className="space-y-10">
          {programs.map((p, i) => (
            <FadeIn key={p.name} delay={i * 0.12}>
              <div className={`${p.bg} border-2 ${p.border} rounded-3xl overflow-hidden`}>
                <div className="p-8 md:p-10">
                  <div className="flex items-start gap-5 mb-6">
                    <span className="text-5xl">{p.emoji}</span>
                    <div>
                      <span className={`text-xs font-black uppercase tracking-widest ${p.accent}`}>{p.age}</span>
                      <h3 className="text-2xl font-black text-gray-900 mt-0.5" style={{ fontFamily: "Nunito, sans-serif" }}>{p.name}</h3>
                      <p className={`${p.accent} font-bold text-sm`}>{p.tagline}</p>
                    </div>
                  </div>
                  <p className="text-gray-600 leading-relaxed mb-6">{p.description}</p>
                  <div className="flex gap-6 mb-6 text-sm text-gray-400 font-bold">
                    <span>⏱️ {p.duration}</span>
                    <span>📅 {p.format}</span>
                  </div>
                  <div className="bg-white/60 rounded-2xl p-5">
                    <h4 className="font-black text-gray-900 text-sm mb-3" style={{ fontFamily: "Nunito, sans-serif" }}>What's included:</h4>
                    <ul className="space-y-2">
                      {p.includes.map((item) => (
                        <li key={item} className="flex items-start gap-2 text-sm">
                          <CheckCircle2 size={16} className="text-[#34d399] shrink-0 mt-0.5" />
                          <span className="text-gray-600">{item}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function ProgramStructure() {
  const phases = [
    { emoji: "🧱", phase: "Phase 1 — Foundation", months: "Months 1–2", desc: "Core skills. Build the basics — voice control, eye contact, basic speech structure, and the habit of speaking regularly.", bg: "bg-[#dbeafe]" },
    { emoji: "🚀", phase: "Phase 2 — Development", months: "Months 3–4", desc: "Depth and complexity. Move into persuasion, debate, impromptu speaking, and group leadership. Start handling pressure.", bg: "bg-[#fef3c7]" },
    { emoji: "🏆", phase: "Phase 3 — Mastery", months: "Months 5–6", desc: "Performance and portfolio. Deliver polished speeches, participate in showcases, and build real speaking experience.", bg: "bg-[#dcfce7]" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7c3aed] uppercase tracking-widest mb-4 text-center">The structure</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            6 months. 3 phases. <span className="marker-purple">Real transformation</span>.
          </h2>
        </FadeIn>
        <div className="space-y-5">
          {phases.map((p, i) => (
            <FadeIn key={p.phase} delay={i * 0.12}>
              <div className={`flex gap-5 items-start ${p.bg} p-6 rounded-2xl border-[3px] border-dashed border-gray-200/60`}>
                <motion.div
                  className="w-14 h-14 rounded-2xl bg-white flex items-center justify-center shrink-0 text-3xl shadow-sm"
                  whileHover={{ rotate: [0, -8, 8, 0] }}
                >
                  {p.emoji}
                </motion.div>
                <div>
                  <h3 className="font-black text-lg text-gray-900" style={{ fontFamily: "Nunito, sans-serif" }}>{p.phase}</h3>
                  <span className="text-sm text-[#7c3aed] font-bold">{p.months}</span>
                  <p className="text-gray-600 leading-relaxed mt-2">{p.desc}</p>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function AdditionalOfferings() {
  const offerings = [
    { emoji: "🏫", title: "School Partnerships", desc: "We bring Find Your Voice directly into schools. Customized programs integrated into your school calendar.", cta: "Learn about school partnerships", link: "/for-schools", bg: "bg-[#dbeafe]", tilt: "rotate-1" },
    { emoji: "🎯", title: "One-on-One Coaching", desc: "Premium, personalized coaching for children who need individual attention or are preparing for a specific event.", cta: "Inquire about coaching", link: "/contact", bg: "bg-[#fef3c7]", tilt: "-rotate-1" },
    { emoji: "💻", title: "Online Sessions", desc: "Can't make it to Gaborone? Our online sessions bring the same structured training to your screen.", cta: "Ask about online availability", link: "/contact", bg: "bg-[#ede9fe]", tilt: "rotate-1" },
  ]

  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#d97706] uppercase tracking-widest mb-4 text-center">More options</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            Beyond the <span className="marker-coral">classroom</span>.
          </h2>
        </FadeIn>
        <div className="space-y-6">
          {offerings.map((o, i) => (
            <FadeIn key={o.title} delay={i * 0.12}>
              <motion.div
                className={`${o.bg} rounded-3xl ${o.tilt} border-[3px] border-dashed border-gray-200/60 p-8 flex flex-col md:flex-row items-start gap-6`}
                whileHover={{ rotate: 0, scale: 1.01 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-5xl shrink-0">{o.emoji}</span>
                <div>
                  <h3 className="font-black text-xl text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{o.title}</h3>
                  <p className="text-gray-600 leading-relaxed mb-4">{o.desc}</p>
                  <Link to={o.link} className="inline-flex items-center gap-2 text-[#f97316] font-bold hover:underline text-sm">{o.cta} <ArrowRight size={16} /></Link>
                </div>
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
    <section className="py-20 px-6 bg-[#dcfce7] relative overflow-hidden">
      <div className="absolute top-8 right-[15%] w-10 h-10 rounded-full bg-[#34d399]/20" />
      <div className="absolute bottom-12 left-[10%] w-14 h-14 rounded-xl bg-[#fbbf24]/15 -rotate-12" />
      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          <span className="text-5xl block mb-6">✨</span>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            Ready to give your child the skills <span className="marker-green">school doesn't teach</span>?
          </h2>
          <p className="mt-5 text-lg text-gray-600">Enrollment is open. Spots are limited to keep groups small and personal.</p>
          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button className="bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, rotate: 1 }} whileTap={{ scale: 0.95 }}>
                Enroll Now <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/contact">
              <motion.button className="bg-white hover:bg-gray-50 text-gray-800 font-bold px-8 py-4 rounded-full text-lg border-2 border-gray-200 transition-colors" style={{ fontFamily: "Nunito, sans-serif" }} whileHover={{ scale: 1.05, rotate: -1 }} whileTap={{ scale: 0.95 }}>
                Ask a Question First
              </motion.button>
            </Link>
          </div>
        </FadeIn>
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
