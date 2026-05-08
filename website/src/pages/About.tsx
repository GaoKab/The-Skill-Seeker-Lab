import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import { ArrowRight } from "lucide-react"

function PageHero() {
  return (
    <section className="relative bg-[#fef3c7] pt-32 pb-20 px-6 overflow-hidden">
      <div className="absolute top-20 right-[10%] w-14 h-14 rounded-full bg-[#fb923c]/20" />
      <div className="absolute bottom-16 left-[6%] w-10 h-10 rounded-xl bg-[#a78bfa]/20 -rotate-12" />
      <div className="absolute top-28 left-[18%] text-4xl text-[#fbbf24]/30 font-black rotate-12 select-none">✦</div>
      <div className="max-w-4xl mx-auto relative z-10">
        <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="inline-block bg-white text-gray-800 font-black text-sm px-4 py-2 rounded-full -rotate-2 shadow-sm mb-6">📖 Our story</motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}
        >
          We're building the academy <span className="marker-yellow">Botswana's children deserve</span>.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          Find Your Voice isn't a workshop or a one-day event. It's a structured communication training academy that develops confident, articulate, and thoughtful young people — one cohort at a time.
        </motion.p>
      </div>
    </section>
  )
}

function Story() {
  return (
    <section className="py-20 px-6 bg-[#fffbf5]">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <h2 className="text-3xl md:text-4xl font-black text-gray-900 mb-10" style={{ fontFamily: "Nunito, sans-serif" }}>
            The story behind <span className="marker-yellow">Find Your Voice</span> 💬
          </h2>
        </FadeIn>
        {[
          "Mpho Kabelo didn't set out to start an academy. It started with a simple observation: brilliant children in Botswana were going quiet. Not because they had nothing to say — but because no one had ever shown them how to say it.",
          "In classrooms, the same three kids would raise their hands. In family gatherings, teenagers would sit in silence while adults spoke. At school presentations, children would read from notes without ever looking up. The pattern was everywhere — and it wasn't about talent. It was about training.",
          "Find Your Voice was created to fill that gap. Not with motivational talks or weekend workshops that fade by Monday, but with a structured system that builds real communication skills over months — through practice, feedback, and repetition.",
          "Based in Gaborone and expanding across Botswana, the academy now trains children ages 6–18 through group classes, school partnerships, one-on-one coaching, and online sessions.",
        ].map((text, i) => (
          <FadeIn key={i} delay={0.1 + i * 0.05}>
            <p className="text-gray-500 text-lg leading-relaxed mb-5">{text}</p>
          </FadeIn>
        ))}
        <FadeIn delay={0.3}>
          <div className="bg-[#fff7ed] border-l-4 border-[#f97316] rounded-r-2xl p-6 mt-8">
            <p className="text-gray-700 font-bold text-lg italic">
              "Communication is a skill, and like any skill, it can be taught."
            </p>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

function Values() {
  const values = [
    { emoji: "🔍", title: "Clarity Over Volume", desc: "We don't teach children to be loud. We teach them to be clear. The child who can organize their thoughts will always outperform the one who shouts.", bg: "bg-[#dbeafe]", tilt: "rotate-1" },
    { emoji: "🎯", title: "Practice, Not Theory", desc: "Every session is built around doing — speeches, debates, group discussions, impromptu challenges. Children learn by speaking, not by watching.", bg: "bg-[#dcfce7]", tilt: "-rotate-1" },
    { emoji: "📈", title: "Long-Term Development", desc: "Our programs run 6 to 12 months because confidence doesn't happen in a day. We build skills progressively, so each phase deepens what came before.", bg: "bg-[#fef3c7]", tilt: "rotate-2" },
    { emoji: "💛", title: "Every Voice Matters", desc: "We keep groups small. Every child gets time at the front of the room, personal feedback, and the space to grow at their own pace.", bg: "bg-[#ede9fe]", tilt: "-rotate-2" },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#f97316] uppercase tracking-widest mb-4 text-center">Our principles</p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14" style={{ fontFamily: "Nunito, sans-serif" }}>
            What guides <span className="marker-coral">everything we do</span>.
          </h2>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6">
          {values.map((v, i) => (
            <FadeIn key={v.title} delay={i * 0.1}>
              <motion.div
                className={`${v.bg} p-8 rounded-3xl ${v.tilt} border-[3px] border-dashed border-gray-200/60`}
                whileHover={{ rotate: 0, scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                <span className="text-4xl block mb-3">{v.emoji}</span>
                <h3 className="text-xl font-black text-gray-900 mb-2" style={{ fontFamily: "Nunito, sans-serif" }}>{v.title}</h3>
                <p className="text-gray-600 leading-relaxed">{v.desc}</p>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

function Vision() {
  return (
    <section className="py-20 px-6 bg-[#fef9e7] relative overflow-hidden">
      <div className="absolute top-10 right-[12%] w-12 h-12 rounded-full bg-[#fb923c]/15" />
      <div className="absolute bottom-10 left-[8%] w-10 h-10 rounded-xl bg-[#34d399]/15 rotate-12" />
      <div className="max-w-3xl mx-auto text-center relative z-10">
        <FadeIn>
          <span className="text-5xl block mb-6">🌍</span>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 mb-6 leading-tight" style={{ fontFamily: "Nunito, sans-serif" }}>
            A Botswana where no young person holds back because they were <span className="marker-yellow">never taught how to speak up</span>.
          </h2>
          <p className="text-gray-500 text-lg leading-relaxed mb-10">
            We're starting in Gaborone. But the plan is bigger — school partnerships nationwide, online programs for children everywhere in Botswana, and eventually a model that can be replicated across Southern Africa. Every child deserves the tools to be heard.
          </p>
          <Link to="/contact">
            <motion.button
              className="bg-[#f97316] hover:bg-[#ea580c] text-white font-black px-8 py-4 rounded-full text-lg inline-flex items-center gap-2 shadow-lg shadow-orange-200 transition-colors"
              style={{ fontFamily: "Nunito, sans-serif" }}
              whileHover={{ scale: 1.05, rotate: 1 }}
              whileTap={{ scale: 0.95 }}
            >
              Join the Movement <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
      </div>
    </section>
  )
}

export default function About() {
  return (
    <>
      <PageHero />
      <Story />
      <Values />
      <Vision />
    </>
  )
}
