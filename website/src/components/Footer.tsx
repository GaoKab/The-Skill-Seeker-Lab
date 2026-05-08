import { Link } from "react-router-dom"

export default function Footer() {
  return (
    <footer className="bg-[#fef9e7] border-t-[3px] border-dashed border-[#fbbf24]/30">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid md:grid-cols-4 gap-10">
          <div className="md:col-span-1">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-2xl bg-[#f97316] flex items-center justify-center shadow-md rotate-3">
                <span className="text-white font-black text-xl" style={{ fontFamily: "Nunito, sans-serif" }}>F</span>
              </div>
              <span className="font-black text-xl text-gray-900" style={{ fontFamily: "Nunito, sans-serif" }}>
                Find Your Voice
              </span>
            </div>
            <p className="text-sm leading-relaxed text-gray-500">
              Building Botswana's next generation of confident communicators, critical thinkers, and young leaders.
            </p>
          </div>

          <div>
            <h4 className="font-black text-gray-900 mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Quick Links</h4>
            <ul className="space-y-2.5 text-sm">
              <li><Link to="/about" className="text-gray-500 hover:text-[#f97316] transition-colors">About Us</Link></li>
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">Programs</Link></li>
              <li><Link to="/how-it-works" className="text-gray-500 hover:text-[#f97316] transition-colors">How It Works</Link></li>
              <li><Link to="/for-schools" className="text-gray-500 hover:text-[#f97316] transition-colors">For Schools</Link></li>
              <li><Link to="/contact" className="text-gray-500 hover:text-[#f97316] transition-colors">Enroll</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-black text-gray-900 mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Programs</h4>
            <ul className="space-y-2.5 text-sm">
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">🌱 Young Speakers (6-10)</Link></li>
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">🔥 Rising Voices (11-14)</Link></li>
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">👑 Future Leaders (15-18)</Link></li>
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">🏫 School Partnerships</Link></li>
              <li><Link to="/programs" className="text-gray-500 hover:text-[#f97316] transition-colors">🎯 One-on-One Coaching</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-black text-gray-900 mb-4" style={{ fontFamily: "Nunito, sans-serif" }}>Get In Touch</h4>
            <ul className="space-y-3 text-sm text-gray-500">
              <li className="flex items-start gap-2">
                <span>📍</span><span>Gaborone, Botswana</span>
              </li>
              <li className="flex items-center gap-2">
                <span>📞</span><span>+267 71 234 567</span>
              </li>
              <li className="flex items-center gap-2">
                <span>✉️</span><span>hello@findyourvoice.co.bw</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t-2 border-dashed border-[#fbbf24]/20 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-sm text-gray-400">
            &copy; {new Date().getFullYear()} Find Your Voice Academy. Made with ❤️ in Botswana.
          </p>
          <p className="text-sm text-gray-400">
            Founded by Mpho Kabelo
          </p>
        </div>
      </div>
    </footer>
  )
}
