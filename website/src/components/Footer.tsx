import { Link } from "react-router-dom"
import { MapPin, Phone, Mail } from "lucide-react"

export default function Footer() {
  return (
    <footer className="bg-slate-900 text-slate-300">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid md:grid-cols-4 gap-10">
          {/* Brand */}
          <div className="md:col-span-1">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-9 h-9 rounded-lg bg-teal-600 flex items-center justify-center">
                <span className="text-white font-bold text-lg">F</span>
              </div>
              <span className="font-bold text-xl text-white">
                Find Your Voice
              </span>
            </div>
            <p className="text-sm leading-relaxed text-slate-400">
              Building Botswana's next generation of confident communicators,
              critical thinkers, and young leaders.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold text-white mb-4">Quick Links</h4>
            <ul className="space-y-2 text-sm">
              <li><Link to="/about" className="hover:text-teal-400 transition-colors">About Us</Link></li>
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">Programs</Link></li>
              <li><Link to="/how-it-works" className="hover:text-teal-400 transition-colors">How It Works</Link></li>
              <li><Link to="/for-schools" className="hover:text-teal-400 transition-colors">For Schools</Link></li>
              <li><Link to="/contact" className="hover:text-teal-400 transition-colors">Enroll</Link></li>
            </ul>
          </div>

          {/* Programs */}
          <div>
            <h4 className="font-semibold text-white mb-4">Programs</h4>
            <ul className="space-y-2 text-sm">
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">Young Speakers (Ages 6–10)</Link></li>
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">Rising Voices (Ages 11–14)</Link></li>
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">Future Leaders (Ages 15–18)</Link></li>
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">School Partnerships</Link></li>
              <li><Link to="/programs" className="hover:text-teal-400 transition-colors">One-on-One Coaching</Link></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-semibold text-white mb-4">Get In Touch</h4>
            <ul className="space-y-3 text-sm">
              <li className="flex items-start gap-2">
                <MapPin size={16} className="mt-0.5 shrink-0 text-teal-400" />
                <span>Gaborone, Botswana</span>
              </li>
              <li className="flex items-center gap-2">
                <Phone size={16} className="shrink-0 text-teal-400" />
                <span>+267 71 234 567</span>
              </li>
              <li className="flex items-center gap-2">
                <Mail size={16} className="shrink-0 text-teal-400" />
                <span>hello@findyourvoice.co.bw</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-slate-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-sm text-slate-500">
            &copy; {new Date().getFullYear()} Find Your Voice Academy. All rights reserved.
          </p>
          <p className="text-sm text-slate-500">
            Founded by Mpho Kabelo &middot; Gaborone, Botswana
          </p>
        </div>
      </div>
    </footer>
  )
}
