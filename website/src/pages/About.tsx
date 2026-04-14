import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import { ArrowRight, Heart, Eye, Compass, Target } from "lucide-react"

function PageHero() {
  return (
    <section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900 pt-32 pb-20 px-6">
      <div className="max-w-7xl mx-auto">
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-teal-400 font-semibold text-sm uppercase tracking-wide"
        >
          About Find Your Voice
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-white mt-4 max-w-3xl tracking-tight"
        >
          We're building the academy Botswana's children deserve.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-slate-300 max-w-2xl leading-relaxed"
        >
          Find Your Voice isn't a workshop. It isn't a one-day event. It's a
          structured communication training academy that develops confident,
          articulate, and thoughtful young people — one cohort at a time.
        </motion.p>
      </div>
    </section>
  )
}

function Story() {
  return (
    <Section>
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <h2 className="text-3xl md:text-4xl font-bold text-slate-900 mb-8">
            The story behind Find Your Voice
          </h2>
        </FadeIn>
        <div className="space-y-5">
          <FadeIn delay={0.1}>
            <p className="text-slate-600 text-lg leading-relaxed">
              Mpho Kabelo didn't set out to start an academy. It started with
              a simple observation: brilliant children in Botswana were going
              quiet. Not because they had nothing to say — but because no one
              had ever shown them <em>how</em> to say it.
            </p>
          </FadeIn>
          <FadeIn delay={0.15}>
            <p className="text-slate-600 text-lg leading-relaxed">
              In classrooms, the same three kids would raise their hands. In
              family gatherings, teenagers would sit in silence while adults
              spoke. At school presentations, children would read from notes
              without ever looking up. The pattern was everywhere — and it
              wasn't about talent. It was about training.
            </p>
          </FadeIn>
          <FadeIn delay={0.2}>
            <p className="text-slate-600 text-lg leading-relaxed">
              Find Your Voice was created to fill that gap. Not with
              motivational talks or weekend workshops that fade by Monday, but
              with a structured system that builds real communication skills
              over months — through practice, feedback, and repetition.
            </p>
          </FadeIn>
          <FadeIn delay={0.25}>
            <p className="text-slate-600 text-lg leading-relaxed">
              Based in Gaborone and expanding across Botswana, the academy now
              trains children ages 6–18 through group classes, school
              partnerships, one-on-one coaching, and online sessions. Every
              program is built around the same principle:{" "}
              <strong>
                communication is a skill, and like any skill, it can be
                taught.
              </strong>
            </p>
          </FadeIn>
        </div>
      </div>
    </Section>
  )
}

function Values() {
  const values = [
    {
      icon: Eye,
      title: "Clarity Over Volume",
      desc: "We don't teach children to be loud. We teach them to be clear. The child who can organize their thoughts and express them simply will always outperform the one who shouts.",
    },
    {
      icon: Heart,
      title: "Practice, Not Theory",
      desc: "Every session is built around doing — speeches, debates, group discussions, impromptu challenges. Children learn by speaking, not by watching someone else do it.",
    },
    {
      icon: Compass,
      title: "Long-Term Development",
      desc: "Our programs run 6 to 12 months because confidence doesn't happen in a day. We build skills progressively, so each phase deepens what came before.",
    },
    {
      icon: Target,
      title: "Every Voice Matters",
      desc: "We keep groups small. Every child gets time at the front of the room, personal feedback, and the space to grow at their own pace. No one gets lost in the crowd.",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="Our principles"
        title="What guides everything we do."
      />
      <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        {values.map((v, i) => (
          <FadeIn key={v.title} delay={i * 0.1}>
            <div className="flex items-start gap-5">
              <div className="w-12 h-12 rounded-xl bg-teal-100 flex items-center justify-center shrink-0">
                <v.icon size={22} className="text-teal-600" />
              </div>
              <div>
                <h3 className="font-bold text-lg text-slate-900 mb-2">
                  {v.title}
                </h3>
                <p className="text-slate-500 leading-relaxed">{v.desc}</p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function Vision() {
  return (
    <Section className="bg-gradient-to-br from-slate-900 via-teal-950 to-slate-900">
      <div className="max-w-3xl mx-auto text-center">
        <FadeIn>
          <span className="text-teal-400 font-semibold text-sm uppercase tracking-wide">
            Our vision
          </span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mt-4 mb-6">
            A Botswana where no young person holds back because they were
            never taught how to speak up.
          </h2>
          <p className="text-slate-300 text-lg leading-relaxed mb-10">
            We're starting in Gaborone. But the plan is bigger — school
            partnerships nationwide, online programs for children everywhere
            in Botswana, and eventually a model that can be replicated across
            Southern Africa. Every child deserves the tools to be heard.
          </p>
          <Link to="/contact">
            <motion.button
              className="bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg inline-flex items-center gap-2 transition-colors"
              whileHover={{ scale: 1.03 }}
              whileTap={{ scale: 0.97 }}
            >
              Join the Movement
              <ArrowRight size={20} />
            </motion.button>
          </Link>
        </FadeIn>
      </div>
    </Section>
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
