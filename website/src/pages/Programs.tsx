import { Link } from "react-router-dom"
import { motion } from "motion/react"
import { FadeIn } from "../components/Section"
import {
  BookOpen,
  Target,
  Award,
  Blocks,
  Rocket,
  Trophy,
  CheckCircle2,
  Clock,
  CalendarDays,
  School,
  Crosshair,
  Monitor,
  ArrowRight,
} from "lucide-react"

const springBounce = { type: "spring" as const, stiffness: 300, damping: 15 }

/* ------------------------------------------------------------------ */
/*  PageHero                                                          */
/* ------------------------------------------------------------------ */
function PageHero() {
  return (
    <section className="relative bg-[#DCFCE7] pt-32 pb-20 px-6 overflow-hidden">
      {/* Decorative blobs */}
      <div className="absolute top-24 right-[12%] w-14 h-14 rounded-full bg-[#86EFAC]/25 clay-sm" />
      <div className="absolute bottom-12 left-[8%] w-16 h-16 rounded-xl bg-[#FCD34D]/20 rotate-6 clay-sm" />
      <div className="absolute top-36 left-[22%] w-8 h-8 rounded-lg bg-[#C4B5FD]/25 -rotate-12 clay-sm" />

      <div className="max-w-4xl mx-auto relative z-10">
        {/* Badge with icon */}
        <motion.span
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-flex items-center gap-2 bg-white text-gray-800 font-black text-sm px-5 py-2.5 rounded-full border-2 border-[#86EFAC] clay-sm mb-6"
        >
          <BookOpen size={16} className="text-[#059669]" />
          Our programs
        </motion.span>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-gray-900 leading-tight"
        >
          Structured programs that build{" "}
          <span className="marker-green">real skills</span>.
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-gray-600 max-w-2xl leading-relaxed"
        >
          Every program is designed around one principle: children learn
          communication by communicating. Not by watching, not by reading — by
          doing.
        </motion.p>
      </div>
    </section>
  )
}

/* ------------------------------------------------------------------ */
/*  CorePrograms                                                      */
/* ------------------------------------------------------------------ */
function CorePrograms() {
  const programs = [
    {
      icon: Blocks,
      iconBg: "bg-[#BBF7D0]",
      iconBorder: "border-[#86EFAC]",
      iconColor: "text-[#059669]",
      age: "Ages 6-10",
      name: "Young Speakers",
      tagline: "Where confidence begins",
      description:
        "Designed for children just starting to find their voice. Through storytelling, show-and-tell, role play, and guided group activities, young speakers learn to organize their thoughts and share them with a supportive audience.",
      includes: [
        "Weekly 60-minute group sessions",
        "Storytelling and show-and-tell exercises",
        "Basic speech structure training",
        "End-of-phase showcase for parents",
        "Progress reports after each phase",
      ],
      duration: "6-month program",
      format: "Weekly sessions",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
      accent: "text-[#059669]",
    },
    {
      icon: Rocket,
      iconBg: "bg-[#FDE68A]",
      iconBorder: "border-[#FCD34D]",
      iconColor: "text-[#D97706]",
      age: "Ages 11-14",
      name: "Rising Voices",
      tagline: "Building thinkers who speak",
      description:
        "The bridge between childhood communication and real-world expression. Students tackle debates, persuasive speaking, group discussions, and impromptu challenges. They learn to defend ideas under pressure.",
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
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
      accent: "text-[#D97706]",
    },
    {
      icon: Award,
      iconBg: "bg-[#DDD6FE]",
      iconBorder: "border-[#C4B5FD]",
      iconColor: "text-[#7C3AED]",
      age: "Ages 15-18",
      name: "Future Leaders",
      tagline: "Preparing the next generation to lead",
      description:
        "Advanced communication training for teens ready to operate at a higher level. Covers presentations, panel discussions, interview preparation, and public-facing speaking opportunities.",
      includes: [
        "Weekly 90-minute sessions",
        "Presentation design and delivery",
        "Panel discussion and interview practice",
        "Leadership communication frameworks",
        "Real speaking opportunities (events, schools)",
        "Personal speaking portfolio",
        "Certificate of completion",
      ],
      duration: "6-month program",
      format: "Weekly sessions",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
      accent: "text-[#7C3AED]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#FFFBF5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#059669] uppercase tracking-widest mb-4 text-center">
            Core programs
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            Three tracks. Every age{" "}
            <span className="marker-green">covered</span>.
          </h2>
        </FadeIn>

        <div className="space-y-10">
          {programs.map((p, i) => (
            <FadeIn key={p.name} delay={i * 0.12}>
              <motion.div
                className={`${p.bg} border-3 ${p.border} rounded-3xl overflow-hidden clay`}
                whileHover={{ y: -4 }}
                transition={springBounce}
              >
                <div className="p-8 md:p-10">
                  {/* Header row */}
                  <div className="flex items-start gap-5 mb-6">
                    <motion.div
                      className={`w-16 h-16 rounded-2xl ${p.iconBg} border-2 ${p.iconBorder} flex items-center justify-center shrink-0 clay-sm`}
                      whileHover={{ rotate: [0, -8, 8, 0] }}
                      transition={springBounce}
                    >
                      <p.icon size={28} className={p.iconColor} />
                    </motion.div>
                    <div>
                      <span
                        className={`text-xs font-black uppercase tracking-widest ${p.accent}`}
                      >
                        {p.age}
                      </span>
                      <h3 className="text-2xl font-black text-gray-900 mt-0.5">
                        {p.name}
                      </h3>
                      <p className={`${p.accent} font-bold text-sm`}>
                        {p.tagline}
                      </p>
                    </div>
                  </div>

                  {/* Description */}
                  <p className="text-gray-600 leading-relaxed mb-6">
                    {p.description}
                  </p>

                  {/* Meta */}
                  <div className="flex gap-6 mb-6 text-sm text-gray-500 font-bold">
                    <span className="inline-flex items-center gap-1.5">
                      <Clock size={14} className="text-gray-400" />
                      {p.duration}
                    </span>
                    <span className="inline-flex items-center gap-1.5">
                      <CalendarDays size={14} className="text-gray-400" />
                      {p.format}
                    </span>
                  </div>

                  {/* Includes */}
                  <div className="bg-white/60 rounded-2xl p-5 border-2 border-white/80 clay-sm">
                    <h4 className="font-black text-gray-900 text-sm mb-3">
                      What's included:
                    </h4>
                    <ul className="space-y-2">
                      {p.includes.map((item) => (
                        <li
                          key={item}
                          className="flex items-start gap-2 text-sm"
                        >
                          <CheckCircle2
                            size={16}
                            className="text-[#34D399] shrink-0 mt-0.5"
                          />
                          <span className="text-gray-600">{item}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ------------------------------------------------------------------ */
/*  ProgramStructure                                                  */
/* ------------------------------------------------------------------ */
function ProgramStructure() {
  const phases = [
    {
      icon: Blocks,
      iconColor: "text-[#2563EB]",
      phase: "Phase 1 — Foundation",
      months: "Months 1-2",
      desc: "Core skills. Build the basics — voice control, eye contact, basic speech structure, and the habit of speaking regularly.",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
    },
    {
      icon: Rocket,
      iconColor: "text-[#D97706]",
      phase: "Phase 2 — Development",
      months: "Months 3-4",
      desc: "Depth and complexity. Move into persuasion, debate, impromptu speaking, and group leadership. Start handling pressure.",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
    },
    {
      icon: Trophy,
      iconColor: "text-[#059669]",
      phase: "Phase 3 — Mastery",
      months: "Months 5-6",
      desc: "Performance and portfolio. Deliver polished speeches, participate in showcases, and build real speaking experience.",
      bg: "bg-[#BBF7D0]",
      border: "border-[#86EFAC]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-white">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#7C3AED] uppercase tracking-widest mb-4 text-center">
            The structure
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            6 months. 3 phases.{" "}
            <span className="marker-purple">Real transformation</span>.
          </h2>
        </FadeIn>

        <div className="space-y-5">
          {phases.map((p, i) => (
            <FadeIn key={p.phase} delay={i * 0.12}>
              <motion.div
                className={`flex gap-5 items-start ${p.bg} border-2 ${p.border} p-6 rounded-2xl clay`}
                whileHover={{ y: -3 }}
                transition={springBounce}
              >
                <motion.div
                  className="w-14 h-14 rounded-2xl bg-white border-2 border-white/80 flex items-center justify-center shrink-0 clay-sm"
                  whileHover={{ rotate: [0, -8, 8, 0] }}
                  transition={springBounce}
                >
                  <p.icon size={24} className={p.iconColor} />
                </motion.div>
                <div>
                  <h3 className="font-black text-lg text-gray-900">
                    {p.phase}
                  </h3>
                  <span className="text-sm text-[#7C3AED] font-bold">
                    {p.months}
                  </span>
                  <p className="text-gray-600 leading-relaxed mt-2">
                    {p.desc}
                  </p>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ------------------------------------------------------------------ */
/*  AdditionalOfferings                                               */
/* ------------------------------------------------------------------ */
function AdditionalOfferings() {
  const offerings = [
    {
      icon: School,
      iconColor: "text-[#2563EB]",
      title: "School Partnerships",
      desc: "We bring Find Your Voice directly into schools. Customized programs integrated into your school calendar.",
      cta: "Learn about school partnerships",
      link: "/for-schools",
      bg: "bg-[#BFDBFE]",
      border: "border-[#93C5FD]",
      iconBg: "bg-[#BFDBFE]",
      iconBorder: "border-[#93C5FD]",
    },
    {
      icon: Crosshair,
      iconColor: "text-[#D97706]",
      title: "One-on-One Coaching",
      desc: "Premium, personalized coaching for children who need individual attention or are preparing for a specific event.",
      cta: "Inquire about coaching",
      link: "/contact",
      bg: "bg-[#FDE68A]",
      border: "border-[#FCD34D]",
      iconBg: "bg-[#FDE68A]",
      iconBorder: "border-[#FCD34D]",
    },
    {
      icon: Monitor,
      iconColor: "text-[#7C3AED]",
      title: "Online Sessions",
      desc: "Can't make it to Gaborone? Our online sessions bring the same structured training to your screen.",
      cta: "Ask about online availability",
      link: "/contact",
      bg: "bg-[#DDD6FE]",
      border: "border-[#C4B5FD]",
      iconBg: "bg-[#DDD6FE]",
      iconBorder: "border-[#C4B5FD]",
    },
  ]

  return (
    <section className="py-20 px-6 bg-[#FFFBF5]">
      <div className="max-w-4xl mx-auto">
        <FadeIn>
          <p className="text-sm font-black text-[#D97706] uppercase tracking-widest mb-4 text-center">
            More options
          </p>
          <h2 className="text-3xl md:text-5xl font-black text-gray-900 text-center mb-14">
            Beyond the <span className="marker-coral">classroom</span>.
          </h2>
        </FadeIn>

        <div className="space-y-6">
          {offerings.map((o, i) => (
            <FadeIn key={o.title} delay={i * 0.12}>
              <motion.div
                className={`${o.bg} border-2 ${o.border} rounded-3xl p-8 flex flex-col md:flex-row items-start gap-6 clay`}
                whileHover={{ y: -4 }}
                transition={springBounce}
              >
                <motion.div
                  className={`w-14 h-14 rounded-2xl bg-white border-2 ${o.iconBorder} flex items-center justify-center shrink-0 clay-sm`}
                  whileHover={{ rotate: [0, -8, 8, 0] }}
                  transition={springBounce}
                >
                  <o.icon size={24} className={o.iconColor} />
                </motion.div>
                <div>
                  <h3 className="font-black text-xl text-gray-900 mb-2">
                    {o.title}
                  </h3>
                  <p className="text-gray-600 leading-relaxed mb-4">
                    {o.desc}
                  </p>
                  <Link
                    to={o.link}
                    className="inline-flex items-center gap-2 text-[#4F46E5] font-bold hover:underline text-sm"
                  >
                    {o.cta} <ArrowRight size={16} />
                  </Link>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ------------------------------------------------------------------ */
/*  CTA                                                               */
/* ------------------------------------------------------------------ */
function CTA() {
  return (
    <section className="py-20 px-6 bg-[#DCFCE7] relative overflow-hidden">
      {/* Decorative blobs */}
      <div className="absolute top-8 right-[15%] w-12 h-12 rounded-full bg-[#86EFAC]/25 clay-sm" />
      <div className="absolute bottom-12 left-[10%] w-14 h-14 rounded-xl bg-[#FCD34D]/20 -rotate-12 clay-sm" />
      <div className="absolute top-20 left-[30%] w-8 h-8 rounded-lg bg-[#C4B5FD]/20 rotate-12 clay-sm" />

      <div className="text-center max-w-3xl mx-auto relative z-10">
        <FadeIn>
          {/* Icon instead of emoji */}
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-white border-2 border-[#86EFAC] clay-sm mb-6">
            <Target size={28} className="text-[#059669]" />
          </div>

          <h2 className="text-3xl md:text-5xl font-black text-gray-900 leading-tight">
            Ready to give your child the skills{" "}
            <span className="marker-green">school doesn't teach</span>?
          </h2>

          <p className="mt-5 text-lg text-gray-600">
            Enrollment is open. Spots are limited to keep groups small and
            personal.
          </p>

          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/contact">
              <motion.button
                className="bg-[#F97316] text-white font-black px-8 py-4 rounded-2xl text-lg inline-flex items-center gap-2 border-2 border-[#EA580C] clay-sm"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
                transition={springBounce}
              >
                Enroll Now <ArrowRight size={20} />
              </motion.button>
            </Link>
            <Link to="/contact">
              <motion.button
                className="bg-white text-gray-800 font-bold px-8 py-4 rounded-2xl text-lg border-2 border-gray-200 clay-sm"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
                transition={springBounce}
              >
                Ask a Question First
              </motion.button>
            </Link>
          </div>
        </FadeIn>
      </div>
    </section>
  )
}

/* ------------------------------------------------------------------ */
/*  Page export                                                       */
/* ------------------------------------------------------------------ */
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
