import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { Section, FadeIn, SectionHeader } from "../components/Section"
import {
  ArrowRight,
  CheckCircle2,
  User,
  Monitor,
  GraduationCap,
  Clock,
  CalendarDays,
  Sparkles,
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
          Programs
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-white mt-4 max-w-3xl tracking-tight"
        >
          Structured programs that build real skills.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-slate-300 max-w-2xl leading-relaxed"
        >
          Every program is designed around one principle: children learn
          communication by communicating. Not by watching, not by reading —
          by doing. Here's how it works at every age.
        </motion.p>
      </div>
    </section>
  )
}

interface ProgramCardProps {
  age: string
  name: string
  tagline: string
  description: string
  includes: string[]
  duration: string
  format: string
  color: string
  borderColor: string
  index: number
}

function ProgramCard({
  age,
  name,
  tagline,
  description,
  includes,
  duration,
  format,
  color,
  borderColor,
  index,
}: ProgramCardProps) {
  return (
    <FadeIn delay={index * 0.12}>
      <div
        className={`rounded-2xl border-2 ${borderColor} overflow-hidden h-full`}
      >
        <div className={`${color} px-8 pt-8 pb-6`}>
          <span className="text-xs font-bold uppercase tracking-widest text-slate-500">
            {age}
          </span>
          <h3 className="text-2xl font-bold text-slate-900 mt-1">{name}</h3>
          <p className="text-teal-700 font-medium mt-1">{tagline}</p>
        </div>
        <div className="px-8 py-8 bg-white">
          <p className="text-slate-600 leading-relaxed mb-6">{description}</p>

          <div className="flex gap-6 mb-6 text-sm">
            <div className="flex items-center gap-2 text-slate-500">
              <Clock size={15} />
              <span>{duration}</span>
            </div>
            <div className="flex items-center gap-2 text-slate-500">
              <CalendarDays size={15} />
              <span>{format}</span>
            </div>
          </div>

          <h4 className="font-semibold text-slate-900 text-sm mb-3">
            What's included:
          </h4>
          <ul className="space-y-2">
            {includes.map((item) => (
              <li key={item} className="flex items-start gap-2 text-sm">
                <CheckCircle2
                  size={16}
                  className="text-teal-500 shrink-0 mt-0.5"
                />
                <span className="text-slate-600">{item}</span>
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
      age: "Ages 6–10",
      name: "Young Speakers",
      tagline: "Where confidence begins",
      description:
        "Designed for children just starting to find their voice. Through storytelling, show-and-tell, role play, and guided group activities, young speakers learn to organize their thoughts and share them with a small, supportive audience.",
      includes: [
        "Weekly 60-minute group sessions",
        "Storytelling and show-and-tell exercises",
        "Basic speech structure training",
        "End-of-phase showcase for parents",
        "Progress reports after each phase",
      ],
      duration: "6-month program",
      format: "Weekly sessions",
      color: "bg-teal-50",
      borderColor: "border-teal-200",
    },
    {
      age: "Ages 11–14",
      name: "Rising Voices",
      tagline: "Building thinkers who speak",
      description:
        "The bridge between childhood communication and real-world expression. Students tackle debates, persuasive speaking, group discussions, and impromptu challenges. They learn to defend ideas under pressure — and change their mind when the argument is better.",
      includes: [
        "Weekly 90-minute group sessions",
        "Structured debate and discussion formats",
        "Persuasive speaking and argumentation",
        "Critical thinking exercises",
        "Feedback from peers and facilitators",
        "Mid-program and final assessments",
      ],
      duration: "6-month program",
      format: "Weekly sessions",
      color: "bg-amber-50",
      borderColor: "border-amber-200",
    },
    {
      age: "Ages 15–18",
      name: "Future Leaders",
      tagline: "Preparing the next generation to lead",
      description:
        "Advanced communication training for teens ready to operate at a higher level. This program covers presentations, panel discussions, interview preparation, and public-facing speaking opportunities. Students leave with a real portfolio of speaking experience.",
      includes: [
        "Weekly 90-minute sessions",
        "Presentation design and delivery",
        "Panel discussion and interview practice",
        "Leadership communication frameworks",
        "Real speaking opportunities (events, schools)",
        "Personal speaking portfolio development",
        "Certificate of completion",
      ],
      duration: "6-month program",
      format: "Weekly sessions",
      color: "bg-slate-50",
      borderColor: "border-slate-300",
    },
  ]

  return (
    <Section>
      <SectionHeader
        label="Core programs"
        title="Three tracks. Every age covered."
        subtitle="Each program runs in 6-month phases with clear milestones, so both you and your child can see the growth."
      />
      <div className="grid lg:grid-cols-3 gap-8">
        {programs.map((p, i) => (
          <ProgramCard key={p.name} {...p} index={i} />
        ))}
      </div>
    </Section>
  )
}

function AdditionalOfferings() {
  const offerings = [
    {
      icon: GraduationCap,
      title: "School Partnerships",
      desc: "We bring Find Your Voice directly into schools. Customized programs integrated into your school calendar — assemblies, after-school clubs, or curriculum-aligned communication training.",
      cta: "Learn about school partnerships",
      link: "/for-schools",
    },
    {
      icon: User,
      title: "One-on-One Coaching",
      desc: "Premium, personalized coaching for children who need individual attention. Whether it's preparing for a specific event, overcoming a particular challenge, or accelerating growth — this is the intensive track.",
      cta: "Inquire about coaching",
      link: "/contact",
    },
    {
      icon: Monitor,
      title: "Online Sessions (Zoom)",
      desc: "Can't make it to Gaborone? Our online sessions bring the same structured training to your screen. Small groups, live facilitation, and real-time practice — not pre-recorded videos.",
      cta: "Ask about online availability",
      link: "/contact",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <SectionHeader
        label="More options"
        title="Beyond the classroom."
        subtitle="Different children need different paths. We've built programs that meet families and schools wherever they are."
      />
      <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {offerings.map((o, i) => (
          <FadeIn key={o.title} delay={i * 0.12}>
            <motion.div
              className="bg-white rounded-2xl border border-slate-200 p-8 h-full flex flex-col"
              whileHover={{ y: -4 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <div className="w-12 h-12 rounded-xl bg-teal-100 flex items-center justify-center mb-5">
                <o.icon size={22} className="text-teal-600" />
              </div>
              <h3 className="font-bold text-xl text-slate-900 mb-3">
                {o.title}
              </h3>
              <p className="text-slate-500 leading-relaxed flex-1">
                {o.desc}
              </p>
              <Link
                to={o.link}
                className="inline-flex items-center gap-2 text-teal-600 font-semibold mt-6 hover:text-teal-700 transition-colors text-sm"
              >
                {o.cta}
                <ArrowRight size={16} />
              </Link>
            </motion.div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

function ProgramStructure() {
  const phases = [
    {
      phase: "Phase 1 — Foundation",
      months: "Months 1–2",
      desc: "Core skills. Build the basics — voice control, eye contact, basic speech structure, and the habit of speaking regularly.",
    },
    {
      phase: "Phase 2 — Development",
      months: "Months 3–4",
      desc: "Depth and complexity. Move into persuasion, debate, impromptu speaking, and group leadership. Start handling pressure.",
    },
    {
      phase: "Phase 3 — Mastery",
      months: "Months 5–6",
      desc: "Performance and portfolio. Deliver polished speeches, participate in showcases, and build real speaking experience.",
    },
  ]

  return (
    <Section>
      <SectionHeader
        label="The structure"
        title="6 months. 3 phases. Real transformation."
        subtitle="Every program follows the same proven structure — progressive skill-building that compounds over time."
      />
      <div className="max-w-3xl mx-auto space-y-6">
        {phases.map((p, i) => (
          <FadeIn key={p.phase} delay={i * 0.12}>
            <div className="flex gap-6 items-start">
              <div className="w-12 h-12 rounded-full bg-teal-600 flex items-center justify-center shrink-0 text-white font-bold">
                {i + 1}
              </div>
              <div>
                <h3 className="font-bold text-lg text-slate-900">
                  {p.phase}
                </h3>
                <span className="text-sm text-teal-600 font-medium">
                  {p.months}
                </span>
                <p className="text-slate-500 leading-relaxed mt-2">
                  {p.desc}
                </p>
              </div>
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
          <Sparkles className="text-teal-400 mx-auto mb-4" size={28} />
          <h2 className="text-3xl md:text-4xl font-bold text-white">
            Ready to give your child the skills that school doesn't teach?
          </h2>
          <p className="mt-5 text-lg text-slate-300">
            Enrollment is open for the next cohort. Spots are limited to keep
            groups small and personal.
          </p>
          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button
                className="bg-teal-500 hover:bg-teal-400 text-slate-900 font-bold px-8 py-4 rounded-xl text-lg inline-flex items-center gap-2 transition-colors"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Enroll Now
                <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/contact">
              <motion.button
                className="border border-slate-500 hover:border-teal-400 text-white font-semibold px-8 py-4 rounded-xl text-lg transition-colors"
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
              >
                Ask a Question First
              </motion.button>
            </Link>
          </div>
        </FadeIn>
      </div>
    </Section>
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
