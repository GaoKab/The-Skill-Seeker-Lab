import { useState } from "react"
import { motion } from "motion/react"
import { Section, FadeIn } from "../components/Section"
import {
  MapPin,
  Phone,
  Mail,
  MessageCircle,
  Send,
  CheckCircle2,
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
          Get Started
        </motion.span>
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-4xl md:text-6xl font-bold text-white mt-4 max-w-3xl tracking-tight"
        >
          Enroll your child or ask us anything.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mt-6 text-lg text-slate-300 max-w-2xl leading-relaxed"
        >
          Whether you're ready to enroll or just have questions — we're here.
          Fill out the form, WhatsApp us, or call. We respond within 24
          hours.
        </motion.p>
      </div>
    </section>
  )
}

function ContactForm() {
  const [submitted, setSubmitted] = useState(false)

  if (submitted) {
    return (
      <Section>
        <div className="max-w-2xl mx-auto text-center">
          <FadeIn>
            <CheckCircle2
              size={56}
              className="text-teal-500 mx-auto mb-6"
            />
            <h2 className="text-3xl font-bold text-slate-900 mb-4">
              We've received your message.
            </h2>
            <p className="text-slate-600 text-lg">
              Thank you for reaching out. A member of our team will get back
              to you within 24 hours. If it's urgent, WhatsApp us directly.
            </p>
          </FadeIn>
        </div>
      </Section>
    )
  }

  return (
    <Section>
      <div className="max-w-6xl mx-auto grid lg:grid-cols-5 gap-16">
        {/* Form */}
        <FadeIn className="lg:col-span-3">
          <h2 className="text-2xl font-bold text-slate-900 mb-8">
            Send us a message
          </h2>
          <form
            onSubmit={(e) => {
              e.preventDefault()
              setSubmitted(true)
            }}
            className="space-y-5"
          >
            <div className="grid sm:grid-cols-2 gap-5">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1.5">
                  Your Name
                </label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Mpho Kabelo"
                  className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1.5">
                  Phone Number
                </label>
                <input
                  type="tel"
                  required
                  placeholder="+267 71 234 567"
                  className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">
                Email Address
              </label>
              <input
                type="email"
                required
                placeholder="your@email.com"
                className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">
                I'm interested in
              </label>
              <select
                required
                className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
              >
                <option value="">Select an option</option>
                <option value="young-speakers">
                  Young Speakers (Ages 6–10)
                </option>
                <option value="rising-voices">
                  Rising Voices (Ages 11–14)
                </option>
                <option value="future-leaders">
                  Future Leaders (Ages 15–18)
                </option>
                <option value="one-on-one">One-on-One Coaching</option>
                <option value="online">Online Sessions</option>
                <option value="school">School Partnership</option>
                <option value="other">General Inquiry</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">
                Child's Age (if enrolling)
              </label>
              <input
                type="text"
                placeholder="e.g. 12"
                className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">
                Your Message
              </label>
              <textarea
                rows={4}
                placeholder="Tell us about your child, your goals, or any questions you have..."
                className="w-full border border-slate-300 rounded-lg px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent resize-none"
              />
            </div>

            <motion.button
              type="submit"
              className="w-full bg-teal-600 hover:bg-teal-700 text-white font-bold py-4 rounded-xl text-lg flex items-center justify-center gap-2 transition-colors"
              whileHover={{ scale: 1.01 }}
              whileTap={{ scale: 0.98 }}
            >
              Send Message
              <Send size={18} />
            </motion.button>
          </form>
        </FadeIn>

        {/* Sidebar */}
        <FadeIn className="lg:col-span-2" delay={0.15}>
          <div className="bg-slate-50 rounded-2xl p-8 space-y-8">
            <div>
              <h3 className="font-bold text-lg text-slate-900 mb-4">
                Contact Information
              </h3>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <MapPin
                    size={18}
                    className="text-teal-600 shrink-0 mt-0.5"
                  />
                  <div>
                    <p className="text-slate-700 font-medium">Location</p>
                    <p className="text-slate-500 text-sm">
                      Gaborone, Botswana
                    </p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <Phone
                    size={18}
                    className="text-teal-600 shrink-0 mt-0.5"
                  />
                  <div>
                    <p className="text-slate-700 font-medium">Phone</p>
                    <p className="text-slate-500 text-sm">+267 71 234 567</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <Mail
                    size={18}
                    className="text-teal-600 shrink-0 mt-0.5"
                  />
                  <div>
                    <p className="text-slate-700 font-medium">Email</p>
                    <p className="text-slate-500 text-sm">
                      hello@findyourvoice.co.bw
                    </p>
                  </div>
                </li>
              </ul>
            </div>

            <div className="border-t border-slate-200 pt-6">
              <h3 className="font-bold text-lg text-slate-900 mb-3">
                Prefer WhatsApp?
              </h3>
              <p className="text-slate-500 text-sm mb-4">
                Most parents find it easiest to reach us on WhatsApp. Tap
                below to start a conversation.
              </p>
              <motion.a
                href="https://wa.me/26771234567?text=Hi%2C%20I'm%20interested%20in%20Find%20Your%20Voice%20for%20my%20child."
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-2 bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-xl transition-colors w-full"
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <MessageCircle size={18} />
                Chat on WhatsApp
              </motion.a>
            </div>

            <div className="border-t border-slate-200 pt-6">
              <h3 className="font-bold text-lg text-slate-900 mb-3">
                Response Time
              </h3>
              <p className="text-slate-500 text-sm">
                We respond to all inquiries within 24 hours. WhatsApp
                messages are usually answered within a few hours during
                business days.
              </p>
            </div>
          </div>
        </FadeIn>
      </div>
    </Section>
  )
}

function FAQ() {
  const faqs = [
    {
      q: "What age groups do you accept?",
      a: "We train children ages 6–18, divided into three programs: Young Speakers (6–10), Rising Voices (11–14), and Future Leaders (15–18).",
    },
    {
      q: "How long is the program?",
      a: "Each program runs for 6 months, divided into three phases: Foundation, Development, and Mastery. Many students continue into the next age track after completing their program.",
    },
    {
      q: "Do you offer trial sessions?",
      a: "Yes. We offer a single trial session so your child can experience the format before committing. Contact us to book one.",
    },
    {
      q: "What if my child is extremely shy?",
      a: "That's exactly who we're designed for. Our groups are small and supportive. We start with low-pressure exercises and build gradually. The shy ones often show the most dramatic transformation.",
    },
    {
      q: "Do you offer online sessions?",
      a: "Yes. We run online sessions via Zoom for families outside Gaborone. Same structure, same facilitators, same results — just delivered remotely.",
    },
    {
      q: "How much does it cost?",
      a: "Pricing depends on the program and format (group, one-on-one, or online). Contact us for current pricing and payment plan options.",
    },
  ]

  return (
    <Section className="bg-slate-50">
      <FadeIn>
        <h2 className="text-3xl font-bold text-slate-900 text-center mb-12">
          Frequently Asked Questions
        </h2>
      </FadeIn>
      <div className="max-w-3xl mx-auto space-y-6">
        {faqs.map((faq, i) => (
          <FadeIn key={faq.q} delay={i * 0.06}>
            <div className="bg-white p-6 rounded-xl border border-slate-200">
              <h3 className="font-semibold text-slate-900 mb-2">{faq.q}</h3>
              <p className="text-slate-500 leading-relaxed">{faq.a}</p>
            </div>
          </FadeIn>
        ))}
      </div>
    </Section>
  )
}

export default function Contact() {
  return (
    <>
      <PageHero />
      <ContactForm />
      <FAQ />
    </>
  )
}
