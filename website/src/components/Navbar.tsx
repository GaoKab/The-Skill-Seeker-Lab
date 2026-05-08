import { useState, useEffect } from "react"
import { Link, useLocation } from "react-router-dom"
import { motion, AnimatePresence } from "motion/react"
import { Menu, X, Mic } from "lucide-react"

const links = [
  { to: "/", label: "Home" },
  { to: "/about", label: "About" },
  { to: "/programs", label: "Programs" },
  { to: "/how-it-works", label: "How It Works" },
  { to: "/for-schools", label: "For Schools" },
]

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const { pathname } = useLocation()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener("scroll", onScroll)
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

  return (
    <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? "bg-white/95 backdrop-blur-sm shadow-sm" : "bg-transparent"}`}>
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-[#818CF8] border-2 border-[#6366F1] flex items-center justify-center clay-sm">
            <Mic className="w-5 h-5 text-white" />
          </div>
          <div>
            <span className="font-bold text-xl text-gray-900 leading-none">Find Your Voice</span>
            <p className="text-[10px] text-[#6366F1] font-semibold uppercase tracking-widest leading-none mt-0.5">Youth Academy</p>
          </div>
        </Link>

        <div className="hidden md:flex items-center gap-1">
          {links.map((link) => (
            <Link
              key={link.to}
              to={link.to}
              className={`text-sm font-semibold transition-colors px-3 py-1.5 rounded-xl relative ${
                pathname === link.to ? "text-[#4F46E5]" : "text-gray-500 hover:text-gray-900"
              }`}
            >
              {link.label}
              {pathname === link.to && (
                <motion.div
                  layoutId="nav-indicator"
                  className="absolute inset-0 bg-[#EEF2FF] rounded-xl border-2 border-[#C7D2FE] -z-10 clay-sm"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
            </Link>
          ))}
          <Link to="/contact" className="ml-3">
            <motion.button
              className="bg-[#F97316] text-white px-5 py-2.5 rounded-2xl text-sm font-bold border-2 border-[#EA580C] clay-sm hover:brightness-105 transition-all"
              whileHover={{ scale: 1.05, y: -1 }}
              whileTap={{ scale: 0.95 }}
            >
              Enroll Now
            </motion.button>
          </Link>
        </div>

        <button className="md:hidden text-gray-700 w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100" onClick={() => setOpen(!open)}>
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      <AnimatePresence>
        {open && (
          <motion.div
            key="mobile-menu"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-white border-t border-gray-100 overflow-hidden"
          >
            <div className="px-6 py-5 flex flex-col gap-2">
              {links.map((link) => (
                <Link
                  key={link.to}
                  to={link.to}
                  onClick={() => setOpen(false)}
                  className={`text-base font-semibold py-2.5 px-4 rounded-xl ${
                    pathname === link.to ? "bg-[#EEF2FF] text-[#4F46E5] border-2 border-[#C7D2FE]" : "text-gray-600"
                  }`}
                >
                  {link.label}
                </Link>
              ))}
              <Link to="/contact" onClick={() => setOpen(false)} className="bg-[#F97316] text-white px-6 py-3 rounded-2xl text-base font-bold text-center mt-2 border-2 border-[#EA580C] clay-sm">
                Enroll Now
              </Link>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  )
}
